import sys
import json

def read_json(input_file:str="")->dict:
    """
    read json file
    """
    with open(input_file, 'r') as f:
        data = json.load(f)
    return data

def write_json(data:dict={}, output_file:str="output.json")-> None:
    """
    write json file
    """
    with open(output_file, 'w') as f:
        json.dump(data, f)
    
def get_update_json(data, depth:int=0)->dict:
    """
    Parameters:
    data (dict): Input dictionary
    depth (int, optional): How many iterations into the sub-dictionaries to substitute.

    Returns:
        dict: Modified version of the input dictionary.
    """
    # if depth == 0:
    #     return data
    result = {}
    for key, value in data.items():
        if isinstance(value, dict):
            result[key] = get_update_json(value, depth)
        else:
            result[key] = {'_content': value, '_type': str(type(value))}

    return result

def main():
    # Parse command-line arguments
    input_file, depth,  output_file = sys.argv[1], int(sys.argv[2]), sys.argv[3]
    data = read_json(input_file=input_file)
    update_data = get_update_json(data, depth)
    write_json(data = update_data, output_file=output_file)

if __name__ == '__main__':
    """
    python substitute.py input.json 3 output.json
    """
    main()