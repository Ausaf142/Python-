class Remote:
    pass

class Player:
    def moverRight(self):
        pass
    def moverLeft(self):
        pass
    def moverTop(self):
        pass

remote1=Remote()
player1=Player() 
if(remote1.isLeftPressed()):
    player1.moverLeft()
    
