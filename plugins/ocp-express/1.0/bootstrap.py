# coding: utf-8
# Copyright (c) 2025 OceanBase.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from __future__ import absolute_import, division, print_function

import os


def bootstrap(plugin_context, cursor = None, start_env=None, *args, **kwargs):
    stdio = plugin_context.stdio
    clients = plugin_context.clients
    if not cursor:
        cursor = plugin_context.get_return('connect').get_return('cursor')

    if not start_env:
        raise Exception("start env is needed")
    success = True
    for server in start_env:
        server_config = start_env[server]
        data = {
            "cluster": {
                "name": server_config["cluster_name"],
                "obClusterId": server_config["ob_cluster_id"],
                "rootSysPassword": server_config["root_sys_password"],
                "serverAddresses": server_config["server_addresses"],
            },
            "agentUsername": server_config["agent_username"],
            "agentPassword": server_config["agent_password"]
        }
        if server not in cursor or not cursor[server].init(data, stdio=stdio):
            stdio.error("failed to send init request to {} ocp express".format(server))
            success = False
        else:
            client = clients[server]
            bootstrap_flag = os.path.join(server_config['home_path'], '.bootstrapped')
            client.execute_command('touch %s' % bootstrap_flag)

    if success:
        return plugin_context.return_true()
    else:
        return plugin_context.return_false()

