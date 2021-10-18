import json
import requests
from ckan.common import config
import ckan.plugins.toolkit as tk
import ckanext.translate.logic.schema as schema


def translate(context, data_dict):
    ibm_url =  config.get('ckanext.translate.ibm_url')
    ibm_api_key = config.get('ckanext.translate.ibm_key')

    tk.check_access("translate", context, data_dict)
    data, errors = tk.navl_validate(
        data_dict, schema.translate(), context)

    if errors:
        raise tk.ValidationError(errors)

    translate_keys, translate_values = zip(*data["input"].items())

    translate_req_dict= {
            "text": list(translate_values),
            "source": data_dict['from'],
            "target": data_dict['to'],
        }

    try:
        response = requests.post('{}/v3/translate?{}'.format(ibm_url, 'version=2018-05-01'), 
                    auth=('apikey', ibm_api_key),
                    headers= {"Content-Type": "application/json"},
                    data=json.dumps(translate_req_dict)
                    )  

        response.raise_for_status()
    except requests.HTTPError as e:
        raise tk.ValidationError({'message': '%s' % e})

    translated_dict = {}
    for index, translated_item in enumerate(response.json()['translations']):
            translated_dict.update({ list(translate_keys)[index]: translated_item['translation'] })

    return {"output" : translated_dict}

def get_actions():
    return {
        'translate': translate,
    } 
