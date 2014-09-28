import os
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb

import jinja2
import webapp2
import logging

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

def current_user_key():
    return ndb.Key('User', users.get_current_user().user_id())

class Data(ndb.Model):
    title = ndb.StringProperty(required=True)
    description = ndb.TextProperty()
    date_added = ndb.DateTimeProperty(required=True, auto_now_add=True)
    closed = ndb.BooleanProperty(required=True, default=False)
    labels = ndb.StringProperty(repeated=True)

class MainPage(webapp2.RequestHandler):
    def get(self):
        data, current_data = Backbuffer().get_data(
            current_data_urlsafe_key=self.request.get('data'));

        template_values = {
            'user': users.get_current_user(),
            'data': data,
            'current_data': current_data,
            'edit': self.request.get('edit'),
            'url': users.create_logout_url(self.request.uri),
            'url_linktext': 'Logout',
        }

        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))

class Backbuffer:
    class Add(webapp2.RequestHandler):
        def post(self):
            data = Data(parent=current_user_key())
            data.title = self.request.get('title')
            data.description = self.request.get('description')
            data.labels = self.request.get_all('label')
            data.put()

            self.redirect('/')

    class Delete(webapp2.RequestHandler):
        def post(self):
            if self.request.get('data'):
                ndb.Key(urlsafe=self.request.get('data')).delete()
            self.redirect('/')

    class Edit(webapp2.RequestHandler):
        def post(self):
            if self.request.get('data'):
                data = ndb.Key(urlsafe=self.request.get('data')).get()
                data.title = self.request.get('title')
                data.description = self.request.get('description')
                data.labels = self.request.get_all('label')

                if self.request.get('closed'):
                    data.closed = True
                else:
                    data.closed = False

                data.put()
            self.redirect('/')

    def get_data(self, current_data_urlsafe_key=None):
        data_query = Data.query(ancestor=current_user_key()).order(
            Data.closed, -Data.date_added)
        data = data_query.fetch()

        current_data = None
        if current_data_urlsafe_key:
            current_data = ndb.Key(urlsafe=current_data_urlsafe_key).get()

        return data, current_data

application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/add', Backbuffer.Add),
    ('/delete', Backbuffer.Delete),
    ('/edit', Backbuffer.Edit),
], debug=True)
