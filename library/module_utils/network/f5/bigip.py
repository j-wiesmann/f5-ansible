# -*- coding: utf-8 -*-
#
# Copyright (c) 2017 F5 Networks Inc.
# GNU General Public License v3.0 (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


import time

try:
    from f5.bigip import ManagementRoot
    from icontrol.exceptions import iControlUnexpectedHTTPError
    HAS_F5SDK = True
except ImportError:
    HAS_F5SDK = False

try:
    from library.module_utils.network.f5.common import F5BaseClient
    from library.module_utils.network.f5.common import F5ModuleError
except ImportError:
    from ansible.module_utils.network.f5.common import F5BaseClient
    from ansible.module_utils.network.f5.common import F5ModuleError


class F5Client(F5BaseClient):
    @property
    def api(self):
        ex = None
        if self._client:
            return self._client
        for x in range(0, 3):
            try:
                result = ManagementRoot(
                    self.params['server'],
                    self.params['user'],
                    self.params['password'],
                    port=self.params['server_port'],
                    verify=self.params['validate_certs'],
                    token='tmos'
                )
                self._client = result
                return self._client
            except Exception as ex:
                time.sleep(1)
        error = 'Unable to connect to {0} on port {1}.'.format(self.params['server'], self.params['server_port'])
        if ex is not None:
            error += ' The reported error was "{0}".'.format(str(ex))
        raise F5ModuleError(error)


class F5RestClient(F5BaseClient):
    @property
    def api(self):
        ex = None
        if self._client:
            return self._client
        for x in range(0, 10):
            try:
                result = iControlRestSession(
                    self.params['server'],
                    self.params['user'],
                    self.params['password'],
                    port=self.params['server_port'],
                    verify=self.params['validate_certs'],
                    token='tmos'
                )
                self._client = result
                return self._client
            except Exception as ex:
                time.sleep(1)
        error = 'Unable to connect to {0} on port {1}.'.format(self.params['server'], self.params['server_port'])
        if ex is not None:
            error += ' The reported error was "{0}".'.format(str(ex))
        raise F5ModuleError(error)
