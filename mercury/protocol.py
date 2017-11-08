import abc


class Capabilities(object):
    CHANNELS = False
    SEND_MESSAGES = False


class Protocol(object, metaclass=abc.ABCMeta):
    prefix = "new_protocol"
    capabilities = Capabilities

    @abc.abstractmethod
    def connect(self):
        pass

    @abc.abstractmethod
    def disconnect(self):
        pass

    def send_message(self, target, contents):
        raise NotImplementedError("This protocol has not implemented sending messages")
