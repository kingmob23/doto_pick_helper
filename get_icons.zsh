#!/bin/zsh

# Путь к файлу с ссылками на изображения
input_file="icon_links"

# Проверить, существует ли файл
if [ ! -f "$input_file" ]; then
    echo "Файл с ссылками ($input_file) не найден."
    exit 1
fi

# Создать папку "icons" (если не существует)
mkdir -p icons

# Чтение массива ссылок из файла и скачивание изображений
while IFS= read -r url; do
    # Извлечь имя героя из URL
    hero_name=$(basename "$url" | sed 's/.*\///; s/-.*\(\.jpg\)/\1/')

    # Собрать имя файла
    filename="icons/$hero_name"

    # Скачать изображение с помощью wget
    wget "$url" -O "$filename"

    # Проверить статус выполнения wget
    if [ $? -eq 0 ]; then
        echo "Скачано: $filename"
    else
        echo "Ошибка при скачивании: $filename"
    fi
done <"$input_file"
