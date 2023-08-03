
FROM python:3.9-slim

WORKDIR /

COPY requirements.txt .


RUN pip install -r requirements.txt

COPY . .


ENV FLASK_APP=src:create_app
ENV FLASK_ENV=development
ENV DATABASE_URL=mysql+pymysql://newuser:newpassword@db:3306/db


EXPOSE 8080

# Run the Flask app
CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]
