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


# Future works

def modifications(json_schema, schema_in_repo):
    """
    Checks whether a schema already existed in repo, and if it does it verifies that they are identical
    """
    return True


def backwards_compatible(json_schema, schema_in_repo):
    """
    Checks whether the changes between the predecessor of the schema and the current version are backwards compatible
    """
    return True
