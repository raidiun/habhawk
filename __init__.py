__all__ = ["classes","dbConnect"]

from . import *

import json

dbSetup = json.load(open("habhawk/connection.config"))

dbc = dbConnect.dbConnection(dbSetup["url"],dbSetup["name"])