# This File is For Strategy

from util.objects import *
from util.routines import *
from util.tools import find_hits

class GeneralIroh(GoslingAgent):
    #This function runs every in game-tick (every time the game updates anything)
    def run(self):
        self.print_debug()
        if self.intent is not None:
            self.debug_intent() # On Screen Debug | Shows Intent
            return
        if self.kickoff_flag:
            self.clear_debug_lines() # Clear Debug Lines on Kickoff
            self.set_intent(kickoff())
            self.add_debug_line('me_to_kickoff', self.me.location, self.ball.location, [0, 0, 255])
            self.add_debug_line('kickoff_to_goal', self.ball.location, self.foe_goal.location, [0, 0, 255])
            self.debugtext = 'Kicking Off' # On Screen Debug | Shows debugtext
            print('Kicking Off') # Log
            return
        target_boost = self.get_closest_large_boost()
        if target_boost is not None and self.me.boost < 33:
            self.set_intent(goto(target_boost.location))
            self.debugtext = 'Getting Boost'
            print ('Getting Boost')
            return
        if self.infront_of_ball():
            self.set_intent(goto(self.friend_goal.location))
            self.debugtext = 'Moving Back'
            print('Moving Back')
            return
        if self.me.boost > 33:
            self.set_intent(short_shot(self.foe_goal.location))
            self.debugtext = 'Shooting'
            print ('Shooting')
            return
