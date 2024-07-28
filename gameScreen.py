# SCREEN CLASS FOR WINDOW HAVING THE FUNCTION OF UPDATING THE ONE SCREEN TO ANOTHER SCREEN

import pygame as py

from pygame import *

from screen import Screen

class GameScreen(Screen):
 
    # INITIALIZATION OF WINDOW HAVING TITLE,
    # WIDTH, HEIGHT AND COLOUR
    # HERE (0,0,255) IS A COLOUR CODE
    def __init__(self, title, width=440, height=445, fill=(0, 0, 255)):
      super().__init__(title, width=440, height=445, fill=(0, 0, 255))

 
  
    def screenUpdate(self):

      super()
         
      k = key.get_pressed()
      if k[K_RETURN]:
        super().endCurrentScreen()
        super().changeCurrentState(0)
        print("ENTER PRESS")


    def screenDisplay(self):
       
      fonte = font.SysFont('comicsansms', 36)
      text = fonte.render('GAME SCREEN', True, (0, 255, 0), (0, 5, 255))
      self.screen.blit(text, (20, 20))
    
       