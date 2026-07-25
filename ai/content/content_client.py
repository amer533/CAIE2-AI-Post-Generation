import os

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()


class ContentClient:
    def __init__(self):
        # Temporary Groq configuration
        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            raise ValueError(
                "GROQ_API_KEY environment variable is not set."
            )

        self.client = OpenAI(
            api_key=api_key,
            base_url="https://api.groq.com/openai/v1",
        )

        self.model = "openai/gpt-oss-20b"

        # Official OpenAI configuration:
        # Uncomment this code when a valid OpenAI key is available,
        # and comment out the Groq configuration above.

        # api_key = os.getenv("OPENAI_API_KEY")
        #
        # if not api_key:
        #     raise ValueError(
        #         "OPENAI_API_KEY environment variable is not set."
        #     )
        #
        # self.client = OpenAI(api_key=api_key)
        # self.model = "gpt-4.1-mini"

    def generate(self, prompt):
        response = self.client.responses.create(
            model=self.model,
            input=prompt,
        )

        return response.output_text