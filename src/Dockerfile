FROM python:3.6.9-alpine
MAINTAINER midhunpk "midhunpk.54@gmail.com"
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ADD . /app
CMD ["python","main.py"]
