# Import and initialize the pygame library
import pygame

class Game:
    """
    contains the basic structure to make a game - animation
    """

    def __init__(self, w, h, fps) -> None:
        self.__WIDTH = w
        self.__HEIGHT = h
        self.__fps = fps
        self.running = False
        self.pause = False
        

    def __setup(self):
        """
        initial setup
        """
        # Set up the drawing window
        pygame.init()
        self.running = True
        self.screen = pygame.display.set_mode([self.__WIDTH, self.__HEIGHT])
        self.screen.fill((255, 255, 255))
        self.counter = 0
        


    def main(self):
        """
        run the game
        """
        self.__setup()
        while self.running:
            self.__checkEvents()
            if not self.pause:
                self.__mainLoop()
            self.counter+=1    
        pygame.quit()    
        

    def __mainLoop(self):
        """
        called every frame
        """
        # Fill the background with white
        self.screen.fill((255, 255, 255))
        rect = pygame.draw.circle(self.screen,"Blue",(self.counter, self.counter),100)
        pygame.draw.rect(self.screen,"Red",rect,5)
        # Flip the display
        pygame.display.flip()

    def __checkEvents(self):
        """
        event management
        """
        for event in pygame.event.get():
            # Did the user click the window close button?
            if event.type == pygame.QUIT:
                self.running = False

w = int(input("width: "))
h= int(input("height: "))
fps = int(input("FPS: "))
myGame = Game(w,h,fps)  
myGame.main()
print("Thanks for play.")
print("¡see you soon!")

        


# Done! Time to quit.