FROM selenium/standalone-chrome:4.21.0

WORKDIR /app

# Копируем только нужные файлы
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY pages/ pages/
COPY tests/ tests/
COPY conftest.py .
COPY pytest.ini .

CMD ["pytest", "-v", "--alluredir=allure-results"]