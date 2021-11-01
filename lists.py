#!/usr/bin/env python3

# Created by: Seti Ngabo
# Created on: Oct 2021
# This program finds the average percentage


def marks_average(the_marks):
    # This function creates a list
    final_total = 0

    # process
    for one_mark in the_marks:
        final_total += one_mark
    final_total = final_total / len(the_marks)

    my_number = final_total + 0.5
    final_total = int(my_number)

    return final_total


def main():
    # This function accepts a list
    my_list = []
    user_input_int = None

    # heading
    print("Please enter 1 mark at a time. Enter -1 to end.")
    print("")

    while user_input_int != -1:
        # input
        user_input_str = input("What is your mark? (as %): ")

        try:
            user_input_int = int(user_input_str)
            my_list.append(user_input_int)

        except Exception:
            print("\nInvalid input, try again.")

    # remove -1
    my_list.pop()

    # call functions
    final_answer = marks_average(my_list)

    # output
    print("\nThe average is: {}%".format(final_answer))

    print("\nDone.")


if __name__ == "__main__":
    main()
