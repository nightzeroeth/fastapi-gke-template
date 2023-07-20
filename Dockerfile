FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . ./

# ENV APP_HOME /app
# WORKDIR $APP_HOME

EXPOSE 8080

# CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080", "--workers", "--reload"]