FROM python:3.7.10

COPY ocr-service /ocr-service
RUN cd  /ocr-service\
    && pip install -r requirements.txt -i "https://pypi.douban.com/simple/"

WORKDIR /ocr-service
EXPOSE 8888
CMD ["python", "manage.py", "runserver"]
