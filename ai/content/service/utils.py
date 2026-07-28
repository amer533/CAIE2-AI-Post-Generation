from ..content_client import ContentClient


client = ContentClient()


class ContentServiceError(Exception):
    """Raised when the AI content service fails."""


def clean_required_text(
    value,
    field_name,
    min_length=1,
    max_length=None,
):
    if not isinstance(value, str):
        raise ValueError(f"{field_name} must be a string.")

    cleaned_value = value.replace("\x00", "").strip()

    if not cleaned_value:
        raise ValueError(f"{field_name} cannot be empty.")

    if len(cleaned_value) < min_length:
        raise ValueError(
            f"{field_name} must be at least {min_length} characters."
        )

    if max_length and len(cleaned_value) > max_length:
        raise ValueError(
            f"{field_name} cannot exceed {max_length} characters."
        )

    return cleaned_value


def clean_optional_text(value, field_name, max_length):
    if value is None:
        return None

    if not isinstance(value, str):
        raise ValueError(f"{field_name} must be a string.")

    cleaned_value = value.replace("\x00", "").strip()

    if not cleaned_value:
        return None

    if len(cleaned_value) > max_length:
        raise ValueError(
            f"{field_name} cannot exceed {max_length} characters."
        )

    return cleaned_value


def run_prompt(prompt):
    try:
        result = client.generate(prompt)

    except Exception as error:
        raise ContentServiceError(
            "The AI content service is currently unavailable."
        ) from error

    if not isinstance(result, str) or not result.strip():
        raise ContentServiceError(
            "The AI content service returned an empty response."
        )

    return result.strip()


def limit_text(text, max_length):
    if len(text) <= max_length:
        return text

    shortened_text = text[: max_length - 3]
    shortened_text = shortened_text.rsplit(" ", 1)[0].strip()

    if not shortened_text:
        shortened_text = text[: max_length - 3].strip()

    return f"{shortened_text}..."