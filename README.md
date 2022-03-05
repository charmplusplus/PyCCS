# PyCCS
## Python interface to CCS

Current best usage examples can be found in [examples](examples/simple_client.py) and the [tests](tests/test_server.py).

### Build
Similar to [Charm4Py](https://github.com/uiuc-ppl/charm4py), this repository requires that the Charm++ repository can be found in ```charm_src/charm```. The following commands will clone this repository and make Charm++ available for use:
```bash
$ git clone https://github.com/UIUC-PPL/pyccs
$ cd pyccs
$ git clone https://github.com/UIUC-PPL/charm charm_src/charm
```

Moreover, Charm++ must be built in the following manner for compatibility with PyCCS:
```bash
./buildold converse netlrts-linux-x86_64 --with-production -j3 --force --build-shared
```

Complete installation commands follow:
```bash
git clone git@github.com:UIUC-PPL/PyCCS.git
cd PyCCS
git clone git@github.com:UIUC-PPL/charm.git charm_src/charm
cd charm_src/charm
./buildold converse netlrts-linux-x86_64 --with-production -j3 --force --build-shared
cd ../..
python3 -m pip install --user .
```

We are working to streamline the build process.
