from google.appengine.ext import ndb

class KarmaScore(ndb.Model):
    Kscore = ndb.IntegerProperty(required = True)
