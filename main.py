# This File is For Strategy

from util.objects import *
from util.routines import *
from util.tools import find_hits

class GeneralIroh(GoslingAgent):
    #This function runs every in game-tick (every time the game updates anything)
    def run(self):

    # Start
        self.print_debug() # On Screen Debug | Shows debugtext
        if self.intent is not None: # Checks to see if there is intent, if there is it keeps it until cleared.
            self.debug_intent() # On Screen Debug | Shows Intent
            return
        
    # Kickoff Logic
        if self.kickoff_flag:
            self.clear_debug_lines() # Clear Debug Lines on Kickoff
            self.set_intent(kickoff())
            self.add_debug_line('me_to_kickoff', self.me.location, self.ball.location, [0, 0, 255])
            self.add_debug_line('kickoff_to_goal', self.ball.location, self.foe_goal.location, [0, 0, 255])
            self.debugtext = 'Kicking Off' # Debug
            print('Kicking Off') # Log
            return
        
    # Game Logic (Split Later)
        targets = {
            'opponent_goal': (self.foe_goal.left_post, self.foe_goal.right_post),
            'team_goal': (self.friend_goal.right_post, self.friend_goal.left_post)
        }
        hits = find_hits(self, targets)
        target_boost = self.get_closest_large_boost()
        if target_boost is not None and self.me.boost < 20:
            self.set_intent(goto(target_boost.location))
            self.debugtext = 'Getting Boost' # Debug
            print ('Getting Boost') # Log
            return
        if self.infront_of_ball():
            self.set_intent(goto(self.friend_goal.location))
            self.debugtext = 'Moving Back: Infront of Ball' # Debug
            print('Moving Back: Infront of Ball') # Log
            return
        if len(hits['opponent_goal']) > 0:
            self.set_intent(hits['opponent_goal'][0])
            self.debugtext = 'Shooting' # Debug
            print('Shooting') # Log
            return
        if len(hits['team_goal']) > 0:
            self.set_intent(hits['team_goal'][0])
            self.debugtext = 'Defending' # Debug
            print('Defending') # Log
            return
        





        # TEST BELOW NOT IN YET NO FUNCTIONALITY
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



        def getKickoffPosition(vec):
            kickoff_locations = [[2048, 2560], [256, 3848], [0, 4608]]
            # 0 == wide diagonal, 1 == short disgonal, 2 == middle
            if abs(vec[0]) >= 350:
                return 0
            elif abs(vec[0]) > 5:
                return 1
            else:
                return 2
            
        self.kickoff_type = getKickoffPosition(self.me.location)
