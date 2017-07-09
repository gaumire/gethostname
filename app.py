#!/usr/bin/env python

from flask import Flask
import socket
import simplejson as json
import uuid

app = Flask(__name__)


@app.route('/')
def gethostname():
    """Return hostname."""
    data = {}
    hostname = socket.gethostname()
    data['hostname'] = hostname
    return json.dumps(data)


@app.route('/uuid')
def getuuid():
    """Return hostname & uuid."""
    data = {}
    hostname = socket.gethostname()
    uuid_data = str(uuid.uuid4())
    data['hostname'] = hostname
    data['uuid'] = uuid_data
    return json.dumps(data)


@app.route('/secret')
def getsecret():
    """Return secrts if any & uuid."""
    data = {}
    hostname = socket.gethostname()
    try:
        secret = open('/run/secrets/mysecret').read()
        if secret is not None:
            data['hostname'] = hostname
            data['secret'] = secret
            return json.dumps(data)

        else:
            data['error'] = 'No secret available!'
            return json.dumps(data)
    except Exception as e:
        data['error'] = e
        return json.dumps(data)
