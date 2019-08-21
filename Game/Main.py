import jinja2
import webapp2
import os
from google.appengine.ext import ndb

jinja_current_dir = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class Score(ndb.Model):
    k = ndb.IntegerProperty(required = False, default = 100)
Karma = Score(k = 100)
Karma.put()

class Begin(webapp2.RequestHandler):
    def get(self):
        template = jinja_current_dir.get_template("/template/act1.html")
        self.response.write(template.render())
class continue1(webapp2.RequestHandler):
    def post(self):
        choice = self.request.get("choice")
        k = Score.query().fetch()
        if choice == "Choice A":
            template = jinja_current_dir.get_template("/template/continue1p1.html")
            self.response.write(template.render())
        elif choice == "Choice B":
            template = jinja_current_dir.get_template("/template/continue1p2.html")
            self.response.write(template.render())
        elif choice == "Choice C":
            template = jinja_current_dir.get_template("/template/continue1p3.html")
            self.response.write(template.render())
class act2(webapp2.RequestHandler):
        def post(self):
            template = jinja_current_dir.get_template("/template/act2.html")
            self.response.write(template.render())
class continue2(webapp2.RequestHandler):
    def post(self):
        choice = self.request.get("choice")
        if choice == "Choice A":
            template = jinja_current_dir.get_template("/template/continue2p1.html")
            self.response.write(template.render())
        if choice == "Choice B":
            template = jinja_current_dir.get_template("/template/continue2p2.html")
            self.response.write(template.render())
        if choice == "Choice C":
            template = jinja_current_dir.get_template("/template/continue2p3.html")
            self.response.write(template.render())
class act3(webapp2.RequestHandler):
        def post(self):
            template = jinja_current_dir.get_template("/template/act3.html")
            self.response.write(template.render())
class continue3(webapp2.RequestHandler):
    def post(self):
        choice = self.request.get("choice")
        if choice == "Choice A":
            template = jinja_current_dir.get_template("/template/continue3p1.html")
            self.response.write(template.render())
        if choice == "Choice B":
            template = jinja_current_dir.get_template("/template/continue3p2.html")
            self.response.write(template.render())
        if choice == "Choice C":
            template = jinja_current_dir.get_template("/template/continue3p3.html")
            self.response.write(template.render())
class act4(webapp2.RequestHandler):
        def post(self):
            template = jinja_current_dir.get_template("/template/act4.html")
            self.response.write(template.render())
class continue4(webapp2.RequestHandler):
    def post(self):
        choice = self.request.get("choice")
        k = Score.query().fetch()
        if choice == "Choice A" and k >= 150:
            template = jinja_current_dir.get_template("/template/continue4p1.html")
            self.response.write(template.render())
        if choice == "Choice A" and k <= 50:
            template = jinja_current_dir.get_template("/template/continue4p2.html")
            self.response.write(template.render())
        if choice == "Choice B":
            template = jinja_current_dir.get_template("/template/continue4p3.html")
            self.response.write(template.render())
app = webapp2.WSGIApplication([
    ('/', Begin),
    ('/continue1', continue1),
    ('/act2', act2),
    ('/continue2', continue2),
    ('/act3', act3),
    ('/continue3', continue3),
    ('/act4', act4),
    ('/continue4', continue4),
], debug=True)
