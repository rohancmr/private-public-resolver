FROM python:3.7.0
MAINTAINER Rohan Kumar (rohank@nvidia.com)

RUN mkdir -p /python
WORKDIR /python

COPY /root/private-public-resolution/app.py /python
COPY /root/private-public-resolution/requirements.txt /python
RUN pip install -r /python/requirements.txt
CMD [ "python", "./app.py" ]

