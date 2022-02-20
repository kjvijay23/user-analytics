FROM python:3.8-slim-buster

ENV FLASK_APP=app.py
ENV FLASK_ENV=development

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY user_analytics .
COPY config.json config.json
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
