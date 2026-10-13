# 1.

# sentence = "python is easy and python is powerfull"
# words = sentence.split()
# freq = {}

# for word in words:
#     if word in freq:
#         freq[word] += 1
#     else:
#         freq[word] = 1

# print(freq)        
# 
# 
# 
# 
# 
# 2


# d = {"a": 1,"b" : 2,"c" : 3}

# reverse_d = {}
# for key,value in d.items():
#     reverse_d[value] = key
# print(reverse_d)    







# 3


# import random

# player = 0
# computer = 0
# boosts_left = 3
# round_no = 1

# while player < 50 and computer < 50:
#     print(f"\n--- Round {round_no} ---")
#     choice = input("1) Normal  2) Speed  3) Boost (" + str(boosts_left) + " left): ")

#     if choice == "2":
#         move = random.randint(3, 8)      # faster, small range
#     elif choice == "3" and boosts_left > 0:
#         move = random.randint(8, 15)     # big jump
#         boosts_left -= 1
#     else:
#         move = random.randint(1, 6)      # normal

#     comp_move = random.randint(1, 8)
#     if random.random() < 0.2:            # computer sometimes boosts
#         comp_move += 5

#     player += move
#     computer += comp_move

#     print("You moved", move, "-> total", player)
#     print("Computer moved", comp_move, "-> total", computer)
#     round_no += 1

# print("\n=== RESULT ===")
# if player >= 50 and computer >= 50:
#     print("Tie!" if player == computer else ("You win!" if player > computer else "Computer wins!"))
# elif player >= 50:
#     print("You win!")
# else:
#     print("Computer wins!")





# gample game 





# import random

# points = 100

# while points > 0:
#     print("Points:", points)
#     guess = input("Heads or tails (h/t): ")
#     bet = int(input("Bet: "))

#     coin = random.choice(["h", "t"])
#     print("Coin:", coin)

#     if guess == coin:
#         points = points + bet
#         print("You win!")
#     else:
#         points = points - bet
#         print("You lose!")

# print("Game over")




# racing game 




import random

player = 0
computer = 0
boosts = 3

while player < 50 and computer < 50:
    print("Player:", player, "Computer:", computer, "Boosts left:", boosts)
    choice = input("Press Enter for normal, or type b to boost: ")

    if choice == "b" and boosts > 0:
        player = player + 10
        boosts = boosts - 1
        print("Boost used!")
    else:
        player = player + random.randint(1, 6)

    computer = computer + random.randint(1, 6)

if player >= 50:
    print("You win!")
else:
    print("Computer wins!")



