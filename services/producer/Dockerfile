FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY ./src /app/src

EXPOSE 30001

CMD ["uvicorn", "src.main:producer_app", "--host", "0.0.0.0", "--port", "30001", "--reload"]
# CMD ["fastapi", "run", "src.main:producer_app", "--host", "0.0.0.0", "--port", "30001", "--reload"]
