# CSE-105-Project

# Hamza Dehaini - A17612477

## Task 1
1. The application that I chose is to make a UCSD PID. I chose this because I am familiar with PIDs, like any other UCSD student. They are also quite distinct in their form compared to the other binary strings that we had to deal with. On top of that, finding out whether a given string is a valid PID or not is immensely important and used, or should be used, on any website that asks for a PID, so that a student won’t have to deal with the consequences of not getting something they are expecting since they mistyped their PID. An example of this is maybe a student is trying to sign up for classes, yet they mistype their PID. If WebReg doesn’t have a system of identifying whether a PID is valid or not, then the student may not get into the classes they want to since WebReg couldn’t register the incorrect PID to that class, delaying graduation and costing thousands of dollars.
2. The alphabet for a PID is =A, 0,1,2,3,4,5,6,7,8,9
3. The set of UCSD PID strings is:
    - A string for a PID starts with an ‘A’ followed by 8 characters from digits 0-9.
    - As explained above, this set is important since a PID is a Personal Identification Number for every student. If a student needs to do something that is required specifically for them, for example registering for classes, it is necessary to see that the PID is imputed correctly so that the student can register for their class.
4. String Examples:
    - An example of a string in this set is A17612477. I chose this example since that is my PID, which guarantees that string is a valid PID.
    - An example of a string not in this set is A12213A55654A. I chose this example because it has multiple ‘A’s and more than 9 characters in total, guaranteeing that this string is not a valid PID.
5. This language is a regular language. I can prove this by making an NFA for the language:
This NFA basically makes sure the string starts with an A and then only goes to the next state if the next character is a digit from 0-9. It does this eight times and accepts the eighth time. If the string is longer than nine characters, it goes to a dead-end state that doesn’t accept the string.
![NFA for PID](screenshots\nfa.PNG)

---

## Task 2

1. The Turing Machine that I will talk about is a function where the input domain has a range of {ab}* and the output codomain has a range of {ab}*.
    - If the first and last characters of the string aren’t the same, the function will delete the last element of the string, making it have a shorter codomain.
    - If the first and last characters of the string are the same, the function will add an ‘a’ and a ‘b’ at the end of the string, making it have a longer codomain.
    - If the input string is of length 0, the function will add an ‘a’ to the string, making it have a longer codomain.
2. ![Turing Machine Diagram](screenshots\turing-machine.PNG)
3. Code: [Program](turing-machine.py)