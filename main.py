﻿import jinja2
import logging
import os
import re
import urllib
import webapp2

from defines import *
from google.appengine.api import mail
from model import *
from util import *


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
    
class IntroPage(webapp2.RequestHandler):

    def get(self):
        template_values = {
            'last': self.request.get('last'),
        }
        template = JINJA_ENVIRONMENT.get_template('intro.html')
        self.response.write(template.render(template_values))

def isEmailValid( email ):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)
    
def getUnenteredMsg( value ):
    return ERROR_NOT_ENTERED % (labels[ value ],)              # toto test
    
def hasAccomodationRight(workplace):
    return workplace in workplacesWithAcc
    
class MainPage(BaseHandler):

    def displayPage(self, params={}, errors=[], errorIds=[]):
        template_values = {
            'workplaces': workplaces,
            'tshirts' : tshirts,
            'orderedWorkplaces': orderedWorkplaces,
            'p': params,
            'errors': errors,
            'errorIds': errorIds,
        }
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))
        
    def get(self):
        self.displayPage()
           
    def saveToSession(self, empl):
        self.session[FIRST_NAME] = empl.firstname
        self.session[LAST_NAME] = empl.lastname
        self.session[EMAIL] = empl.email
        self.session[EMPLOYER] = empl.employer
        self.session[WORKPLACE] = empl.workplace
        self.session[ACCOMODATION] = empl.accomodation
        self.session[RESIDENCE] = empl.residence
        self.session[ROOMMATE] = empl.roommate
        
    def validateEmail(self, email, errors):
        if not email:
            errors.append( getUnenteredMsg( EMAIL ))
            return
        
        if not isEmailValid(email):
            errors.append( ERROR_EMAIL_INVALID )
            return
        
        key = ndb.Key(EmployeeEntity, email)
        if exist(key):
            errors.append( ERROR_EMAIL_EXIST )
            return
        
        return key
                    
    #todo using employee
    def validateData(self):
        errors = []
        errorIds = []
        
        if not self.request.get('firstname'):
            errors.append( getUnenteredMsg( FIRST_NAME ))
            errorIds.append('firstname')
            
        if not self.request.get('lastname'):
            errors.append( getUnenteredMsg( LAST_NAME ))
            errorIds.append('lastname')
            
        key = self.validateEmail( self.request.get('email'), errors )
        if not key:
            errorIds.append('email')
                   
        if not self.request.get('employer'):
            errors.append( getUnenteredMsg( EMPLOYER ))
            errorIds.append('employer')
            
        workplace = self.request.get('workplace')
        if not workplace:
            errors.append( getUnenteredMsg( WORKPLACE ))
            errorIds.append('workplace')
            
        if workplace != 'BA':                                           #todo extract fn
            if ( self.request.get('accomodation') ):
                if not self.request.get('residence'):
                    errors.append( getUnenteredMsg( RESIDENCE ))
                    errorIds.append('residence')
                    
                if not self.request.get('roommate'):
                    errors.append( getUnenteredMsg( ROOMMATE ))
                    errorIds.append('roommate')
        
        return (errors, errorIds, key)
            
            
    def post(self):
        errors, errorIds, key = self.validateData() 
        if errors:
            self.displayPage( self.request.params, errors, errorIds )
            return
        
        email = self.request.get('email')
        logging.info('employee: ' + email)
        logging.info('post data: ' + unicode(self.request.params)) 
        
        empl = Employee()
        empl.firstname = self.request.get('firstname')
        empl.lastname = self.request.get('lastname')
        empl.email = email
        empl.employer = self.request.get('employer')
        empl.workplace = self.request.get('workplace')
        empl.tshirt = self.request.get('tshirt')
        if hasAccomodationRight(empl.workplace):
            if (self.request.get('accomodation')):
                empl.accomodation = 'yes'
                empl.residence = self.request.get('residence')
                empl.roommate = self.request.get('roommate')
            else:
                empl.accomodation = 'no'
        
        persistEmployee( empl )
        try:
            sendMail(empl)
        except:
            logging.exception('Failed to send email %s ', email)    
        
        self.redirect('/results')

        
def sendMail(empl):
    userAddress = empl.email
    senderAddress = MAIL_FROM
    subject = MAIL_SUBJECT
    #todo convert database data to displayable
    body = MAIL_TEXT % \
    {
        FIRST_NAME      : empl.firstname,
        LAST_NAME       : empl.lastname,
        EMPLOYER        : eployerLabels[empl.employer],
        WORKPLACE       : workplaces[ empl.workplace ],
        ACCOMODATION    : accomodationLabels[ empl.accomodation ],
        RESIDENCE       : empl.residence,
        ROOMMATE        : empl.roommate,
        CHARACTER       : empl.character,
    }
    mail.send_mail(senderAddress, userAddress, subject, body)
    
        
class ResultPage(BaseHandler):
            
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('results.html')
        self.response.write(template.render())

application = webapp2.WSGIApplication([
        ('/', IntroPage),
        ('/main', MainPage),
        ('/results', ResultPage),
    ], config = sessionConfig)

def main():
    # Set the logging level in the main function
    # See the section on Requests and App Caching for information on how
    # App Engine reuses your request handlers when you specify a main function
    logging.getLogger().setLevel(logging.INFO)
    

if __name__ == '__main__':
    main()