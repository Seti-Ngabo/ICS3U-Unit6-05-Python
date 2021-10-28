#!/usr/bin/env python3

# Created by: Seti Ngabo
# Created on: Oct 2021
# This program finds the average percentage


def marks_average(the_marks, counter):
    # this function creates a list

    numbers = counter - 1
    sub_total = 0
    for one_mark in the_marks:
        sub_total = sub_total + one_mark
    the_final_answer = sub_total / numbers

    return the_final_answer


def main():
    # this function accepts a list

    the_marks = []
    counter = 0

    print("Please enter 1 mark at a time. Enter -1 to end.")
    print("")

    while True:
        user_number = input("What is your mark? (as %): ")
        counter = counter + 1
        try:
            my_mark = int(user_number)
            if my_mark == -1:
                break
            elif my_mark < 0 or my_mark > 100:
                print("\nPlease enter a mark between 0 - 100.")
                print("\nDone.")
                exit()
            the_marks.append(my_mark)

        except (Exception):
            print("\nInvalid input, try again.")
            print("\nDone.")
            exit()

    final_answer = marks_average(the_marks, counter)
    print("\nThe average is {0}% ".format(final_answer))

    print("\nDone.")


if __name__ == "__main__":
    main()
