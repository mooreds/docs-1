import os
import json
import sys
import subprocess
from pprint import pprint
from collections import OrderedDict

if sys.version_info[0] < 3:
    print('Please run this with Python 3')
    sys.exit(1)

connectorsList = [];
sidebarsFile = 'sidebars.json'
dataConnectorsFile = "data-connectors.md"

# move the generated data connectors file
files = os.listdir('.')
if dataConnectorsFile in files:
    os.rename(dataConnectorsFile, "../references/" + dataConnectorsFile)


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





