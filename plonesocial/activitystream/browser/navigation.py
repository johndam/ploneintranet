from zope.interface import implements
from zope.viewlet.interfaces import IViewlet
from zope.publisher.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.component import getMultiAdapter


class PloneSocialNavigation(BrowserView):
    """Provide toplevel navigation that spans plonesocial.activitystream
    and plonesocial.network.
    """
    implements(IViewlet)

    def __init__(self, context, request, view, manager):
        self.context = context
        self.request = request
        self.view = self.__parent__ = view
        self.manager = manager

    def update(self):
        pass

    render = ViewPageTemplateFile("templates/navigation.pt")

    def portal_url(self):
        portal_state = getMultiAdapter(
            (self.context, self.request),
            name=u'plone_portal_state')
        return portal_state.portal_url()

    def items(self):
        menu = (dict(url='@@stream',
                     title='Network updates',
                     state=''),
                dict(url='@@stream/explore',
                     title='Explore',
                     state=''),
                dict(url='@@profile',
                     title='My profile',
                     state=''))
        for item in menu:
            if self.request.URL.endswith(item['url']):
                item['state'] = 'active'
        return menu
