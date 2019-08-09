from os.path import abspath
import json

PATH = abspath('stack.json')

try:
    with open(PATH) as file:
        PARAMETERS = json.load(file)
except Exception:
    print('ERROR::No stack.json file available')
    print('PATH::', PATH)
    raise


def get_endpoint():
    return PARAMETERS['ServiceEndpoint']
