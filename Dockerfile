#
FROM python:3.11-alpine

#
WORKDIR /src

#
COPY ./requirements.txt /src/requirements.txt

#
RUN pip install --no-cache-dir -r /src/requirements.txt

#
COPY ./app /src/app

EXPOSE 10000

#
CMD ["fastapi", "run", "app/main.py", "--port", "10000"]