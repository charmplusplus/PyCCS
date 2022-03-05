Simple example to mirror that shown in the [charm repository](https://github.com/UIUC-PPL/charm/tree/main/examples/converse/ccstest).

Usage:
```bash
python3 simple_client.py server_ip server_port
```

This client assumes that the server in that example is running as shown below:
```bash
./charmrun +p2 ./server ++server ++server-port 10000
```

Then, the client can be run like so:
```bash
python3 simple_client.py 127.0.0.1 10000
```

