import json

def is_josn(data):
    try:
        real_data = json.loads(data)
        valid = True
    except ValueError:
        valid = False
    return valid
