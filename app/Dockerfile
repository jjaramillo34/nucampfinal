# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.9.6-alpine

EXPOSE 8000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
#COPY ./requirements.txt .
#RUN pip install -r requirements.txt
# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt
RUN --mount=type=cache,target=/root/.cache \
    pip install -r requirements.txt

# copy entrypoint.sh
# COPY ./entrypoint.sh /entrypoint.sh
# COPY ./.env /.env

# Copy the Django project
COPY . .

# Set the working directory
WORKDIR /usr/src/app

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
#RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
#USER appuser

# run entrypoint.sh
#ENTRYPOINT ["/entrypoint.sh"]
#RUN ["chmod", "+x", "/entrypoint.sh"]

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
#CMD ["gunicorn", "--bind", "0.0.0.0:8083", "mysite.wsgi"] 
