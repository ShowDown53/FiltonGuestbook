from google.appengine.ext import ndb

class Message(ndb.Model):
    name = ndb.StringProperty()
    email = ndb.StringProperty()
    message = ndb.TextProperty()
    date = ndb.DateTimeProperty(auto_now_add = True)
