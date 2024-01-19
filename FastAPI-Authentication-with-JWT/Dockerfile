FROM python:3.7
WORKDIR /code

RUN apt-get update && \
    apt-get install -y nano net-tools && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
    
RUN python3 -m pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
EXPOSE 8000
COPY . .
CMD [ "python3", "main.py" ]