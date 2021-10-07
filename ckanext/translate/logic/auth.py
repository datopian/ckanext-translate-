import ckan.plugins.toolkit as tk

@tk.auth_disallow_anonymous_access
def translate(context, data_dict):
    return {"success": True}


def get_auth_functions():
    return {
        "translate": translate,
    }
