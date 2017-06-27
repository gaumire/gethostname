#!/usr/bin/env python

from flask import Flask
import socket
app = Flask(__name__)


@app.route('/')
def gethostname():
    """Return hostname."""
    hostname = socket.gethostname()
    return hostname
