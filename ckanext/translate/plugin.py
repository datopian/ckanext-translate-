import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

from ckanext.translate.logic import (
    action, auth
)


class TranslatePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IAuthFunctions)
    plugins.implements(plugins.IActions)
    

    # IConfigurer
    def update_config(self, config_):
        toolkit.add_template_directory(config_, "templates")
        toolkit.add_public_directory(config_, "public")
        toolkit.add_resource("assets", "translate")

    # IConfigurer
    def update_config_schema(self, schema):
        not_empty = toolkit.get_validator("not_empty")
        schema.update({
            'ckanext.translate.ibm_url': [not_empty, str],
            'ckanext.translate.ibm_key': [not_empty, str],
        })
        return schema
    
    # IAuthFunctions
    def get_auth_functions(self):
        return auth.get_auth_functions()

    # IActions
    def get_actions(self):
        return action.get_actions()
