import ckan.plugins.toolkit as tk
import string

def translate():
    not_empty = tk.get_validator("not_empty")
    json_object = tk.get_validator("json_object")
    return {
        "input": [not_empty, json_object],
        "from": [not_empty],
        "to": [not_empty],
    }
