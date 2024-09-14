FROM python:3.8

COPY main.py main.py
RUN apt-get update && apt-get install -y nano vim gstreamer-1.0 python3-gst-1.0 gir1.2-gst-rtsp-server-1.0

CMD ["/bin/sh"]
