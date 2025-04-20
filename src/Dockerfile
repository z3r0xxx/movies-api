# Используем официальный образ Python в качестве базового
FROM python:3.9-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файлы проекта в контейнер
COPY . /app/

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Открываем порт 8000 для FastAPI
EXPOSE 8000

# Запускаем сервер Uvicorn с параметрами для продакшн-режима
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
