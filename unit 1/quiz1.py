# Create a new document called quiz1.py copy/ paste the following questions
# on your document and answer the following questions.

# quiz rules:
# - There is no talking during the quiz
# - You may only use your classnotes and w3schools.com for reference
# - If you have a question about a quiz question, please raise your hand
# - Once finished, submit your code to your repository using the source control 
# button. Your commit should be "completed quiz 1."

'note: all written responses should be written/ formatted as strings.'

# 1. In your own words, describe the differences between a linear search and a 
# binary search. Please write your response using complete sentences.

# Linear and binary search are both algorithms used to find a target element within a collection of data, but they differ significantly in their approach and efficiency.

# 2. How many steps would it take to get to the desired number of 98 using linear search?
# Please write your response using complete sentences.
 4 steps

listA = [10,24,34,35,67,98,101]

# 3. How many steps would it take to get to the desired number of 150 using a binary search?
# Please write your response using complete sentences.
listB = [1,40, 44, 55, 70, 93, 99, 134, 145, 150, 200, 244] 

3 Steps The search begins with the entire list: [1, 40, 44, 55, 70, 93, 99, 134, 145, 150, 200, 244]. The middle element is 99. Since 150 is greater than 99, the algorithm eliminates the left half of the list.

# 4. In your own words describe what an algorithm is. 
# Please write your response using complete sentences.

An algorithm is a well-defined, step-by-step procedure or set of instructions designed to solve a specific problem or accomplish a particular task.
It provides a precise sequence of operations that, when executed, will consistently produce the desired output from a given input.
Algorithms are the fundamental building blocks of computer programs, guiding the computer on exactly how to process information and achieve a goal.


# 5. A person and their family is visiting a medical building. the medical building has
# 10 floors. The patient that the person and their family is visiting is on the 7th floor 
# of the building. The family also knows what room they need to go to to visit the
# patient on the 7th floor. which big-O time complexity would best describe the steps it
# would for them to get to the desired room and why? 
# Please write your response using complete sentences.

The Big-O time complexity that best describes the steps for the family to get to the desired room is O(1) (constant time) because the number of floors they must travel and the steps involved are fixed and do not grow with the size of the building. 
Even though the building has 10 floors and they are going to the 7th, the path is predetermined, requiring a fixed number of actions like finding an elevator, 
traveling to the 7th floor, and then finding the specific room. 

# 6. You and your friends are headed out to a party, as you're preparing to walk out the door to meet with
# your pals, your realize you forgot your phone. you you can't remember exactly where you misplaced it 
# but you know it is in one of your pairs of pants. You have 10 pairs of paints. which big-O time complexity
# would best describe the steps it would take to find your phone?
# Please write your response using complete sentences.

The big-O time complexity that best describes the steps to find your phone is O(n), which represents linear time.
This is because you must check each of the n pairs of pants one by one until you find your phone, a process known as a linear search. 

# 7. Create a class that will represent and create game console objects. 
# Your class should have 4 attributes and 3 methods. 
# Once you've created your class, create 2 unique video game consoles.
 
 Class:50,60,70,88,90,100

# 8. Create a class that will represent a video game for your console.
# Your class should have 4 attributes and 3 methods objects.
# ONCE You've created your class, create 2 unique video games objects.. 

print("Hello, World)"

