import logging
"""Легко настроить вывод всех необходимых сообщений, но важно понимать, что сообщения сортируются по срочности, 
начиная от нижнего уровня к верхнему. «Debug» — это диагностические сообщения о работе программы, «info» — важная 
информация, «warning» — предупреждения о потенциальных проблемах, «error» — конкретные ошибки, а «critical» — ситуации,
 которые могут привести к сбоям в работе программы."""


def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    try: # пробуем выполнить код
        a / b
        logging.info(f"Normalnoe dilenie {a} / {b}")
        return a / b

    except: # в случаее если есть ошибка
        logging.error(f"Dilenie na 0 zaprecheno" , exc_info=True)
        return 0

def square(a):
    try:
        a**2
        logging.info(f"Normalnoe dilenie {a}")
        return a**2
    except:
        logging.error(f" a < 0 " , exc_info=True)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filemode="w", filename="calc.log", format="%(asctime)s | %(levelname)s |"
                                                                                      " %(message)s")
    # level с какого уровня мы принимаем сообщение

    print(divide(1, 2))
    print(divide(3, 0))
    print(square(2))
    print(square(-2))

    # logging.debug("gf")  # « Debug » — это диагностические сообщения о работе программы
    # logging.info("j") # « info » — важная информация,
    # logging.warning("f")  # «warning» - предупреждения о потенциальных проблемах
    # logging.error("g") # «error» — конкретные ошибки
    # logging.critical("c") # «critical» — ситуации, которые могут привести к сбоям в работе программы.
