import numpy as np

def runChop(score, action, displ = 0):
    """
    Takes Current Score and action and returns resulting Score
    in:
        score: Array of 4 numbers [p1 left, p1 right, p2 left, p2 right]
        action: options 1 thru 4 (LL, LR, RL, RR)
    out:
        score: array size 4
    """
    fingers = 5

    if action == 1:
        score[2] = (score[2] + score[0]) % fingers
    elif action == 2:
        score[3] = (score[3] + score[0]) % fingers
    elif action == 3:
        score[2] = (score[2] + score[1]) % fingers
    elif action == 4:
        score[3] = (score[3] + score[1]) % fingers
    if displ:
        print("final score", score)
    if(sum(score[0:2]) == 0 or sum(score[2:4]) == 0):
        score[0] = -1
    return score

initScore = np.ones(4)
myScore = initScore.copy()
while(myScore[0] != -1):
    temp = myScore[0:2].copy()
    myScore[0:2] = myScore[2:4]
    myScore[2:4] = temp

    print(myScore)
    myaction = int(input("enter action 1-4 (LL, LR, RL, RR)"))

    runChop(myScore, myaction, 1)



print(myScore, initScore)
