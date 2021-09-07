FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
RUN pip install requests && pip install FastAPI
COPY ./app /app


