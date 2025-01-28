# Используем базовый образ
FROM ubuntu:latest

# Устанавливаем необходимые пакеты
RUN apt-get update && apt-get install -y python3

# Копируем файлы приложения в контейнер
COPY . /cell_web

# Устанавливаем рабочую директорию
WORKDIR /cell_web

# Запускаем приложение
CMD ["python3", "app.py"]