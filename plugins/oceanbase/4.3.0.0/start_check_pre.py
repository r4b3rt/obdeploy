# coding: utf-8
# OceanBase Deploy.
# Copyright (C) 2021 OceanBase
#
# This file is part of OceanBase Deploy.
#
# OceanBase Deploy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# OceanBase Deploy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with OceanBase Deploy.  If not, see <https://www.gnu.org/licenses/>.


from __future__ import absolute_import, division, print_function

from math import sqrt

import _errno as err
from tool import set_plugin_context_variables

success = True
production_mode = False


def start_check_pre(plugin_context, init_check_status=False, strict_check=False, work_dir_check=False, work_dir_empty_check=True, generate_configs={}, precheck=False, source_option='start', *args, **kwargs):

    def get_system_memory(memory_limit, min_pool_memory):
        if memory_limit <= 8 << 30:
            system_memory = 2 << 30
        elif memory_limit <= 16 << 30:
            system_memory = 3 << 30
        elif memory_limit <= 32 << 30:
            system_memory = 5 << 30
        elif memory_limit <= 48 << 30:
            system_memory = 7 << 30
        elif memory_limit <= 64 << 30:
            system_memory = 10 << 30
        else:
            memory_limit_gb = memory_limit >> 30
            system_memory = int(3 * (sqrt(memory_limit_gb) - 3)) << 30
        return max(system_memory, min_pool_memory)
    check_status = {}
    cluster_config = plugin_context.cluster_config

    def check_pass(server, item):
        status = check_status[server]
        if status[item].status == err.CheckStatus.WAIT:
            status[item].status = err.CheckStatus.PASS

    def check_fail(server, item, error, suggests=[]):
        status = check_status[server][item]
        if status.status == err.CheckStatus.WAIT:
            status.error = error
            status.suggests = suggests
            status.status = err.CheckStatus.FAIL

    def wait_2_pass(server):
        status = check_status[server]
        for item in status:
            check_pass(server, item)

    def alert(server, item, error, suggests=[]):
        global success
        if strict_check:
            success = False
            check_fail(server, item, error, suggests)
            stdio.error(error)
        else:
            stdio.warn(error)

    def critical(server, item, error, suggests=[]):
        global success
        success = False
        check_fail(server, item, error, suggests)
        stdio.error(error)

    def alert_strict(server, item, error, suggests=[]):
        global success, production_mode
        if strict_check or production_mode:
            success = False
            check_fail(server, item, error, suggests)
            print_with_suggests(error, suggests)
        else:
            stdio.warn(error)

    def error(server, item, _error, suggests=[]):
        global success
        if plugin_context.dev_mode:
            stdio.warn(_error)
        else:
            check_fail(server, item, _error, suggests)
            print_with_suggests(_error, suggests)
            success = False

    def get_success():
        global success
        return success

    def change_success():
        global success
        success = True

    def print_with_suggests(error, suggests=[]):
        stdio.error('{}, {}'.format(error, suggests[0].msg if suggests else ''))

    kernel_check_items = [
        {'check_item': 'vm.max_map_count', 'need': [327600, 1310720], 'recommend': 655360},
        {'check_item': 'vm.min_free_kbytes', 'need': [32768, 2097152], 'recommend': 2097152},
        {'check_item': 'vm.overcommit_memory', 'need': 0, 'recommend': 0},
        {'check_item': 'fs.file-max', 'need': [6573688, float('inf')], 'recommend': 6573688},
    ]

    kernel_check_status = {}
    for kernel_param in kernel_check_items:
        check_item = kernel_param['check_item']
        kernel_check_status[check_item] = err.CheckStatus()

    check_status = {}
    plugin_context.set_variable('start_check_status', check_status)
    cluster_config = plugin_context.cluster_config
    stdio = plugin_context.stdio
    global production_mode

    for server in cluster_config.servers:
        server_config = cluster_config.get_server_conf_with_default(server)
        production_mode = server_config.get('production_mode', False)
        check_status[server] = {
            'port': err.CheckStatus(),
            'mem': err.CheckStatus(),
            'disk': err.CheckStatus(),
            'ulimit': err.CheckStatus(),
            'aio': err.CheckStatus(),
            'net': err.CheckStatus(),
            'ntp': err.CheckStatus(),
            'scenario': err.CheckStatus(),
            'ocp tenant memory': err.CheckStatus(),
            'ocp tenant disk': err.CheckStatus()
        }
        check_status[server].update(kernel_check_status)
        if work_dir_check:
             check_status[server]['dir'] = err.CheckStatus()
    plugin_context.set_variable('start_check_status', check_status)
    if init_check_status:
        return plugin_context.return_true(start_check_status=check_status)

    clog_sub_dir = 'clog/tenant_1'
    slog_dir_key = 'data_dir'
    slog_size = float(4 << 30)
    max_user_processes = {
        'need': lambda x: 120000,
        'recd': lambda x: 655350,
        'name': 'nproc'
    }

    context_dict = {
        'slog_size': slog_size,
        'start_check_status': check_status,
        'kernel_check_items': kernel_check_items,
        'max_user_processes': max_user_processes,
        'get_system_memory': get_system_memory,
        'slog_dir_key': slog_dir_key,
        'clog_sub_dir': clog_sub_dir,
        'check_pass': check_pass,
        'check_fail': check_fail,
        'wait_2_pass': wait_2_pass,
        'alert': alert,
        'alert_strict': alert_strict,
        'error': error,
        'critical': critical,
        'print_with_suggests': print_with_suggests,
        'get_success': get_success,
        'production_mode': production_mode
    }
    change_success()
    set_plugin_context_variables(plugin_context, context_dict)
    return plugin_context.return_true()