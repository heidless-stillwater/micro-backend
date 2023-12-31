
FROM python:3.11.3
ENV PYTHONUNBUFFERED True

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#ENV APP_HOME /root
WORKDIR /api
COPY . /api

EXPOSE 8000

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000" ]

#CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]