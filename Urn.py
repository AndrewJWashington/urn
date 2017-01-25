# From Question 20 on pg. 55 of Sheldon Ross  - A First Course in Probability 9e
# Let an urn be filled w/ 30 objects, 20 of which are red, the other 10 are blue.
# Objects are taken out randomly
# Find P(All red objects are gone before all blue objects are)
import random

NUM_RUNS = 100000

class Ball(object):
    def __init__(self, color):
        self.color = color

def lastBall():
    urn = [Ball("red")]
    for i in range(0, 20):
        urn.append(Ball("red"))
    for i in range(0, 10):
        urn.append(Ball("blue"))
    for i in range(0, len(urn) - 1 ):
        #print(urn[i].color)
        #print("Pick ", i, ": ")
        x = random.randrange(len(urn))
        #print(x)
        #print(urn[x].color)
        urn.pop(x)
    return urn[0].color

red = 0;
blue = 0;

for i in range(1, NUM_RUNS + 1):
    result = lastBall()
    if result == "red":
        red = red + 1;
    if result == "blue":
        blue = blue + 1;

print("Blue: ",blue)
print("Red: ", red)
print("P(red taken first): ", blue / NUM_RUNS)
