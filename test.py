import openai
import requests

# msg = "meaning of UOP"
# openai_api_key = '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'
# openai.api_key = openai_api_key
#
# def ask_openai(message):
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role": "system", "content": "You are an helpful assistant."},
#             {"role": "user", "content": message},
#         ]
#     )
#     answer = response.choices[0].text.strip()
#     return answer
#
# print(ask_openai(msg))

# response = openai.ChatCompletion.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant."},
#         {"role": "user", "content": "Who won the world series in 2020?"},
#         {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
#         {"role": "user", "content": "Where was it played?"}
#     ]
# )

import os
import openai
openai.api_key = "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"


def ask_openai(message):
  try:
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": "You are an helpful assistant."},
        {"role": "user", "content": message},
      ]
    )
  except Exception as e:
    print(e)
    answer = "Something went wrong."
  else:
    answer = response.choices[0].message["content"]
  return answer

print(ask_openai("what's the meaning of war"))

