# -*- coding: utf-8 -*-
"""
Created on Tue May  9 16:41:31 2023

@author: Sumit
"""
from pydantic import BaseModel
class BankNote(BaseModel):
    variance:float
    skewness:float
    curtosis:float
    entropy:float
    