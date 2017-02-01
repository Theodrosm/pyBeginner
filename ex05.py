# Exercise 5
## Objective: create a function combine(word1,word2); when run, the function should return a portmanteau of the inputted parameters
def combine(word1,word2):
        return word1[0:4] +word2[4:len(word2)]

print(combine("cryogenics","helicopter"))
