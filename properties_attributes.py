


class Connector:

    def __init__(self, source):
        self.source = source
        self._timeout = 60
        self.__private_timeout = 30


conn = Connector("localhost")
print(conn._timeout)
print(conn.__private_timeout)

