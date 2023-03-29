# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 22:33:14 2023

@author: carlh
"""

import Gpt4Sender 

API_KEY = "your_api_key"
sender_email = "your_email"
account_password = "email_account_password"

test = Gpt4Sender(sender_email,account_password,API_KEY,"https://api.openai.com/v1/chat/completions",1,0)


test.send_email()
