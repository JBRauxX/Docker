FROM python:3.7.4
RUN apt-get update -y && apt-get upgrade -y
RUN pip install --upgrade pip
COPY requirements.txt /.
RUN pip install -r /requirements.txt
RUN useradd -ms /bin/bash user
USER user
RUN python3 -m pip install --upgrade pip 
WORKDIR /user
COPY requirements.txt /user/
RUN pip install -r /user/requirements.txt