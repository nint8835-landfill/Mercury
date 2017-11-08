from .exceptions import InvalidProtocolException, UnsupportedOperationException, DuplicateProtocolException


class ProtocolManager(object):

    def __init__(self):
        self._protocols = {}

    def register_protocol(self, protocol):
        if protocol.prefix in self._protocols:
            raise DuplicateProtocolException("There is already a protocol registered with the prefix \"{}\"".format(protocol.prefix))
        self._protocols[protocol.prefix] = protocol

    def send_message(self, target, contents):
        protocol_prefix = target.split(":")[0]
        target_without_prefix = ":".join(target.split(":")[1:])

        if protocol_prefix not in self._protocols:
            raise InvalidProtocolException("Unknown protocol \"{}\"".format(protocol_prefix))
        protocol = self._protocols[protocol_prefix]
        if not protocol.capabilities.SEND_MESSAGE:
            raise UnsupportedOperationException("The protocol \"{}\" does not support the \"send_message\" operation".format(protocol_prefix))
        protocol.send_message(target_without_prefix, contents)
