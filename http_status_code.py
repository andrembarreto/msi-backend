from enum import IntFlag


class HTTPStatusCode(IntFlag):
    SUCCESS = 0
    BAD_FORMAT = 1
    MISSING_POINTS = 2
    MISSING_BUS_LINE = 3
