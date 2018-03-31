#
# From: https://stackoverflow.com/a/24488061/470577
# Usage:
#
#     def printer():
#         print 'ipsem lorem'
#
#     t = PerpetualTimer(5,printer)
#     t.start()

from threading import Timer, Thread, Event


class PerpetualTimer():

    def __init__(self, t, hFunction):
        self.t = t
        self.hFunction = hFunction
        self.thread = Timer(self.t, self.handle_function)

    def handle_function(self):
        self.hFunction()
        self.thread = Timer(self.t, self.handle_function)
        self.thread.start()

    def start(self):
        self.thread.start()

    def cancel(self):
        self.thread.cancel()
