.. _bigip_snmp_community:


bigip_snmp_community - Manages SNMP communities on a BIG-IP.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.6


.. contents::
   :local:
   :depth: 2


Synopsis
--------

* Assists in managing SNMP communities on a BIG-IP. Different SNMP versions are supported by this module. Take note of the different parameters offered by this module, as different parameters work for different versions of SNMP. Typically this becomes an interest if you are mixing versions ``v2c`` and ``3``.


Requirements (on host that executes module)
-------------------------------------------

  * f5-sdk >= 3.0.9


Options
-------

.. raw:: html

    <table border=1 cellpadding=4>
    <tr>
    <th class="head">parameter</th>
    <th class="head">required</th>
    <th class="head">default</th>
    <th class="head">choices</th>
    <th class="head">comments</th>
    </tr>
                <tr><td>access<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>ro</li><li>rw</li><li>read-only</li><li>read-write</li></ul></td>
        <td><div>Specifies the user&#x27;s access level to the MIB.</div><div>When creating a new community, if this parameter is not specified, the default is <code>ro</code>.</div><div>When <code>ro</code>, specifies that the user can view the MIB, but cannot modify the MIB.</div><div>When <code>rw</code>, specifies that the user can view and modify the MIB.</div>        </td></tr>
                <tr><td>community<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Specifies the community string (password) for access to the MIB.</div><div>This parameter is only relevant when <code>version</code> is <code>v1</code>, or <code>v2c</code>. If <code>version</code> is something else, this parameter is ignored.</div>        </td></tr>
                <tr><td>ip_version<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>4</li><li>6</li></ul></td>
        <td><div>Specifies whether the record applies to IPv4 or IPv6 addresses.</div><div>When creating a new community, if this value is not specified, the default of <code>4</code> will be used.</div><div>This parameter is only relevant when <code>version</code> is <code>v1</code>, or <code>v2c</code>. If <code>version</code> is something else, this parameter is ignored.</div>        </td></tr>
                <tr><td>name<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Name that identifies the SNMP community.</div><div>When <code>version</code> is <code>v1</code> or <code>v2c</code>, this parameter is required.</div><div>The name <code>public</code> is a reserved name on the BIG-IP. This module handles that name differently than others. Functionally, you should not see a difference however.</div>        </td></tr>
                <tr><td>oid<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Specifies the object identifier (OID) for the record.</div><div>When <code>version</code> is <code>v3</code>, this parameter is required.</div><div>When <code>version</code> is either <code>v1</code> or <code>v2c</code>, if this value is specified, then <code>source</code> must not be set to <code>all</code>.</div>        </td></tr>
                <tr><td>partition<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>Common</td>
        <td></td>
        <td><div>Device partition to manage resources on.</div>        </td></tr>
                <tr><td>password<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td></td>
        <td><div>The password for the user account used to connect to the BIG-IP. You can omit this option if the environment variable <code>F5_PASSWORD</code> is set.</div></br>
    <div style="font-size: small;">aliases: pass, pwd<div>        </td></tr>
                <tr><td>port<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Specifies the port for the trap destination.</div><div>This parameter is only relevant when <code>version</code> is <code>v1</code>, or <code>v2c</code>. If <code>version</code> is something else, this parameter is ignored.</div>        </td></tr>
                <tr><td rowspan="2">provider<br/><div style="font-size: small;"> (added in 2.5)</div></td>
    <td>no</td>
    <td></td><td></td>
    <td> <div>A dict object containing connection details.</div>    </tr>
    <tr>
    <td colspan="5">
    <table border=1 cellpadding=4>
    <caption><b>Dictionary object provider</b></caption>
    <tr>
    <th class="head">parameter</th>
    <th class="head">required</th>
    <th class="head">default</th>
    <th class="head">choices</th>
    <th class="head">comments</th>
    </tr>
                    <tr><td>ssh_keyfile<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td></td>
                <td></td>
                <td><div>Specifies the SSH keyfile to use to authenticate the connection to the remote device.  This argument is only used for <em>cli</em> transports. If the value is not specified in the task, the value of environment variable <code>ANSIBLE_NET_SSH_KEYFILE</code> will be used instead.</div>        </td></tr>
                    <tr><td>timeout<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td>10</td>
                <td></td>
                <td><div>Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.</div>        </td></tr>
                    <tr><td>server<br/><div style="font-size: small;"></div></td>
        <td>yes</td>
        <td></td>
                <td></td>
                <td><div>The BIG-IP host. You can omit this option if the environment variable <code>F5_SERVER</code> is set.</div>        </td></tr>
                    <tr><td>user<br/><div style="font-size: small;"></div></td>
        <td>yes</td>
        <td></td>
                <td></td>
                <td><div>The username to connect to the BIG-IP with. This user must have administrative privileges on the device. You can omit this option if the environment variable <code>F5_USER</code> is set.</div>        </td></tr>
                    <tr><td>server_port<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td>443</td>
                <td></td>
                <td><div>The BIG-IP server port. You can omit this option if the environment variable <code>F5_SERVER_PORT</code> is set.</div>        </td></tr>
                    <tr><td>password<br/><div style="font-size: small;"></div></td>
        <td>yes</td>
        <td></td>
                <td></td>
                <td><div>The password for the user account used to connect to the BIG-IP. You can omit this option if the environment variable <code>F5_PASSWORD</code> is set.</div>        </td></tr>
                    <tr><td>validate_certs<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td>True</td>
                <td><ul><li>yes</li><li>no</li></ul></td>
                <td><div>If <code>no</code>, SSL certificates will not be validated. Use this only on personally controlled sites using self-signed certificates. You can omit this option if the environment variable <code>F5_VALIDATE_CERTS</code> is set.</div>        </td></tr>
                    <tr><td>transport<br/><div style="font-size: small;"></div></td>
        <td>yes</td>
        <td>cli</td>
                <td><ul><li>rest</li><li>cli</li></ul></td>
                <td><div>Configures the transport connection to use when connecting to the remote device.</div>        </td></tr>
        </table>
    </td>
    </tr>
        </td></tr>
                <tr><td>server<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td></td>
        <td><div>The BIG-IP host. You can omit this option if the environment variable <code>F5_SERVER</code> is set.</div>        </td></tr>
                <tr><td>server_port<br/><div style="font-size: small;"> (added in 2.2)</div></td>
    <td>no</td>
    <td>443</td>
        <td></td>
        <td><div>The BIG-IP server port. You can omit this option if the environment variable <code>F5_SERVER_PORT</code> is set.</div>        </td></tr>
                <tr><td>snmp_auth_password<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Specifies the password for the user.</div><div>When creating a new SNMP <code>v3</code> community, this parameter is required.</div><div>This value must be at least 8 characters long.</div>        </td></tr>
                <tr><td>snmp_auth_protocol<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>md5</li><li>sha</li><li>none</li></ul></td>
        <td><div>Specifies the authentication method for the user.</div><div>When <code>md5</code>, specifies that the system uses the MD5 algorithm to authenticate the user.</div><div>When <code>sha</code>, specifies that the secure hash algorithm (SHA) to authenticate the user.</div><div>When <code>none</code>, specifies that user does not require authentication.</div><div>When creating a new SNMP <code>v3</code> community, if this parameter is not specified, the default of <code>sha</code> will be used.</div>        </td></tr>
                <tr><td>snmp_privacy_password<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Specifies the password for the user.</div><div>When creating a new SNMP <code>v3</code> community, this parameter is required.</div><div>This value must be at least 8 characters long.</div>        </td></tr>
                <tr><td>snmp_privacy_protocol<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>aes</li><li>des</li><li>none</li></ul></td>
        <td><div>Specifies the encryption protocol.</div><div>When <code>aes</code>, specifies that the system encrypts the user information using AES (Advanced Encryption Standard).</div><div>When <code>des</code>, specifies that the system encrypts the user information using DES (Data Encryption Standard).</div><div>When <code>none</code>, specifies that the system does not encrypt the user information.</div><div>When creating a new SNMP <code>v3</code> community, if this parameter is not specified, the default of <code>aes</code> will be used.</div>        </td></tr>
                <tr><td>snmp_username<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Specifies the name of the user for whom you want to grant access to the SNMP v3 MIB.</div><div>This parameter is only relevant when <code>version</code> is <code>v3</code>. If <code>version</code> is something else, this parameter is ignored.</div><div>When creating a new SNMP <code>v3</code> community, this parameter is required.</div><div>This parameter cannot be changed once it has been set.</div>        </td></tr>
                <tr><td>source<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>all</td>
        <td></td>
        <td><div>Specifies the source address for access to the MIB.</div><div>This parameter can accept a value of <code>all</code>.</div><div>If this parameter is not specified, the value <code>all</code> is used.</div><div>This parameter is only relevant when <code>version</code> is <code>v1</code>, or <code>v2c</code>. If <code>version</code> is something else, this parameter is ignored.</div><div>If <code>source</code> is set to <code>all</code>, then it is not possible to specify an <code>oid</code>. This will raise an error.</div><div>This parameter should be provided when <code>state</code> is <code>absent</code>, so that the correct community is removed. To remove the <code>public</code> SNMP community that comes with a BIG-IP, this parameter should be set to <code>default</code>.</div>        </td></tr>
                <tr><td>state<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>present</td>
        <td><ul><li>present</li><li>absent</li></ul></td>
        <td><div>When <code>present</code>, ensures that the address list and entries exists.</div><div>When <code>absent</code>, ensures the address list is removed.</div>        </td></tr>
                <tr><td>update_password<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>always</td>
        <td><ul><li>always</li><li>on_create</li></ul></td>
        <td><div><code>always</code> will allow to update passwords if the user chooses to do so. <code>on_create</code> will only set the password for newly created resources.</div>        </td></tr>
                <tr><td>user<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td></td>
        <td><div>The username to connect to the BIG-IP with. This user must have administrative privileges on the device. You can omit this option if the environment variable <code>F5_USER</code> is set.</div>        </td></tr>
                <tr><td>validate_certs<br/><div style="font-size: small;"> (added in 2.0)</div></td>
    <td>no</td>
    <td>True</td>
        <td><ul><li>yes</li><li>no</li></ul></td>
        <td><div>If <code>no</code>, SSL certificates will not be validated. Use this only on personally controlled sites using self-signed certificates. You can omit this option if the environment variable <code>F5_VALIDATE_CERTS</code> is set.</div>        </td></tr>
                <tr><td>version<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>v2c</td>
        <td><ul><li>v1</li><li>v2c</li><li>v3</li></ul></td>
        <td><div>Specifies to which Simple Network Management Protocol (SNMP) version the trap destination applies.</div>        </td></tr>
        </table>
    </br>



