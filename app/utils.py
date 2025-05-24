from .config import settings

def translate_message(message: str, lang: str) -> str:
    """
    Placeholder for translation logic.
    For now, just return the message with language label.
    """
    language_name = settings.SUPPORTED_LANGUAGES.get(lang, "English")
    return f"[{language_name}] {message}"
