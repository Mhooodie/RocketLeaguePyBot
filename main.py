# This File is For Strategy

from util.objects import *
from util.routines import *
from util.tools import find_hits

class Bot(GoslingAgent):
    #This function runs every in game-tick (every time the game updates anything)
    def run(self):
        self.print_debug()
        white = self.renderer.white()
        self.renderer.draw_line_3d(self.me.location, self.ball.location, white)
        if self.intent is not None:
            self.debug_intent()
            return
        if self.kickoff_flag:
            self.set_intent(kickoff())
            self.debugtext = 'Kicking Off'
            print('Kicking Off')
            return
        
        if self.infront_of_ball():
            self.set_intent(goto(self.friend_goal.location))
            self.debugtext = 'Moving Back'
            print('Moving Back')
            return

        if self.me.boost > 50:
            self.set_intent(short_shot(self.foe_goal.location))
            self.debugtext = 'Shooting'
            print ('Shooting')
            return

        target_boost = self.get_closest_large_boost()
        if target_boost is not None:
            self.set_intent(goto(target_boost.location))
            self.debugtext = 'Getting Boost'
            print ('Getting Boost')
            return
        
        # self.print_debug()
        # white = self.renderer.white()
        # self.renderer.draw_line_3d(self.me.location, self.ball.location, white)
        # if self.intent is not None:
        #     self.debug_intent()
        #     return
        # if self.kickoff_flag:
        #     self.set_intent(kickoff())
        #     self.debugtext = 'Kicking Off'
        #     print('Kicking Off')
        #     return
        
        # if self.infront_of_ball():
        #     self.set_intent(goto(self.friend_goal.location))
        #     self.debugtext = 'Moving Back'
        #     print('Moving Back')
        #     return

        # if self.me.boost > 50:
        #     self.set_intent(short_shot(self.foe_goal.location))
        #     self.debugtext = 'Shooting'
        #     print ('Shooting')
        #     return

        # target_boost = self.get_closest_large_boost()
        # if target_boost is not None:
        #     self.set_intent(goto(target_boost.location))
        #     self.debugtext = 'Getting Boost'
        #     print ('Getting Boost')
        #     return