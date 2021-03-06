# создать образ на основе базового слоя python (там будет ОС и интерпретатор Python)
FROM python:3.8.5

RUN mkdir /code
COPY requirements.txt /code
RUN pip install -r /code/requirements.txt
COPY . /code
WORKDIR /code
CMD python manage.py migrate && gunicorn Blog.wsgi:application --bind 0.0.0.0:8000