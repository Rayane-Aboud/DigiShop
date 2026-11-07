import openai

import os
openai.api_key = os.environ["OPENAI_API_KEY"]

prompt = f'''
given sql table in sqllite3 that has attributes:
id:integer
user_id:integer
product_name:string
description:Text
price:string
brand:string
category:string
date:DateTime
return :
    
'''
response = openai.Completion.create(
    engine="davinci",
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=1,
)

print(response)