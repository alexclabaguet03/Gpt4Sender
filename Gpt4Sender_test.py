# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 22:33:14 2023

@author: carlh
"""

import Gpt4Sender 

API_KEY = "your api key"
test = Gpt4Sender("testingthisout@outlook.fr","Cacahuete(-)",
                  API_key,
                  "https://api.openai.com/v1/chat/completions",1,1)


test.send_email()
