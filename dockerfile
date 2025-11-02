FROM python:3.11-slim

WORKDIR /app

COPY tests/requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

CMD ["pytest", "tests/"]

