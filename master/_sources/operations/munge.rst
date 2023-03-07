.. _munge-ops:

================
Munge operations
================

The ``slurmctld`` charm contains an internal `etcd3 <https://etcd.io>`_ server
that, among other uses, stores the `Munge <https://github.com/dun/munge/>`_
key.

The etcd server has authentication enabled by default, to protect the Munge
key. In order to be able to retrieve the Munge key, an etcd account is
required. OSD provides the Juju action ``etcd-create-munge-account`` on the
``slurmctld`` charm to automate the creation of such an account.

By default, etcd is started using plain HTTP. It is possible to use HTTPS by
supplying the necessary certificates to ``slurmctld``.


Creating an etcd account
========================

To create an etcd account to query the Munge key requires a username and
password to be specified:

.. code-block:: bash

   $ juju run-action slurmctld/leader etcd-create-munge-account user="theusername" password="aVerySafePassword!" --wait
   unit-slurmctld-7:
     UnitId: slurmctld/7
     id: "654"
     results:
       Stdout: |
         User theusername created
         Role munge-readers is granted to user theusername
       created-new-user: theusername
     status: completed
     timing:
       completed: 2022-05-12 17:57:44 +0000 UTC
       enqueued: 2022-05-12 17:57:41 +0000 UTC
       started: 2022-05-12 17:57:44 +0000 UTC


Querying the munge key
======================

The etcd server is running on the ``slurmctld`` node and listening on the port
``2379``. The Munge key is stored at ``munge/key`` entry. The Munge key is
binary data and is stored encoded in a base 64 representation. The examples
below demonstrate how to query the secret key and decode them to be used.

Using Bash
----------

It is possible to get the Munge key using Bash, with ``curl`` and ``jq``.
First, you need to get an access token for your username and then query the
key:

.. code-block:: bash

   user=theusername
   pass=aVerySafePassword!
   host=10.107.185.126
   port=2379

   token=$(curl -L -s -X POST "$host:$port/v3/auth/authenticate" -d '{"name":"'"$user"'", "password":"'"$pass"'"}' | jq .token | tr -d '"')
   key=$(printf munge/key | base64)

   munge_key=$(curl -L -s -X POST "$host:$port/v3/kv/range" -H "Authorization: ${token}" -d '{"key":"'$key'"}' | jq .kvs[0].value | tr -d '"' | base64 -d)

As an example, running the above commands will result in:

.. code-block:: bash

   $ echo $munge_key # it is base64 encoded
   +CzBbB5c+WduA0bSNb5x6+U3Mj/QuladAFH5vqyyQyvyA5YUcUikz64YEakqB852D7Ml5jmCOuxpa0VXoYMeiaRFRw2WFyR+6H66buQeCBClgfk4t0QQKKRZsaPjVojkmhoNTgQz/8mseHDnrOpxyTEsFeAw9kMzhraK1fvHOgMbDDDnkmN1oOscNhBmnreQmcr+gy2NliGiRjCjyMh6TgwJqQCBU/4LCSs+cetbvKLMdj+7X8PbYpSALx8x4JXUjNj9sv1jLLu3f684P/G3unB709hhNvj3NoSPTZ68FhgjxqUFtXF91/Dce0hJForv9EAwgyTHmCJ+WNUI5ag+1P454nWFYqJkXTSX5gvPYBCwTGbOAjgLdyPa+SGOXeHutpCJtPjbpOtL9PkP+T5+mQrgDE1KjkDYLdlIyobVNUXfziPH82uSZft8ZRuke+vP+GpExSWsdj7sYuVAhUu9Utkfiyy1hVdmKoXeppJopjnj2J+Zmaa8/qvxYXNhmrbPdp8hadSdu2XRrNGu0AbYAGUsLrvSOSKc9J8+tkjFa5Qzcn8xR8HSWK12/mjF941NyCxDLqkfD6066KmL3ARqxdU7qVjZSMlIF8UzCiKIH2WDHkZa5LIV7Cj7ZxUTaAIjdAxmwr4ajnRqK1GFI736F+BqTWLRAuXM18S4r7KDjBYSUMNiXdL7qqY3Ao/LkniraGr4CxIBApicV0SuWfMafwoCb59oMNzyaCAiuI/JjFPqxD0Tn36ngtRHgdQnESuZeTSV68b7tOBc+MkzbUhBzmWy9TGSF2gsq6hoxIRj1oYdrTpwPQrfut4VLOkiWnJuJtaKX55z3c/o3bDZ1Ykd/unUL1vdDjlyo6VrNRu+/ijttiWAGm0PJOoMMe3PEqBjDBJAHdudlyez+bsUvH+Mm3Vnuu1gIlQ4vzxNcX1kUQC/8Mef7LjaRhD1DwUhPFw0E/AEhW0wKRuPD5vEGU1nlJLZbGcEy5x6I0qhyV/pr/SbLj5W6fTuQ5XVoHbKe5fh4U7iX7JDb1UlRZWoqZ9jbHqoWwwwkTe1VEr+tXtDFU4PJ8aEcyO4qRrSibKfXd+EYWJQ0Y+BRt+iRohXjy5CV9PMctwuciZhWMP0DGoYPfsObqoCLgLF56Gu6uVOhyC0AFrEm2LAOWzVlsxENCK4jYMtznwrRV4mwPVsFLZqCVIaAwW/KDfse7Bs2Y8RcA6Jl/Rv/kk2byyFhy230GqMcXiNEtCCViJvC/H6+V58IygJkpftrncFXafQ0u+ti/4U3ZRDD4Hfy3tepKxo9Sj9p8BBHZT7jVFYsQh3TVJqZow5lPRuumM0rz2k4izC9nW/TxGe/bmvPGzQxfQDYiEgQg==
   # decode the key and save it to a file:
   $ echo $munge_key | base64 -d > munge.key

