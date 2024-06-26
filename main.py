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
            'center': (Vector3(-3584*side(self.team), 0, 0), Vector3(3584*side(self.team), 0, 0)) # Z was 73
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
        team = side(self.team) # -1 for blue 1 for orange
        infront_of_ball25 = self.infront_of_ball25()
        infront_of_ball5 = self.infront_of_ball5()
        infront_of_ball = self.infront_of_ball()
        if target_boost is not None:
            me_to_target_boost = abs(self.me.location - target_boost.location).magnitude()

        basicretreat = self.friend_goal.location + Vector3(0, -500*side(self.team), 0)

        retreatTM1 = self.friend_goal.location + Vector3(0, -500*side(self.team), 0)
        retreatTM2 = self.friend_goal.location + Vector3(0, -1700*side(self.team), 0)
        retreatTM3 = self.friend_goal.location + Vector3(0, -2900*side(self.team), 0)
        retreatTM4 = self.friend_goal.location + Vector3(0, -3500*side(self.team), 0)

        retreatTL1 = self.friend_goal.location + Vector3(-2048*side(self.team), -500*side(self.team), 0)
        retreatTL2 = self.friend_goal.location + Vector3(-2048*side(self.team), -1700*side(self.team), 0)
        retreatTL3 = self.friend_goal.location + Vector3(-2048*side(self.team), -2900*side(self.team), 0)
        retreatTL4 = self.friend_goal.location + Vector3(-2048*side(self.team), -3500*side(self.team), 0)

        retreatTR1 = self.friend_goal.location + Vector3(2048*side(self.team), -500*side(self.team), 0)
        retreatTR2 = self.friend_goal.location + Vector3(2048*side(self.team), -1700*side(self.team), 0)
        retreatTR3 = self.friend_goal.location + Vector3(2048*side(self.team), -2900*side(self.team), 0)
        retreatTR4 = self.friend_goal.location + Vector3(2048*side(self.team), -3500*side(self.team), 0)

        retreatmidcenter = Vector3(0, 0, 0)
        retreatmidleft = Vector3(-3584*side(self.team), 0, 0)
        retreatmidright = Vector3(3584*side(self.team), 0, 0)
        retreatmidleftmid = Vector3(-1792*side(self.team), 0, 0)
        retreatmidrightmid = Vector3(1792*side(self.team), 0, 0)

        # Team - Foe Reatreat Points

        retreatFM1 = self.friend_goal.location + Vector3(0, 500*side(self.team), 0)
        retreatFM2 = self.friend_goal.location + Vector3(0, 1700*side(self.team), 0)
        retreatFM3 = self.friend_goal.location + Vector3(0, 2900*side(self.team), 0)
        retreatFM4 = self.friend_goal.location + Vector3(0, 3500*side(self.team), 0)

        retreatFL1 = self.friend_goal.location + Vector3(-2048*side(self.team), 500*side(self.team), 0)
        retreatFL2 = self.friend_goal.location + Vector3(-2048*side(self.team), 1700*side(self.team), 0)
        retreatFL3 = self.friend_goal.location + Vector3(-2048*side(self.team), 2900*side(self.team), 0)
        retreatFL4 = self.friend_goal.location + Vector3(-2048*side(self.team), 3500*side(self.team), 0)

        retreatFR1 = self.friend_goal.location + Vector3(2048*side(self.team), 500*side(self.team), 0)
        retreatFR2 = self.friend_goal.location + Vector3(2048*side(self.team), 1700*side(self.team), 0)
        retreatFR3 = self.friend_goal.location + Vector3(2048*side(self.team), 2900*side(self.team), 0)
        retreatFR4 = self.friend_goal.location + Vector3(2048*side(self.team), 3500*side(self.team), 0)

