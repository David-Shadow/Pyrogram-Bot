FROM python:3.9-slim-bullseye

COPY . .
RUN apt update -y && apt upgrade -y
RUN apt install git -y

RUN pip3 install --no-cache-dir -r requirements.txt

RUN cd /
RUN mkdir /RBot
WORKDIR /RBot
COPY start.sh /start.sh
CMD ["bash","/start.sh"]
