from os.path import abspath
import json

PATH = abspath('stack.json')
try:
    PARAMETERS = json.loads(PATH)
except Exception:
    print('ERROR:::No stack.json file available')
    raise


def get_endpoint():
    return PARAMETERS['ServiceEndpoint']
