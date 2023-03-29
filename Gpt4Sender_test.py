# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 22:33:14 2023

@author: carlh
"""

import Gpt4Sender 

test = Gpt4Sender("testingthisout@outlook.fr","Cacahuete(-)",
                  "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",
                  "https://api.openai.com/v1/chat/completions",1,1)


test.send_email()