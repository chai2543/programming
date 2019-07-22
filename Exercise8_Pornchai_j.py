#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#นาย พรชัย จันมิตร 362515241011 EE36241N
a=input("Username :")
b=input("Password :")
if a=="chai" and b=="1011":
    print("Welcome to Shoes Shop.")
    print("--------------Menu--------------")
    print("1. Adidas 1590 THB")
    print("2. Nike 2450 THB")
    print("3. Nanyang 240 THB")
    print("4. Baoji 490 THB")
    print("5. Onitsuka Tiger 3510 THB")
    A=1590
    N=2450
    n=240
    B=490
    O=3510
    Shoes=int(input("What do you want?(1-5) : "))
    Much=int(input("How many do you want? : "))
    if Shoes==1:
        print("You buy ",Much," of Adidas ",A*Much, " THB")
    elif Shoes==2:
        print("You buy ",Much," of  Nike ",N*Much, " THB")
    elif Shoes==3:
        print("You buy ",Much," of Nanyang ",n*Much, " THB")
    elif Shoes==4:
        print("You buy ",Much," of Baoji ",B*Much, " THB")
    elif Shoes==5:
        print("You buy ",Much," of Onitsuka Tiger ",O*Much, " THB")
    
else :
    print("Sorry, it's error ")

