# encoding: utf-8
# Copyright 2011 California Institute of Technology. ALL RIGHTS
# RESERVED. U.S. Government Sponsorship acknowledged.

'''EDRN Knowledge Environment Reviews: Testing base code.
'''

from Products.Five import fiveconfigure
from Products.Five import zcml
from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import onsetup

# Traditional Products we have to load manually for test cases:
# (none at this time)

@onsetup
def setupEKESite():
    '''Set up additional products required.'''
    fiveconfigure.debug_mode = True
    import eke.review
    zcml.load_config('configure.zcml', eke.review)
    fiveconfigure.debug_mode = False

setupEKESite()
ptc.setupPloneSite(products=['eke.review'])

class BaseTestCase(ptc.PloneTestCase):
    '''Base for tests in this package.'''
    
class FunctionalBaseTestCase(ptc.FunctionalTestCase):
    '''Base class for functional (doc-)tests.'''
