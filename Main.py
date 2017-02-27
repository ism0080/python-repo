import View

class Main(object):
    def __init__(self, name):
        self.name = name

    def go(self):
        View.start()
        View.say("Hello, " + self.name)
        View.stop()

stuff = Main("Elliot")

stuff.go()
