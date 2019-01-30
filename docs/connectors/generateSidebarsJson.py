import os
import json
import sys
import subprocess
from pprint import pprint
from collections import OrderedDict


connectorsList = [];
sidebarsFile = 'sidebars.json'
dataConnectorsFile = "data-connectors.md"

# move the generated data connectors file
os.rename(dataConnectorsFile, "../references/" + dataConnectorsFile)

files = os.listdir('.')
for possibleMarkdown in files:
    if possibleMarkdown.endswith(".md"):
        name = possibleMarkdown.replace(".md", "")
        connectorsList.append("connectors/" + name)

connectorsList.sort()
os.chdir("../../website")

with open(sidebarsFile, 'r') as f:
    data = OrderedDict(json.load(f));
    data["connectors"]["Data connectors"] = connectorsList

with open(sidebarsFile, 'r+') as f:
    json.dump(data, f, indent=2)





