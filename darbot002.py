# inspired by attackbot-cadet
#
# there is safety in numbers
# Keep your friends close, but your enemies closer

import rg

class Robot:
    def act(self, game):
        
        print
        print "Turn: " +str( game.turn) + "\tBot: " + str(self.robot_id)
        # find closest friend & enemy
        closestFriend = (1000, 1000)
        closestEnemy = (1000, 1000)
        for loc, bot in game.get('robots').items():
            if bot.player_id != self.player_id:
                if rg.wdist(loc, self.location) <= rg.wdist(closestEnemy, self.location):
                    closestEnemy = loc
            else:
                if rg.wdist(loc, self.location) <= rg.wdist(closestFriend, self.location) and self.robot_id != bot.robot_id:
                    closestFriend = loc
        
        for loc, bot in game['robots'].iteritems():
            # if there are enemies around, attack them
            if bot.player_id != self.player_id:
                if rg.dist(loc, self.location) <= 1:
                    return ['attack', loc]
            else:
                # if there are friends around, move to them
                if rg.dist(loc, self.location) > 2:
                    return ['move', rg.toward(self.location, closestFriend)]
                    
        # move towards enemy
        return ['move', rg.toward(self.location, closestEnemy)]
