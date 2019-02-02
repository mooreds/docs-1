import os
import json
import sys
import subprocess
from pprint import pprint
from collections import OrderedDict
from collections import defaultdict

if sys.version_info[0] < 3:
    print('Please run this with Python 3')
    sys.exit(1)

# Go one level up to the connectors/directory
os.chdir("..")

sidebarsList = []
connectorsList = []
sidebarsFile = '../../website/sidebars.json'
dataConnectorsFile = "data-connectors.md"

dataConnectorsTemplateFile = "connectorUtils/data-connectors-template.txt"
fileNameToDisplayName = {}

SIDEBAR_LABEL = "sidebar_label: "
ID = "id: "


def bulletPointAndLink(connectorName):
    displayName = fileNameToDisplayName[connectorName]
    fileReference = "../connectors/" + connectorName + ".md"
    return "* [" + displayName + "]" + "(" + fileReference + ")"

# Get all the documentation files. Read each file to get its display name
files = os.listdir(".")
for fileName in files:
    if fileName.endswith(".md") and fileName != dataConnectorsFile:
        name = fileName.replace(".md", "")
        connectorsList.append(name)

        with open(fileName, 'r') as connectorFile:
            connectorDisplayName = name
            markdownId = name
            lines = connectorFile.readlines()

            # Read the id and sidebar_label from the markdown, with defaults (above) if they aren't found
            for line in lines:
                if line.startswith(ID):
                    markdownId = line[len(ID): -1] # -1 to trim off the newline
                if line.startswith(SIDEBAR_LABEL):
                    connectorDisplayName = line[len(SIDEBAR_LABEL) : -1]  
            
            fileNameToDisplayName[name] = connectorDisplayName
            sidebarsList.append("connectors/" + markdownId)


sidebarsList.sort()
connectorsList.sort()

# Replace the sidebars.json "connectors" key with the newly formed connector list
with open(sidebarsFile, 'r') as f:
    data = OrderedDict(json.load(f));
    data["connectors"]["Data connectors"] = sidebarsList

with open(sidebarsFile, 'w+') as f:
    json.dump(data, f, indent=2)


# Create data-connector.md file
with open(dataConnectorsTemplateFile) as template:
    lines = template.readlines()

    with open(dataConnectorsFile, "w+") as f:
        f.writelines(lines)


# Write to the data-connector.md file with all the connector names + display names
connectorsByLetter = OrderedDict()
for name in connectorsList:
    firstLetter = name[0].upper()
    if firstLetter not in connectorsByLetter:
        connectorsByLetter[firstLetter] = []
    connectorsByLetter[firstLetter].append(name)

with open(dataConnectorsFile, "a") as f:
    for letter in connectorsByLetter.keys():
        f.write("## " + letter)
        f.write("\n")
        f.write("\n")
        for connector in connectorsByLetter.get(letter):
            f.write(bulletPointAndLink(connector))
            f.write("\n")
        f.write("\n")

# move the generated data connectors file
os.rename(dataConnectorsFile, "../references/" + dataConnectorsFile)
    




