# -*- coding: utf-8 -*-
"""Dilara Ünsal - HW#1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KLF-x-U2lpb-xYiCr5zqliVoCWPvZokh
"""

# Homework 1

#1
mylist = [1, 2, 3, 4, 5, 6]
a = int(len(mylist)/2)
i = 0
while i in range(0,a):
  mylist = mylist.append((mylist[i]))
  mylist.pop(0)
  i += 1
print(mylist)

#2
n = int(input("Please enter an integer number: "))
even = []
for i in range(0, n+1):
  if i%2==0:
    even.insert(j,i)
    j += 1
print("Even numbers are: " + even)