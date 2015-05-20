# -*- coding: utf-8 -*-
"""Base module for unittesting."""

from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import unittest2 as unittest


class PloneintranetAsyncLayer(PloneSandboxLayer):
    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        """Set up Zope."""
        # Load ZCML
        import plone.app.discussion

        self.loadZCML(package=plone.app.discussion)
        import plone.dexterity

        self.loadZCML(package=plone.dexterity)

        import ploneintranet.attachments

        self.loadZCML(package=ploneintranet.async)

        import ploneintranet.docconv.client

        self.loadZCML(package=ploneintranet.docconv.client)
        z2.installProduct(app, 'ploneintranet.async')

    def setUpPloneSite(self, portal):
        """Set up Plone."""
        # Install into Plone site using portal_setup

    def tearDownZope(self, app):
        """Tear down Zope."""
        z2.uninstallProduct(app, 'ploneintranet.async')


FIXTURE = PloneintranetAsyncLayer()
INTEGRATION_TESTING = IntegrationTesting(
    bases=(FIXTURE,), name="PloneintranetAsyncLayer:Integration")
FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(FIXTURE,), name="PloneintranetAsyncLayer:Functional")


class IntegrationTestCase(unittest.TestCase):
    """Base class for integration tests."""

    layer = INTEGRATION_TESTING


class FunctionalTestCase(unittest.TestCase):
    """Base class for functional tests."""

    layer = FUNCTIONAL_TESTING
