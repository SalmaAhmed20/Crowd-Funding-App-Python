FROM python:3
WORKDIR /app

COPY . /app/
RUN pip3 install python-dotenv
ENTRYPOINT [ "python3" ,"main.py"]