# SCREEN CLASS FOR WINDOW HAVING THE FUNCTION OF UPDATING THE ONE SCREEN TO ANOTHER SCREEN

import pygame as py

from pygame import *

from screen import Screen
from button import Button 

class MenuScreen(Screen):
 
    # INITIALIZATION OF WINDOW HAVING TITLE,
    # WIDTH, HEIGHT AND COLOUR
    # HERE (0,0,255) IS A COLOUR CODE
    def __init__(self, title, width=440, height=445, fill=(0, 0, 255)):
      super().__init__(title, width=440, height=445, fill=(0, 0, 255))

      # MENU BUTTON
      self.MENU_BUTTON2 = Button(150, 150, 150, 50, (255, 250, 250), (255, 0, 0), "TimesNewRoman", (255, 255, 255), "Main Menu")
      
      self.changeS = False



    def screenUpdate(self):

      super()
      print("Menu SCreen Update")
      fonte = font.SysFont('comicsansms', 36)
      text = fonte.render('Appuyer sur ENTER', True, (0, 255, 0), (0, 5, 255))
      self.screen.blit(text, (20, 20))
 
      mouse_pos = py.mouse.get_pos()          # STORING THE MOUSE EVENT TO CHECK THE POSITION OF THE MOUSE
      mouse_click = py.mouse.get_pressed()    # CHECKING THE MOUSE CLICK EVENT
      keys = py.key.get_pressed()             # KEY PRESSED OR NOT

      self.MENU_BUTTON2.showButton(self.returnTitle())
      buttonPressed = self.MENU_BUTTON2.focusCheck(mouse_pos, mouse_click)
  
      
      if (buttonPressed) :
          super().endCurrentScreen()
          super().changeCurrentState(1)







  
