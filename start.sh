#!/bin/bash
./wait-for-it.sh db:3306
exec gunicorn -w 1 -b 0.0.0.0:8000 "src:create_app()"
