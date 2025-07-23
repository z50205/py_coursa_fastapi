FROM python:3.10-alpine

WORKDIR /app

COPY ./requirement.txt /requirement.txt

RUN pip install --no-cache-dir --upgrade -r /requirement.txt

COPY ./coursa /app

CMD ["fastapi", "run", "app.py", "--port", "8000"]