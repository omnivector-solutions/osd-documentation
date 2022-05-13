.. _munge-ops:

================
Munge operations
================

The ``slurmctld`` charm contains an internal `etcd3 <https://etcd.io>`_ server
that, among other uses, stores the `Munge <https://github.com/dun/munge/>`_
key.

The etcd server has authentication enabled by default, to protect the Munge
key. In order to be able to retrieve the Munge key, an etcd account is
required.  OSD provides Juju action ``etcd-create-munge-account`` on the
``slurmctld`` charm to automate the creation of such an account.


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
``2379``. The Munge key is stored at ``munge/key`` entry. The examples below
demonstrate how to query the secret key.

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

   token=$(curl -L -s -X POST "$host:$port/v3/auth/authenticate" -d '{"name":"'"$user"'", "password":"'"$pass"'"}' | jq .token)
   token=${token//\"/}
   key=$(printf munge/key | base64)

   munge_key=$(curl -L -s -X POST "$host:$port/v3/kv/range" -H "Authorization: ${token}" -d '{"key":"'$key'"}' | jq .kvs[0].value)

As an example, running the above commands will result in:

.. code-block:: bash

   $ echo $munge_key
   "NzI5dVpXcysrWlEvYjNzWUFNbGluaWxITm44eGlLRStLWWtpTzRNNHIwT3lKV05sandVRFVsTHZTTjRkQ2dkWXA1R0t6VGk4Nks3blZvaHBXVy9EMEE1TTNOdGlpMjF0SEN4QW1zTm1VdFYxa01tYTd3UlVEcGxGRnBGYmR6MkZwa3daUGtreW5YUzY1U000dEptdWdBSGV5eGg1eHM1Q2Ryc3l3VERQL1VTOXNDdm5TalBncGtPdTNUc2xMQmVVcEtzYnJ6cUtTbTZLaFBlZWNZYXEwTGMwTzRJYnNqTEpNbTZEWXpQbkU5UGFSL2ZMdDMxU29PRjZsTHgyMzRpaCtmZm5MODlSNXc3SjAvcnVxZGZvU3NlQkNvekRHMlRjZG1LeXRPWUgxNndqUWdPUW96eHJ2SVFmUllQRlBDVkxHMTlHUndDSzBWRDRWR09CRGRFZEtwUTl5Q2QxcjFYUzhjTkdhTUNuRHFQenJsTDBNbzlncldUU3g4ZTZHTnhOeDZWT2FvL3E3SmFXWllMd1lLRHpkUHZ5bkUzVXBpS2lBTlNQbDd2a1JVYTFYNDNKUWFQdS8yTGtybUczOWUzK2tpS2JVRjJWMjV3aExEeHA2a2d1NDRWbE1jdGErcFZuR2Q2Zk1vYmdBVDd1eHJSMUJuUDAzUHhhTXE4YzlzNjVmNzlDUXpaZkt1V3drYm1pTmxOL3lsaU5ueDNnMjJOQ2JhVGgvcUdWdVB3Yk94bU9yMkNGTFgvbjJuV1U2ZkhGK285QUpROVpVa1VqWkt4WWJLUUlxdG9Ga29KWnMxKzRGa0FGSUNSMEk4YkNZSTAyU3hIZkx4cGpJWTNuY1IvQUx2OUlHSkVjTjNWVHRnVlJ5UlRWeTZUYXEweFZxT2JGWHlBUGwybWltS3RVZWlSNEc5RTZtL0w1ZGdIUVA0TkRRYzNqVnRBeTRDSzFXQUZhVE0yNWVEai9zOUNuV3lBOVRPekJwbVYvZE9kN0xCR3JFNE9wM3NQSUg4Nk1TTkpNaFY3TFl2dmhJT2FYdUlJSTAwZjAweVVENUV4Y0hVOEdMT1VmUDlMTkFCS1FiMFhDWVVXS1NaTWtSUUx1UzI2MGxuWFhBUkIxd2xLWVo0dTdZZ2IzWnE3WGh2L3BqblZOV2FvUjR0dWJBQlJBS2JiRUxJMlZmazNpNTRtdkxvdnRyN1hXRzMwUGNIbXRQRE1hdFliWlQ5TFVDTUZ6NzZ3MjFlK3ZhY3cvREZLd0ZwNEdIV29BRzRSYUxORHBxM1FjVzZ0WXdVd0FpbXFDNitwblJhTjNsZ1ExNXpCNWo4MGQzTUJMaHZnZDVweExhS0ZoeHFRWmU2QXdGQ0xWTFJBY2Q0b0Zkb3RNMzNGUUVGYjFDV2tFNUNMVFQwZU1yYm1zWFdsMVlWdVlkWW0vYWc4bkpYdC9VMDJNeHV0bG80N1Z6aXhDSmdvUzd3dmFCaXhzL1Q4MlJzWlhSSWNvN2Y1cVdkdW0wMm5kT0FJK2NtbUZjd1Z4b1hnZ2hvYVIzbEJ6M3A1NUZmc0pteVVpci9GUHVTekR5eG1DS3A0eUs5aUxmakwxL3VPK2ltK0VQdUNSWHgwRS9aL1BSZkJuQ29jbk5RUlZlV0lSNWtDK1piK2FlN0ZzRVhEazVJcHU5eDRZcm5KUHhSTGY0L3JVTVBRRGEzaDB3TlU2N3BwL1JuN1VlWHRCNXdLanorUUJWNGI5aEljb0U0bHpHRVdUTkg2QXlTb1NNc0tYblQ1VDliWk9SRTFsVzdnZVY4VHptK0hTbjhDNWJmMzA4NmhFRE81dG1EcmlTdz09"


.. note::

   The etcd key must be base64 encoded when using ``curl``.


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
   munge_key = client.get(key="munge/key")[0]
