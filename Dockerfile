FROM python:3.7.4
LABEL Author="Pujita Atluri"
LABEL Email="pujita78@hotmail.com"
LABEL version="0.0.1"
WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt
CMD ["python", "run_app.py"]