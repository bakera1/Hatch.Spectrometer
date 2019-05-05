import logging
import picamera
from fraction import Fraction

class Camera:

    def __init__(self):

        self.logger = logging.getlooger('Spectrometer')
        self.logger.info("initialising camera")
        self.camera = picamera.PiCamera()

    def take_picture(self, name, shutter=100000):

        try:
            self.logger.info("allowing camera to warmup")

            #TODO: make these configurable
            self.camera.vflip = True
            self.camera.framerate = Fraction(1, 2)
            self.camera.shutter_speed = shutter
            self.camera.iso = 100
            self.camera.exposure_mode = 'off'
            self.camera.awb_mode = 'off'
            self.camera.awb_gains = (1, 1)
            self.time.sleep(3)
            self.logger.info("capturing image")
            self.camera.capture(name, resize=(1296, 972))
        finally:
            self.camera.close()
        return name
