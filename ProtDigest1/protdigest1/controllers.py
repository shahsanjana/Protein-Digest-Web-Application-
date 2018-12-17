"""This module contains the controller classes of the application."""

# symbols which are imported by "from hoyataxa.controllers import *"
__all__ = ['Root']

# standard library imports
# import logging
import datetime

# third-party imports
from turbogears import controllers, expose, flash
from proteininfo import digest


from turbogears import validate, validators
from turbogears import widgets, error_handler

class SearchFields(widgets.WidgetsList):
    sequence= widgets.TextField(label="Protein Sequence",
                                default="WVEAILADGYNQCRWKDIQH")
    enzyme = widgets.SingleSelectField(label="Enzyme",
                                     options=["Trypsin",
                                              "Lys N",
                                              "Lys C", "Proteinase K","Thermolysin"],
                                     default="Trypsin")
    

    cleave=widgets.SingleSelectField(label="Missed Cleavage Sites",
                                        options =["0","1","2","3","4","5"],
                                        default = "0")
    minlen = widgets.TextField(label="Minimum Number of Amino Acids in Peptide",
                               default="0")
    maxlen = widgets.TextField(label = "Maximum Number of Amino Acids in Peptide",
                               default="500")
    minmw= widgets.TextField(label = "Minimum Molecular Weight",
                             default= "0" )
    maxmw = widgets.TextField(label ="Maximum Molecular Weight",
                              default = "10000")
  
    
                               
                                
                                    

class SearchFieldsSchema(validators.Schema):
    sequence = validators.All(validators.PlainText(),
                           validators.String(min=2,strip=True))
    enzyme = validators.OneOf(["Trypsin","Lys N","Lys C", "Proteinase K", "Thermolysin"])
    cleave = validators.OneOf(["0","1","2","3","4","5"])
    minlen = validators.All(validators.Int(),
                           validators.String(min=1,strip=True))
    maxlen = validators.All(validators.Int(),
                           validators.String(min=1,strip=True))
    minmw = validators.All(validators.Int(),
                           validators.String(min=1,strip=True))
    maxmw = validators.All(validators.Int(),
                           validators.String(min=1,strip=True))
    
    
 
search_form = widgets.TableForm(
    fields = SearchFields(),
    validator = SearchFieldsSchema(),
    action = "peptidetable",
    submit_text = "Search"
    )

class Root(controllers.RootController):
    """The root controller of the application."""

    @expose(template="protdigest1.templates.welcome")
    def index(self):
        """"Show the welcome page."""
        return dict(form=search_form,
                    title="Protein Digester")

    @validate(form=search_form)
    @error_handler(index)
    @expose(template="protdigest1.templates.digest") 
    def peptidetable(self, sequence, enzyme, cleave, minlen, maxlen, minmw, maxmw):
        (l0,l1)=digest(sequence,enzyme,cleave,minlen,maxlen,minmw,maxmw)
        rows=l0
        rows2=l1
        return dict(rows=rows,rows2=rows2) 
        






