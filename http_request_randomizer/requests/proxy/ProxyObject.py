from enum_custom import MultiValueEnum


class ProxyObject(object):
    def __init__(self, source, ip, port, anonymity_level, country=None,  protocols=[], tunnel=False):
        """ Proxy object implementation - base for all the parsing logic

        :param source: The name of the proxy list from which the proxy was collected
        :param ip: The IP address of the proxy
        :param port: The port number of the proxy
        :param anonymity_level: The anonymity level of the proxy. Can be any of :AnonymityLevel
        :param country: Alpha-2 country code of the country in which the proxy is geo-located
        :param protocols:  A list of protocols that the proxy supports. May contain one or more of {HTTP, HTTPS, SOCKS5, SOCKS6}
        :param tunnel: Whether or not the proxy supports tunneling to HTTPS target URLs.
        """
        self.source = source
        self.ip = ip
        self.port = port
        self.anonymity_level = anonymity_level
        self.country = country
        self.protocols = protocols
        self.tunnel = tunnel

    def getAddress(self):
        return "{0}:{1}".format(self.ip, self.port)

    def __str__(self):
        """ Method is heavily used for Logging - make sure we have a readable output

        :return: The address representation of the proxy
        """
        return "{0} | {1}".format(self.getAddress(), self.source)

    def print_everything(self):
        print("Address: {0} | Src: {1} | | Country: {2} | Anonymity: {3} | Protoc: {4} | Tunnel: {5}" \
              .format(self.getAddress(), self.source, self.country, self.anonymity_level, self.protocols,
                      self.tunnel))


class AnonymityLevel(MultiValueEnum):
    """
    TRANSPARENT: The proxy does not hide the requester's IP address.
    ANONYMOUS: The proxy hides the requester's IP address, but adds headers to the forwarded request that make it clear that the request was made using a proxy.
    ELITE: The proxy hides the requester's IP address and does not add any proxy-related headers to the request.
    UNKNOWN: The proxy anonymity capabilities are not exposed
    """
    TRANSPARENT = 'transparent', 'transparent proxy', 'LOW'
    ANONYMOUS = 'anonymous', 'anonymous proxy'
    ELITE = 'elite', 'elite proxy', 'HIGH'
    UNKNOWN = 'unknown', 'none'
