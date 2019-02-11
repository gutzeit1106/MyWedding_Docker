FROM gutzeit1106/ub1604_tifig:latest
RUN apt-get install python3 python3-pip -y
RUN pip3 install --upgrade pip
RUN pip3 install flask
RUN mkdir -p /usr/src/app
COPY ./app/ /usr/src/app/
WORKDIR /usr/src/app/
CMD ["python3","/usr/src/app/application.py"]
EXPOSE 80