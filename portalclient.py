# Project: Quick Example ESRI Portal Token Generation (Rest API)
# Author: Faizan Tayyab (http://faizantayyab.com)
# License: Copyright 2020
# Python: 2.7

"""Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE."""

# Import packages

import requests

import json
 
# Variables

username = ""  # ****************************************************  enter in your username 

password = ""  # ****************************************************  enter in your password

# Change the base URL to point to your Portal implementation
baseurl = ""

token_url = baseurl  + "/portal/sharing/rest/generateToken"

# Change parameters as required
r = requests.post(token_url,data={"username": username, "password": password, "client": "referer","referer": "https://localhost", "f": "pjson"})

# Display token from response
print(json.loads(r.text))
