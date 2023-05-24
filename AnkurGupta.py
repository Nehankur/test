import openai
import io
openai.api_key = "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"

adda = openai.Completion.create(
  model = "text-davinci-003",
  prompt = "Tell me about India",
  max_tokens = 5000,
  tempreture = 0.9
)

print(adda)
