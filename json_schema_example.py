from jsonschema import validate, ValidationError

schema = {
    "type": "object",
    "properties": {
        "name": {
            "type": "string",
            "description": "The name of the person"
        },
        "age": {
            "type": "integer",
            "description": "The age of the person"
        }
    },
    "required": ["name", "age"]
}


data = {
    "name": "John Doe"
}

validate(instance=data, schema=schema)