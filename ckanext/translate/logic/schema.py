import ckan.plugins.toolkit as tk
import string

def translate():
    not_empty = tk.get_validator("not_empty")
    input_validators = [not_empty]

    if tk.check_ckan_version(min_version='2.8.5'):
        json_object = tk.get_validator("json_object")
        input_validators = [not_empty, json_object]

    return {
        "input": input_validators,
        "from": [not_empty],
        "to": [not_empty],
    }
