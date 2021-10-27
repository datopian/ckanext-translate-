 [![CKAN](https://img.shields.io/badge/ckan-2.7-orange.svg?style=flat-square)](https://github.com/ckan/ckan/tree/2.7) [![CKAN](https://img.shields.io/badge/ckan-2.8-orange.svg?style=flat-square)](https://github.com/ckan/ckan/tree/2.8) [![CKAN](https://img.shields.io/badge/ckan-2.9-orange.svg?style=flat-square)](https://github.com/ckan/ckan/tree/2.9) 

 Note: This plugin is tested with CKAN 2.8 or later version but hasn't been tested on earlier version. 

# ckanext-translate
This extension provides an REST API that translates the provided text into the given languages. At the moment, it uses [IBM Watson Language Translator](https://www.ibm.com/cloud/watson-language-translator) APIs on backend for translation. In the future, other third-part services can be integrated.


## Installation
To install ckanext-translate extension. 
1. Activate your CKAN virtual environment, for example:
    ```
     . /usr/lib/ckan/default/bin/activate
    ```

2. Clone the source and install it on the virtualenv
    ```
    git clone https://github.com/datopian/ckanext-translate.git
    cd ckanext-translate
    pip install -e .
  	pip install -r requirements.txt
    ```

3. Add `translate` to the `ckan.plugins` setting in your CKAN
   config file (by default the config file is located at
   `/etc/ckan/default/ckan.ini`) and restart ckan service.


## Config settings
  Following environment variables must be added. To get a IBM Watson Translator API key and url, you need to sign up for IBM cloud account and create [Language translator](https://www.ibm.com/cloud/watson-language-translator) instance. 

  ```
    ckanext.translate.ibm_url = <IBM watson translator url>
    ckanext.translate.ibm_key = <IBM watson translator API key> 
  ```


## API Documentation
**API Endpont:** `/api/3/action/translate`

`input` You can pass keys values text for the translate.  \
`from` Parameter to specify the language code of the language you want to translate from. \
`to` Parameter to specify the language code of the language you want to translate. 


Request example:
```json
{
  "input": {
    "title": "My dataset title",
    "notes": "Some notes about my dataset."
  },
  "from": "en",
  "to": "fr"
}
 ```

Response example: 

```json
{
"result": {
  "output": {
      "title": "Mon titre de jeu de données",
      "notes": "Quelques notes sur mon jeu de données."
    }
  }  
}
```



## Developer installation
To install ckanext-translate for development, activate your CKAN virtualenv and
do:

    git clone https://github.com/datopian/ckanext-translate.git
    cd ckanext-translate
    python setup.py develop
