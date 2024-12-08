from pyccs import Server
import pytest
from unittest.mock import patch, Mock
import ctypes 


#make sure server is running before running these tests 

@pytest.fixture
def connected_server():
  server = Server('127.0.0.1', 10000)
  server.connect()
  yield server

def test_construction():
  import ipaddress
  s = Server('192.168.0.1', 500)
  assert s is not None

  addr = ipaddress.IPv4Address('192.168.0.1')

  s = Server(addr, 500)
  assert s is not None

  addr = ipaddress.IPv6Address('2001:db8:3333:4444:5555:6666:7777:8888')

  s = Server(addr, 500)
  assert s is not None

def test_connect():
  server = Server('127.0.0.1', 10000)
  retval = server.connect()
  assert retval == 0

def test_sendrecv(connected_server):
  send_hdlr = "ping\0".encode('ascii')
  send_msg = "ping\0".encode('ascii')
  retval = connected_server.send_request(send_hdlr, 0, send_msg)
  assert retval == 0
  response = connected_server.receive_response(35,1)
  assert response == b'hello ping from processor 0\n\x00\x00\x00\x00\x00\x00\x00'


@pytest.mark.skip(reason="Server currently has no functionality to handle broadcast")
def test_broadcast(connected_server):
  send_hdlr = "ping\0".encode('ascii')
  send_msg = "ping\0".encode('ascii')

  retval = connected_server.send_broadcast_request(send_hdlr, send_msg)
  assert retval == 0

  response = connected_server.receive_response(35,1)
  assert response == b'hello ping from processor 0\n\x00\x00\x00\x00\x00\x00\x00'
  response = connected_server.receive_response(35,1)
  assert response == b'hello ping from processor 1\n\x00\x00\x00\x00\x00\x00\x00'

def test_metadata(connected_server):
  n_pes = connected_server.num_pes()
  n_nodes = connected_server.num_nodes()
  node_size = connected_server.node_size(0)

  assert n_pes == 2
  assert n_nodes == 2
  assert node_size == 1

def test_receive_response_msg(connected_server):
  send_hdlr = "ping\0".encode('ascii')
  send_msg = "steven\0".encode('ascii')

  retval = connected_server.send_request(send_hdlr, 0, send_msg)
  assert retval == 0
  responsemsg = connected_server.receive_response_message()
  assert responsemsg == b'hello steven from processor 0\n\x00'

  retval = connected_server.send_request(send_hdlr, 1, send_msg)
  assert retval == 0 
  responsemsg = connected_server.receive_response_message()
  assert responsemsg == b'hello steven from processor 1\n\x00'
