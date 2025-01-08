import unittest
from runner import Runner

def is_frozen(val)->bool:
    def decorator(cls):
        if val:
            for attr_name in dir(cls):
                if attr_name.startswith('test_'):
                    attr = getattr(cls, attr_name)
                    setattr(cls, attr_name, unittest.skip('Тесты в этом кейсе заморожены')(attr))
        return cls
    return decorator

@is_frozen(False)
class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner_test = Runner('Bolt')
        for _ in range(10):
            runner_test.walk()
        self.assertEqual(runner_test.distance, 50)

    def test_run(self):
        runner_test1 = Runner('Useyn')
        for _ in range(10):
            runner_test1.run()
        self.assertEqual(runner_test1.distance, 100)

    def test_challenge(self):
        runner_test2 = Runner('Bolt')
        runner_test3 = Runner('Useyn')
        for _ in range(10):
            runner_test2.run()
            runner_test3.walk()
        self.assertNotEqual(runner_test2.distance, runner_test3.distance)


if __name__ == '__main__':
    unittest.main()
