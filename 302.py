#---------------------------------Задача 3: Работа с файлами----------------#
# Реализуйте класс FileManager, представляющий управление файлами.
# Класс должен содержать методы read_file и write_file,
# которые будут читать данные из файла и записывать данные в файл соответственно.
# Создайте собственный класс исключения FileNotFoundError,
# который будет возбуждаться, если файл не может быть найден при чтении или записи.

class FileNotFoundError(Exception):
    pass

class FileManager:
    def read_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                data = file.read()
                return data
        except FileNotFoundError:
            raise FileNotFoundError("File not found")

    def write_file(self, file_path, data):
        try:
            with open(file_path, 'w') as file:
                file.write(data)
        except FileNotFoundError:
            raise FileNotFoundError("File not found")

# Пример использования класса FileManager
file_manager = FileManager()

# Чтение данных из файла
try:
    file_data = file_manager.read_file('test.txt')
    print(file_data)
except FileNotFoundError as e:
    print(e)

# Запись данных в файл
try:
    file_manager.write_file('output.txt', 'Hello, World!')
except FileNotFoundError as e:
    print(e)










