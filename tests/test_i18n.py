"""Tests for the i18n (Internationalization) system

Comprehensive tests for translation management, language switching,
and nested key access.
"""

import pytest
from app.arkham.i18n.manager import I18nManager, i18n


class TestI18nManager:
    """Test cases for I18nManager class"""
    
    def test_initialization(self):
        """Test that I18nManager initializes correctly"""
        manager = I18nManager()
        assert manager.current_language == 'ru'
        assert 'en' in manager.SUPPORTED_LANGUAGES
        assert 'ru' in manager.SUPPORTED_LANGUAGES
    
    def test_default_language_is_russian(self):
        """Test that default language is Russian"""
        manager = I18nManager()
        assert manager.get_current_language() == 'ru'
    
    def test_set_language_valid(self):
        """Test setting language to valid option"""
        manager = I18nManager()
        assert manager.set_language('en') is True
        assert manager.get_current_language() == 'en'
    
    def test_set_language_invalid(self):
        """Test setting language to invalid option"""
        manager = I18nManager()
        assert manager.set_language('fr') is False
        assert manager.get_current_language() == 'ru'
    
    def test_get_translation_basic(self):
        """Test basic translation retrieval"""
        manager = I18nManager()
        title = manager.get('app_name', 'common')
        assert title == 'АркхамМиррор'
    
    def test_get_translation_english(self):
        """Test English translation retrieval"""
        manager = I18nManager()
        manager.set_language('en')
        title = manager.get('app_name', 'common')
        assert title == 'ArkhamMirror'
    
    def test_get_nested_key(self):
        """Test nested key access with dot notation"""
        manager = I18nManager()
        entity_type = manager.get('entities.types.PERSON', 'pages')
        assert entity_type == 'Человек'
    
    def test_get_nested_key_english(self):
        """Test nested key access in English"""
        manager = I18nManager()
        manager.set_language('en')
        entity_type = manager.get('entities.types.PERSON', 'pages')
        assert entity_type == 'Person'
    
    def test_get_with_default(self):
        """Test fallback to default value"""
        manager = I18nManager()
        result = manager.get('nonexistent_key', 'common', 'default_value')
        assert result == 'default_value'
    
    def test_get_all_namespace(self):
        """Test retrieving all translations in a namespace"""
        manager = I18nManager()
        common = manager.get_all('common')
        assert isinstance(common, dict)
        assert len(common) > 0
        assert 'app_name' in common
    
    def test_supported_languages(self):
        """Test getting list of supported languages"""
        manager = I18nManager()
        langs = manager.get_supported_languages()
        assert 'en' in langs
        assert 'ru' in langs
        assert len(langs) == 2
    
    def test_multiple_namespaces(self):
        """Test loading multiple namespaces"""
        manager = I18nManager()
        
        common_key = manager.get('submit', 'common')
        pages_key = manager.get('knowledge.title', 'pages')
        component_key = manager.get('header.search', 'components')
        error_key = manager.get('network_error', 'errors')
        validation_key = manager.get('required', 'validations')
        
        assert common_key is not None
        assert pages_key is not None
        assert component_key is not None
        assert error_key is not None
        assert validation_key is not None
    
    def test_language_switching_consistency(self):
        """Test that language switching works correctly"""
        manager = I18nManager()
        
        # Get Russian translation
        ru_text = manager.get('app_name', 'common')
        assert ru_text == 'АркхамМиррор'
        
        # Switch to English
        manager.set_language('en')
        en_text = manager.get('app_name', 'common')
        assert en_text == 'ArkhamMirror'
        
        # Switch back to Russian
        manager.set_language('ru')
        ru_text_again = manager.get('app_name', 'common')
        assert ru_text_again == 'АркхамМиррор'
    
    def test_reload_translations(self):
        """Test reloading translations from disk"""
        manager = I18nManager()
        original = manager.get('app_name', 'common')
        
        # Reload
        manager.reload_translations()
        reloaded = manager.get('app_name', 'common')
        
        assert original == reloaded
    
    def test_global_i18n_instance(self):
        """Test that global i18n instance works"""
        text = i18n.get('app_name', 'common')
        assert text == 'АркхамМиррор'
        
        i18n.set_language('en')
        en_text = i18n.get('app_name', 'common')
        assert en_text == 'ArkhamMirror'
        
        # Reset to Russian
        i18n.set_language('ru')


class TestTranslationCompleteness:
    """Test that all necessary translations are present"""
    
    def test_common_namespace_completeness(self):
        """Test that common namespace has essential translations"""
        manager = I18nManager()
        essential_keys = ['submit', 'cancel', 'delete', 'loading', 'error']
        
        for key in essential_keys:
            value = manager.get(key, 'common')
            assert value is not None
            assert value != key  # Should not return the key as fallback
    
    def test_pages_namespace_completeness(self):
        """Test that pages namespace has all 9 pages"""
        manager = I18nManager()
        pages = ['home', 'knowledge', 'entities', 'search', 'graph', 'qa', 'timeline', 'contradictions', 'ach']
        
        pages_ns = manager.get_all('pages')
        for page in pages:
            assert page in pages_ns
            assert 'title' in pages_ns[page]
    
    def test_entity_types_completeness(self):
        """Test that all entity types are translated"""
        manager = I18nManager()
        entity_types = ['PERSON', 'ORGANIZATION', 'LOCATION', 'EVENT', 'OBJECT', 'CONCEPT', 'DOCUMENT']
        
        for entity_type in entity_types:
            value = manager.get(f'entities.types.{entity_type}', 'pages')
            assert value is not None
            assert value != f'entities.types.{entity_type}'
    
    def test_bilingual_consistency(self):
        """Test that both languages have the same structure"""
        manager = I18nManager()
        
        # Get Russian structure
        manager.set_language('ru')
        ru_keys = set(manager.get_all('common').keys())
        
        # Get English structure
        manager.set_language('en')
        en_keys = set(manager.get_all('common').keys())
        
        # Keys should match
        assert ru_keys == en_keys


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
