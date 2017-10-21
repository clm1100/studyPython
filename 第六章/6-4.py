import easygui ,random
secret = random.randint(1,99);
guess = 0
tries = 0
easygui.msgbox('shu ru shu zi')
while guess != secret and tries < 6:
    guess = easygui.integerbox('shu ru')
    if not guess: break
    if guess <secret:
        easygui.msgbox(str(guess)+"is xiao")
    elif guess>secret:
        easygui.msgbox(str(guess)+'is da')
    tries+=1
if guess==secret:
    easygui.msgbox("success")
else:
    easygui.msgbox('faile')