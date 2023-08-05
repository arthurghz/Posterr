# Base image
FROM python:3.9-slim as base

# Install dependencies
FROM base as builder
WORKDIR /install
COPY requirements.txt .
RUN pip install --prefix=/install -r requirements.txt

# Final image
FROM base
WORKDIR /app
COPY --from=builder /install /usr/local
COPY . .

ENV FLASK_APP=src:create_app
ENV FLASK_ENV=development
ENV DATABASE_URL=mysql+pymysql://posterr_service:password@db:3306/posterr_db

EXPOSE 8080

CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]
