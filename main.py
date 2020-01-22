import json
import os

def convert_lua_to_json(path_in="./Auc-ScanData.lua", path_out="./Auc-ScanData.json"):
    """Converts raw lua to json file by calling convert.sh

    Parameters
    ----------
    path_in : str, defaults to "./Auc-ScanData.lua"
        Path to raw lua file. 

    path_out : str, defaults to "./Auc-ScanData.json"
        Path to output json file
    """
    print "--------------------"
    print "convert_lua_to_json" # TODO: refactor to py3
    print "--------------------"
    os.system("./bin/convert.sh" + " " + path_in + " " + path_out)

def convert_json_to_csv(path_in="./Auc-ScanData.json", path_out="./Auc-ScanData.csv"): 
    """Converts json to something that is csv-readable. 

    Parameters
    ----------
    path_in : str, defaults to "./Auc-ScanData.json"
        Path to converted json file.

    path_out : str, defaults to "./Auc-ScanData.csv"
        Path to output csv file.
    """
    print "--------------------"
    print "convert_json_to_csv" # TODO: refactor to py3
    print "--------------------"
    print "Reading in", path_in # TODO: refactor to py3
    with open(path_in, "r") as f:
        content = json.load(f)

    data = content['scans']['Mograine']['ropes'][0]
    data = data.lstrip("return ")
    data = data.replace("{", "")
    data = data.replace("},", "\n")

    print "Writing to", path_out # TODO: refactor to py3
    with open(path_out, "w") as out: 
        out.write(data.encode('utf-8'))

if __name__ == "__main__":
    convert_lua_to_json()
    convert_json_to_csv()
