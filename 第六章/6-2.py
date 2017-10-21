import easygui
flavor = easygui.choicebox("what is your name",choices=("Button[1]", "Button[2]", "Button[3]"))
easygui.msgbox('your picked'+flavor)

