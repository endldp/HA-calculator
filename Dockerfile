FROM python:3.11-alpine
WORKDIR /opt/calculator
COPY rootfs/opt/calculator /opt/calculator
RUN pip install --no-cache-dir flask gunicorn
COPY run.sh /run.sh
RUN chmod +x /run.sh
EXPOSE 8099
CMD ["/run.sh"]
