# FastAPI Docs
https://fastapi.tiangolo.com/


# docker network
```
docker network create microNet
```

# backend
```
docker build . -t backend
#docker run --name backend --rm --network microNet -p 8000:8000 backend
docker run --name backend --rm -p 8000:8000 backend
```

# frontend
```
docker build . -t frontend-test

docker run --name frontend --rm --network microNet -p 3000:3000 frontend

```

# gcloud
```
gcloud run deploy micro-backoend-prot --port 8080 --source .
```




