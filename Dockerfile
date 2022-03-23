FROM python:3.10.3-alpine

ADD . .
RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--timeout", "2000", "app:app"]
