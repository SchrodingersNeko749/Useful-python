import json
import sys
import argparse
import win32clipboard

filePath = ""


# Create the argument parser
parser = argparse.ArgumentParser(description='Perform operations on a JSON file.')

# Add arguments
parser.add_argument('-o', '--operation', default='c',help='put in filename or [c] to get data from clipboard')
parser.add_argument('-t', '--type', choices=['a', 'v'], default='a', help='json data to extract (attributes[a] or values[v]). default a')
parser.add_argument('-r', '--root-node', default='', help='the root node to start from')


args = parser.parse_args()
operation = args.operation

data = None
if operation == 'c':
    win32clipboard.OpenClipboard()
    rawdata = win32clipboard.GetClipboardData()
    try:
        data = json.loads(rawdata)
        print(data)
    except:
        print("failed to read json data from clipboard")
else:     
    with open(args.operation, 'r', encoding='utf-8') as file:
        # Load the JSON data into a Python object
        data = json.load(file)
node = args.root_node
jsonDataType = args.type
    

if node != '':
    parts = node.split(".")
    for part in parts:
        if part in data:
            data = data[part]
if isinstance(data, list):
    data = data[0]
for key, value in data.items():
    match jsonDataType:
        case 'a':
            print(key)
        case 'v':
            print(value)
    
    