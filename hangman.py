import random

words = ['book', 'tree', 'python', 'bag', 'umbrella', 'dog', 'clock', 'engineer', 'toothpaste', 'shirmoz']

# i = random.randint(0, len(words)-1)
# word = words[i]

word = random.choice(words) # clock
joon = 10
tole_kalame= len(word)

while joon > 0:
    print('- ' * tole_kalame) # - - - - -

    user_character = input() # s

    if user_character in word:
        print('yes')
        tole_kalame=tole_kalame-1
        print(user_character)
        if tole_kalame==0:
            print('movafagh shodid, kalame mored nazar:',word)
    else:
        joon = joon - 1
        print('no')
