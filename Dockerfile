FROM python:3.7.0
MAINTAINER Rohan Kumar (rohank@nvidia.com)

RUN mkdir -p /python
WORKDIR /python

RUN git clone https://github.com/rohancmr/private-public-resolver.git && \
	pip install -r /python/private-public-resolver/requirements.txt

WORKDIR /python/private-public-resolver

CMD [ "python", "./app.py" ]

