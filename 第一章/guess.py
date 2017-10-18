import random
secret =  random.randint(1,99)
guess = 0
tries = 0
print "guess number"
while  guess != secret and tries  < 6: 
    guess = input("what's you guess")
    if guess < secret:
        print "too small,"
    elif guess >secret: 
        print "too big"
    tries += 1
if guess == secret :
    print "good"
else:
    print "game is over"