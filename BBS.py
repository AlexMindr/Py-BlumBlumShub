import os
import random
import sympy
import PySimpleGUI as sg

file_path = r"./output.bin"


def convert_bytes(num):
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0


def file_size(filep):
    if os.path.isfile(filep):
        file_info = os.stat(filep)
        return file_info.st_size


def initializeaza_random():
    x0 = random.randint(10 ** 2, 10 ** 10)
    p = random.randint(10 ** 12, 10 ** 12 * 9)
    q = random.randint(10 ** 12, 10 ** 12 * 9)

    while p % 4 != 3:
        p = sympy.nextprime(p)
    while q % 4 != 3:
        q = sympy.nextprime(q)

    n = p * q

    if p == q:
        initializeaza_random()
    else:
        return n, x0


def BlumBlumShub(size_mb=0.02):
    n, x0 = initializeaza_random()
    size_convertit = 1048576 * size_mb
    x = x0
    fout = open("output.bin", "wb")
    while file_size(file_path) <= size_convertit:
        x = x ** 2 % n
        b = x % 2
        b = bin(b)
        fout.write(str.encode(b))
    fout.close()

    print("Fisierul generat are " + convert_bytes(file_size(file_path)))


def Generator():
    interface = sg.Window('Generator Blum-Blum-Shub').Layout(
        [[sg.Text('Introduceti dimensiunea fisierului care urmeaza a fi generat in MB')],
         [sg.Input(), sg.Text(), sg.Text("MB")], [sg.OK(), sg.Cancel()], [sg.Text('Fisierul output: output.bin')]])

    event, values = interface.Read()
    if event != 'Cancel':
        try:
            BlumBlumShub(float(values[0]))
        except ValueError as e:
            print(e)
            exit()

    interface.Close()


if __name__ == '__main__':
    Generator()
