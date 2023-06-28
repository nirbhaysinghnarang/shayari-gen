
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")


class Shayari:
    def __init__(self,params):
        assert(type(params)==list)
        self._params = params

    def generate(self):
        prompt = f"Write me a shayari in Hindi/Urdu but in English text using these three words: {str(self._params)}"
        print(self._params)
        completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=[{"role": "user", "content": prompt}])
        return completion.choices[0]["message"]["content"]



