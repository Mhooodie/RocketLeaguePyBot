# This File is For Strategy

from util.objects import *
from util.routines import *
from util.tools import find_hits
from rlbot.utils.structures.quick_chats import QuickChats

class GeneralIroh(GoslingAgent):
    #This function runs every in game-tick (every time the game updates anything)
    def run(self):

# Setup Var's
        targets = {
            'opponent_goal': (self.foe_goal.left_post, self.foe_goal.right_post),
            'team_goal': (self.friend_goal.right_post, self.friend_goal.left_post), # Defending on enemy side for some reason ***
            'center': (Vector3(-3584*side(self.team), 0, 73), Vector3(3584*side(self.team), 0, 73)) 
        }
        hits = find_hits(self, targets)
        target_boost = self.get_closest_large_boost()
        target_boost2 = self.get_closest_small_boost()
        #target_boost3 = self.get_closest_boost(target_boost, target_boost2) # Figure out how to find closest boost BIG OR SMALL ***
        ball_to_opponent = abs(self.ball.location - self.foes[0].location).magnitude()
        ball_to_me = abs(self.ball.location - self.foes[0].location).magnitude()
        ball_to_teamgoal = abs(self.ball.location - self.friend_goal.location).magnitude()
        ball_to_opponentgoal = abs(self.ball.location - self.foe_goal.location).magnitude()
        me_to_oponent = abs(self.me.location - self.foes[0].location).magnitude()
        me_to_teamgoal = abs(self.me.location - self.friend_goal.location).magnitude()
        me_to_opponentgoal = abs(self.me.location - self.foe_goal.location).magnitude()
        opponent_to_teamgoal = abs(self.foes[0].location - self.friend_goal.location).magnitude()
        opponent_to_oppgoal = abs(self.foes[0].location - self.foe_goal.location).magnitude()


# Setup Functions'
        def KickoffInitiation(kickoff_type):
            print('Kickoff Initialized')
            if kickoff_type == 0: # Wide Diagnonal / Corners
                if self.ball_local[1] > 0:
                    self.debugtext = 'Kickoff off from: Right Wide Diagonal' # Debug
                    print('Kickoff off from: Right Wide Diagnonal') # Log
                    self.set_intent(kickoff_wide())
                    return
                else:
                    self.debugtext = 'Kickoff off from: Left Wide Diagonal' # Debug
                    print('Kickoff off from: Left Wide Diagnonal') # Log
                    self.set_intent(kickoff_wide())
                    return
            elif kickoff_type == 1: # Short Diagonal / Back Sides
                if self.ball_local[1] < 0:
                    self.debugtext = 'Kicking off from: Right Short Diagonal' # Debug
                    print('Kicking off from: Right Short Diagonal') # Log
                    self.set_intent(kickoff_short())
                    return
                else:
                    self.debugtext = 'Kicking off from: Left Short Diagonal' # Debug
                    print('Kicking off from: Left Short Diagonal') # Log
                    self.set_intent(kickoff_short())
                    return
            elif kickoff_type == 2: # Middle / Back Middle
                self.debugtext = 'Kicking off from: Middle' # Debug
                print('Kicking off from: Middle') # Log
                self.set_intent(kickoff_center())
                return
            else:
                self.debugtext = 'Error KickoffInitiation Cannot recognize Kickoff Position' # Debug
                print('Error KickoffInitiation Cannot recognize Kickoff Position') # Log
                self.set_intent(kickoff())
                return
            
        def demo():
            if self.me.boost > 80 and ball_to_teamgoal < opponent_to_teamgoal < me_to_teamgoal:
                self.debugtext = 'BLOW EM TO SMITHERINES!' # Debug
                print('BLOW EM TO SMITHERINES!') # Log
                self.set_intent(goto(self.foes[0].location)) # defaultThrottle(agent, 2300) Fix gotodemo
                return
            
        def ballside():
            if self.team == 1: # Orange
                if self.ball.location[1] > 0:
                    self.debugtext = 'Ball On Team Side' # Debug
                    print('Ball On Team Side') # Log
                    return True
                else:
                    return False
            else: # Blue
                if self.ball.location[1] < 0:
                    self.debugtext = 'Ball On Team Side' # Debug
                    print('Ball On Team Side') # Log
                    return True
                else:
                    return False

        def ballsidecolumn():
            if self.team == 1: # Orange
                if self.ball.location[1] > 0:
                    pass # My Side   
                else:
                    pass # Opp Side
            else: # Blue
                if self.ball.location[1] < 0:
                    pass # My Side   
                else:
                    pass # Opp Side
        
        def ballcolumn():
            if self.team == 1: # Orange
                pass
            else: # Blue
                pass

        def ballrow():
            if self.team == 1: # Orange
                pass
            else: # Blue
                pass

