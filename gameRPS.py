import random

print("1.Rock 2.Paper 3.Scissors. Enter a number:")
choicePlayer = input(int())
choiceCPU = random.randint(1, 3)
if choicePlayer == choiceCPU:
    print("Draw")
elif choicePlayer == 1 and choiceCPU == 2:
    print("CPU wins")
elif choicePlayer == 2 and choiceCPU == 3:
    print("CPU wins")
elif choicePlayer == 3 and choiceCPU == 1:
    print("CPU wins")
elif choicePlayer < 1 or choicePlayer > 3:
    print("Play the game stupid")
else:
    print("You won")
