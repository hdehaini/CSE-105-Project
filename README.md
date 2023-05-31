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

```

import unittest


def print_tape(full_tape, current_index, written_char, current_state, future_state, direction):
    for char in full_tape:
        print(char + ", ", end="")
    print("...")
    print(" " * (current_index * 3) + '\u2191')
    print("Current State: " + current_state)
    print("Current Tape Head to be Read: " + str(full_tape[current_index]))
    print("Current Tape Head to be Written: " + written_char)
    print("Tape Head Transition: " + direction)
    print("Next State: " + future_state)
    print("\n")


def turing_machine(input_string):
    tape = list(input_string + "_" + "_" + "_")
    curr = 0
    write = ""
    state = "q0"
    next_state = ""
    transition = ""

    while state != "q_acc":
        if state == "q0":
            if tape[curr] == "_":
                write = "a"
                next_state = "q_acc"
                transition = "R"
                print_tape(tape, curr, write, state, next_state, transition)
                tape[curr] = write
                curr += 1
                state = "q_acc"

            elif tape[curr] == "a":
                write = "a"
                next_state = "q1"
                transition = "R"
                print_tape(tape, curr, write, state, next_state, transition)
                tape[curr] = write
                curr += 1
                state = "q1"

            elif tape[curr] == "b":
                write = "b"
                next_state = "q5"
                transition = "R"
                print_tape(tape, curr, write, state, next_state, transition)
                tape[curr] = write
                curr += 1
                state = "q5"

        elif state == "q1":
            if tape[curr] == "_":
                write = "_"
                next_state = "q2"
                transition = "L"
                print_tape(tape, curr, write, state, next_state, transition)
                tape[curr] = write
                curr -= 1
                state = "q2"

            elif tape[curr] == "a":
                write = "a"
                next_state = "q1"
                transition = "R"
                print_tape(tape, curr, write, state, next_state, transition)
                tape[curr] = write
                curr += 1
                state = "q1"

            elif tape[curr] == "b":
                write = "b"
                next_state = "q1"
                transition = "R"
                print_tape(tape, curr, write, state, next_state, transition)
                tape[curr] = write
                curr += 1
                state = "q1"

        elif state == "q2":
            if tape[curr] == "a":

                write = "a"
                next_state = "q3"
                transition = "R"
                print_tape(tape, curr, write, state, next_state, transition)
                tape[curr] = write
                curr += 1
                state = "q3"

                write = "a"
                next_state = "q4"
                transition = "R"
                print_tape(tape, curr, write, state, next_state, transition)
                tape[curr] = write
                curr += 1
                state = "q4"

                write = "b"
                next_state = "q_acc"
                transition = "R"
                print_tape(tape, curr, write, state, next_state, transition)
                tape[curr] = write
                curr += 1
                state = "q_acc"

            elif tape[curr] == "b":
                write = "_"
                next_state = "q_acc"
                transition = "R"
                print_tape(tape, curr, write, state, next_state, transition)
                tape[curr] = write
                curr += 1
                state = "q_acc"

        elif state == "q5":
            if tape[curr] == "_":
                write = "_"
                next_state = "q6"
                transition = "L"
                print_tape(tape, curr, write, state, next_state, transition)
                tape[curr] = write
                curr -= 1
                state = "q6"

            elif tape[curr] == "a":
                write = "a"
                next_state = "q5"
                transition = "R"
                print_tape(tape, curr, write, state, next_state, transition)
                tape[curr] = write
                curr += 1
                state = "q5"

            elif tape[curr] == "b":
                write = "b"
                next_state = "q5"
                transition = "R"
                print_tape(tape, curr, write, state, next_state, transition)
                tape[curr] = write
                curr += 1
                state = "q5"

        elif state == "q6":
            if tape[curr] == "b":

                write = "b"
                next_state = "q7"
                transition = "R"
                print_tape(tape, curr, write, state, next_state, transition)
                tape[curr] = write
                curr += 1
                state = "q7"

                write = "a"
                next_state = "q8"
                transition = "R"
                print_tape(tape, curr, write, state, next_state, transition)
                tape[curr] = write
                curr += 1
                state = "q8"

                write = "b"
                next_state = "q_acc"
                transition = "R"
                print_tape(tape, curr, write, state, next_state, transition)
                tape[curr] = write
                curr += 1
                state = "q_acc"

            elif tape[curr] == "a":
                write = "_"
                next_state = "q_acc"
                transition = "R"
                print_tape(tape, curr, write, state, next_state, transition)
                tape[curr] = write
                curr += 1
                state = "q_acc"
    for char in tape:
        print(char + ", ", end="")
    print("...")
    print(" " * (curr * 3) + '\u2191')
    print("Turing Machine has halted at accept state: " + state)
    print("\n")
    print("The final output tape: ", end="")
    for char in tape:
        print(char + ", ", end="")
    print("...")
    line = '_' * 100
    print("\n")
    print(line)
    print("\n")
    tape = [char for char in tape if char != "_"]
    return "".join(tape)


input_string = "aaabbaaa"
output_string = turing_machine(input_string)
# Output: aaabbaaaab

input_string = "abb"
output_string = turing_machine(input_string)
# Output: ab

input_string = "bba"
output_string = turing_machine(input_string)
# Output: bb

input_string = "bb"
output_string = turing_machine(input_string)
# Output: bbab

input_string = ""
output_string = turing_machine(input_string)
# Output: a


class TuringMachineTestCase(unittest.TestCase):
    def test_turing_machine_aaabbaaa(self):
        input_string = "aaabbaaa"
        expected_output = "aaabbaaaab"
        output_string = turing_machine(input_string)
        self.assertEqual(output_string, expected_output)

    def test_turing_machine_abb(self):
        input_string = "abb"
        expected_output = "ab"
        output_string = turing_machine(input_string)
        self.assertEqual(output_string, expected_output)

    def test_turing_machine_bba(self):
        input_string = "bba"
        expected_output = "bb"
        output_string = turing_machine(input_string)
        self.assertEqual(output_string, expected_output)

    def test_turing_machine_bb(self):
        input_string = "bb"
        expected_output = "bbab"
        output_string = turing_machine(input_string)
        self.assertEqual(output_string, expected_output)

    def test_turing_machine_empty_string(self):
        input_string = ""
        expected_output = "a"
        output_string = turing_machine(input_string)
        self.assertEqual(output_string, expected_output)


if __name__ == '__main__':
    unittest.main()

```
4. Longer Codomains


