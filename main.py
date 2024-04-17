# This file is for strategy
from util.objects import *
from util.routines import *

class Bot(GoslingAgent):
    # This function runs every in-game tick (every time the game updates anything)
    def run(self):
        if self.kickoff_flag:
            self.set_intent(kickoff())
            return
        self.set_intent(atba())
