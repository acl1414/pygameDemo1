# SCREEN CLASS FOR WINDOW HAVING THE FUNCTION OF UPDATING THE ONE SCREEN TO ANOTHER SCREEN

import pygame as py

from pygame import *

from screen import Screen
from vaisseau import Vaisseau

class GameScreen(Screen):
 
    # INITIALIZATION OF WINDOW HAVING TITLE,
    # WIDTH, HEIGHT AND COLOUR
    # HERE (0,0,255) IS A COLOUR CODE
    def __init__(self, title, width, height, fill=(0, 0, 255)):
      super().__init__(title, width, height, fill=(0, 0, 255))
      
      self.width= width
      self.height=height
      self.fond = image.load('assets/background.png')
      self.vaisseau = Vaisseau(0,self.height*7/8)
      #self.fond = self.fond.convert()
      self.list_missile = []
 

 
  #
  # UPDATE DES OBJETS
  #
    def screenUpdate(self):

      super()
         

      # Gestion claver   
      k = key.get_pressed()

      if k[K_ESCAPE]:   # ESC ==> sortir de l'écran
        super().endCurrentScreen()
        super().changeCurrentState(0)
      elif k[K_LEFT]:
        self.vaisseau.move_left()
      elif k[K_RIGHT]:
        self.vaisseau.move_right()
      elif k[K_SPACE]:
        self.vaisseau.tir( self.list_missile)
       

      # Update des missiles
      for m in self.list_missile:
        m.update()

          
      # Delete missile hors zone
      for i in self.list_missile:
       
        if i.is_to_deleted() :
          self.list_missile.remove(i)






  #
  # AFFICHAGE DES OBJETS
  #
    def screenDisplay(self):

      self.screen.blit(self.fond, (0,0))
      self.vaisseau.display(self.screen)

      # Affichage des missiles
      for index in range(len(self.list_missile)):
        m = self.list_missile[index]
        m.display(self.screen)
       
       