```

a, a, a, b, b, a, a, a, _, _, _, ...
↑
Current State: q0
Current Tape Head to be Read: a     
Current Tape Head to be Written: a  
Tape Head Transition: R
Next State: q1


a, a, a, b, b, a, a, a, _, _, _, ...
   ↑
Current State: q1
Current Tape Head to be Read: a     
Current Tape Head to be Written: a
Tape Head Transition: R
Next State: q1


a, a, a, b, b, a, a, a, _, _, _, ...
      ↑
Current State: q1
Current Tape Head to be Read: a
Current Tape Head to be Written: a
Tape Head Transition: R
Next State: q1


a, a, a, b, b, a, a, a, _, _, _, ...
         ↑
Current State: q1
Current Tape Head to be Read: b
Current Tape Head to be Written: b
Tape Head Transition: R
Next State: q1


a, a, a, b, b, a, a, a, _, _, _, ...
            ↑
Current State: q1
Current Tape Head to be Read: b
Current Tape Head to be Written: b
Tape Head Transition: R
Next State: q1


a, a, a, b, b, a, a, a, _, _, _, ...
               ↑
Current State: q1
Current Tape Head to be Read: a
Current Tape Head to be Written: a
Tape Head Transition: R
Next State: q1


a, a, a, b, b, a, a, a, _, _, _, ...
                  ↑
Current State: q1
Current Tape Head to be Read: a
Current Tape Head to be Written: a
Tape Head Transition: R
Next State: q1


a, a, a, b, b, a, a, a, _, _, _, ...
                     ↑
Current State: q1
Current Tape Head to be Read: a
Current Tape Head to be Written: a
Tape Head Transition: R
Next State: q1


a, a, a, b, b, a, a, a, _, _, _, ...
                        ↑
Current State: q1
Current Tape Head to be Read: _
Current Tape Head to be Written: _
Tape Head Transition: L
Next State: q2


a, a, a, b, b, a, a, a, _, _, _, ...
                     ↑
Current State: q2
Current Tape Head to be Read: a
Current Tape Head to be Written: a
Tape Head Transition: R
Next State: q3


a, a, a, b, b, a, a, a, _, _, _, ...
                        ↑
Current State: q3
Current Tape Head to be Read: _
Current Tape Head to be Written: a
Tape Head Transition: R
Next State: q4


a, a, a, b, b, a, a, a, a, _, _, ...
                           ↑
Current State: q4
Current Tape Head to be Read: _
Current Tape Head to be Written: b
Tape Head Transition: R
Next State: q_acc


a, a, a, b, b, a, a, a, a, b, _, ...
                              ↑
Turing Machine has halted at accept state: q_acc


The final output tape: a, a, a, b, b, a, a, a, a, b, _, ...


____________________________________________________________________________________________________

```

