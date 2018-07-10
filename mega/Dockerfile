FROM python:3.6-alpine
ADD . /code
WORKDIR /code
RUN pip3 install redis flask
CMD ["python", "main.py"]