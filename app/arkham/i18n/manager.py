"""Translation Manager for ArkhamMirror

Manages loading and accessing translations with support for:
- Multiple languages (English, Russian)
- Nested key access (e.g., 'knowledge.title')
- Fallback to default language
- Dynamic language switching
"""

import json
import os
from typing import Dict, Any, Optional
from pathlib import Path


class I18nManager:
    """Manager for handling translations and internationalization."""
    
    SUPPORTED_LANGUAGES = ['en', 'ru']
    DEFAULT_LANGUAGE = 'ru'  # Russian by default
    
    def __init__(self):
        """Initialize the translation manager."""
        self.locales_dir = Path(__file__).parent.parent / 'locales'
        self.translations: Dict[str, Dict[str, Any]] = {}
        self.current_language = self.DEFAULT_LANGUAGE
        self._load_all_translations()
    
    def _load_all_translations(self):
        """Load all translation files from the locales directory."""
        for lang in self.SUPPORTED_LANGUAGES:
            lang_dir = self.locales_dir / lang
            self.translations[lang] = {}
            
            if not lang_dir.exists():
                print(f"Warning: Language directory {lang_dir} does not exist")
                continue
            
            # Load all JSON files in the language directory
            for json_file in lang_dir.glob('*.json'):
                namespace = json_file.stem  # filename without extension
                try:
                    with open(json_file, 'r', encoding='utf-8') as f:
                        self.translations[lang][namespace] = json.load(f)
                except (json.JSONDecodeError, IOError) as e:
                    print(f"Error loading {json_file}: {e}")
                    self.translations[lang][namespace] = {}
    
    def set_language(self, lang: str) -> bool:
        """Set the current language.
        
        Args:
            lang: Language code ('en' or 'ru')
            
        Returns:
            True if language was set, False if language not supported
        """
        if lang in self.SUPPORTED_LANGUAGES:
            self.current_language = lang
            return True
        return False
    
    def get(self, key: str, namespace: str = 'common', default: str = '') -> str:
        """Get a translation string.
        
        Supports nested keys with dot notation:
            i18n.get('knowledge.title', 'pages')
            i18n.get('entities.types.PERSON', 'pages')
        
        Args:
            key: Translation key, can use dots for nested access (e.g., 'button.submit')
            namespace: Namespace/file name without extension (default: 'common')
            default: Default value if translation not found
            
        Returns:
            Translated string or default value
        """
        try:
            # Get the namespace from current language
            if self.current_language not in self.translations:
                return default or key
            
            translations = self.translations[self.current_language]
            if namespace not in translations:
                return default or key
            
            # Navigate through nested keys
            value = translations[namespace]
            keys = key.split('.')
            
            for k in keys:
                if isinstance(value, dict):
                    value = value.get(k)
                    if value is None:
                        return default or key
                else:
                    return default or key
            
            # Return value if it's a string
            if isinstance(value, str):
                return value
            else:
                return default or key
                
        except (KeyError, TypeError, AttributeError):
            return default or key
    
    def get_all(self, namespace: str = 'common') -> Dict[str, Any]:
        """Get all translations for a namespace.
        
        Args:
            namespace: Namespace/file name without extension
            
        Returns:
            Dictionary of all translations in the namespace
        """
        try:
            if self.current_language not in self.translations:
                return {}
            
            translations = self.translations[self.current_language]
            return translations.get(namespace, {})
        except (KeyError, TypeError):
            return {}
    
    def reload_translations(self):
        """Reload all translations from disk.
        
        Useful for development when translation files are modified.
        """
        self.translations = {}
        self._load_all_translations()
    
    def get_supported_languages(self) -> list:
        """Get list of supported language codes.
        
        Returns:
            List of supported language codes
        """
        return self.SUPPORTED_LANGUAGES
    
    def get_current_language(self) -> str:
        """Get the current language code.
        
        Returns:
            Current language code
        """
        return self.current_language


# Global instance
i18n = I18nManager()
