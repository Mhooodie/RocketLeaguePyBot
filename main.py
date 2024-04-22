# This File is For Strategy

from util.objects import *
from util.routines import *
from util.tools import find_hits
from rlbot.utils.structures.quick_chats import QuickChats

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
            kickoff_type = self.getKickoffPosition(self.me.location) # Gets Kickoff Location
            self.KickoffInitiation(kickoff_type) # Starts Kick off Routine
            self.clear_debug_lines() # Clear Debug Lines on Kickoff
            self.add_debug_line('me_to_kickoff', self.me.location, self.ball.location, [0, 0, 255])
            self.add_debug_line('kickoff_to_goal', self.ball.location, self.foe_goal.location, [0, 0, 255])
            print('Kicking Off') # Log
            #self.send_quick_chat(False, quick_chat='Wow') # Test Quickchat, test later with custom chats FIX LATER
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
        
