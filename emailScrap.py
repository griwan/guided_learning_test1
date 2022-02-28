import re
import json

f = open("websiteData.txt","r",encoding='utf-8')
email_list = []
for lines in f:
    emails = re.findall(r'[\w\.-]+@[\w\.-]+',lines)
    if len(emails)>0:
        email_list+=emails

res = {i:email_list.count(i) for i in email_list}

output = {}
for email,occ in res.items():
    username = email.split('@')[0]
    if re.match(r'[\w\.-]+\.[\w\.-]+',username):
        cat = 'human'
    elif len(username)>=8:
        cat = 'human'
    else:
        cat = 'non-human'
    output[email] = {"Occurance":occ,"EmailType":cat}

with open('result.json', 'w') as j:
    json.dump(output, j,indent=4)
