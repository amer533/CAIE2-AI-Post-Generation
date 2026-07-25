from .content_client import ContentClient

client = ContentClient()


def _build_prompt(title, tone=None):
    prompt = f"Write a short blog post about: {title}."

    if tone:
        prompt += f" Use a {tone.strip()} tone."

    return prompt




def generate_post(title, tone=None):
    if not title or not title.strip():
        raise ValueError("Title cannot be empty.")

    title = title.strip()

    if len(title) < 5:
        raise ValueError("Title must be at least 5 characters.")

    prompt = _build_prompt(title, tone)
    raw_content = client.generate(prompt)  

    content = raw_content.strip()

    if not content:
        raise ValueError("Generated content is empty.")

    content = content[:500]

    return {
        "title": title,
        "content": content,
        "length": len(content)
    }
    