# Setup Functions'

        def KickoffInitiation(kickoff_type):
            #Initializes Kickoff
            print('Kickoff Initialized')
            if kickoff_type == 0: # Wide Diagnonal / Corners
                if self.ball_local[1] > 0:
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
            #Foe Demoed Actions
            if self.me.boost > 80 and ball_to_teamgoal < opponent_to_teamgoal < me_to_teamgoal and ballside() == True:
                self.debugtext = 'BLOW EM TO SMITHERINES!' # Debug
                print('BLOW EM TO SMITHERINES!') # Log
                self.set_intent(goto_demo(self.foes[0].location)) # defaultThrottle(agent, 2300) Fix gotodemo
                return
            if self.foes[0].demolished:
                if infront_of_ball25 == False: # Infront of ball means closer to opponent net
                    self.set_intent(goto(self.friend_goal.location))
                    self.debugtext = 'Target Down | Repositioning 25' # Debug
                    print('Target Down | Repositioning 25') # Log  
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
            
        def ballside():
            if self.team == 1: # Orange
                if self.ball.location[1] > 0:
                    return True
                else:
                    return False
            else: # Blue
                if self.ball.location[1] < 0:
                    return True
                else:
                    return False
                
        def foeside():
            if self.team == 1: # Orange
                if self.foes[0].location[1] > 0:
                    self.debugtext = 'Foe On Team Side' # Debug
                    print('Foe On Team Side') # Log
                    return True
                else:
                    return False
            else: # Blue
                if self.foes[0].location[1] < 0:
                    self.debugtext = 'Foe On Team Side' # Debug
                    print('Foe On Team Side') # Log
                    return True
                else:
                    return False

        def ballnotgoingin():
            pass
            # Use ball prediction to return true if ball going in in next 6 seconds

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
        
        def ballcolumn(): # Splits field into 3 columns left middle right
            if self.team == 1: # Orange
                if self.ball.location[0] < -893: # Left Returns 1
                    return 1
                elif self.ball.location[0] > -893 and self.ball.location[0] < 893: # Middle Returns 2
                    return 2
                elif self.ball.location[0] > 893: # Right Returns 3
                    return 3
            else: # Blue
                if self.ball.location[0] > 893: # Left Returns 1
                    return 1
                elif self.ball.location[0] > -893 and self.ball.location[0] < 893: # Middle Returns 2
                    return 2
                elif self.ball.location[0] < -893: # Right Returns 3
                    return 3     
                
        def mecolumn(): # Splits field into 3 columns left middle right
            if self.team == 1: # Orange
                if self.me.location[0] < -893: # Left Returns 1
                    return 1
                elif self.me.location[0] > -893 and self.me.location[0] < 893: # Middle Returns 2
                    return 2
                elif self.me.location[0] > 893: # Right Returns 3
                    return 3
            else: # Blue
                if self.me.location[0] > 893: # Left Returns 1
                    return 1
                elif self.me.location[0] > -893 and self.me.location[0] < 893: # Middle Returns 2
                    return 2
                elif self.me.location[0] < -893: # Right Returns 3
                    return 3

        def foecolumn(): # Splits field into 3 columns left middle right
            if self.team == 1: # Orange
                if self.foes[0].location[0] < -893: # Left Returns 1
                    return 1
                elif self.foes[0].location[0] > -893 and self.foes[0].location[0] < 893: # Middle Returns 2
                    return 2
                elif self.foes[0].location[0] > 893: # Right Returns 3
                    return 3
            else: # Blue
                if self.foes[0].location[0] > 893: # Left Returns 1
                    return 1
                elif self.foes[0].location[0] > -893 and self.foes[0].location[0] < 893: # Middle Returns 2
                    return 2
                elif self.foes[0].location[0] < -893: # Right Returns 3
                    return 3      

        def oppballside():
            if self.team == 1: # Orange
                if self.foes[0].location[0] > self.ball.location[0]: # On Left
                    return 1
                elif self.foes[0].location[0] < self.ball.location[0]: # On Right
                    return 2                
            else: # Blue           
                if self.foes[0].location[0] < self.ball.location[0]: # On Left
                    return 1
                elif self.foes[0].location[0] > self.ball.location[0]: # On Right
                    return 2

        def ballrow():
            if self.team == 1: # Orange
                pass
            else: # Blue
                pass

        def hitintent():
            pass
            # Put hits in here later so I can shorten code

        def iswithinrange(me, ball):
            return me in range(ball - 150, ball + 150) # use local location range
        
        def checkshots():
            if len(hits['opponent_goal']) > 0:
                self.set_intent(hits['opponent_goal'][0])
                self.debugtext = 'Shooting'
                print('Shooting')
                return
            if len(hits['center']) > 0 and ballside() == True and infront_of_ball == False:
                self.set_intent(hits['center'][0])
                self.debugtext = 'Centering Ball'
                print('Centering Ball')
                return
            if len(hits['team_goal']) > 0 and ballside() == True:
                self.set_intent(hits['team_goal'][0])
                self.debugtext = 'Defending'
                print('Defending')
                return

        def checknet():
            if side(self.team) == -1: # If Blue Team
                if self.ball.location[1] < -5140:
                    self.clear_intent()
                    self.debugtext = 'Ball In Net' # Debug
                    print('Ball In Net') # Log
                    self.set_intent(goto(self.friend_goal.location + Vector3(0, -200, 0)))
                    if self.me.location[1] > 5141:
                        if len(hits['opponent_goal']) > 0: # Shoot at opponent goal if shot
                            self.set_intent(hits['opponent_goal'][0])
                            self.debugtext = ('Shooting Out of Goal') # Debug
                            print('Shooting Out of Goal') # Log
                            return
                        else:
                            self.debugtext = 'Shooting Out of Goal' # Debug
                            print('Shooting Out of Goal') # Log
                            self.set_intent(short_shot(self.foe_goal.location))
                            return
            elif side(self.team) == 0: # If Orange Team
                if self.ball.location[1] > 5140:
                    self.debugtext = 'Ball In Net' # Debug
                    print('Ball In Net') # Log
                    self.set_intent(goto(self.friend_goal.location + Vector3(0, 200, 0)))
                    if self.me.location[1] > 5141:
                        if len(hits['opponent_goal']) > 0: # Shoot at opponent goal if shot
                            self.set_intent(hits['opponent_goal'][0])
                            self.debugtext = ('Shooting Out of Goal') # Debug
                            print('Shooting Out of Goal') # Log
                            return
                        else:
                            self.debugtext = 'Shooting Out of Goal' # Debug
                            print('Shooting Out of Goal') # Log
                            self.set_intent(short_shot(self.foe_goal.location))
                            return

        def defensivepos():
            self.set_intent(goto_defense(self.friend_goal.location + Vector3(0, 200*side(self.team), 0)))
            self.debugtext = 'Defensive Position!' # Debug
            print('Defense Position!') # Log
            if ball_to_me < ball_to_opponent:
                if len(hits['opponent_goal']) > 0:
                    self.set_intent(hits['opponent_goal'][0])
                    return
                elif len(hits['center']) > 0:
                    self.set_intent(hits['center'][0])
                    return
                elif len(hits['team_goal']) > 0:
                    self.set_intent(hits['team_goal'][0])
                    return
                elif ball_to_me < ball_to_opponent and ballside() == True:
                    self.set_intent(short_shot(self.foe_goal.location))
                    return
            return

        def backup():
            self.set_intent(goto(basicretreat))
            # Check cases where does not need to backup

        # def stuckinnet():
        #     if self.debugtext == 'Defensive Position!':
        #         return
        #     elif self.intent == short_shot or jump_shot or aerial_shot:
        #         if 
            

