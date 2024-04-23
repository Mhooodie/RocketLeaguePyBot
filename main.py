# This File is For Strategy

from util.objects import *
from util.routines import *
from util.tools import find_hits
from rlbot.utils.structures.quick_chats import QuickChats

class GeneralIroh(GoslingAgent):
    #This function runs every in game-tick (every time the game updates anything)
    def run(self):

    # Setup Var's
        ball_local = self.me.local(self.ball.location - self.me.location)
        self.onright = True # Using to setup flips for speed kickoff like Kamael
        targets = {
            'opponent_goal': (self.foe_goal.left_post, self.foe_goal.right_post),
            'team_goal': (self.friend_goal.right_post, self.friend_goal.left_post)
        }
        hits = find_hits(self, targets)
        target_boost = self.get_closest_large_boost()
        target_boost2 = self.get_closest_small_boost()
        #target_boost3 = self.get_closest_boost(target_boost, target_boost2) # Figure out how to find closest boost BIG OR SMALL
        ball_to_opponent = abs(self.ball.location - self.foes[0].location).magnitude()
        ball_to_me = abs(self.ball.location - self.foes[0].location).magnitude()
        ball_to_teamgoal = abs(self.ball.location - self.friend_goal.location).magnitude()
        me_to_oponent = abs(self.me.location - self.foes[0].location).magnitude()
        me_to_teamgoal = abs(self.me.location - self.friend_goal.location).magnitude()

    # Setup Functions'
        def KickoffInitiation(self, kickoff_type):
            print('Kickoff Initialized')
            if kickoff_type == 0: # Wide Diagnonal / Corners
                if ball_local[1] > 0:
                    self.debugtext = 'Kickoff off from: Right Wide Diagonal' # Debug
                    print('Kickoff off from: Right Wide Diagnonal') # Log
                    self.set_intent(kickoff())
                    return
                else:
                    self.debugtext = 'Kickoff off from: Left Wide Diagonal' # Debug
                    print('Kickoff off from: Left Wide Diagnonal') # Log
                    self.set_intent(kickoff())
                    return   
            elif kickoff_type == 1: # Short Diagonal / Back Sides
                if ball_local[1] < 0:
                    self.debugtext = 'Kicking off from: Right Short Diagonal' # Debug
                    print('Kicking off from: Right Short Diagonal') # Log
                    self.set_intent(kickoff())
                    return
                else:
                    self.debugtext = 'Kicking off from: Left Short Diagonal' # Debug
                    print('Kicking off from: Left Short Diagonal') # Log
                    self.set_intent(kickoff())
                    return  
            elif kickoff_type == 2: # Middle / Back Middle
                self.debugtext = 'Kicking off from: Middle' # Debug
                print('Kicking off from: Middle') # Log
                self.set_intent(kickoff())
                return
            else:
                print('Error KickoffInitiation Cannot recognize Kickoff Position')
                self.set_intent(kickoff())
                return
            
    # Start
        self.print_debug() # On Screen Debug | Shows debugtext
        if self.intent is not None: # Checks to see if there is intent, if there is it keeps it until cleared.
            self.debug_intent() # On Screen Debug | Shows Intent
            return

    # Kickoff Logic
        if self.kickoff_flag:
            kickoff_type = self.getKickoffPosition(self.me.location) # Gets Kickoff Location
            KickoffInitiation(self, kickoff_type) # Starts Kick off Routine
            self.clear_debug_lines() # Clear Debug Lines on Kickoff
            self.add_debug_line('me_to_kickoff', self.me.location, self.ball.location, [0, 0, 255])
            self.add_debug_line('kickoff_to_goal', self.ball.location, self.foe_goal.location, [0, 0, 255])
            print(f'Kicking Off | Type: {kickoff_type}') # Log
            #self.send_quick_chat(False, quick_chat='GG') # Test Quickchat, test later with custom chats FIX LATER
            return

    # Game Logic (Split Later)
        # if I am closer to ball then enemy after kickoff short shot
        if target_boost is not None and self.me.boost < 20: # Gets large boost if boost under 20 and conditions in function are met
            self.set_intent(goto(target_boost.location))
            self.debugtext = 'Getting Large Boost' # Debug
            print ('Getting Large Boost') # Log
            #print (f'Closest Boost ANY: {target_boost3}')
            return 
        if self.infront_of_ball(): # If infront of ball move back
            self.set_intent(goto(self.friend_goal.location))
            self.debugtext = 'Moving Back: Infront of Ball' # Debug
            print('Moving Back: Infront of Ball') # Log
            return
        if len(hits['opponent_goal']) > 0: # Shoot at opponent goal if shot
            self.set_intent(hits['opponent_goal'][0])
            self.debugtext = 'Shooting' # Debug
            print('Shooting') # Log
            return
        if len(hits['team_goal']) > 0: # Shoot at sides of my goal if shot
            self.set_intent(hits['team_goal'][0])
            self.debugtext = 'Defending' # Debug
            print('Defending') # Log
            return   