Examples
--------

 ::

    
    - name: Create an SMNP v2c read-only community
      bigip_snmp_community:
        name: foo
        version: v2c
        source: all
        oid: .1
        access: ro
        password: secret
        server: lb.mydomain.com
        state: present
        user: admin
      delegate_to: localhost

    - name: Create an SMNP v3 read-write community
      bigip_snmp_community:
        name: foo
        version: v3
        snmp_username: foo
        snmp_auth_protocol: sha
        snmp_auth_password: secret
        snmp_privacy_protocol: aes
        snmp_privacy_password: secret
        oid: .1
        access: rw
        password: secret
        server: lb.mydomain.com
        state: present
        user: admin
      delegate_to: localhost

    - name: Remove the default 'public' SNMP community
      bigip_snmp_community:
        name: public
        source: default
        password: secret
        server: lb.mydomain.com
        state: absent
        user: admin
      delegate_to: localhost


Return Values
-------------

Common return values are `documented here <http://docs.ansible.com/ansible/latest/common_return_values.html>`_, the following are the fields unique to this module:

.. raw:: html

    <table border=1 cellpadding=4>
    <tr>
    <th class="head">name</th>
    <th class="head">description</th>
    <th class="head">returned</th>
    <th class="head">type</th>
    <th class="head">sample</th>
    </tr>

        <tr>
        <td> param2 </td>
        <td> The new param2 value of the resource. </td>
        <td align=center> changed </td>
        <td align=center> string </td>
        <td align=center> Foo is bar </td>
    </tr>
            <tr>
        <td> param1 </td>
        <td> The new param1 value of the resource. </td>
        <td align=center> changed </td>
        <td align=center> bool </td>
        <td align=center> True </td>
    </tr>
        
    </table>
    </br></br>

Notes
-----

.. note::
    - For more information on using Ansible to manage F5 Networks devices see https://www.ansible.com/integrations/networks/f5.
    - Requires the f5-sdk Python package on the host. This is as easy as ``pip install f5-sdk``.



Status
~~~~~~

This module is flagged as **preview** which means that it is not guaranteed to have a backwards compatible interface.


Support
~~~~~~~

This module is community maintained without core committer oversight.

For more information on what this means please read :doc:`/usage/support`


For help developing modules, should you be so inclined, please read :doc:`Getting Involved </development/getting-involved>`, :doc:`Writing a Module </development/writing-a-module>` and :doc:`Guidelines </development/guidelines>`.