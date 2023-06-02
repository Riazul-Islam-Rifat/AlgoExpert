def minRewards(scores):
    # List where number of rewards will be stored
    rewards = [1]*len(scores)

    # The following for loop works for 1,3,6,8 .. [Local min to right]
    for i in range(1,len(scores)):
        if scores[i]>scores[i-1]:
            rewards[i] = rewards[i-1]+1

    # The next for loop works for 8,4,3,2,....9,5 [Local min to left]
    for i in reversed(range(len(scores)-1)):
        if scores[i]>scores[i+1]:
            rewards[i] = max(rewards[i],rewards[i+1]+1)
    return sum(rewards)