import attr

import openai
import funcy as fy

from lugia.settings import API_KEY


openai.api_key = API_KEY


@attr.s()
class OpenAI:
    model = attr.ib(default="gpt-3.5-turbo")

    def chat(self, query):
        resp = openai.ChatCompletion.create(
            model=self.model, messages=[{"role": "user", "content": query}]
        )

        return self._parse_response(resp)

    def _parse_response(self, resp):
        choices = resp.get("choices", [])
        texts = [fy.get_in(choice, ["message", "content"]) for choice in choices]

        return " ".join(texts)
