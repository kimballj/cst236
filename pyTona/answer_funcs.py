import getpass


def feet_to_miles(feet):
    return str(float(feet) / 5280)

def hal_20():
    return "I'm afraid I can't do that {0}".format(getpass.getuser())
