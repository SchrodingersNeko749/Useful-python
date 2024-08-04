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

data = {}
if operation == 'c':
    win32clipboard.OpenClipboard()
    rawdata = win32clipboard.GetClipboardData()
    try:
        data = json.loads(rawdata)
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
        index_parts = part.split("[")
        
        index = "all"
        # if we have an array object
        if len(index_parts) > 1 : 
            index = index_parts[1]
            index = index.strip("]")
            
            partname = index_parts[0]
            part = partname
        if isinstance(data, list):
            #print(data)
            if index == "all":
                newData = []
                for d in data :
                    #print(d)
                    finalValue = d[part]
                    newData.append(finalValue)
                
                data = newData
                    #data.append(last_parts)
            elif index == "count":
                print(data.count)
            
            else:
                print("test")
                data = data[int(index)]
        #print(data)    
        if part in data:
            data = data[part]
            
if (type(data) == dict):
    for key, value in data.items():
            match jsonDataType:
                case 'a':
                    print(key)
                case 'v':
                    print(value)
elif type(data) == list:
    for d in data:
        print(d)
else:
    print(data)
    # print( test)
    
