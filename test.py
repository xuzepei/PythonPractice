
#sudo pip install Pillow

#!/usr/bin/python
# -*- coding: utf-8 -*-
import math



def test():
    capital = 1900000
    incomeOfMonth = 20000
    total = capital
    bonus = 15500
    rateOfYear = 0.045
    expenseOfMonth = 6000

    for i in range(1,145):
        interestOfMonth = (total + (incomeOfMonth - expenseOfMonth)*i)*rateOfYear/12.0 
        #print("$$$interestOfMonth: " + str(interestOfMonth) + " in " + str(i) + " month.\n")
        total = total + incomeOfMonth - expenseOfMonth + interestOfMonth
        #print("$$$totalInMonth: " + str(total) + " in " + str(i) + " month.\n")

        if i%12 == 0:
            total = total + bonus
            print("$$$:" + str((i / 12)) + " year," + " total: " + str(total) + "\n")
            print("--------------------------")

    print("$$$total: " + str(total) + "\n")


test()
