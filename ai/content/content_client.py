from django.conf import settings
from openai import OpenAI


class ContentClient:
    def __init__(self):
        self.client = OpenAI(
            api_key=settings.OPENAI_API_KEY
        )
        self.model = settings.OPENAI_MODEL

    def generate(self, prompt):
        response = self.client.responses.create(
            model=self.model,
            input=prompt,
        )

        return response.output_text