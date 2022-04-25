{% include navigation.html %}

# Create Task

### Question 3A

**i. Describes the overall purpose of the program**
<br>
For the create task, I chose to make a program that would allow the user to find different statistics regarding the recent test scores of an AP Computer Science Principles Class. Based on what the user chooses, the program can give the user the maximum score, the minimum score, the average of the scores, and the letter grade assigned to each student based on their score. The purpose of the program is to easily analyze the data in the list of students and allows the user to find each of the different statistics regarding the students in the Computer Science class. 

**ii. Describes what functionality of the program is demonstrated in the video**
<br>

**iii. Describes the input and output of the program demonstrated in the video**
<br>
In the video, we will be showing the input and output of the program. In the code, there is a menu, where the user can input their choice for which type of statistic they would want from the class data. The user is able to choose between finding the minimum, the maximum, The output is the corresponding outcome for the choice they made in the menu. For example, if they choose the number 1, they will recieve the minimum of the class data, and if they choose number 4, then they will recieve the list of the names, scores, and the letter grade that corresponds with the score.


### Question 3B
**i. The first program code segment must show how data have been stored in the list.** 

<img width="272" alt="image" src="https://user-images.githubusercontent.com/89224064/165024769-03de261c-e170-469e-bc75-48af9d895dda.png">

**ii. The second program code segment must show the data in the same list being used, such as creating new data from the existing data or accessing multiple elements in the list, as part of fulfilling the program’s purpose.**
<br>

    # Procedure to calculate the stats of the class scores
def calculate_stats(option):
    # The option is the user's choice for the type of stat they want to see for the class
    # 1: Minimum, 2: Maximum, 3: Average
    # Algorithm to calculate the minimum score
    if option == 1:
        min = 100      # Initialize 'min' to maximum possible value --> 100
        for student in student_record:  # Iterate over all of student_record and find minimum
            if student[1] < min:
                min = student[1]
        print(border)
        print("Minimum Score in Class:", min)

    # Algorithm to calculate the maximum score
    elif option == 2:
        max = 0     # Initialize 'max' to minimum possible value --> 0
        for student in student_record:  # Iterate over all of student_record and find maximum
            if student[1] > max:
                max = student[1]
        print(border)
        print("Maximum Score in Class:", max)

    # Algorithm to calculate the average score of the class
    elif option == 3:
        sum = 0     # Initialize 'sum' of scores to 0
        for student in student_record:  # Iterate over all of student_record to find sum of all scores
            sum += student[1]
        average = sum/len(student_record)   # Find average by dividing 'sum' by number of students in student_records
        print(border)
        print("Average Score of Class:", average)
    return


**iii. Identifies the name of the list being used in this response**

In this response, the name of the list being used is called student_record. In this list, it has the student name, along with their score they recieved on the last test. This information is used throughout the procedure to find the different stats of the class.

**iv. Describes what the data contained in the list represent in your program**

The data in our list represents the student name and their score on the last test they had taken. This is a static list and does not change, and involves 10 different students and their scores. These values in the list are then used to find the stats of the class (minimum, maximum, average, and letter grade).

**v. Explains how the selected list manages complexity in your program code by explaining why your program code could not be written, or how it would be written differently, if you did not use the list**

In my program, the list is very important and it would be hard for the code to run without it. The purpose of the program is to find the statistics of the class based on the raw data. This raw data comes from the list, where we can store the students name and their score. The use of lists allows the rpgram to be scalable to any number of students in a class and requires no change to the algorithm and procedure itself. It would be very hard to write the program wihtou a list or similar data structure, as it would require you to change the alogirthm for each change, rather than just changing the list.

### Question 3C

**i. The first program code segment must be a student-developed
procedure that:
□ Defines the procedure’s name and return type (if necessary)
□ Contains and uses one or more parameters that have an effect
on the functionality of the procedure
□ Implements an algorithm that includes sequencing, selection,
and iteration**
<img width="839" alt="image" src="https://user-images.githubusercontent.com/89224064/165153420-ca511155-c313-4a77-ba61-067c130a7440.png">
        
        
**ii. The second program code segment must show where your student-developed procedure is being called in your program.**

<img width="406" alt="image" src="https://user-images.githubusercontent.com/89224064/165153506-8761aa40-ac53-4b9b-8896-bdbdc8775bf9.png">

<br>

**iii. Describes in general what the identified procedure does and how it contributes to the overall functionality of the program**

This procedure checks calculates the different statistics for the AP Computer Science class based on the user input. The user can choose the option they want for which stastic they would want for the class, and the procedure involves the different options. Depending on which option the user will choose, the program will run that specific code. For example, if they choose the number one, the minimum, or the lowest score of the class will be shown. 

**iv. Explains in detailed steps how the algorithm implemented in the identified procedure works. Your explanation must be detailed enough for someone else to recreate it.**

In the program and procedure, there are three different algorithms that each have a different function. To find the average of the class, the algorithm iterates through the list and adds the scores of each student. It then takes the sum and divides it by the length of the lists, which is the number of students. This results in the average score, which is represented on the console. To find the minimum score, the program initlializes the minimum score to the maximum possible score, which is 100. The code then iterates through all the students in student_record, and if the score of an individual is lower than the minimum, then it replaces the minimum and moves to the next. The result is the lowest score in the class. To find the maximum score, the program initlializes the max to the minimum possible score, which is 0. The code then iterates through all the students in student_record, and if the score of an individual is higher than the max stored in the variable, then it replaces the maximum value and moves to the next in the student_record until it iterates through all. The result is the highest score in the class, represnted in the console. 

### Question 3D
**i. Describes two calls to the procedure identified in written response: Each call must pass a different argument(s) that causes a
different segment of code in the algorithm to execute.**
