# -*- coding: utf-8 -*-
"""
Created on Mon Mar 17 14:16:37 2025

@author: 91912
"""

import datetime

class BankAcc:
    total_acc = 0  
    
    def __init__(self, name, type, bal=0):
        self.name, self.type, self.bal = name, type, bal
        self.id, self.log = BankAcc.total_acc + 1, []
        BankAcc.total_acc += 1
        self._log(f"Acc opened with Rs.{bal}")
    
    def dep(self, amt):
        if self._valid(amt):
            self.bal += amt
            self._log(f"Deposited Rs.{amt}")
            return f"New bal: Rs.{self.bal}"
        return "Invalid amt"
    
    def wd(self, amt):
        if self._valid(amt) and amt <= self.bal:
            self.bal -= amt
            self._log(f"Withdrew Rs.{amt}")
            return f"New bal: Rs.{self.bal}"
        return "Insufficient bal or invalid amt"
    
    def trans(self, recv, amt):
        if self._valid(amt) and amt <= self.bal:
            self.bal -= amt
            recv.bal += amt
            self._log(f"Transferred Rs.{amt} to {recv.name}")
            recv._log(f"Received Rs.{amt} from {self.name}")
            return f"New bal: Rs.{self.bal}"
        return "Insufficient bal or invalid amt"
    
    def bal_chk(self):
        return f"Bal: Rs.{self.bal}"
    
    def hist(self):
        return "\n".join(self.log) or "No transactions"
    
    def _log(self, msg):
        self.log.append(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}")
    
    @classmethod
    def total(cls):
        return f"Total accs: {cls.total_acc}"
    
    @staticmethod
    def _valid(amt):
        return isinstance(amt, (int, float)) and amt > 0

acc1, acc2 = BankAcc("Amit", "Savings", 8000), BankAcc("Priya", "Current", 5000)

print(acc1.dep(2500))
print(acc1.wd(1200))
print(acc1.trans(acc2, 2000))
print(acc1.bal_chk())
print(acc1.hist())
print(BankAcc.total())
