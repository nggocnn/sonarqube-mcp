FROM python:3.12-slim

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app

RUN pip install -e .

CMD ["sonarqube-mcp", "--transport", "sse"]