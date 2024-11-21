def custom_write(file_name, strings):
    strings_positions = {}
    with open(file_name, 'w', encoding='utf-8') as file:
        byte_offset = 0
        for i, string in enumerate(strings, start=1):
            file.seek(byte_offset)
            strings_positions[(i, byte_offset)] = string
            file.write(string + '\n')
            byte_offset = file.tell()
    file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]
result = custom_write('test.txt', info)

for elem in result.items():
    print(elem)
