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

# OceanBase official website
OB_OFFICIAL_WEBSITE = 'https://www.oceanbase.com/'

# post telemetry data to OceanBase official
TELEMETRY_WEBSITE = '<TELEMETRY_WEBSITE>'
TELEMETRY_URL = '{}/api/web/oceanbase/report'.format(TELEMETRY_WEBSITE if TELEMETRY_WEBSITE else 'https://openwebapi.oceanbase.com')
TELEMETRY_COMPONENT = 'obd'
TELEMETRY_COMPONENT_OB = "obd_web_ob"
TELEMETRY_COMPONENT_OCP = "obd_web_ocp"
TELEMETRY_SIG = 'dbe97393a695335d67de91dd4049ba'

# obdeploy version
VERSION = '<VERSION>'
# obdeploy build commit
REVISION = '<CID>'
# obdeploy build branch
BUILD_BRANCH = '<B_BRANCH>'
# obdeploy build time
BUILD_TIME = '<B_TIME>'
# obdeploy build plugin list
BUILD_PLUGIN_LIST = '<B_PLUGIN_LIST>'

# obdeploy home path
CONST_OBD_HOME = "OBD_HOME"
# obdeploy forbidden variable
FORBIDDEN_VARS = (CONST_OBD_HOME)

# tool variable
COMP_OBCLIENT = "obclient"
COMP_OCEANBASE_DIAGNOSTIC_TOOL = "oceanbase-diagnostic-tool"
COMP_OBDIAG = "obdiag"
COMP_JRE = 'openjdk-jre'

# ocp
COMP_OCP_EXPRESS = 'ocp-express'
COMP_OCP_SERVER = 'ocp-server'
COMP_OCP_SERVER_CE = 'ocp-server-ce'
COMPS_OCP = [COMP_OCP_SERVER, COMP_OCP_SERVER_CE]
COMPS_OCP_CE_AND_EXPRESS = [COMP_OCP_SERVER_CE, COMP_OCP_EXPRESS]

# ob
COMP_OB = "oceanbase"
COMP_OB_CE = "oceanbase-ce"
COMPS_OB = [COMP_OB, COMP_OB_CE]

# obproxy
COMP_ODP = "obproxy"
COMP_ODP_CE = "obproxy-ce"
COMPS_ODP = [COMP_ODP, COMP_ODP_CE]

# ob-configserver
COMP_OB_CONFIGSERVER = "ob-configserver"

# obagent
COMP_OBAGENT = 'obagent'

# oblogproxy
COMP_OBLOGPROXY = 'oblogproxy'

# service docs url
DISABLE_SWAGGER = '<DISABLE_SWAGGER>'

# component files type
PKG_RPM_FILE = 'rpm'
PKG_REPO_FILE = 'repository'

RSA_KEY_SIZE = 512


# test tool
TOOL_TPCH = 'obtpch'
TOOL_TPCC = 'obtpcc'
TOOL_SYSBENCH = 'ob-sysbench'
TEST_TOOLS = {
    TOOL_TPCH: 'tpch',
    TOOL_TPCC: 'tpcc',
    TOOL_SYSBENCH: 'sysbench',
}
TOOL_TPCC_BENCHMARKSQL = 'OB-BenchmarkSQL-5.0.jar'

#workflow stages
STAGE_FIRST = 10
STAGE_SECOND = 20
STAGE_THIRD = 30
STAGE_FOURTH = 40
STAGE_FIFTH = 50
STAGE_SIXTH = 60
STAGE_SEVENTH = 70
STAGE_EIGHTH = 80
STAGE_NINTH = 90
STAGE_TENTH = 100
