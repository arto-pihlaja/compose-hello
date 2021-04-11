FROM python:3.8-slim-buster
# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# install pip requirements, they don't change often
WORKDIR /app
COPY req2.txt /app
RUN python -m pip install -r req2.txt
COPY app /app

CMD ["python", "./app.py"] 