# Update Functions
        if self.kickoff_flag == False: 
            checknet() # Checks if Ball In Net, Hits out
            #stuckinnet()
            oppballside()
            foecolumn()
            mecolumn()
            ballcolumn()
            ballside()
            # print(f'0 {infront_of_ball}')
            # print(f'5 {infront_of_ball5}')
            # print(f'25 {infront_of_ball25}')

# Camera, ACTION!
        self.print_debug() # On Screen Debug | Shows Debugtext
        if self.intent is not None: # If Intent Repears Until Cleared
            self.debug_intent() # On Screen Debug | Shows Intent
            return

#Chats
        #self.send_quick_chat(QuickChats.CHAT_EVERYONE, Custom_Toxic_GitGut)
        #self.send_quick_chat(QuickChats.CHAT_EVERYONE, Custom_Excuses_Lag)
        #self.send_quick_chat(QuickChats.CHAT_EVERYONE, Custom_Compliments_proud)
        #self.send_quick_chat(QuickChats.CHAT_EVERYONE, Custom_Toxic_404NoSkill)

# Kickoff Action
        if self.kickoff_flag:
            kickoff_type = self.getKickoffPosition(self.me.location) # Gets Kickoff Location
            KickoffInitiation(kickoff_type) # Starts Kickoff Routine
            self.clear_debug_lines()
            self.add_debug_line('me_to_kickoff', self.me.location, self.ball.location, [0, 0, 255])
            self.add_debug_line('kickoff_to_goal', self.ball.location, self.foe_goal.location, [0, 0, 255])
            print(f'Kicking Off | Type: {kickoff_type}') # Log
            return

# Pre-Logic Functions
        # If me | opp | ball | teamnet ZOOM at net and block
        demo() # Check if Opponent Demoed

# Defensive Actions
        if ball_to_teamgoal <= 2500 and ballside() == True:
            defensivepos()
            


