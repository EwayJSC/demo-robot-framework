FROM python:3.7

WORKDIR /home/app
RUN mkdir results/
ADD ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

ADD ./ ./
CMD ["python", "app.py"]