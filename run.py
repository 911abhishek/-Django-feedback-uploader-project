#!/usr/bin/env python3

import os

import requests

dir_path = "/data/feedback"

feedback_list = []

for file in os.listdir(dir_path):

  file_path = os.path.join(dir_path,file)

  with open(file_path,"r") as f:

    lines = f.readlines()

    title = lines[0].strip()

    name = lines[1].strip()  

    date = lines[2].strip()

    feedback = ' '.join([line.strip() for line in lines[3:]])

    feedback_dict= {"title":title, "name":name, "date":date, "feedback":feedback}

    feedback_list.append(feedback_dict)

url = "http://34.145.70.216/feedback"
for feedback in feedback_list:
    response = requests.post(url,feedback)
    if response.status_code == 201:
       print("success")
    else:
       print("went wrong")