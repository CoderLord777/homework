import logging
import unittest
from rt_with_exceptions import Runner


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            runner_test = Runner('Bolt', -10)
            for _ in range(10):
                runner_test.walk()
            self.assertEqual(runner_test.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning('Неверная скорость для Runner ', exc_info=True)

    def test_run(self):
        try:
            runner_test1 = Runner(['Бегун Василий'], 10)
            for _ in range(10):
                runner_test1.run()
            self.assertEqual(runner_test1.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

    def test_challenge(self):
        runner_test2 = Runner('Bolt')
        runner_test3 = Runner('Useyn')
        for _ in range(10):
            runner_test2.run()
            runner_test3.walk()
        self.assertNotEqual(runner_test2.distance, runner_test3.distance)


logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='utf-8',
                    format="%(asctime)s | %(levelname)s | %(message)s")
if __name__ == '__main__':
    unittest.main()
