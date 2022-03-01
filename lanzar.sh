#!/bin/sh
/home/vagrant/env/bin/gunicorn --bind localhost:8000 blogclase.wsgi
