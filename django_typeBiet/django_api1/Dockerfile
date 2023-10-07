FROM python:3.7.1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
COPY requirements.txt /user/
RUN pip install --no-cache-dir -r /user/requirements.txt
RUN pip install --upgrade pip
RUN useradd -ms /bin/bash user
USER user
RUN python3 -m pip install --upgrade pip 
WORKDIR /user
COPY requirements.txt /user/
RUN pip install --no-cache-dir -r /user/requirements.txt
EXPOSE 8000
CMD 'cd /src/ python manage.py makemigrations && python manage.py migrate'