#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "ab9c70b5-ca5c-4cbb-b576-54f200431fec")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "NF48Q~xg7w2QIQgS5NqEKHZcmeyUhC-DPqosLbSW")
