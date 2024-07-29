FROM python:3.8
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 80
ENTRYPOINT ["python", "intro.py"]
