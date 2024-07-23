from random import choice
dice_array=['⚀','⚁','⚂','⚃','⚄','⚅']
def roll_dice():
    dice=choice(dice_array) 
    return dice
print(roll_dice())