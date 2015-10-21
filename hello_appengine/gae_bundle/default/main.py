import webapp2


class WelcomePage(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("Hello World!")

    def post(self):
        self.response.out.write("You made a post.")

app = webapp2.WSGIApplication([(r'.*/', WelcomePage)
                               ], debug=True)
