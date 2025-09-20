FROM python:3.11-slim-bullseye

# Install Chrome from official repo
RUN apt-get update && \
    apt-get install -y wget gnupg2 && \
    wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && \
    apt-get install -y google-chrome-stable && \
    rm -rf /var/lib/apt/lists/*

# Install ChromeDriver from apt (simplest way)
RUN apt-get update && \
    apt-get install -y chromedriver && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

CMD ["pytest", "-v", "--alluredir=allure-results"]

#FROM python:3.11-bullseye
#
## Устанавливаем Java (для Allure) + Chrome
#RUN apt-get update && \
#    apt-get install -y --no-install-recommends \
#    wget \
#    gnupg2 \
#    unzip \
#    # ← ДОБАВЛЯЕМ Java
#    openjdk-17-jre && \
#    # Устанавливаем Chrome (твой существующий код)
#    wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
#    sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' && \
#    apt-get update && \
#    apt-get install -y --no-install-recommends google-chrome-stable && \
#    apt-get purge --auto-remove -y && \
#    rm -rf /var/lib/apt/lists/*
#
## Устанавливаем ChromeDriver (твой существующий код)
#RUN CHROME_MAJOR_VERSION=$(google-chrome --version | sed -E 's/.* ([0-9]+)\.[0-9]+\.[0-9]+.*/\1/') && \
#    CHROMEDRIVER_VERSION=$(wget -q -O - "https://googlechromelabs.github.io/chrome-for-testing/LATEST_RELEASE_${CHROME_MAJOR_VERSION}") && \
#    wget -q -O /tmp/chromedriver.zip "https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/${CHROMEDRIVER_VERSION}/linux64/chromedriver-linux64.zip" && \
#    unzip /tmp/chromedriver.zip -d /usr/local/bin/ && \
#    mv /usr/local/bin/chromedriver-linux64/chromedriver /usr/local/bin/ && \
#    rm -rf /tmp/chromedriver.zip /usr/local/bin/chromedriver-linux64 && \
#    chmod +x /usr/local/bin/chromedriver
#
## Устанавливаем Allure CLI
#RUN wget https://github.com/allure-framework/allure2/releases/download/2.27.0/allure-2.27.0.tgz && \
#    tar -zxvf allure-2.27.0.tgz -C /opt/ && \
#    ln -s /opt/allure-2.27.0/bin/allure /usr/bin/allure && \
#    rm allure-2.27.0.tgz
#
#WORKDIR /app
#COPY requirements.txt .
#RUN pip install --no-cache-dir -r requirements.txt
#COPY . .
#
## Запускаем тесты И сервер Allure сразу
#CMD ["sh", "-c", "pytest -v --alluredir=allure-results && allure serve allure-results -h 0.0.0.0 -p 8800"]