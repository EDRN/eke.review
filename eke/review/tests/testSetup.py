# encoding: utf-8
# Copyright 2010 California Institute of Technology. ALL RIGHTS
# RESERVED. U.S. Government Sponsorship acknowledged.

'''EDRN Knowledge Environment Reviews: test the setup of this package.
'''

from base import BaseTestCase
from eke.review.config import PROJECTNAME
from Products.Archetypes.public import listTypes
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.utils import safe_hasattr
import unittest

class SetupTest(BaseTestCase):
    '''Unit tests the setup of this package.'''
    def testDependencies(self):
        '''Check if our dependent packages are installed when we're installed.'''
        skinsTool = getToolByName(self.portal, 'portal_skins')
        self.failUnless(safe_hasattr(skinsTool, 'PloneFormGen'), "PloneFormGen not installed, but it's supposed to be")
    def testWidgets(self):
        '''Ensure our custom widgets are available to PloneFormGen'''
        classes = listTypes(PROJECTNAME)
        myTypes = [item['name'] for item in classes]
        typesTool = getToolByName(self.portal, 'portal_types')
        for typeName in ('FormFolder', 'FieldsetFolder'):
            ptType = typesTool.getTypeInfo(typeName).allowed_content_types
            for myType in myTypes:
                self.failUnless(myType in ptType, 'My widget "%s" missing from "%s"' % (myType, typeName))

def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(SetupTest))
    return suite
    
