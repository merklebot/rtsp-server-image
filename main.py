import gi
gi.require_version('Gst', '1.0')
gi.require_version('GstRtspServer', '1.0')
from gi.repository import Gst, GstRtspServer, GObject

Gst.init(None)

class CustomRTSPMediaFactory(GstRtspServer.RTSPMediaFactory):
    def __init__(self):
        super(CustomRTSPMediaFactory, self).__init__()

    def do_create_element(self, url):
        # This is the GStreamer pipeline that will generate the video stream
        pipeline_str = (
            'avfvideosrc ! '
            'video/x-raw,width=640,height=480,framerate=30/1 ! '
            'videoconvert ! '
            'x264enc speed-preset=ultrafast tune=zerolatency bitrate=500 ! '
            'rtph264pay name=pay0 pt=96 config-interval=1'
        )
        return Gst.parse_launch(pipeline_str)

def main():
    server = GstRtspServer.RTSPServer()
    server.props.service = "8554"

    factory = CustomRTSPMediaFactory()
    factory.set_shared(True)

    mount_points = server.get_mount_points()
    mount_points.add_factory("/test", factory)

    server.attach(None)

    print("RTSP server is streaming at rtsp://localhost:8554/test")

    loop = GObject.MainLoop()
    loop.run()

if __name__ == '__main__':
    main()
