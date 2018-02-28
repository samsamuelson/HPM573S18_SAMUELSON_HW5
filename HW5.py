import random
import matplotlib.pyplot as plt



#1 - represents Heads
#2 - represents Tails
class Game:

    def Simulate(self):

        reward = -250
        twoBack = 0
        oneBack = 0
        for i in range(1,21):

            outcome = random.randint(1,2)

            if twoBack == 2 and oneBack == 2 and outcome == 1:
                reward = reward + 100

            twoBack = oneBack
            oneBack = outcome

        return reward

g = Game()

sumOfRewards = 0
results = []
numberOfLosses = 0
for i in range(0, 1000):
    rew = g.Simulate()
    results.append(rew)

    if rew < 0:
        numberOfLosses = numberOfLosses + 1

    sumOfRewards = sumOfRewards + rew

print("Average of 1000 realizations is {}".format( sumOfRewards/1000))
print("Probability of loss is {}".format( numberOfLosses/1000))


bin_edges = [-250, -150, -50, 50, 150, 250, 350]
plt.hist(results, bins=bin_edges, edgecolor='b')
plt.xlabel("Game Outcome")
plt.ylabel("Frequency")
plt.title("Fair Coin Game Outcome Histogram")
plt.show()
