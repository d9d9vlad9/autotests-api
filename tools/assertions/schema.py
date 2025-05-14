from typing import Any
from jsonschema import validate, ValidationError
from jsonschema.validators import Draft202012Validator



def validate_json_schema(instance: Any, schema: dict) -> None:
    """
    Валидация JSON-схемы с использованием jsonschema.
    :param instance: JSON-объект для проверки.
    :param schema: JSON-схема для проверки.
    :raises AssertionError: Если валидация не проходит.
    :return: None
    """
    try:
        validate(
            instance=instance, 
            schema=schema, 
            format_checker=Draft202012Validator.FORMAT_CHECKER
            )
    except ValidationError as e:
        raise ValidationError(f"JSON schema validation failed: {e}") from e