.. note::

   The etcd key must be base64 encoded when using ``curl``.

.. note::

   If the server is using HTTPS with a self-signed certificate, or a non-public
   Certificate Authority (CA), you need to supply the public certificate in the
   ``curl`` commands by adding ``--cacert path/to/cert.crt``.


Using Python
------------

To get the Munge key in Python, we suggest using the `etcd3gw
<https://opendev.org/openstack/etcd3gw>`_ as a starting point:

.. code-block:: python

   from etcd3gw.client import Etcd3Client
   from etcd3gw.exceptions import Etcd3Exception


   class Etcd3AuthClient(Etcd3Client):
       """Handle etcd3 requests with auth."""
       def __init__(self, host='localhost', port=2379, protocol="http",
                    ca_cert=None, cert_key=None, cert_cert=None, timeout=None,
                    username=None, password=None, api_path="/v3/"):
           """Initialize class."""
           super(Etcd3AuthClient, self).__init__(host=host, port=port,
                                                 protocol=protocol,
                                                 ca_cert=ca_cert,
                                                 cert_key=cert_key,
                                                 cert_cert=cert_cert,
                                                 timeout=timeout,
                                                 api_path=api_path)
           self.username = username
           self.password = password

       def authenticate(self):
           """Authenticate the client."""
           if 'Authorization' in self.session.headers:
               del self.session.headers['Authorization']

           response = super(Etcd3AuthClient, self).post(
               self.get_url('/auth/authenticate'),
               json={"name": self.username, "password": self.password}
           )

           self.session.headers['Authorization'] = response['token']

       def post(self, *args, **kwargs):
           """Wrap the internal post function with authentication."""
           try:
               return super(Etcd3AuthClient, self).post(*args, **kwargs)
           except Etcd3Exception as e:
               if self.username and self.password:
                   print("# etcd: Might need to (re)authenticate: %r:\n%s",
                         e, e.detail_text)
                   self.authenticate()
                   return super(Etcd3AuthClient, self).post(*args, **kwargs)
               raise


   client = Etcd3AuthClient(host="10.107.185.126",
                            username="theusername",
                            password="aVerySafePassword!")
   client.authenticate()
   munge_key_encoded = client.get(key="munge/key")[0]
   munge_key = b64decode(munge_key_encoded)

.. note::

   The Python3 code does not automatically identify if the connection uses HTTP
   or HTTPS. By default, the library assumes HTTP. If the server is using HTTPS
   you need to specify ``protocol="https"`` when instantiating the client:

   .. code-block:: python

      client = Etcd3AuthClient(host="10.107.185.126", protocol="https",
                               username="theusername",
                               password="aVerySafePassword!")

Configuring HTTPS
=================

To use HTTPS for the connection, you need to supply the TLS certificates to
``slurmctld-charm`` via Juju Configuration options. You need to supply the
public certificate (a ``.crt`` file) and the private key (a ``.key`` file).
Additionally, you must provide the Certificate Authority's (CA) public
certificate (another ``.crt`` file) if using self-signed certificates or a
non-public CA.

To configure these certificates:

.. code-block:: bash

   # the public and private TLS files
   $ juju config slurmctld tls-cert="$(cat tls.crt)"
   $ juju config slurmctld tls-key="$(cat tls.key)"

   # the optional CA public certificate
   $ juju config slurmctld tls-ca-cert="$(cat CA.crt)"
