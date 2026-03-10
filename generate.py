import random

cards = ['2 of Hearts', '3 of Diamonds', '4 of Clubs', '5 of Spades']
print(random.choice(['heads', 'tails']))
print(random.randint(1, 10))
random.shuffle(cards)
for card in cards:
    print(card)