#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 11:49:03 2026

@author: geo
"""

class BankAccount():
    
    def __init__(self, balance=0):
        if balance < 0:
            raise ValueError("Initial balance cannot be negative")            
        self.__balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")
        # or raise an exception
    @property        
    def balance(self):
        return self.__balance
    
myAccount = BankAccount(1e6)

myAccount.__balance = 2e6

print(myAccount.balance)    