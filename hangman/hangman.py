import random
data = [{"Imagine Dragons": "Alternative", "Maroon 5": "Lost Star", "Taylor Swift": "Single in a year", "Coldplay": "Feeling Healed", "OMAM": "Lionheart"},
        {"Iron Man": "Downey", "Transfromers": "Car", "Spiderman": "8 legs", "Wreck-It Ralph 2": "Network", "Toy Story": "Potato"},
        ]
used = []

def letsguess(word):
    display = ' '.join(alp if not alp.isalpha() else '_' for alp in word )
    count = 15
    score = 0
    print(display, "\tscore %d, remaining wrong guess %d" % (score, count))
    while count>0:
        char = input()
        count-=1
        if char in word.lower() and char.isalpha():
            if (char not in used):
                score+=15
            display = findIndex(word, display, char)
            used.append(char)
            print(display, "\tscore %d, remaining wrong guess %d" % (score, count))
        else:
            score-=5
            print(display, "\tscore %d, remaining wrong guess %d, wrong guessed: %s" % (score, count, char))
        if ('_' not in display):
            print("\nyou win!")
            return
    print("\nloser")
    return 

def findIndex(word, display, char):
    while 1:
        i = word.lower().find(char)
        if i == -1:
            break
        display = display[:2*i] + word[i] + display[2*i+1:]
        word = word[:i] + '.' + word[i+1:]
    return display

print("\nSelect Category:")
print("1: Artists")
print("2: Movies")
cat = int(input("\nChoose: ")) -1
word = random.choice(list(data[cat].keys()))
print("\nHint: %s\n" % (data[cat][word]))
letsguess(word)