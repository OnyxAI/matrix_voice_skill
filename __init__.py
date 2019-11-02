from os.path import dirname, join

from onyx.skills.core import OnyxSkill
from onyx.util.log import getLogger

__author__ = ''

LOGGER = getLogger(__name__)

class Matrix_VoiceSkill(OnyxSkill):
    def __init__(self):
        super(Matrix_VoiceSkill, self).__init__(name="Matrix_VoiceSkill")


    def initialize(self):
        LOGGER.info("Matrix_Voice Skill initialize")

    def stop(self):
        pass

def create_skill():
    return Matrix_VoiceSkill()
