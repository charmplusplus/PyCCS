from typing import Union, Optional
import logging
from ipaddress import IPv4Address, IPv6Address
from dataclasses import dataclass, field
from ctypes import Structure, c_int, POINTER, c_char, c_uint, c_byte, CDLL, pointer
from .auth import CcsSec_secretKey, CCS_RAND_state
IPAddress = Union[IPv4Address, IPv6Address]

DEFAULT_TIMEOUT_PERIOD = 60

class SocketIP(Structure):
    _fields_ = [("tag", c_int)]

class CcsServer(Structure):
    _fields_ = [("hostAddr", c_char * 128),
                ("hostIP", SocketIP),
                ("hostPort", c_uint),
                ("isAuth", c_int),
                ("level", c_int),
                ("key", CcsSec_secretKey),
                ("clientID", c_int),
                ("clientSalt", c_int),
                ("replySalt", c_int),
                ("rand", CCS_RAND_state),
                ("numNodes", c_int),
                ("numPes", c_int),
                ("numProcs", POINTER(c_int)),
                # NOTE: SOCKET is defined as int
                ("replyFd", c_int)]

def _construct_address(addr: str) -> IPAddress:
    try:
        return IPv4Address(addr)
    except AddressValueError:
        # will throw again if addr is invalid
        # address
        return IPv6Address(addr)

def _find_library() -> str:
    import os
    import sys

    local_dir = os.path.join(sys.prefix, 'lib')
    try:
        lib_path = os.path.join(local_dir, 'libccs-client.so')
        assert os.path.exists(lib_path)
        return lib_path
    except:
        raise

@dataclass
class ConnectionInfo:
    host_ip: IPAddress
    host_port: int = 0
    secret_key: bytearray = None
    num_nodes: int = 0
    num_pes: int = 0
    node_first: dict[int, int] = field(default_factory=dict)
    node_size: dict[int, int] = field(default_factory=dict)

@dataclass
class AuthInfo:
    key: bytearray
    level: int
    client_id: int
    client_salt: int

class Server:
    def __init__(self, address: Union[IPv4Address, IPv6Address, str],
                 port: int,
                 secret_key: Optional[bytearray] = None
                 ):

        if isinstance(address, str):
            address = _construct_address(address)

        self._lib = CDLL(_find_library())
        self.is_timeout_set = False
        self.timeout_period = DEFAULT_TIMEOUT_PERIOD
        self.conn_info = ConnectionInfo(address, port, secret_key)
        self.print_debug = False
        self._server = None

    def _server_create(self) -> CcsServer:
        return CcsServer()

    def connect(self, timeout: int = DEFAULT_TIMEOUT_PERIOD) -> int:
        if self._server is None:
            self._server = self._server_create()
        logging.getLogger().debug('Attempting a connection...')
        ip = str(self.conn_info.host_ip).encode('ascii')
        port = self.conn_info.host_port
        retval = self._lib.CcsConnectWithTimeout(pointer(self._server),
                                                 ip,
                                                 port,
                                                 None,
                                                 timeout
                                                 )
        return retval

    def send_request(self, handler_id: bytes, pe: int, msg: bytes) -> int:
        encoded_id = handler_id
        assert self._server is not None
        return self._lib.CcsSendRequest(pointer(self._server),
                                        encoded_id,
                                        pe,
                                        len(msg),
                                        msg
                                        )

    def send_broadcast_request(self, handler_id: bytes, msg: bytes) -> int:
        assert self._server is not None
        return self._lib.CcsSendBroadcastRequest(pointer(self._server),
                                                 handler_id,
                                                 len(msg),
                                                 msg
                                                 )

    def receive_response(self, max_size: int, timeout: int = DEFAULT_TIMEOUT_PERIOD) -> bytearray:
        buf = bytearray(max_size)
        char_array = c_char * max_size
        self._lib.CcsRecvResponse(pointer(self._server),
                                  max_size,
                                  char_array.from_buffer(buf),
                                  timeout
                                  )
        return buf

    def num_nodes(self) -> int:
        return self._lib.CcsNumNodes(pointer(self._server))

    def num_pes(self) -> int:
        return self._lib.CcsNumPes(pointer(self._server))

    def node_size(self, node: int) -> int:
        return self._lib.CcsNodeSize(pointer(self._server), node)
