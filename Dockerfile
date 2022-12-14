FROM python:3

RUN mkdir proj_site
COPY . ./proj_site
WORKDIR proj_site
RUN pip install -r requirements.txt

ENTRYPOINT python proj_site/manage.py runserver 0.0.0.0:8000
EXPOSE 8000