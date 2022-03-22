import pygame
#import your controller

mylist = []

for a in range(1,5):
  number = int(input("Please enter a number: "))
  mylist.append(number)

print(*mylist, sep = "\n")

def newlist(mylist):
  number = len(newlist)
  temp=newlist[0]
  newlist[0]=newlist[number - 1]
  newlist[number-1]= temp
print(newlist)




def main():
    pygame.init()
    #Create an instance on your controller object
    #Call your mainloop
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()

