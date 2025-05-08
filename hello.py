#!/usr/bin/env python

import requests

from cowsay import cowsay


print("hello world!")

print(requests.get("https://google.com/").status_code)

print(cowsay("test"))
