# first stage
FROM python:3.8 AS builder
COPY requirements.txt .

# install dependencies to the local user directory (eg. /root/.local)
RUN pip install --user -r requirements.txt -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com

# second unnamed stage
FROM python:3.8.6-slim
WORKDIR /code

# copy only the dependencies installation from the 1st stage image
COPY --from=builder /root/.local /root/.local
COPY . .

# update PATH environment variable
ENV PATH=/root/.local:$PATH
ENV PYTHONPATH /root/.local:${PYTHONPATH}

EXPOSE 5000

CMD [ "python", "./server.py" ]