```

b, b, _, _, _, ...
↑
Current State: q0
Current Tape Head to be Read: b
Current Tape Head to be Written: b
Tape Head Transition: R
Next State: q5


b, b, _, _, _, ...
   ↑
Current State: q5
Current Tape Head to be Read: b
Current Tape Head to be Written: b
Tape Head Transition: R
Next State: q5


b, b, _, _, _, ...
      ↑
Current State: q5
Current Tape Head to be Read: _
Current Tape Head to be Written: _
Tape Head Transition: L
Next State: q6


b, b, _, _, _, ...
   ↑
Current State: q6
Current Tape Head to be Read: b
Current Tape Head to be Written: b
Tape Head Transition: R
Next State: q7


b, b, _, _, _, ...
      ↑
Current State: q7
Current Tape Head to be Read: _
Current Tape Head to be Written: a
Tape Head Transition: R
Next State: q8


b, b, a, _, _, ...
         ↑
Current State: q8
Current Tape Head to be Read: _
Current Tape Head to be Written: b
Tape Head Transition: R
Next State: q_acc


b, b, a, b, _, ...
            ↑
Turing Machine has halted at accept state: q_acc


The final output tape: b, b, a, b, _, ...


____________________________________________________________________________________________________

```

```

._, _, _, ...
↑
Current State: q0
Current Tape Head to be Read: _
Current Tape Head to be Written: a
Tape Head Transition: R
Next State: q_acc


a, _, _, ...
   ↑
Turing Machine has halted at accept state: q_acc


The final output tape: a, _, _, ...


____________________________________________________________________________________________________
```

1. Shorter Codomain:

```
a, b, b, _, _, _, ...
↑
Current State: q0
Current Tape Head to be Read: a
Current Tape Head to be Written: a
Tape Head Transition: R
Next State: q1


a, b, b, _, _, _, ...
   ↑
Current State: q1
Current Tape Head to be Read: b
Current Tape Head to be Written: b
Tape Head Transition: R
Next State: q1


a, b, b, _, _, _, ...
      ↑
Current State: q1
Current Tape Head to be Read: b
Current Tape Head to be Written: b
Tape Head Transition: R
Next State: q1


a, b, b, _, _, _, ...
         ↑
Current State: q1
Current Tape Head to be Read: _
Current Tape Head to be Written: _
Tape Head Transition: L
Next State: q2


a, b, b, _, _, _, ...
      ↑
Current State: q2
Current Tape Head to be Read: b
Current Tape Head to be Written: _
Tape Head Transition: R
Next State: q_acc


a, b, _, _, _, _, ...
         ↑
Turing Machine has halted at accept state: q_acc


The final output tape: a, b, _, _, _, _, ...


____________________________________________________________________________________________________


b, b, a, _, _, _, ...
↑
Current State: q0
Current Tape Head to be Read: b
Current Tape Head to be Written: b
Tape Head Transition: R
Next State: q5


b, b, a, _, _, _, ...
   ↑
Current State: q5
Current Tape Head to be Read: b
Current Tape Head to be Written: b
Tape Head Transition: R
Next State: q5


b, b, a, _, _, _, ...
      ↑
Current State: q5
Current Tape Head to be Read: a
Current Tape Head to be Written: a
Tape Head Transition: R
Next State: q5


b, b, a, _, _, _, ...
         ↑
Current State: q5
Current Tape Head to be Read: _
Current Tape Head to be Written: _
Tape Head Transition: L
Next State: q6


b, b, a, _, _, _, ...
      ↑
Current State: q6
Current Tape Head to be Read: a
Current Tape Head to be Written: _
Tape Head Transition: R
Next State: q_acc


b, b, _, _, _, _, ...
         ↑
Turing Machine has halted at accept state: q_acc


The final output tape: b, b, _, _, _, _, ...


____________________________________________________________________________________________________
```