# Offensive Pre-Checks

        if self.ball.location[2] > 880 and ball_to_opponentgoal < 1000 and self.ball.location[0] > 900*side(self.team) and self.ball.location[0] < -900*side(self.team):
            self.debugtext = 'Ball Falling From Above Goal'
            print('Ball Falling From Above Goal')

        if me_to_opponentgoal < opponent_to_oppgoal and ball_to_opponentgoal < me_to_opponentgoal: # Opponent Behind me Ball Infront
            hits = find_hits(self, targets)
            if len(hits['opponent_goal']) > 0:
                self.set_intent(hits['opponent_goal'][0])
                self.debugtext = 'Shooting | Opponent Behind Me'
                print('Shooting | Opponent Behind Me')
                return
            elif infront_of_ball == False and opponent_to_oppgoal > 4000:
                self.set_intent(short_shot(self.foe_goal.location + Vector3(0, -600*side(self.team), 0)))
                self.debugtext = 'Short Shot | Center Opp Goal'
                hits = find_hits(self, targets)
                return
            
        if ball_to_me < ball_to_opponent and infront_of_ball5 == False: # If I am Closer to the ball and infront of it then shoot
            print('Closer & Infront of Ball 5')
            hits = find_hits(self, targets)
            if len(hits['opponent_goal']) > 0:
                self.set_intent(hits['opponent_goal'][0])
                self.debugtext = 'Shooting | Closer, More Boost, Infront of Ball 5'
                print('Shooting | Closer, More Boost, Infront of Ball 5')
                return
            elif ball_to_me < ball_to_opponent and infront_of_ball5 == False:
                self.set_intent(short_shot(self.foe_goal.location + Vector3(0, -600*side(self.team), 0)))
                self.debugtext = 'Short Shot | Closer, More Boost, Infront of Ball 5' 
                print('Short Shot | Closer, More Boost, Infront of Ball 5')
                hits = find_hits(self, targets)
                return

# Movement Actions
        if target_boost is not None and self.me.boost < 20 and ball_to_me > ball_to_opponent and ballside() == False: # DELETE BALL ME BALL OPP LATER IF NOT GETTING BOOST ***
            self.set_intent(goto(target_boost.location)) # add check for opponent shooting into goto ***
            self.debugtext = f'Getting Large Boost At {target_boost.location}' # Debug
            print (f'Getting Large Boost At {target_boost.location}') # Log
            return # Dont want to always get large boost especially if far so fix this later ***
            # angles = defaultPD(agent, local_target, self.direction)

# Offensive Actions
        if infront_of_ball25 == True: # If infront of ball move back
            backup()
            checkshots()
            self.debugtext = 'Moving Back: Infront of Ball 25' # Debug
            print('Moving Back: Infront of Ball 25') # Log
            if self.ball.location[1] == self.me.location[1]: # Fix later -> if iswithinrange(self.me.location[0], self.ball.location[0]):
                self.set_intent(goto(self.friend_goal.right_post))
                self.debugtext = 'Moving Back: Infront of Ball 25 & Ball In Way' # Debug
                print('Moving Back: Infront of Ball 25 & Ball In Way') # Log
                return
            return
        checkshots()
        
# Null
        print('No Other Parameters Met')

        if ballside() == True and ball_to_opponent < ball_to_me:
            defensivepos()
        elif ballside() == True and ball_to_opponent > ball_to_me:
            checkshots()
        elif ballside() == False  and ball_to_opponent > ball_to_me:
            checkshots()
        elif ballside() == False and ball_to_opponent < ball_to_me:
            defensivepos()

        # checkshots()
        # defensivepos() THESE WILL BREAK KICKOFF
        # if self.intent == None:
        #     defensivepos()
        # if ballside() == True or ballside() == False:
        #     defensivepos()
        if self.infront_of_ball == False:
            if len(hits['opponent_goal']) > 0:
                self.set_intent(hits['opponent_goal'][0])
                self.debugtext = 'Shooting | Closer, More Boost, Infront of Ball 5'
                print('Shooting | Closer, More Boost, Infront of Ball 5')
                return
            else:
                self.set_intent(short_shot(self.foe_goal.location))
        if ballside() == False:
            if len(hits['opponent_goal']) > 0:
                self.set_intent(hits['opponent_goal'][0])
                self.debugtext = 'Shooting | Closer, More Boost, Infront of Ball 5'
                print('Shooting | Closer, More Boost, Infront of Ball 5')
                return
            else:
                self.set_intent(short_shot(self.foe_goal.location))
        if ballside == True:
            if len(hits['opponent_goal']) > 0:
                self.set_intent(hits['opponent_goal'][0])
                self.debugtext = 'Shooting | Closer, More Boost, Infront of Ball 5'
                print('Shooting | Closer, More Boost, Infront of Ball 5')
                return
            else:
                defensivepos()