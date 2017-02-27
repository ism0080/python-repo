import View
import CheckMark

class Main(object):
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    def go(self):
        View.start()
        View.say("Hello, " + self.name)
        result = CheckMark.checkMark(self.mark)
        View.say("Your result is " + result)
        View.stop()

stuff = Main("Elliot", 51)

stuff.go()
