import logging

logging.basicConfig(
    level = logging.ERROR,
    format ='[%(asctime)s-%(levelname)s]%(message)s',
    datefmt = '%y-%m-%d %H:%M',
    filename = 'a.txt',
    filemode = 'a')

if __name__ == '__main__':
    logging.error('ggg')
    print('exit')
    input()
    