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
# Snippet for CreateAuthzExtension
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-network-services


# [START networkservices_v1_generated_DepService_CreateAuthzExtension_async]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import network_services_v1


async def sample_create_authz_extension():
    # Create a client
    client = network_services_v1.DepServiceAsyncClient()

    # Initialize request argument(s)
    authz_extension = network_services_v1.AuthzExtension()
    authz_extension.name = "name_value"
    authz_extension.load_balancing_scheme = "EXTERNAL_MANAGED"
    authz_extension.authority = "authority_value"
    authz_extension.service = "service_value"

    request = network_services_v1.CreateAuthzExtensionRequest(
        parent="parent_value",
        authz_extension_id="authz_extension_id_value",
        authz_extension=authz_extension,
    )

    # Make the request
    operation = client.create_authz_extension(request=request)

    print("Waiting for operation to complete...")

    response = (await operation).result()

    # Handle the response
    print(response)

# [END networkservices_v1_generated_DepService_CreateAuthzExtension_async]
