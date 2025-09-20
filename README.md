# Мой первый готовый проект по автотестированию

Это мой первый проект автотестирования с Docker и Allure!

## 📦 Что внутри?
- Selenium WebDriver
- Page Object Pattern
- Docker контейнеризация
- Allure отчеты
- GitHub Actions CI/CD

#️ Как запустить?

### Локально:
```bash
# Собрать Docker образ
docker build -t my-autotests .

# Запустить тесты
docker run -p 8800:8800 my-autotests
