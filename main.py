from src import controller
import pygame


def main():
    pygame.init()
    team = {"lead": "Michelle Kang", "backend": "Alex Rodriguez", "frontend": "Christopher Micu"}
    print("Software Lead is:", team["lead"])
    print("Backend is:", team["backend"])
    print("Frontend is:", team["frontend"])
    main_window = controller.Controller()
    main_window.mainLoop()

main()


