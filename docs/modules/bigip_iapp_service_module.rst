.. _bigip_iapp_service:


bigip_iapp_service - Manages TCL iApp services on a BIG-IP
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.4


.. contents::
   :local:
   :depth: 2


Synopsis
--------

* Manages TCL iApp services on a BIG-IP.
* If you are looking for the API that is communicated with on the BIG-IP, the one the is used is ``/mgmt/tm/sys/application/service/``. There are a couple of APIs in a BIG-IP that might seem like they are relevant to iApp Services, but the API mentioned here is the one that is used.


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
                <tr><td>force<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>yes</li><li>no</li></ul></td>
        <td><div>Forces the updating of an iApp service even if the parameters to the service have not changed. This option is of particular importance if the iApp template that underlies the service has been updated in-place. This option is equivalent to re-configuring the iApp if that template has changed.</div>        </td></tr>
                <tr><td>name<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td></td>
        <td><div>The name of the iApp service that you want to deploy.</div>        </td></tr>
                <tr><td>parameters<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>A hash of all the required template variables for the iApp template. If your parameters are stored in a file (the more common scenario) it is recommended you use either the `file` or `template` lookups to supply the expected parameters.</div><div>These parameters typically consist of the <code>lists</code>, <code>tables</code>, and <code>variables</code> fields.</div>        </td></tr>
                <tr><td>partition<br/><div style="font-size: small;"> (added in 2.5)</div></td>
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
                <tr><td>state<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>present</td>
        <td><ul><li>present</li><li>absent</li></ul></td>
        <td><div>When <code>present</code>, ensures that the iApp service is created and running. When <code>absent</code>, ensures that the iApp service has been removed.</div>        </td></tr>
                <tr><td>strict_updates<br/><div style="font-size: small;"> (added in 2.5)</div></td>
    <td>no</td>
    <td>True</td>
        <td></td>
        <td><div>Indicates whether the application service is tied to the template, so when the template is updated, the application service changes to reflect the updates.</div><div>When <code>yes</code>, disallows any updates to the resources that the iApp service has created, if they are not updated directly through the iApp.</div><div>When <code>no</code>, allows updates outside of the iApp.</div><div>If this option is specified in the Ansible task, it will take precedence over any similar setting in the iApp Server payload that you provide in the <code>parameters</code> field.</div>        </td></tr>
                <tr><td>template<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>The iApp template from which to instantiate a new service. This template must exist on your BIG-IP before you can successfully create a service. This parameter is required if the <code>state</code> parameter is <code>present</code>.</div>        </td></tr>
                <tr><td>traffic_group<br/><div style="font-size: small;"> (added in 2.5)</div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>The traffic group for the iApp service. When creating a new service, if this value is not specified, the default of <code>/Common/traffic-group-1</code> will be used.</div><div>If this option is specified in the Ansible task, it will take precedence over any similar setting in the iApp Server payload that you provide in the <code>parameters</code> field.</div>        </td></tr>
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
        </table>
    </br>



Examples
--------

 ::

    
    - name: Create HTTP iApp service from iApp template
      bigip_iapp_service:
        name: foo-service
        template: f5.http
        parameters: "{{ lookup('file', 'f5.http.parameters.json') }}"
        password: secret
        server: lb.mydomain.com
        state: present
        user: admin
      delegate_to: localhost

    - name: Upgrade foo-service to v1.2.0rc4 of the f5.http template
      bigip_iapp_service:
        name: foo-service
        template: f5.http.v1.2.0rc4
        password: secret
        server: lb.mydomain.com
        state: present
        user: admin
      delegate_to: localhost

    - name: Configure a service using parameters in YAML
      bigip_iapp_service:
        name: tests
        template: web_frontends
        password: admin
        server: "{{ inventory_hostname }}"
        server_port: "{{ bigip_port }}"
        validate_certs: "{{ validate_certs }}"
        state: present
        user: admin
        parameters:
          variables:
            - name: var__vs_address
              value: 1.1.1.1
            - name: pm__apache_servers_for_http
              value: 2.2.2.1:80
            - name: pm__apache_servers_for_https
              value: 2.2.2.2:80
      delegate_to: localhost

    - name: Re-configure a service whose underlying iApp was updated in place
      bigip_iapp_service:
        name: tests
        template: web_frontends
        password: admin
        force: yes
        server: "{{ inventory_hostname }}"
        server_port: "{{ bigip_port }}"
        validate_certs: "{{ validate_certs }}"
        state: present
        user: admin
        parameters:
          variables:
            - name: var__vs_address
              value: 1.1.1.1
            - name: pm__apache_servers_for_http
              value: 2.2.2.1:80
            - name: pm__apache_servers_for_https
              value: 2.2.2.2:80
      delegate_to: localhost

    - name: Try to remove the iApp template before the associated Service is removed
      bigip_iapp_template:
        name: web_frontends
        state: absent
      register: result
      failed_when:
        - result is not success
        - "'referenced by one or more applications' not in result.msg"

    - name: Configure a service using more complicated parameters
      bigip_iapp_service:
        name: tests
        template: web_frontends
        password: admin
        server: "{{ inventory_hostname }}"
        server_port: "{{ bigip_port }}"
        validate_certs: "{{ validate_certs }}"
        state: present
        user: admin
        parameters:
          variables:
            - name: var__vs_address
              value: 1.1.1.1
            - name: pm__apache_servers_for_http
              value: 2.2.2.1:80
            - name: pm__apache_servers_for_https
              value: 2.2.2.2:80
          lists:
            - name: irules__irules
              value:
                - foo
                - bar
          tables:
            - name: basic__snatpool_members
            - name: net__snatpool_members
            - name: optimizations__hosts
            - name: pool__hosts
              columnNames:
                - name
              rows:
                - row:
                    - internal.company.bar
            - name: pool__members
              columnNames:
                - addr
                - port
                - connection_limit
              rows:
                - row:
                    - "none"
                    - 80
                    - 0
            - name: server_pools__servers
      delegate_to: localhost



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