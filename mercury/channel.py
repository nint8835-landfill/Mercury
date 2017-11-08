import abc


class Channel(object, metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def send_message(message):
        pass