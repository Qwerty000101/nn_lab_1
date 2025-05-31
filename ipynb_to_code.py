import json

def ipynb_to_py(ipynb_path, output_py_path):
    """
    Конвертирует Jupyter Notebook (.ipynb) в Python-скрипт (.py),
    добавляя:
    1. Текст из markdown-ячеек в виде многострочных комментариев (''')
    2. Нумерацию ячеек с кодом (например, # Ячейка 1)
    
    Параметры:
    - ipynb_path (str): Путь к исходному .ipynb файлу.
    - output_py_path (str): Путь к выходному .py файлу.
    """
    with open(ipynb_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    with open(output_py_path, 'w', encoding='utf-8') as f_out:
        cell_number = 1
        for cell in notebook['cells']:
            if cell['cell_type'] == 'markdown':
                # Записываем markdown-ячейку как многострочный комментарий
                f_out.write('"""\n')
                for line in cell['source']:
                    f_out.write(line)
                f_out.write('\n"""\n\n')
            
            elif cell['cell_type'] == 'code':
                # Добавляем комментарий с номером ячейки
                f_out.write(f'# Ячейка {cell_number}\n')
                
                # Записываем код из ячейки
                for line in cell['source']:
                    f_out.write(line)
                f_out.write('\n\n')  # Добавляем пустую строку для читаемости
                
                cell_number += 1

if __name__ == '__main__':
    input_file = 'notebook.ipynb'  # Укажите путь к вашему .ipynb файлу
    output_file = 'output.py'       # Укажите путь к выходному .py файлу
    
    ipynb_to_py(input_file, output_file)
    print(f'Файл {input_file} успешно преобразован в {output_file}')