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
# Snippet for CreateWasmPluginVersion
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-network-services


# [START networkservices_v1_generated_NetworkServices_CreateWasmPluginVersion_sync]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import network_services_v1


def sample_create_wasm_plugin_version():
    # Create a client
    client = network_services_v1.NetworkServicesClient()

    # Initialize request argument(s)
    wasm_plugin_version = network_services_v1.WasmPluginVersion()
    wasm_plugin_version.plugin_config_data = b'plugin_config_data_blob'

    request = network_services_v1.CreateWasmPluginVersionRequest(
        parent="parent_value",
        wasm_plugin_version_id="wasm_plugin_version_id_value",
        wasm_plugin_version=wasm_plugin_version,
    )

    # Make the request
    operation = client.create_wasm_plugin_version(request=request)

    print("Waiting for operation to complete...")

    response = operation.result()

    # Handle the response
    print(response)

# [END networkservices_v1_generated_NetworkServices_CreateWasmPluginVersion_sync]
