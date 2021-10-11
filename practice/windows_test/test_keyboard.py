from pykeyboard import *

if __name__ == '__main__':
    print('start')
    k = PyKeyboard()
    k.type_string('123456');
    k.press_keys([k.alt_key, 'q'])
    print('exit')