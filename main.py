from util.objects import *
from util.routines import *

class Bot(GoslingAgent):
    def run(self):
        d1 = abs(self.ball.location.y - self.foe_goal.location.y) # Distance Ball to Goal
        d2 = abs(self.me.location.y - self.foe_goal.location.y) # Distance Me to Goal
        is_infront_ball = d1 > d2
        if self.kickoff_flag:
            self.set_intent(kickoff())
            return
        if is_infront_ball:
            self.set_intent(goto(self.friend_goal.location))
            return
        self.set_intent(short_shot(self.foe_goal.location))
