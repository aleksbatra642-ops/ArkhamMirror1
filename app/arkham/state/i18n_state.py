"""Internationalization State for Reflex

Manages the global language state and provides methods to switch languages.
"""

import reflex as rx
from app.arkham.i18n.manager import i18n


class I18nState(rx.State):
    """State for managing internationalization and language selection."""
    
    current_language: str = i18n.DEFAULT_LANGUAGE
    available_languages: list = i18n.SUPPORTED_LANGUAGES
    
    def set_language(self, lang: str):
        """Set the current language.
        
        Args:
            lang: Language code ('en' or 'ru')
        """
        if lang in self.available_languages:
            self.current_language = lang
            i18n.set_language(lang)
    
    def switch_to_russian(self):
        """Switch to Russian language."""
        self.set_language('ru')
    
    def switch_to_english(self):
        """Switch to English language."""
        self.set_language('en')
    
    def get_text(self, key: str, namespace: str = 'common', default: str = '') -> str:
        """Get translated text based on current language.
        
        Args:
            key: Translation key (supports dot notation for nested keys)
            namespace: Namespace/file name without extension
            default: Default value if translation not found
            
        Returns:
            Translated text
        """
        return i18n.get(key, namespace, default)
    
    def get_all_translations(self, namespace: str = 'common') -> dict:
        """Get all translations for a namespace.
        
        Args:
            namespace: Namespace/file name without extension
            
        Returns:
            Dictionary of all translations in the namespace
        """
        return i18n.get_all(namespace)
