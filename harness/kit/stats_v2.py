"""Статистика v2: непарные сравнения независимых прогонов. Только stdlib."""
import itertools, math, random, statistics

MIN_N = 4  # ниже — решающие правила (эквивалентность, не-хуже) не применяются


def _mean(x):
    return statistics.mean(x)


def boot_diff(a, b, n=10000, seed=7, level=0.95):
    """Bootstrap CI разности средних mean(a) − mean(b); группы ресэмплируются независимо."""
    if len(a) < 2 or len(b) < 2:
        return None
    rnd = random.Random(seed)
    ds = sorted(_mean([rnd.choice(a) for _ in a]) - _mean([rnd.choice(b) for _ in b]) for _ in range(n))
    lo = (1 - level) / 2
    return round(ds[int(lo * n)], 3), round(ds[min(n - 1, int((1 - lo) * n))], 3)


def boot_interaction(s1, s0, p1, p0, n=10000, seed=7, level=0.95):
    """CI взаимодействия: (mean s1 − mean s0) − (mean p1 − mean p0).

    s1 = стек+Spine, s0 = стек, p1 = plain+Spine, p0 = plain."""
    if min(map(len, (s1, s0, p1, p0))) < 2:
        return None
    rnd = random.Random(seed)

    def r(g):
        return _mean([rnd.choice(g) for _ in g])

    ds = sorted((r(s1) - r(s0)) - (r(p1) - r(p0)) for _ in range(n))
    lo = (1 - level) / 2
    return round(ds[int(lo * n)], 3), round(ds[min(n - 1, int((1 - lo) * n))], 3)


def perm_test(a, b, max_exact=200000, n_mc=20000, seed=7):
    """Двусторонний перестановочный тест разности средних. Точный при малых n."""
    obs = abs(_mean(a) - _mean(b))
    pool, k = list(a) + list(b), len(a)
    total = math.comb(len(pool), k)
    hits = cnt = 0
    if total <= max_exact:
        s = sum(pool)
        for idx in itertools.combinations(range(len(pool)), k):
            sa = sum(pool[i] for i in idx)
            d = abs(sa / k - (s - sa) / (len(pool) - k))
            hits += d >= obs - 1e-12
            cnt += 1
    else:
        rnd = random.Random(seed)
        for _ in range(n_mc):
            rnd.shuffle(pool)
            d = abs(_mean(pool[:k]) - _mean(pool[k:]))
            hits += d >= obs - 1e-12
            cnt += 1
    return round(hits / cnt, 4)


def fisher_exact(a_yes, a_n, b_yes, b_n):
    """Двусторонний точный тест Фишера для долей (например, PASS гейта)."""
    a_no, b_no = a_n - a_yes, b_n - b_yes
    row1, col1, n = a_n, a_yes + b_yes, a_n + b_n
    if n == 0 or row1 == 0 or col1 == 0 or row1 == n or col1 == n:
        return 1.0

    def p(x):
        return math.comb(col1, x) * math.comb(n - col1, row1 - x) / math.comb(n, row1)

    p_obs = p(a_yes)
    lo, hi = max(0, row1 - (n - col1)), min(row1, col1)
    return round(min(1.0, sum(p(x) for x in range(lo, hi + 1) if p(x) <= p_obs + 1e-12)), 4)


def equivalence(a, b, margin=0.25, level=0.90):
    """TOST-подобное правило: «≈ 0», если 90% CI разности целиком внутри ±margin."""
    if min(len(a), len(b)) < MIN_N:
        return f"n<{MIN_N}", None
    ci = boot_diff(a, b, level=level)
    if -margin < ci[0] and ci[1] < margin:
        return "equivalent", ci
    if ci[0] > margin or ci[1] < -margin:
        return "different", ci
    return "inconclusive", ci


def non_inferior(a, b, margin=0.25, level=0.90):
    """a не хуже b, если нижняя граница 90% CI (a − b) > −margin."""
    if min(len(a), len(b)) < MIN_N:
        return None, None
    ci = boot_diff(a, b, level=level)
    return ci[0] > -margin, ci


def holm(pvals, alpha=0.05):
    """Поправка Холма: [(индекс, p, порог, значимо)] в исходном порядке."""
    m = len(pvals)
    order = sorted(range(m), key=lambda i: pvals[i])
    out, prev = [], 0.0
    for rank, i in enumerate(order):
        thr = alpha / (m - rank)
        prev = max(prev, thr)
        out.append((i, pvals[i], round(prev, 4), pvals[i] <= prev))
    return out
