from google.appengine.ext import ndb
from defines import * 

def exist(key):
    return key.get()

def existEmpl( email ):
    key = ndb.Key(EmployeeEntity, email)
    return exist(key)
    
class Employee:
    firstname = ''
    lastname = ''
    email = ''
    employer = ''
    workplace = ''
    accomodation = 'no'
    residence = ''
    roommate = ''
    transport = 'no'
    
    
class EmployeeEntity(ndb.Model):
    firstname = ndb.StringProperty(required = True)
    lastname = ndb.StringProperty(required = True)
    email = ndb.StringProperty(required = True)
    employer = ndb.StringProperty(required = True)
    workplace = ndb.StringProperty(required = True)
    accomodation = ndb.StringProperty()
    transport = ndb.StringProperty()
    residence = ndb.StringProperty()
    roommate = ndb.StringProperty()
    
    def set(self, emp):
        self.firstname      = emp.firstname   
        self.lastname       = emp.lastname    
        self.email          = emp.email       
        self.employer       = emp.employer    
        self.workplace      = emp.workplace   
        self.accomodation   = emp.accomodation
        self.transport      = emp.transport
        self.residence      = emp.residence   
        self.roommate       = emp.roommate    
        
def persistEmployee( empl, key ):
    #todo another email check  
    entity = EmployeeEntity(key=key)
    entity.set(empl)
    entity.put()
        