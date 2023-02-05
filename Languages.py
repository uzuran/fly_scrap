from configparser import ConfigParser

config_obj = ConfigParser()

conf_lang = config_obj["DEFAULT"]


# TODO here is the function for get from configparser by key.
def get(key: str):
    config_obj.read("czech.ini", encoding='UTF-8')
    return config_obj.get("DEFAULT", key)

