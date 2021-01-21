from kivy.app import App
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.graphics.texture import Texture
from kivy.uix.image import Image
from kivy.clock import Clock

import cv2

class MainScreen(Widget):

    image_texture = ObjectProperty(None)
    image_capture = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.image_capture = cv2.VideoCapture(0)
        Clock.schedule_interval(self.update, 1.0 / 30)

    def analysis_screen(self, dt):
        ret, frame = self.image_capture.read()
        if ret:
            buf1 = cv2.flip(frame, 0)
            buf = buf1.tostring()
            image_texture = Texture.create(
                size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
            image_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
            self.image_texture = image_texture


class ImageApp(App):
    def __init__(self, **kwargs):
        super(ImageApp, self).__init__(**kwargs)
        self.title = ''

    def build(self):
        return ImageWidget()