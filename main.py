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

        # blue = 0
        blue_right_corner = [-2048, -2560]
        blue_left_corner = [2048, -2560]
        blue_back_right = [-256.0, -3840]
        blue_back_left = [256.0, -3840]
        blue_back_center = [0.0, -4608]

        # orange = 1
        orange_right_corner = [2048, 2560]
        orange_left_corner = [-2048, 2560]
        orange_back_right = [256.0, 3840]
        orange_back_left = [-256.0, 3840]
        orange_back_center = [0.0, 4608]

        print(self.team) # Tells what team I am on (DELETE THIS LATER)
        
        if self.kickoff_flag:
            self.clear_debug_lines() # Clear Debug Lines on Kickoff
            self.set_intent(kickoff())
            self.add_debug_line('me_to_kickoff', self.me.location, self.ball.location, [0, 0, 255])
            self.add_debug_line('kickoff_to_goal', self.ball.location, self.foe_goal.location, [0, 0, 255])
            self.debugtext = 'Kicking Off' # On Screen Debug | Shows debugtext
            print('Kicking Off') # Log
            return
        targets = {
            'opponent_goal': (self.foe_goal.left_post, self.foe_goal.right_post),
            'team_goal': (self.friend_goal.right_post, self.friend_goal.left_post)
        }
        hits = find_hits(self, targets)
        target_boost = self.get_closest_large_boost()
        if target_boost is not None and self.me.boost < 20:
            self.set_intent(goto(target_boost.location))
            self.debugtext = 'Getting Boost'
            print ('Getting Boost')
            return
        if self.infront_of_ball():
            self.set_intent(goto(self.friend_goal.location))
            self.debugtext = 'Moving Back: Infront of Ball'
            print('Moving Back: Infront of Ball')
            return
        if len(hits['opponent_goal']) > 0:
            self.set_intent(hits['opponent_goal'][0])
            return
        if len(hits['team_goal']) > 0:
            self.set_intent(hits['team_goal'][0])
            return
        self.debugtext = 'Shooting'
