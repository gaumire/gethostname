FROM alpine

COPY . /app

RUN apk add --no-cache py-pip \
	&& pip install flask && pip install simplejson

ENV FLASK_APP /app/app.py

ENTRYPOINT ["/usr/bin/flask"]

CMD ["run", "-h 0.0.0.0"]

EXPOSE 5000
