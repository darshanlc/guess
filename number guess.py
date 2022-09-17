"""
problem statement:

guess the secret number
limit the number of guess to 5 or any other number
if limit exceeds print game over
print number of guesses remaining

"""


def game_over():
    if i == 0:
        print("game over!!!")
        quit()


n = 56
i = 10
while 1:

    print("enter your guess")
    g = int(input())
    if g == n:
        print("yeah!!! you guess the correct number💕")
        print("you guess the number correctly while you left with another", abs(1-i), "chances")
        if i-1 > 5:
            print("you do not take so much chances to guess the number🤑")
        else:
            print("you take more than half of the chances to guess the number😒")
        break
    if g <= n:
        print("your guess is lower than secret number")
        i -= 1
        print("your remaining guess is", i)
        game_over()
        continue
    if g >= n:
        print("your guess is greater")
        i -= 1
        print("your remaining guess is", i)
        game_over()
        continue
