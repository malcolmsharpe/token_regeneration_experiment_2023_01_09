import os
import openai

openai.api_key_path = 'api_key.txt'

prompt = open('example2.txt').read()

print('"""' + prompt + '"""')

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=prompt,
  temperature=0.0,
  max_tokens=0,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
  echo=True,
  logprobs=5
)

top_logprobs = response['choices'][0]['logprobs']['top_logprobs']
#print(top_logprobs)
out = []
for entry in top_logprobs:
    if entry is None: continue

    ranking = [(entry[tok], tok) for tok in entry]
    ranking.sort()
    out.append(ranking[-1][1])
print('"""' + ''.join(out) + '"""')
