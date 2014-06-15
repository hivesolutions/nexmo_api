#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Twilio API
# Copyright (C) 2008-2014 Hive Solutions Lda.
#
# This file is part of Hive Twilio API.
#
# Hive Twilio API is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Hive Twilio API is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Hive Twilio API. If not, see <http://www.gnu.org/licenses/>.

__author__ = "João Magalhães <joamag@hive.pt>"
""" The author(s) of the module """

__version__ = "1.0.0"
""" The version of the module """

__revision__ = "$LastChangedRevision$"
""" The revision number of the module """

__date__ = "$LastChangedDate$"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2008-2014 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "GNU General Public License (GPL), Version 3"
""" The license for the module """

import appier

from nexmo import account

BASE_URL = "https://rest.nexmo.com/ni/json/"
""" The default base url to be used when no other
base url value is provided to the constructor """

class Api(
    appier.Api,
    account.AccountApi
):

    def __init__(self, *args, **kwargs):
        appier.OAuth1Api.__init__(self, *args, **kwargs)
        self.base_url = kwargs.get("base_url", BASE_URL)
        self.key = kwargs.get("key", None)
        self.secret = kwargs.get("secret", None)
