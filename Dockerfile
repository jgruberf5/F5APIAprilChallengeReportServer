FROM python:3

WORKDIR /usr/src/f5apichallengereportserver

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

ENV FLASK_APP=reportserver
ENV FLASK_ENV=production

RUN flask init-db

CMD ["flask", "run", "--with-threads", "--host", "0.0.0.0", "-p", "5000"]
