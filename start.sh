#!/bin/bash
exec gunicorn project_name.wsgi:application \
    --bind 0.0.0.0:$PORT \
    --workers 3
