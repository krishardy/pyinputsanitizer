import re
import logging
import collections


REGEXP_INT = re.compile(r'/^d+$/')
REGEXP_FLOAT = re.compile(r'/^d+(?:\.d+)$')
REGEXP_MAC = re.compile(r'/^[0-9a-bA-B]:[0-9a-bA-B]:[0-9a-bA-B]:[0-9a-bA-B]:[0-9a-bA-B]:[0-9a-bA-B]$/')

logger = logging.getLogger(__name__)


"""
def Sanitizer(packet_data, type_map):
    if isinstance(packet_data, (dict, collections.OrderedDict)):
        for key in packet_data.keys():
            if key in type_map:
                packet_data[key] = Sanitizer(packet_data[key], type_map[key])
            else:
                del packet_data[key]
    else:
        return type_map.sanitize(packet_data)
"""


class Input(object):
    def __init__(
            self, type_=str, regexp=None, precast_parser=None,
            postcast_parser=None, default=None, required=False):
        """
        
        :param type_: The type of value to expect (a cast to this type will be
                attempted)
        :type type_: type
        :param regexp:
        :type regexp: str or _sre.SRE_Pattern
        :param precast_parser: Callable which accepts the value and returns a
                value.  Runs before the cast to `type_` is tried.
        :type precast_parser: callable
        :param postcast_parser: Callable which accepts the value and returns a
                value.  Runs after the cast to `type_` is tried.
        :type postcast_parser: callable
        :param default: Default value to use if validation fails
        :type default: any
        """
        self._type = type_
        self.regexp = regexp
        self.precast_parser = precast_parser
        self.postcast_parser = postcast_parser
        self.default = default
        self.required = required

    def sanitize(self, value, suppress_exc=True):
        """
        
        :param value: 
        :return: 
        """
        if len(value) == 0 and self.required is True:
            return self.default

        print(re.match(self.regexp, value))

        try:
            if self.regexp and re.match(self.regexp, value) is None:
                if suppress_exc == False:
                    raise ValueError("{} failed regexp match".format(value))
                return self.default

            if callable(self.precast_parser):
                value = self.precast_parser(value)
            value = self._type(value)
            if callable(self.postcast_parser):
                value = self.postcast_parser(value)
        except Exception as e:
            if suppress_exc is False:
                raise e
            logger.warning("Sanitization of value '{}' failed.")
            return self.default

        return value


class IntInput(Input):
    def __init__(self, regexp=REGEXP_INT, **kwargs):
        super(IntInput, self).__init__(type_=int, regexp=regexp, **kwargs)


class FloatInput(Input):
    def __init__(self, regexp=REGEXP_FLOAT, **kwargs):
        super(FloatInput, self).__init__(type_=float, regexp=regexp, **kwargs)


class MACInput(Input):
    def __init__(self, regexp=REGEXP_MAC, **kwargs):
        super(MACInput, self).__init__(type_=str, regexp=regexp, **kwargs)


class ListInput(Input):
    def __init__(self, min_length=None, max_length=None, **kwargs):
        super(ListInput, self).__init__(*args, **kwargs)
        self.min_length = min_length
        self.max_lenght = max_length

    def sanitize(self, value, suppress_exc=True):
        if isinstance(value, list) is False:
            if suppress_exc == False:
                raise ValueError("{} is not a list".format(value))
            out = []
            if self.min_length is not None and self.min_length > 0:
                out = [self.default] * self.min_length
            return out

        out = []
        for i in xrange(value):
            out.append(super(ListInput, self).sanitize(value[i], suppress_exc))

        if len(value) < self.min_length:
            out.extend([self.default] * (self.min_length - len(value)))

        if len(value) > self.max_length:
            out = out[:self.max_length]

        return out

