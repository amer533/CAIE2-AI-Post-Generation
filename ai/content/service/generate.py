from django.conf import settings

from .utils import (
    clean_optional_text,
    clean_required_text,
    limit_text,
    run_prompt,
)


MIN_TITLE_LENGTH = getattr(
    settings,
    "AI_POST_MIN_TITLE_LENGTH",
    5,
)

MAX_TITLE_LENGTH = getattr(
    settings,
    "AI_POST_MAX_TITLE_LENGTH",
    200,
)

MAX_TONE_LENGTH = getattr(
    settings,
    "AI_POST_MAX_TONE_LENGTH",
    50,
)

MAX_CONTENT_LENGTH = getattr(
    settings,
    "AI_POST_MAX_CONTENT_LENGTH",
    500,
)


def _build_prompt(title, tone=None):
    selected_tone = tone or "clear and professional"

    return (
        "Write a short blog post using the following requirements:\n"
        f"- Topic: {title}\n"
        f"- Tone: {selected_tone}\n"
        f"- Maximum length: approximately {MAX_CONTENT_LENGTH} characters\n"
        "- Return only the blog post content.\n"
        "- Do not include a title or an introduction about the task.\n"
        "- Keep the writing clear, coherent, and relevant."
    )


def generate_post(title, tone=None):
    clean_title = clean_required_text(
        value=title,
        field_name="Title",
        min_length=MIN_TITLE_LENGTH,
        max_length=MAX_TITLE_LENGTH,
    )

    clean_tone = clean_optional_text(
        value=tone,
        field_name="Tone",
        max_length=MAX_TONE_LENGTH,
    )

    prompt = _build_prompt(clean_title, clean_tone)
    generated_content = run_prompt(prompt)

    content = limit_text(
        generated_content,
        MAX_CONTENT_LENGTH,
    )

    return {
        "title": clean_title,
        "content": content,
        "length": len(content),
    }