import random
class Agent:
    def chooseAction(self, observations, possibleActions):
        lidar = observations['lidar']  
        velocity = observations['velocity']
        l10 = lidar[1]
        center = lidar[2]
        r10 = lidar[3]
        avg=(l10+r10)/2

        if r10 < avg:
            direction = 'left'
        elif l10 < avg:  
            direction = 'right'
        else:
            direction = 'straight'
    
        if velocity==0:
            speed= 'accelerate'
        elif velocity < 0.3 and center >1:
            speed = 'accelerate'
        elif (lidar[0]<1 or lidar[4]<1) or velocity>0.6:
            speed = 'brake'
        else:
            speed = 'coast'

        action = (direction, speed)
        return action



