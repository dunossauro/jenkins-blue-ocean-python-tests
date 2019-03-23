FROM python:3.7.2

RUN pip3 install pipenv
RUN pipenv run nose2 --plugin nose2.plugins.junitxml --junit-xml
