from random import randint
import numpy as np
import matplotlib.pyplot as plt

# Define a set of endpoints
endPoints = np.array([[0, 0], [1, 0], [.5, 1]])

# Give a starting position
startPos = np.array([.5, .5])

# How much in the directon the point will move each round
scale = 0.5

# Number of repetitions
n = 1000

def plotNextPos(scale, currentPos, endPoints):
    # randomize a number to choose a direction
    choice = randint(0, len(endPoints)-1)

    # check which of the endpoints the number corresponds to
    chosenEndPoint = endPoints[choice]

    # find the nudge that the point will move
    # which is scale times the distance between
    # the selected endpoint and the currentpos
    nudge = scale * (chosenEndPoint - currentPos)

    # find the new position by adding the nudge
    x, y = currentPos + nudge

    # plot the new position as a scatter
    plt.scatter(x, y, s=35, c="#b56e6f")

    # return the new position
    return np.array([x, y])

plt.style.use("ggplot")

# Remove the ticks
labels = ['', '', '', '']
labelPlace = [-0.1, 0.3, .7, 1.1]
plt.xticks(labelPlace, labels)
plt.yticks(labelPlace, labels)
plt.xlim([-0.1, 1.1])
plt.ylim([-0.1, 1.1])
plt.title("n = {}".format(n))

for x in range(n):
    startPos = plotNextPos(scale, startPos, endPoints)

for point in endPoints:
    plt.scatter(point[0], point[1], s=75, c="#6eb5b4")

plt.show()
