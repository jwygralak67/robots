import rg

class Robot:
    def __init__(self):
        self.age={}
        
    def act(self, game):
        
        myId = self.robot_id
        myAge = 0

        if myId in self.age:
            self.age[myId] += 1
            myAge = self.age[myId]
        else:
            self.age[myId] = 0
       
        # get off the spawn point fast
        if myAge <= 3:
            return ['move', rg.toward(self.location, rg.CENTER_POINT)]
        
        # if there are enemies around, attack them
        for loc, bot in game.robots.iteritems():
            if bot.player_id != self.player_id:
                if rg.dist(loc, self.location) <= 1:
                    return ['attack', loc]

                # if we're in the center, stay put
        if self.location == rg.CENTER_POINT:
            return ['guard']

        # move toward the center slowly
        if game.turn % 2:
            return ['move', rg.toward(self.location, rg.CENTER_POINT)]
        
        return['guard']
