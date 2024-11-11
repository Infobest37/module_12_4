import unittest
import logging
from Running import Runner

# Настраиваем логирование сразу после импортов
logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log", encoding="UTF-8",
                    format="%(asctime)s | %(levelname)s | %(message)s")

class RunnerTest(unittest.TestCase):

    def setUp(cls):
        print('setUp')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def test_walk(self):
        try:
            runner = Runner('walk', -5)  # Передаём отрицательное значение для проверки логирования
            for _ in range(10):
                runner.walk()
            logging.info("test_walk выполнен успешно")
        except ValueError as e:
            logging.warning(f"WARNING с сообщением Неверная скорость для Runner: {e}")

    def test_run(self):
        try:
            runner = Runner("run", 5)
            for _ in range(10):
                runner.run()
            logging.info('"test_run" выполнен успешно')
        except Exception as e:
            logging.warning(f"Неверный тип данных для объекта Runner: {e}", exc_info=True)

    def test_challenge(self):
        runner1 = Runner('challenge', 5)
        runner2 = Runner('challenge2', 10)
        for _ in range(10):
            runner1.walk()
        for _ in range(10):
            runner2.run()
        self.assertNotEqual(runner2.distance, runner1.distance)
        logging.info('"test_challenge" выполнен успешно')

if __name__ == '__main__':
    # Здесь можно добавить запуск тестов, чтобы запускались логи
    unittest.main()
