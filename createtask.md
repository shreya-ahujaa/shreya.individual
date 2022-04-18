### Question 3A

**i. Describes the overall purpose of the program**
<br>
For the create task, I chose to make the function MadLibs, which is a automatically generated story based on words that users input into the program. During the class, we had worked on PBL projects, and one of the topics my team and I had worked on for one class was regarding student resources and things that could make students more relaxed during stressful times. This is a fun game that students can use to destress and get their mind off of school and other work for some time, and it fits all of the Collegeboard requirements.

**ii. Describes what functionality of the program is demonstrated in the video**
<br>
In the video, we can see all the parts of the program being executed. First, we see how the code works when the user inputs the different values into each of the sections. The result is the created story. We then see what happens if one of the user input values are empty. The story is cleared/doesnt create, and it prompts the user to input a value for the one they are missing.

**iii. Describes the input and output of the program demonstrated in the video**
<br>
In the video, we will be showing the input and output of the program. The input is where the users can choose different words for the different types that the code prompts them to use. For example, the things, verb, and animal. The output of the program is the sentnece that is created, which uses the words the user had inputted. It puts the words into places of the story, and creates a fun and short passage with the user input.


### Question 3B
**i. The first program code segment must show how data have been stored in the list.** 

<img width="500" alt="image" src="https://user-images.githubusercontent.com/89224064/163756531-702f1e8d-74f4-4d88-9ab5-9bce924889f6.png">

**ii. The second program code segment must show the data in the same list being used, such as creating new data from the existing data or accessing multiple elements in the list, as part of fulfilling the program’s purpose.**

<img width="1142" alt="image" src="https://user-images.githubusercontent.com/89224064/163756698-28e61752-0050-4fee-a74c-6d45e9176d87.png">

**iii. Identifies the name of the list being used in this response**

In this response, there are muliple lists being used to store the user input values. The names of the three lists in this code segment are listThings, listVerb, and listAnimal. 

**iv. Describes what the data contained in the list represent in your program**

The data in our list represents the user input values. After the user inputs the values into the boxes shown in the video, the values are turned into variables, and then are stored in a list. The purpose of the list is to combine the different word types into one list, allowing the code to be more organized and efficient.

**v. Explains how the selected list manages complexity in your program code by explaining why your program code could not be written, or how it would be written differently, if you did not use the list**

In this example of the lists, it manages the complexity in our program by organizing the user input values of one type of word (example: things, verb) into the same data structure, that being a list. It helps keep the code more organized and efficient. If we did not have the list, then when creating the story, we would have to write out each object. With the lists, we are able to compile the different word types into one, and then call that list into the story. it is much less coding than if we had to write out each variable, and creates more efficiency and organization. 

### Question 3C

**i. The first program code segment must be a student-developed
procedure that:
□ Defines the procedure’s name and return type (if necessary)
□ Contains and uses one or more parameters that have an effect
on the functionality of the procedure
□ Implements an algorithm that includes sequencing, selection,
and iteration**

<img width="300" alt="image" src="https://user-images.githubusercontent.com/89224064/163757665-f1ed5080-44f2-4b56-9c6f-a6ede26ad22f.png">

**ii. The second program code segment must show where your student-developed procedure is being called in your program.**

<img width="578" alt="image" src="https://user-images.githubusercontent.com/89224064/163757746-70ffb96d-e4f6-4bcc-8530-8fe449985b8a.png">

**iii. Describes in general what the identified procedure does and how it contributes to the overall functionality of the program**

This procedure checks the user input values for errors, such as them not filling out one of the requirements needed to build the story. It checks each of the values which are stored in the variables, and then prompts the user to input a value for the one(s) they are missing. This contributes to the overall functionality of the program, as it checks for errors and lets the user know where they are missing values so they know where they must input the values to allow the story to be created. 

**iv. Explains in detailed steps how the algorithm implemented in the identified procedure works. Your explanation must be detailed enough for someone else to recreate it.**

The procedure works by reading the user input values after storing them into variables. The code checks each value, and if one of the boxes is blank, the the error becomes true. The result is a boolean value, either true or false, for wether the error is true or false. If the error is true, then the story is not generated, but if it error is false, the story is built and created with the user input values in the places where they should be, determined by another function in the code.

### Question 3D
**i. Describes two calls to the procedure identified in written response: Each call must pass a different argument(s) that causes a
different segment of code in the algorithm to execute.**
