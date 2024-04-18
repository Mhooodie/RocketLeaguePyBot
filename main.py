from util.objects import *
from util.routines import *
from util.tools import find_hits

class Bot(GoslingAgent):
    def run(self):
        if self.intent is not None:
            return
        if self.kickoff_flag:
            self.set_intent(kickoff())
            print ('Kicking Off')
            return
        
        if self.infront_of_ball():
            self.set_intent(goto(self.friend_goal.location))
            print('Moving Back')
            return

        if self.me.boost > 99:
            self.set_intent(short_shot(self.foe_goal.location))
            print ('Shooting')
            return

        target_boost = self.get_closest_large_boost()
        if target_boost is not None:
            self.set_intent(goto(target_boost.location))
            print ('Getting Boost')
            return

# ---------------------- SAVE ----------------------------

#If infront of ball go back then go back to ball else ball infront of it shoot

# class Bot(GoslingAgent):
#     def run(self):
#         if self.intent is not None:
#             return
#         d1 = abs(self.ball.location.y - self.foe_goal.location.y) # Distance Ball to Goal
#         d2 = abs(self.me.location.y - self.foe_goal.location.y) # Distance Me to Goal
#         infront_of_ball = d1 > d2
#         if self.kickoff_flag:
#             self.set_intent(kickoff())
#             return
#         if infront_of_ball:
#             self.set_intent(goto(self.friend_goal.location))
#             return
#         self.set_intent(short_shot(self.foe_goal.location))

# ---------------------- SAVE ----------------------------

#If shot at opponent goal shoot else no shot it shoots at corner of own goal

# class Bot(GoslingAgent):
#     def run(self):
#         if self.intent is not None:
#             return
#         if self.kickoff_flag:
#             self.set_intent(kickoff())
#             return
#         targets = {
#             'at_opponent_goal': (self.foe_goal.left_post, self.foe_goal.right_post),
#             'away_from_our_net': (self.friend_goal.right_post, self.friend_goal.left_post)
#         }
#         hits = find_hits(self,targets)
#         if len(hits['at_opponent_goal']) > 0:
#             self.set_intent(hits['at_opponent_goal'][0])
#             print('Shooting')
#             return
#         if len(hits['away_from_our_net']) > 0:
#             self.set_intent(hits['away_from_our_net'][0])
#             print('Defending')
#             return

# ---------------------- SAVE ----------------------------

# Go to first boost in index

# class Bot(GoslingAgent):
#     def run(self):
#         if self.intent is not None:
#             return
#         if self.kickoff_flag:
#             self.set_intent(kickoff())
#             return
#         available_large_boosts = [boost for boost in self.boosts if boost.large and boost.active]
#         available_small_boosts = [boost for boost in self.boosts if boost.small and boost.active]
#         if len(available_large_boosts) > 0:
#             self.set_intent(goto(available_large_boosts[0].location))
#             print('Going For Boost', available_large_boosts[0].index)
#             return

# ---------------------- SAVE ----------------------------

# class Bot(GoslingAgent):
#     def run(self):
#         if self.intent is not None:
#             return
#         if self.kickoff_flag:
#             self.set_intent(kickoff())
#             print ('Kicking Off')
#             return
        
#         if self.me.boost > 99:
#             self.set_intent(short_shot(self.foe_goal.location))
#             print ('Shooting')
#             return

#         available_boosts = [boost for boost in self.boosts if boost.large and boost.active]
#         closest_boost = None
#         closest_distance = 10000
#         for boost in available_boosts:
#             distance = (self.me.location - boost.location).magnitude()
#             if closest_boost is None or distance < closest_distance:
#                 closest_boost = boost
#                 closest_distance = distance

#         if closest_boost is not None:
#             self.set_intent(goto(closest_boost.location))
#             print ('Getting Boost')
#             return

# ---------------------- SAVE ----------------------------

# class Bot(GoslingAgent):
#     def run(self):
#         if self.intent is not None:
#             return
#         if self.kickoff_flag:
#             self.set_intent(kickoff())
#             print ('Kicking Off')
#             return
        
#         if self.me.boost > 99:
#             self.set_intent(short_shot(self.foe_goal.location))
#             print ('Shooting')
#             return

#         target_boost = self.get_closest_large_boost()

#         if target_boost is not None:
#             self.set_intent(goto(target_boost.location))
#             print ('Getting Boost')
#             return

# ---------------------- SAVE ----------------------------