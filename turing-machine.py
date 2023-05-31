# Resources: ChatGPT and GitHub CoPilot
# This is a Turing Machine that accepts {a, b}∗
# If the input string strats and ends with the same character, it adds a "ab" at the end of the string
# If the input string does not start and end with the same character, it removes the last character of the string
# If the input string is empty, it adds an "a" to the end of the string
# With these conditions, there will be a mapped string that is longer and shorter than the input string


import unittest

# Helper function to print the current step of the tape


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


# Actual function to implement the Turing Machine
def turing_machine(input_string):

    # Defines the tape, current index, current state, next state, and transition - notice blanks are added at the end of the tape
    tape = list(input_string + "_" + "_" + "_")
    curr = 0
    write = ""
    state = "q0"
    next_state = ""
    transition = ""

    # While loop to keep the machine running until it reaches the accept state
    while state != "q_acc":

        # If current state is q0, it will check the current tape head and transition to the next state
        # If it is a blank, it will write an "a" and transition to q_acc
        # If it is an "a", it will write an "a" and transition to q1
        # If it is a "b", it will write a "b" and transition to q5
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

        # If current state is q1, it will keep reading and writing the same character until it reaches a blank
        # If it is a blank, it will write a blank and transition to q2 after going left on the tape
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

        # If current state is q2, it will check the current tape head, which is the character before the blank, or the last character of the input string
        # If it is an "a", it will write an "a" and transition to q3, replace the blank space with an "a", then q4, replace the blank space with an "b", then q_acc
        # This is the case where the input string starts and ends with the same character
        #
        # If it is a "b", it will remove the last character of the string by writing a blank and transition to q_acc
        # This is the case where the input string does not start and end with the same character
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

        # If current state is q3, it will keep reading and writing the same character until it reaches a blank
        # If it is a blank, it will write a blank and transition to q4 after going left on the tape
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

        # If current state is q4, it will check the current tape head, which is the character before the blank, or the last character of the input string
        # If it is an "a", it will remove the last character of the string by writing a blank and transition to q_acc
        # This is the case where the input string does not start and end with the same character
        #
        # If it is a "b", it will write a "b" and transition to q7, replace the blank space with an "a", then q8, replace the blank space with an "b", then q_acc
        # This is the case where the input string starts and ends with the same character
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

    # Lastly, if the current state is q_acc, the while loop will break and it will print the final tape and halt the machine
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

    # Takes the tape and removes all the blank spaces for testing purposes
    tape = [char for char in tape if char != "_"]
    return "".join(tape)


# Example where the input string starts and ends with the same character of "a"
input_string = "aaabbaaa"
output_string = turing_machine(input_string)
# Output: aaabbaaaab

# Example where the input string does not start and end with the same character of "a" and "b"
input_string = "abb"
output_string = turing_machine(input_string)
# Output: ab

# Example where the input string does not start and end with the same character of "b" and "a"
input_string = "bba"
output_string = turing_machine(input_string)
# Output: bb

# Example where the input string starts and ends with the same character of "b"
input_string = "bb"
output_string = turing_machine(input_string)
# Output: bbab

# Example where the input string is empty
input_string = ""
output_string = turing_machine(input_string)
# Output: a


# Unit tests
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
