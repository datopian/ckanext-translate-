from ckan.common import config
import ckan.plugins.toolkit as tk
import ckanext.translate.logic.schema as schema
from ibm_watson import LanguageTranslatorV3, ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

IBM_URL =  config.get('ckanext.translate.ibm_url')
IBM_API_KEY = config.get('ckanext.translate.ibm_key')

authenticator = IAMAuthenticator(IBM_API_KEY)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(IBM_URL)

def translate(context, data_dict):
    tk.check_access("translate", context, data_dict)
    data, errors = tk.navl_validate(
        data_dict, schema.translate(), context)

    translate_from = data_dict['from']
    translate_to = data_dict['to']
    traslate_keys, traslate_values = zip(*data["input"].items())

    if errors:
        raise tk.ValidationError(errors)

    try:
        translation = language_translator.translate(text =list(traslate_values), 
            source = translate_from,
            target = translate_to,
            ).get_result()

    except ApiException as ex:  
        raise tk.ValidationError({'message': ex.message})

    translated_dict = []
    for index, translated_item in enumerate(translation['translations']):
            translated_dict.append({ list(traslate_keys)[index]: translated_item['translation'] })

    return {"output" : translated_dict}

def get_actions():
    return {
        'translate': translate,
    } 
