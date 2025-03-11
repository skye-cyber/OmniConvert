"""Clear the screen using ctypes in windows and os.system('clear') in unix systems"""
import os
import ctypes


def clear_screen():
    if os.name == 'nt':  # Windows system
        ctypes.windll.kernel32.SetConsoleCursorPosition(
            ctypes.windll.kernel32.GetStdHandle(-11), (0, 0))
        ctypes.windll.kernel32.FillConsoleOutputCharacter(
            ctypes.windll.kernel32.GetStdHandle(-11), b'\x00',
            80*10, (0, 0))
    else:  # Unix/Linux/MacOS systems
        os.system('clear')
