import os
def reset_text(function):
    print("ERROR : Invalid input")
    continue_txt_input = input("PRESS ENTER TO CONTINUE\n:")
    os.system("clear")
    return function()

