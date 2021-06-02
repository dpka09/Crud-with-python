FROM python:3.9.5-alpine

WORKDIR /docker_hms

COPY . /docker_hms

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
