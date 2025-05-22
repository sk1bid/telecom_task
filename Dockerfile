FROM ubuntu:22.04
RUN apt-get update && apt-get install -y\
    python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*
RUN pip3 install requests
COPY checker.py /checker.py
CMD ["python3", "/checker.py"]