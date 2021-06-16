import json
import jsonschema
from jsonschema import validate

from models.event import json_schema


def validate_json(line: str):
    try:
        json_data = json.loads(line)
    except ValueError as err:
        return False, err

    try:
        validate(instance=json_data, schema=json_schema)
    except jsonschema.exceptions.ValidationError as err:
        return False, err

    return True, json_data
