FROM python:3.9.7
WORKDIR /apps
COPY requirements.txt /apps/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /apps/
EXPOSE 8000
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
