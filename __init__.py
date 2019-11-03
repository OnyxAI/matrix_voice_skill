from os.path import dirname, join

from onyx.skills.core import OnyxSkill
from onyx.util.log import getLogger

import time


__author__ = ''

LOGGER = getLogger(__name__)

try:
    from matrix_lite import led
except:
    LOGGER.error("Impossible to load matric library !")
    pass

class Matrix_VoiceSkill(OnyxSkill):
    def __init__(self):
        super(Matrix_VoiceSkill, self).__init__(name="Matrix_VoiceSkill")


    def initialize(self):
        LOGGER.info("Matrix_Voice Skill initialize")

        self.emitter.on('onyx_detect', self.handle_detect)
        self.emitter.on('onyx_detect_finish', self.handle_detect_finish)
        self.emitter.on('onyx_recognizer:utterance', self.handle_detect_finish)
        self.emitter.on('onyx_detect_error', self.handle_detect_error)
        self.emitter.on('intent_failure', self.handle_detect_error)

    def handle_detect(self, message):
        try:
            led.set('blue')
        except:
            LOGGER.error("Impossible to set light to blue")
            pass

    def handle_detect_finish(self, message):
        try:
            let.set()
        except:
            LOGGER.error("Impossible to set light to nothing")
            pass

    def handle_detect_error(self, message):
        try:
            led.set('red')
            time.sleep(5)
            let.set()
        except:
            LOGGER.error("Impossible to set light to red")
            pass

    def stop(self):
        pass

def create_skill():
    return Matrix_VoiceSkill()
