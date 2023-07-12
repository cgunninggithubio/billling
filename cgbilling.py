
# Author:chloe gunning
# Date:7/10/23
#
# This module calculates and displays billing information
# for students in the class registration system.  Student and
# class records are reviewed and tuition fees are calculated.
# -----------------------------------------------------------------
# import datetime
from datetime import date, time, datetime





def display_bill(id, s_in_state, c_rosters, c_hours):
    # ------------------------------------------------------------
    # This function displays the student's bill. It takes four
    # parameters: id, the student id; s_in_state, the list of
    # in-state students; c_rosters, the rosters of students in
    # each course; c_hours, the number of hours in each course.
    # The function has no return value.
    # ------------------------------------------------------------
    # establish tuition cost for in state versus out of state
    if s_in_state[id]:
        bill = 225
    else:
        bill = 850
# initialize cost so we can add
    total = 0
    hours = 0

    for c in c_rosters:
        if id in c_rosters[c]:
            hour = c_hours[c]
            hours += hour
            total += hours * bill
            ctotal = hour * bill


def display_hours_and_bill(hours, total):
    # ------------------------------------------------------------
    # This function prints the number of course hours the student
    # is taking and the total tuition cost. It takes two parameters:
    # hours and cost. This function has no return value.
    # ------------------------------------------------------------
    dt1 = datetime.today()
    print('Tuition Summary')
    print(f'Student:{id}')
    print(f'Generated on {dt1}')

    print("course\tHours\tCost")
    print("------\t-----\t--------")
    print(f'{c}\t{hour}\t{ctotal}')
    print("------\t-----\t--------")
    print(f'total:\t\t{hours}\t\t{total}')

    display_hours_and_bill(5, 4)