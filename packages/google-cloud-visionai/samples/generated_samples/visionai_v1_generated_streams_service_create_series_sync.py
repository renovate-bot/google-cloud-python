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
# Snippet for CreateSeries
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-visionai


# [START visionai_v1_generated_StreamsService_CreateSeries_sync]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import visionai_v1


def sample_create_series():
    # Create a client
    client = visionai_v1.StreamsServiceClient()

    # Initialize request argument(s)
    series = visionai_v1.Series()
    series.stream = "stream_value"
    series.event = "event_value"

    request = visionai_v1.CreateSeriesRequest(
        parent="parent_value",
        series_id="series_id_value",
        series=series,
    )

    # Make the request
    operation = client.create_series(request=request)

    print("Waiting for operation to complete...")

    response = operation.result()

    # Handle the response
    print(response)

# [END visionai_v1_generated_StreamsService_CreateSeries_sync]
