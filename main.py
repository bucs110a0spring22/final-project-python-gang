from src import controller
import pygame


def main():
    pygame.init()
    main_window = controller.Controller()
    main_window.mainLoop()

main()


    #Create an instance on your controller object
    #Call your mainloop
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
#if __name__ == '__main__':
    #main()

