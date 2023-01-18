from configparser import ConfigParser

config_obj = ConfigParser()
config_obj["DEFAULT"] = {
    "User_key": "Uživatelské jméno",
    "Password_key": "Heslo",
    "Log_key": "Přihlašení",
    "Registration_key": "Registrace"
}

with open("czech.ini", "w") as config_file:
    config_obj.write(config_file)