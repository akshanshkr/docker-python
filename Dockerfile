FROM python
WORKDIR /myapp
COPY . . 
RUN pip3 install mysql-connector-python

CMD ["python", "db.py"]