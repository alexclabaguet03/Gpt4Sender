# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 21:15:00 2023

@author: carlh
"""

import requests
import json
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage




class Gpt4Sender:
    def __init__(self,sender_email,account_password,API_KEY,API_ENDPOINT,save_in_file,send_pic):
        self.sender_email = sender_email
        self.account_password = account_password
        self.API_KEY = API_KEY
        self.API_ENDPOINT = API_ENDPOINT
        self.save_in_file = save_in_file
        self.send_pic = send_pic

    def generate_chat_completion(self,messages, model="gpt-4", temperature=1, max_tokens=None):
        headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {self.API_KEY}",
        }
        data = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
        }
        if max_tokens is not None:
           data["max_tokens"] = max_tokens
        response = requests.post(self.API_ENDPOINT, headers=headers, data=json.dumps(data))
        if response.status_code == 200:
           return response.json()["choices"][0]["message"]["content"]
        else:
           raise Exception(f"Error {response.status_code}: {response.text}")
   

    def send_email(self):
       question = input("What is your question?: ")
       system_info = input("What the should GPT know about itself: ")
       messages = [
       {"role": "system", "content": system_info},
       {"role": "user", "content": question}
       ]
       print("\n....ChatGpt is generating an answer....")
       response_text = self.generate_chat_completion(messages)
       print("\n-----Here is GPT4's answer-----")
       print(response_text)
       print("-------------------------------")
       to_addresses = input("Enter recipient email addresses separated by commas: ").split(',')
       subject = input("Email subject: ")
       body = response_text + "\n\nSincerely,\n\nAlex Lecon\n\nepflaiteam.ch"
       msg = MIMEMultipart()
       msg['Subject'] = subject
       msg.attach(MIMEText(body, 'plain'))
       if self.save_in_file:
           with open('answer.txt', 'w') as file:
               file.write(response_text)
           file_path = "answer.txt"
           with open(file_path, 'rb') as file:
                  attachment = MIMEApplication(file.read(), _subtype='txt')
                  attachment.add_header('Content-Disposition', 'attachment', filename=file_path)
                  msg.attach(attachment)
       if self.send_pic:
           image_file = 'image.jpg'
           with open(image_file, 'rb') as f:
               img_data = f.read()
               image = MIMEImage(img_data, name=os.path.basename(image_file))
               msg.attach(image)
       with smtplib.SMTP('smtp.office365.com', 587) as server:
          server.starttls()
          server.login(self.sender_email, self.account_password)
          for to_address in to_addresses:
              msg['To'] = to_address
              server.sendmail(self.sender_email, to_address, msg.as_string())
       print("\nEmail(s) sent successfully!")
