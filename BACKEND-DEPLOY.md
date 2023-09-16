# FastAPI Docs
https://fastapi.tiangolo.com/

# local
```
uvicorn main:app --reload
```

# docker network
```
docker network create microNetwork
```

# backend
```
docker build . -t micro-backend

docker run --name micro-backend --rm --network microNetwork -p 8000:8000 micro-backend

docker run --name micro-backend --rm -p 8000:8000 micro-backend

```

# frontend
```
docker build . -t frontend-test

docker run --name frontend --rm --network microNet -p 3000:3000 frontend

```

# gcloud
```
gcloud builds submit --tag gcr.io/cloud-run-install/micro-backend

gcloud run deploy --image gcr.io/cloud-run-install/micro-backend --platform managed --port=8000


# gcloud run deploy micro-backend --port 8000 --source .
```




