# Jenkins UI Tests

Учебный проект по автоматизации UI-тестов Jenkins.

## Описание

Проект создан для изучения:

- Python
- Selenium
- Pytest
- Page Object Model (POM)
- Git
- GitLab
- CI/CD

В качестве тестируемого приложения используется Jenkins.

---

## Стек

- Python 3.13
- Selenium
- Pytest
- python-dotenv

---

## Структура проекта

```text
jenkins-ui-tests/

├── pages/
│   └── login_page.py
│
├── tests/
│   └── test_login_page.py
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .env
├── .env.example
└── README.md
```

---

## Установка

Создать виртуальное окружение:

```bash
python -m venv .venv
```

Активировать:

```bash
.venv\Scripts\activate
```

Установить зависимости:

```bash
pip install -r requirements.txt
```

---

## Настройка окружения

Создать файл:

```env
.env
```

Пример:

```env
JENKINS_URL=http://localhost:8080
JENKINS_USER=admin
JENKINS_PASSWORD=admin
```

---

## Запуск тестов

```bash
pytest
```

Запуск подробного отчета:

```bash
pytest -v
```

---

## Реализовано

- [x] Page Object Model
- [x] Работа через .env
- [x] Pytest fixtures
- [ ] GitLab CI/CD
- [ ] Docker
- [ ] Allure Report