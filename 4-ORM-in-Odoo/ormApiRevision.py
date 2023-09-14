'''

module
├── models
│   ├── *.py                  #Business Object
│   └── __init__.py           #Object views (UI Display)
├── data                      
│   └── *.xml                 #configdata/reports/views/demodata/moduleparam/security
├── __init__.py               #web controllers
└── __manifest__.py           #static web data

'''





#_________________________________________________________________
API
#_________________________________________________________________

class odoo.models.BaseModel

      odoo.models.AbstractModel
      #alias of odoo.models.BaseModel

class odoo.models.Model (env, ids, prefetch_ids)
#Main super-class for regular database-persisted Odoo models
class odoo.models.TransientModel (env, ids, prefetch_ids)
#Model super-class for transient records, meant to be temporarily persistent, and regularly vacuum-cleaned.



#_________________________________________________________________
Fields:
#_________________________________________________________________
class odoo.fields.Field()
#general method for accessing & assigning
Basic Fields:
  class odoo.fields.Boolean()
  class odoo.fields.Char()
  class odoo.fields.Float()
  class odoo.fields.Integer()
  class odoo.fields.Text()
Advanced Fields:
      class odoo.fields.Binary()
      class odoo.fields.Html()
      class odoo.fields.Image()
      class odoo.fields.Monetary()
      class odoo.fields.Selection()

      Datetime Fields:
            class odoo.fields.Date()
            class odoo.fields.Datetime()
      Relational Fields:
            class odoo.fields.Many2one()
            class odoo.fields.One2many()
            class odoo.fields.Many2many()
            class odoo.fields.Command()
      Pseudo-relational Fields:
            class odoo.fields.Reference()
            class odoo.fields.Many2oneReference()
      Computed Fields:
#fields can be computed instead of read from db using 'compute' param
      Related Fields:
#provides value of sub-field on current record (special type of   computed field)


Automatic Fields:
Model.Id
      Access log Fields: 
      #automatically set and updated if _log_access is enabled
            Model.create_date
            #stores when record was created, Datetime
            Model.create_uid
            #stores who created the record, Many2one to a res.users
            Model.write_date
            #stores when the record was last updated, Datetime
            Model.write_uid
            #stores who last updated the record, Many2one to a res.users

Reserved Field names:
#pre-defined behaviours beyond automated fields
#should be defined on a model when the related behaviour is desired
      Model.name
      Model.active
          toggle_active()
          Model.action_archive()
          Model.action_unarchive()
      Model.state
      Model.parent_id
      Model.parent_path
      Model.company_id







#_________________________________________________________________
Recordsets:
#ordered collection of records of the same model
#interactions between records and model are performed through recordsets
#_________________________________________________________________

- Fields access
- Record cache & prefetching





#____________________________________________________________________
Method decorators:
#____________________________________________________________________

odoo.api.autovacuum()
odoo.api.constrains()
odoo.api.depends()
odoo.api.depends_context()
odoo.api.model()
odoo.api.model_create_multi()
odoo.api.onchange()
odoo.api.ondelete(*, at_uninstall)
odoo.api.returns(model,downgrade=None,upgrade=None)





#____________________________________________________________________
Environment:
#____________________________________________________________________

odoo.api.Environment(cr,uid,context,su=False)
#cr: the current database cursor (for database queries);
#uid: the current user id (for access rights checks);
#context: the current context dictionary (arbitrary metadata);
#su: whether in superuser mode.

Environment.lang
Environment.user
Environment.company
Environment.companies

Useful env methods:
Environment.ref(xml_id, raise_if_not_found=True)
#return record corresponding to given xml_id
Environment.is_superuser() 
#return wether in superuser mode
Environment.is_admin()    
#return wether current user has group"Access rights" or is in superuser mode
Environment.is_system()    
#return wether current user has group "Settings" or is in superuser mode

Altering the environment:
Model.with_context([context][, **overrides])
Model.with_user(user)
Model.with_company(company)
Model.with_company(company)
Model.with_env(env)
Model.sudo([flag=True])

SQL Execution:
self.env.cr.execute("some_sql", params)
Environment.flush_all() #flush all pending computations and updates to the db
Model.flush_model(fnames=None)
Model.flush_recordset(fnames=None)
Environment.invalidate_all(flush=True) #invalidate cache of all records
Model.invalidate_model(fnames=None, flush=True)
Model.invalidate_recordset(fnames=Nine,flush=True)
Model.modified(fnames,create=False,before=False)








#____________________________________________________________________
Common ORM methods
#____________________________________________________________________
Create/update:
Model.create(vals_list)
Model.copy(default=None)
Model.default_get(fields_list)
Model.name_create(name)
Model.write(vals)

Search/read:
Model.browse([ids])
Model.search(domain[, offset=0][, limit=None][, order=None][, count=False])
Model.searcg_count(domain)
Model.name_search(name='',args=None, operator='ilike', limit=100)
Model.read([fields])
Model.read_group(domain, fields, groupby, offset=0, limit=None, orderby=False, lazy=True)
Model.fields_get([allfields][,attributes])

Fields:
Model.fields_get([allfields][, attributes])

Search domains:
#A domain is a list of criteria,
#each criterion being a triple 
(either a list or a tuple) 
(field_name, operator, value)

Unlink:
Model.unlink()
#deletes records in self
  
Record(set) information:
Model.ids
odoo.models.env
Model.exists()
Model.ensure_one()
Model.name_get()
Model.get_metadata()

Operations:
Filter:
Model.filtered(func)
Model.filtered_domain(domain)
Map:
Model.mapped(func)
Sort:
Model.sorted(key=None, reverse=False)






#____________________________________________________________________
Inheritance and extension
#____________________________________________________________________

Classical inheritance:
Extension:
Delegation:
Fields incremental definition:






#____________________________________________________________________
Error management
#____________________________________________________________________

exception odoo.exceptions.accessError(message)
exception odoo.exceptions.CacheMiss(record, field)
exception odoo.exceptions.MissingError(message)
exception odoo.exceptions.RedirectWarning(message, action, button_text, additional_context=None)
exception odoo.exceptions.UserError(message)
exception odoo.exceptions.ValidationError(message)