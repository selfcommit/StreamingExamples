import webapp2
import random


class RandomNumber(webapp2.RequestHandler):
    def get(self):
        number = random.random()
        self.response.out.write(number)

    def post(self):
        number = self.request.get("number")
        new_number = int(number) + int(random.random()*10)
        self.response.out.write(new_number)

app = webapp2.WSGIApplication([(r'.*/', RandomNumber)
                               ], debug=True)
