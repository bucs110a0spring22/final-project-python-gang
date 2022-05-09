:warning: Everything between << >> needs to be replaced (remove << >> after replacing)
# CS110 Project Proposal
# Random Outfit Generator 
## CS 110 Final Project
### 2022
### Ever been indecisive and didn't know what outfit you wanted to wear for the day? This is the perfect project for you then. You import your clothing and then you can either randomize the speific clothing on whatever part of your body you desire of if you realy don't know what you want to wear you can randomize everything. 

<< [repl](#) >>

## Presentation Slides
https://docs.google.com/presentation/d/1IqmnRE14ZFnZqptrWbfXia5kWDbTcCo0-SPAfcaYtyM/edit?usp=sharing
## Demonstration 
https://drive.google.com/file/d/17UhvMrJRBB8KA7nALUvyGRwyL8AbATtP/view?usp=sharing

### Team: Python Gang
#### Team Members
Michelle Kang- Software Lead
Christopher Micu- Front End Specialist
Alexander Rodriguez- Back End Specialist

***

## Project Description *(Software Lead)*

For our final project, we created a random outfit generator using 3 different clothing pieces. We wanted to help those who have a hard time deciding what to wear for the day. Our program has a variety of shirts, pants, and shoes randomly generated and layed out for the user to get inspiration for their own outfits. Simply click run to get your first outfit, and if you do not like the first one try running the program again until you find the outift you like.

***    

## User Interface Design *(Front End Specialist)*
Start Menu:
![IMG_3290](IMG_3290.JPG)
Game Screen:
![IMG_3293](IMG_3294.jpg)
Game Over:
![IMG_3294](IMG_3295.jpg)
* << A wireframe or drawing of the user interface concept along with a short description of the interface. You should have one for each screen in your program. >>
    * For example, if your program has a start screen, game screen, and game over screen, you should include a wireframe / screenshot / drawing of each one and a short description of the components
* << You should also have a screenshot of each screen for your final GUI >>

***        

## Program Design *(Backend Specialist)*


* Non-Standard libraries
  * pygame
  * sys
    * << You should have a list of any additional libraries or modules used (pygame, request) beyond non-standard python. >>
    * For each additional module you should include
        * url for the module documentation
        * a short description of the module
* Class Interface Design
    * << A simple drawing that shows the class relationships in your code (see below for an example). >>
    * ![IMG_3296](IMG_3296.jpg)
        * ![class diagram](assets/class_diagram.jpg)
    * This does not need to be overly detailed, but should show how your code fits into the Model/View/Controller paradigm.
* Classes
    * << You should have a list of each of your classes with a description. >>

## Project Structure *(Software Lead)*

The Project is broken down into the following file structure:

* main.py
* src
    * <all of your python files should go here>
* assets
    * <all of your media, i.e. images, font files, etc, should go here)
    * Pants, Shirts, Shoes
* etc
    * <This is a catch all folder for things that are not part of your project, but you want to keep with your project. Your demo video should go here.>

***

## Tasks and Responsibilities *(Software Lead)*

As a team, we were able to brainstorm a project idea that we all liked and assigned responsbilities that we agreed were fair to all of us. We got started by finding external clothing, backgrounds, and code information so that Alex could implent as he was coding. After Alex is researching and implementing his code, Michelle and Chris were able to check over the code to see if it is dry and make sure everything in the proposal is completed. We all gathered to check over the replit for any errors or imcompletion before it is submitted. 

### Software Lead - Michelle

Michelle is the Software Lead in our team and is responsible for taking all the code from the Front End Specialist and Back End Specialist and bringing it all together into this repl. She also made sure the slides and presentation follow the rubric. Made sure the entire team worked in unison and along with Chris, made sure the entire code ran smoothly and the project is ready to submit.

### Front End Specialist - Christopher Micu

Christopher is the Front End Specialist in our team and is also responsible for coding, as well as completing most of the presentation and script. He will be coding the background hand in hand with Alex. Conducted significant research by finding different pieces of clothing required for our program, as well as the background. He made sure they were all of similar sizes with transparent background.

### Back End Specialist - Alex

Alexander is the Backend Specialist in our team. He is responsible for the writting the main driver code and conducted research in order to do so. He also worked on coding most of the components such as the background and the change of clothes as inputted by the user. He is also aided by the Chris with finding references for the main code.

## Testing *(Software Lead)*

In our testing strategy, we planned to run the random feature one by one as we implemented each of the 3 clothing classes. Although it is not a class, the background was the very first function we implemented along with the desired screen size. After we were able to run the background and screen sucessfully we moved on. The shirt class was the first coded and ran multiple times by each of us to check for errors. We did this for each class before moving onto the next. 

## ATP

| Step          | Procedure     | Expected Results | Actual Results |
|-----------|:-------------:| :-----------------| -------------- |
|  1  | Click on run to begin | The GUI window opens and generates a random set of clothes|
|  2  | Click on background  | The entire outfit changes to another random set of clothes |                 |
|  3  | Click on the body  | Once again another random outfit would be generated. The chances of any piece of clothing being the same as the first two are very low. |                 |
|  4  | Click on the logo in the top left  | Another random outfit will be generated different from the first three |               |
|  5  | Click on stop code  | Code terminates properly |                 |

