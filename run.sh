#!/bin/sh
set -e
if [ -f /data/options.json ]; then
  export CALC_OPTIONS=$(cat /data/options.json)
fi
chown -R 1000:1000 /data
exec gunicorn -w 2 -b 0.0.0.0:8099 app:app
