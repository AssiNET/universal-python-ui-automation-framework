import time


class IceAssertionError(AssertionError):
    def __init__(self, message, image):
        self.message = time.strftime("%X") + " " + message
        self.image = image

    def __str__(self):
        return repr(self.message)
