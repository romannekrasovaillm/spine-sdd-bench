FROM debian:bookworm-slim
RUN apt-get update \
 && apt-get install -y --no-install-recommends git ca-certificates ripgrep procps \
 && rm -rf /var/lib/apt/lists/*
ENV LANG=C.UTF-8
WORKDIR /home/architect/project
