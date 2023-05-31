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
