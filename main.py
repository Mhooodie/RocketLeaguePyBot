# This file is for strategy
from util.objects import *
from util.routines import *

class Bot(GoslingAgent):
    # This function runs every in-game tick (every time the game updates anything)
    def run(self):
        # set_intent tells the bot what it's trying to do
        speed = 2000
        self.set_intent(drive(speed)) 
        '''2300 max line above'''
