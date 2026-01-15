# Локализация Приложения

## Обзор

Приложение обладает полным i18n (интернационализация) системой для поддержки множества языков. Приложение стартует на **русском языке** по умолчанию.

## Файловая структура

```
app/arkham/
├── i18n/
│   ├── __init__.py
│   └── manager.py           # Класс I18nManager
│
├── locales/
│   ├── ru/
│   │   ├── common.json       # Общие строки
│   │   ├── pages.json        # Страницы
│   │   ├── components.json   # Компоненты
│   │   ├── errors.json       # Ошибки
│   │   └── validations.json  # Валидация
│   └── en/
│       ├── common.json
│       ├── pages.json
│       ├── components.json
│       ├── errors.json
│       └── validations.json
│
├── state/
│   └── i18n_state.py     # Состояние Reflex для i18n
└── ...
```

## Компоненты

### I18nManager

**Методы:**

```python
from app.arkham.i18n.manager import i18n

# Получить перевод
i18n.get('knowledge.title', 'pages')

# Установить язык
i18n.set_language('en')

# От Reload переводы
i18n.reload_translations()
```

### I18nState

**Reflex State для управления языком:**

```python
from app.arkham.state.i18n_state import I18nState

# В компоненте
I18nState.set_language('ru')
I18nState.switch_to_english()
I18nState.switch_to_russian()
```

## Як Користовать

### В Python (Контроллеры, Сервисы)

```python
from app.arkham.i18n.manager import i18n

def process_knowledge():
    title = i18n.get('knowledge.title', 'pages')
    add_button_label = i18n.get('knowledge.add_new', 'pages')
    error_msg = i18n.get('network_error', 'errors')
    return title, add_button_label, error_msg
```

### В UI Компонентах (Reflex)

```python
import reflex as rx
from app.arkham.i18n.manager import i18n
from app.arkham.state.i18n_state import I18nState

def knowledge_page():
    return rx.vstack(
        rx.heading(i18n.get('knowledge.title', 'pages')),
        rx.button(
            i18n.get('knowledge.add_new', 'pages'),
            on_click=lambda: IssueState.add_knowledge()
        ),
        rx.cond(
            IssueState.knowledge_items,
            rx.foreach(IssueState.knowledge_items, _render_item),
            rx.text(i18n.get('knowledge.empty', 'pages'))
        )
    )

def _render_item(item):
    return rx.box(
        rx.heading(item['title'], size='md'),
        rx.text(item['description']),
        rx.hstack(
            rx.button(
                i18n.get('edit', 'common'),
                on_click=lambda: IssueState.edit(item['id'])
            ),
            rx.button(
                i18n.get('delete', 'common'),
                on_click=lambda: IssueState.delete(item['id']),
                color_scheme='red'
            )
        )
    )
```

## Переключатель Языка

### На UI

```python
import reflex as rx
from app.arkham.state.i18n_state import I18nState

def language_switcher():
    return rx.hstack(
        rx.button(
            "🇧🇺 EN",
            on_click=I18nState.switch_to_english,
            size="sm",
            color_scheme="blue"
        ),
        rx.button(
            "🇦🇸 RU",
            on_click=I18nState.switch_to_russian,
            size="sm",
            color_scheme="red"
        ),
        spacing="1"
    )
```

## Прототипирование

### Добавление Нового Перевода

1. Открыть добычо касающийся JSON файл (e.g., `app/arkham/locales/ru/common.json`)
2. Добавить ключ и значение:
   ```json
   {
     "new_key": "Переводенная строка"
   }
   ```
3. Добавить такоже на английский вариант (`app/arkham/locales/en/common.json`)

### Протестировать

```python
# В Python
from app.arkham.i18n.manager import i18n

# Пытаясь русский
text_ru = i18n.get('new_key', 'common')
print(f"Russian: {text_ru}")  # Ответ: Russian: Переводенная строка

# Переключить на английский
i18n.set_language('en')
text_en = i18n.get('new_key', 'common')
print(f"English: {text_en}")
```

## Метрики

- **Поддерживаемые языки:** 2 (русский, английский)
- **JSON файлы:** 5 на язык (10 всего)
- **Переводов:** 200+
- **Намеспества:** common, pages, components, errors, validations
- **Проглубина ключей:** Несколько уровней (e.g., `entities.types.PERSON`)

## Продвинутые Опции

### Динамические Очистяющие Элементы

```python
from string import Template

error_msg = i18n.get('too_long', 'validations')
# Вывед: "Максимум {max} символов"

formatted = error_msg.format(max=100)
# Вывед: "Максимум 100 символов"
```

### Дебагинг

```python
# Отображение всех переводов намеспества
all_pages = i18n.get_all('pages')
for key, value in all_pages.items():
    print(f"{key}: {value}")

# Проверка текущего языка
print(f"Current language: {i18n.get_current_language()}")

# Проверка поддерживаемых языков
print(f"Supported: {i18n.get_supported_languages()}")
```

## Вынос

Все необходимые компоненты для локализации уже реализованы. Остается обновить исходящие компоненты для использования i18n системы.

---

**Начало:** January 15, 2026  
**Версия:** 1.0