# Start
        self.print_debug() # On Screen Debug | Shows debugtext
        if self.intent is not None: # Checks to see if there is intent, if there is it keeps it until cleared.
            self.debug_intent() # On Screen Debug | Shows Intent
            return

# Kickoff Logic
        if self.kickoff_flag:
            kickoff_type = self.getKickoffPosition(self.me.location) # Gets Kickoff Location
            print(self.ball_local)
            KickoffInitiation(kickoff_type) # Starts Kick off Routine
            self.clear_debug_lines()
            self.add_debug_line('me_to_kickoff', self.me.location, self.ball.location, [0, 0, 255])
            self.add_debug_line('kickoff_to_goal', self.ball.location, self.foe_goal.location, [0, 0, 255])
            print(f'Kicking Off | Type: {kickoff_type}') # Log
            #self.send_quick_chat(False, QuickChats.Compliments_IGotIt) # Test Quickchat, test later with custom chats FIX LATER
            return
        
# Game Logic

    # Opponent Demolished
        demo()
        if self.foes[0].demolished:
            if self.infront_of_ball25(): # Infront of ball means closer to opponent net
                self.set_intent(goto(self.friend_goal.location))
                self.debugtext = 'Target Down | Repositioning' # Debug
                print('Target Down | Repositioning') # Log  
                return
            elif len(hits['opponent_goal']) > 0:
                self.set_intent(hits['opponent_goal'][0])
                self.debugtext = 'Target Neutralized | Shooting' # Debug
                print('Target Neutralized | Shooting') # Log
                return
            else:
                self.set_intent(goto(self.friend_goal.location))
                self.debugtext = 'Target Down | Repositioning' # Debug
                print('Target Down | Repositioning') # Log  
                return
            
    # Offensive Pre Checks
        if me_to_opponentgoal < opponent_to_oppgoal and ball_to_opponentgoal < me_to_opponentgoal:
            if len(hits['opponent_goal']) > 0:
                self.set_intent(hits['opponent_goal'][0])
                self.debugtext = f'Shooting | Opponent Behind Me {hits[0]}' # Debug
                print(f'Shooting | Opponent Behind Me {hits[0]}') # Log
                return
            elif self.infront_of_ball:
                self.set_intent(short_shot(self.foe_goal.location + Vector3(0, 500*side(self.team), 0)))
                self.debugtext = 'Short Shot | Center Opp Goal' # Debug
                return
            elif len(hits['opponent_goal']) > 0:
                self.set_intent(hits['opponent_goal'][0])
                self.debugtext = f'Shooting | Opponent Behind Me {hits[0]}' # Debug
                print(f'Shooting | Opponent Behind Me {hits[0]}') # Log
                return
            
        if ball_to_me < ball_to_opponent and self.me.boost >= self.foes[0].boost and self.infront_of_ball25(): # If I am Closer to the ball, infront of it, and have more boost then I shoot
            if len(hits['opponent_goal']) > 0:
                self.set_intent(hits['opponent_goal'][0])
                self.debugtext = f'Shooting | Closer, More Boost, Infront of Ball {hits[0]}' # Debug
                print(f'Shooting | Closer, More Boost, Infront of Ball {hits[0]}') # Log
                return
            else:
                self.set_intent(short_shot(self.foe_goal.location + Vector3(0, 500*side(self.team), 0)))
                self.debugtext = 'Short Shot | Closer, More Boost, Infront of Ball' # Debug
                print('Short Shot | Closer, More Boost, Infront of Ball') # Log
                if len(hits['opponent_goal']) > 0:
                    self.set_intent(hits['opponent_goal'][0])
                    self.debugtext = f'Shooting | Closer, More Boost, Infront of Ball {hits[0]}' # Debug
                    print(f'Shooting | Closer, More Boost, Infront of Ball {hits[0]}') # Log
                    return                
                else:
                    return
                    
    # General Movement Checks
        target_boost = self.get_closest_large_boost() # Boost to Friend_Goal < Ball to Friend Goal AND Foe to Ball > Me to Ball AND My Boost < 20
        if target_boost is not None:
            me_to_targboost = abs(self.me.location - target_boost.location).magnitude()
        if target_boost is not None and self.me.boost < 20:
            self.set_intent(goto(target_boost.location)) # add check for opponent shooting into goto ***
            self.debugtext = f'Getting Large Boost At {target_boost.location}' # Debug
            print (f'Getting Large Boost At {target_boost.location}') # Log
            return # Dont want to always get large boost especially if far so fix this later ***
        
    # Defense Checks
        ballside() # True if on team side
        if self.ball.location[1] < 5030*side(self.team):
            self.debugtext = 'Ball In Net' # Debug
            print('Ball In Net') # Log
            self.set_intent(goto(self.friend_goal.location + Vector3(0, 500*side(self.team), 0)))
            if self.me.location[1] < 5030*side(self.team):
                if len(hits['opponent_goal']) > 0: # Shoot at opponent goal if shot
                    self.set_intent(hits['opponent_goal'][0])
                    self.debugtext = (f'Shooting Out of Goal | {hits[0]}') # Debug
                    print(f'Shooting Out of Goal | {hits[0]}') # Log
                    return
                else:
                    self.debugtext = 'Shooting Out of Goal' # Debug
                    print('Shooting Out of Goal') # Log
                    self.set_intent(short_shot(self.foe_goal.location))
                    return

        if ball_to_teamgoal <= 2000:
            self.set_intent(goto_defense(self.friend_goal.location + Vector3(0, 200*side(self.team), 0)))
            self.debugtext = 'Defensive Position!' # Debug
            print('Defense Position!') # Log
            if ball_to_opponent >= ball_to_me:
                if len(hits['center']) > 0:
                    self.set_intent(hits['center'][0])
                    return
                elif len(hits['team_goal']) > 0:
                    self.set_intent(hits['team_goal'][0])
                    return
                elif len(hits['opponent_goal']) > 0:
                    self.set_intent(hits['opponent_goal'][0])
                    return
                else:
                    self.set_intent(short_shot(self.foe_goal.location))
                    return
            return
        
        if ballside() == True and ball_to_opponent < ball_to_me:
            self.set_intent(goto_defense(self.friend_goal.location + Vector3(0, 200*side(self.team), 0)))
            self.debugtext = 'Defensive Position!' # Debug
            print('Defense Position!') # Log
            if ball_to_opponent >= ball_to_me:
                if len(hits['center']) > 0:
                    self.set_intent(hits['center'][0])
                    return
                elif len(hits['team_goal']) > 0:
                    self.set_intent(hits['team_goal'][0])
                    return
                elif len(hits['opponent_goal']) > 0:
                    self.set_intent(hits['opponent_goal'][0])
                    return
                else:
                    self.set_intent(short_shot(self.foe_goal.location))
                    return
            return

    # Offense Checks
        if self.infront_of_ball25(): # If infront of ball move back
            self.set_intent(goto(self.friend_goal.location + Vector3(0, -500*side(self.team), 0)))
            self.debugtext = 'Moving Back: Infront of Ball' # Debug
            print('Moving Back: Infront of Ball') # Log
            if self.ball.location[1] == self.me.location[1]:
                self.set_intent(goto(self.friend_goal.right_post))
                self.debugtext = 'Moving Back: Infront of Ball & Ball In Way' # Debug
                print('Moving Back: Infront of Ball & Ball In Way') # Log
                return
            return
        if len(hits['opponent_goal']) > 0: # Shoot at opponent goal if shot
            self.set_intent(hits['opponent_goal'][0])
            self.debugtext = 'Shooting' # Debug
            print('Shooting') # Log
            return
        #  and ball_to_teamgoal < ball_to_opponentgoal and me_to_teamgoal < ball_to_teamgoal for bellow code testing switch with ballside()
        if len(hits['center']) > 0 and ballside() == True and self.infront_of_ball:
            self.set_intent(hits['center'][0])
            self.debugtext = 'Centering Ball' # Debug
            print('Centering Ball') # Log
            return
        if len(hits['team_goal']) > 0 and ballside() == True: # Shoot at sides of my goal if shot
            self.set_intent(hits['team_goal'][0])
            self.debugtext = 'Defending' # Debug
            print('Defending') # Log
            return   
        
    # If Nothing Else
        if self.infront_of_ball():
            self.set_intent(short_shot(self.foe_goal))
            self.debugtext = 'Shooting Short Shot | No Other Parameters Met' # Debug
            print('Shooting Short Shot | No Other Parameters Met') # Log
            return
