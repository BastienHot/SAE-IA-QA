FROM python:3.9

WORKDIR /backend

COPY . /backend

RUN pip install -r ./requirements.txt

EXPOSE 7860


RUN python run.py
