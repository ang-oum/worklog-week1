# imports web controllers into parent folder (    ./crm(module)     )
# imports Odoo ORM framework API


from . import controllers   # ./crm(module)/controllers
from . import models        # ./crm(module)/models
from . import report        # ./crm(module)/report
from . import wizard        # ./crm(module)/wizard

from odoo import api, SUPERUSER_ID 



