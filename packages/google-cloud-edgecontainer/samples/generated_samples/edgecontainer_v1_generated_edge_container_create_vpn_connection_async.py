# -*- coding: utf-8 -*-
# Copyright 2025 Google LLC
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
#
# Generated code. DO NOT EDIT!
#
# Snippet for CreateVpnConnection
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-edgecontainer


# [START edgecontainer_v1_generated_EdgeContainer_CreateVpnConnection_async]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import edgecontainer_v1


async def sample_create_vpn_connection():
    # Create a client
    client = edgecontainer_v1.EdgeContainerAsyncClient()

    # Initialize request argument(s)
    vpn_connection = edgecontainer_v1.VpnConnection()
    vpn_connection.name = "name_value"

    request = edgecontainer_v1.CreateVpnConnectionRequest(
        parent="parent_value",
        vpn_connection_id="vpn_connection_id_value",
        vpn_connection=vpn_connection,
    )

    # Make the request
    operation = client.create_vpn_connection(request=request)

    print("Waiting for operation to complete...")

    response = (await operation).result()

    # Handle the response
    print(response)

# [END edgecontainer_v1_generated_EdgeContainer_CreateVpnConnection_async]
