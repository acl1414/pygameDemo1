import pygame as py
 
# SCREEN CLASS FOR WINDOW HAVING THE FUNCTION OF UPDATING THE ONE SCREEN TO ANOTHER SCREEN


from screen import Screen
from menuScreen import MenuScreen
from gameScreen import GameScreen
 
from button import Button 


py.init()       # INITIALIZATION OF THE PYGAME
py.font.init()  # INITIALIZATION OF SYSTEM FONTS
 

menu_screen = MenuScreen("Menu Screen")      # CREATING THE OBJECT OF THE CLASS Screen FOR MENU SCREEN
game_screen = GameScreen("Control Screen")  # CREATING THE OBJECT OF THE CLASS Screen FOR CONTROL SCREEN

 
win = menu_screen.makeCurrentScreen()    # CALLING OF THE FUNCTION TO MAKE THE SCREEN FOR THE WINDOW

print("menu heigt",menu_screen.height)
print("menu screen",menu_screen.screen)

current_screen = menu_screen
state = 0


done = False
toggle = False

 
# MAIN LOOPING
while not done:
    
    current_screen.screenUpdate()     
 
 
    # Check si l'écran doit changer
    changeScreen, newScreen = current_screen.checkState()
    if (changeScreen) :
        pass
    else :
        if (newScreen == 0) :
            win = menu_screen.makeCurrentScreen()   
            current_screen = menu_screen
        else :         
            win = game_screen.makeCurrentScreen()   
            current_screen = game_screen


    # CHECKING IF THE EXIT BUTTON HAS BEEN CLICKED OR NOT
    for event in py.event.get():

        if(event.type == py.QUIT):  # IF CLICKED THEN CLOSE THE WINDOW
            done = True
 

    py.display.update()


    
     
# CLOSE THE PROGRAM
py.quit()
