# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator 2.3.33.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class OnPremHdfs(Model):
    """OnPremHdfs.

    :param protocol: The protocol to use when communicating with the HDFS
     cluster. http or https. Possible values include: 'http', 'https'
    :type protocol: str or ~_restclient.models.enum
    :param namenode_address: The IP address or DNS hostname of the HDFS
     namenode. Optionally includes a port.
    :type namenode_address: str
    :param hdfs_server_certificate: The base-64 encoded TLS certificate of the
     HDFS server (Optional).
    :type hdfs_server_certificate: str
    :param kerberos_realm: The Kerberos realm.
    :type kerberos_realm: str
    :param kerberos_kdc_address: The IP address or DNS hostname
    :type kerberos_kdc_address: str
    :param kerberos_principal: The Kerberos principal to use for
     authentication and authorization.
    :type kerberos_principal: str
    :param credential_value: Either the base-64 encoded keytab file, or a
     Kerberos password, depending on the value of credentialType
    :type credential_value: str
    :param credential_type: HDFS Authentication type. Possible values include:
     'KerberosKeytab', 'KerberosPassword'
    :type credential_type: str or ~_restclient.models.HdfsCredentialType
    """

    _attribute_map = {
        'protocol': {'key': 'protocol', 'type': 'str'},
        'namenode_address': {'key': 'nameNodeAddress', 'type': 'str'},
        'hdfs_server_certificate': {'key': 'hdfsServerCertificate', 'type': 'str'},
        'kerberos_realm': {'key': 'kerberosRealm', 'type': 'str'},
        'kerberos_kdc_address': {'key': 'kerberosKdcAddress', 'type': 'str'},
        'kerberos_principal': {'key': 'kerberosPrincipal', 'type': 'str'},
        'credential_value': {'key': 'credentialValue', 'type': 'str'},
        'credential_type': {'key': 'credentialType', 'type': 'HdfsCredentialType'},
    }

    def __init__(self, protocol=None, namenode_address=None, hdfs_server_certificate=None, kerberos_realm=None, kerberos_kdc_address=None, kerberos_principal=None, credential_value=None, credential_type=None):
        super(OnPremHdfs, self).__init__()
        self.protocol = protocol
        self.namenode_address = namenode_address
        self.hdfs_server_certificate = hdfs_server_certificate
        self.kerberos_realm = kerberos_realm
        self.kerberos_kdc_address = kerberos_kdc_address
        self.kerberos_principal = kerberos_principal
        self.credential_value = credential_value
        self.credential_type = credential_type
