"""
Реализовать метод __str__, позволяющий выводить все папки и файлы из данной, например так:
> print(folder1)
V folder1
|-> V folder2
|   |-> V folder3
|   |   |-> file3
|   |-> file2
|-> file1
А так же возможность проверить, находится ли файл или папка в другой папке:
> print(file3 in folder2)
True
"""


class PrintableFolder:
    def __init__(self, name, content):
        self.name = name
        self.content = content

    def __str__(self, count_tabs=0):
        result = ''
        tab = '|    ' * count_tabs
        for inner_object in self.content:
            if isinstance(inner_object, PrintableFolder):
                result = f'{result}\n{tab}|-> {inner_object.__str__(count_tabs+1)}'
            else:
                result = f'{result}\n{tab}|-> {inner_object}'

        return f'V {self.name}{result}'

    def __contains__(self, file):
        values = []
        result = False
        for inner_object in self.content:
            if isinstance(inner_object, PrintableFolder):
                result = file in inner_object
                values.append(inner_object)
            else:
                values.append(inner_object)

        if file in values:
            result = True

        return result


class PrintableFile:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


file3 = PrintableFile('file3')
file4 = PrintableFile('file4')
folder3 = PrintableFolder('folder3', [file3, file4])
file2 = PrintableFile('file2')
folder2 = PrintableFolder('folder2', [folder3, file2])
file1 = PrintableFile('file1')
folder1 = PrintableFolder('folder1', [folder2, file1])

print(folder1)
print(file3 in folder2)