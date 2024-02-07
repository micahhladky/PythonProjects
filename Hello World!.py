import random
import string

msg = ''
goal_phrase = 'Hello, World!'
all_letters = string.ascii_letters + string.whitespace + string.punctuation
print("Options include: ", all_letters)

#while msg != goalphrase:
for goal_phrase_letter in goal_phrase:
    Random_Letter = random.choice(all_letters)
    while goal_phrase_letter != Random_Letter:
        Random_Letter = random.choice(all_letters)
    msg += Random_Letter
    print("msg = ", msg)

print(msg)

