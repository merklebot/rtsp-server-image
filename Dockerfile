FROM python:3.8

COPY main.py main.py
RUN apt-get update && apt-get install -y nano vim gstreamer-1.0 python3-gst-1.0 gir1.2-gst-rtsp-server-1.0 libgirepository1.0-dev gcc libcairo2-dev pkg-config python3-dev gir1.2-gtk-4.0
RUN pip install PyGObject

CMD ["/bin/sh"]
