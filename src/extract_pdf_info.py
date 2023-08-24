import pdfplumber


def parse_pdf_data(pdf_file_path):
    pdf_data = {}

    try:
        # Открываем PDF-файл с помощью библиотеки pdfplumber
        with pdfplumber.open(pdf_file_path) as pdf:
            # Извлекаем текст с первой страницы
            first_page = pdf.pages[0]
            lines = first_page.extract_text().split('\n')

            current_key = None
            current_value = ""

            # Обрабатываем каждую строку текста
            for line in lines:
                line = line.strip()

                # Если строка пустая, пропускаем её
                if not line:
                    continue

                # Ищем разделитель ":" и пытаемся разделить строку на ключ и значение
                parts = line.split(":")

                if len(parts) > 1:
                    key = parts[0].strip()
                    value = ":".join(parts[1:]).strip()

                    # Если текущий ключ уже существует, сохраняем его значение
                    if current_key:
                        pdf_data[current_key] = current_value.strip()

                    current_key = key
                    current_value = value
                elif current_key is not None:
                    # Если строка не содержит ":", добавляем её к текущему значению
                    current_value += ' ' + line

            # Если есть последний ключ и значение, сохраняем их
            if current_key:
                pdf_data[current_key] = current_value.strip()

        # Разделяем значения словаря по пробелам и создаем новые пары ключ-значение
        new_pdf_data = {}
        for key, value in pdf_data.items():
            parts = value.split()
            new_pdf_data[key] = parts[0]
            for i in range(1, len(parts), 2):
                new_pdf_data[parts[i]] = parts[i + 1]

        pdf_data = new_pdf_data

    except Exception as e:
        # В случае ошибки сохраняем её в словаре
        pdf_data['Ошибка'] = str(e)

    return pdf_data


if __name__ == "__main__":
    input_pdf_file_path = '../data/test_task.pdf'  # Укажите путь к вашему PDF-файлу
    info = parse_pdf_data(input_pdf_file_path)
    print(info)
