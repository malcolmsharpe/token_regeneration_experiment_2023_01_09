null = None #???

response = {
  "choices": [
    {
      "finish_reason": "length",
      "index": 0,
      "logprobs": {
        "text_offset": [
          0,
          4,
          7,
          9,
          14,
          17,
          23,
          37
        ],
        "token_logprobs": [
          null,
          -1.2819546,
          -0.9657405,
          -2.1369379,
          -3.4559553,
          -8.250245,
          -14.824792,
          -3.4046385
        ],
        "tokens": [
          "This",
          " is",
          " a",
          " test",
          " of",
          " token",
          " probabilities",
          "."
        ],
        "top_logprobs": [
          null,
          {
            " article": -4.2783694,
            " is": -1.2819546,
            " post": -4.566227,
            " was": -4.2785344,
            " will": -4.3295193
          },
          {
            " a": -0.9657405,
            " an": -2.5580046,
            " my": -3.4007819,
            " not": -3.6683521,
            " the": -1.7196867
          },
          {
            " great": -3.6982958,
            " sample": -3.5835142,
            " simple": -3.4811277,
            " test": -2.1369379,
            " very": -3.6834874
          },
          {
            "\n": -0.3512753,
            " message": -3.6645505,
            " of": -3.4559553,
            " string": -3.9084146,
            ".": -4.1852655
          },
          {
            "\n": -3.9467056,
            " a": -2.4538188,
            " how": -4.4596777,
            " my": -3.761269,
            " the": -0.6110149
          },
          {
            "\n": -2.0300207,
            "ization": -1.3926486,
            "ize": -2.93212,
            "izer": -2.8354473,
            "izing": -1.8264847
          },
          {
            "\n": -0.17835176,
            " for": -3.9248552,
            " with": -4.818597,
            ".": -3.4046385,
            ":": -4.341651
          }
        ]
      },
      "text": "This is a test of token probabilities."
    }
  ],
  "created": 1673308494,
  "id": "cmpl-6WwGcQAv4sBnW8MNzDgzCcs4UISwt",
  "model": "text-davinci-003",
  "object": "text_completion",
  "usage": {
    "prompt_tokens": 8,
    "total_tokens": 8
  }
}

top_logprobs = response['choices'][0]['logprobs']['top_logprobs']
out = []
for entry in top_logprobs:
    if entry is None: continue

    ranking = [(entry[tok], tok) for tok in entry]
    ranking.sort()
    out.append(ranking[-1][1])
print('"""' + ''.join(out) + '"""')
