 [![CKAN](https://img.shields.io/badge/ckan-2.7-orange.svg?style=flat-square)](https://github.com/ckan/ckan/tree/2.7) [![CKAN](https://img.shields.io/badge/ckan-2.8-orange.svg?style=flat-square)](https://github.com/ckan/ckan/tree/2.8) [![CKAN](https://img.shields.io/badge/ckan-2.9-orange.svg?style=flat-square)](https://github.com/ckan/ckan/tree/2.9) 

 Note: This plugin has been tested with CKAN 2.8+. It hasn't been tested on earlier versions.

# ckanext-translate

This extension provides a REST API that translates the provided text into the given languages. At the moment, it uses [Google Translate API v3](https://cloud.google.com/translate/docs/advanced/translate-text-advance) APIs on backend for translation. In the future, other third-party services can be integrated.


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

  The following environment variables must be added. To get a Google Translate API key, follow the instructions [here](https://cloud.google.com/translate/docs/setup).

  ```
  ckanext.translate.google_service_account_file=/path/to/service_account.json
  ckanext.translate.google_project_id=project_id # e.g. ckan-auto-translate
  ckanext.translate.google_location=project_location # e.g. global
  ```

  There's also an optional variable to provide a list of stopwords to be ignored during translation (`ckanext.translate.ignore_list_path`). This can be helpful if you need to retain the original language for certain words or phrases. For example, if you want to keep the phrase "CKAN is awesome" in English for all languages, you can add it to a `.txt` file with one word or phrase per line:

  ```
  CKAN is awesome
  Another phrase to keep
  ```

  Let's assume you saved this file as `/srv/app/ignore_list.txt`. You can then add the following environment variable:

  ```
  ckanext.translate.ignore_list_path=/srv/app/ignore_list.txt
  ```

## API Documentation

**API Endpont:** `/api/3/action/translate`

`input` Parameter to specify the text to be translated.
`from` Parameter to specify the language code of the language you want to translate from.
`to` Parameter to specify the language code of the language you want to translate to.


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
