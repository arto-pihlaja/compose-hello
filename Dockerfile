# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-slim-buster

EXPOSE 5000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1
# install pip requirements, they don't change often
WORKDIR /app
COPY conts/requirements.txt /app
RUN python -m pip install -r requirements.txt

# copy code - may change often
COPY conts /app

# Creates a non-root user and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN useradd appuser && chown -R appuser /app
#USER root
#USER appuser - not using this, because it 
# CMD ["flask", "run"]  - for some reason, this never makes the port available 
CMD ["python", "./app.py"] 
