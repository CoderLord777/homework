import unittest
from runner_and_tournament import Tournament, Runner


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner('Усейн', 10)
        self.runner2 = Runner('Андрей', 9)
        self.runner3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for _, res in cls.all_results.items():
            print(res)

    def test_tournament_1(self):
        test = Tournament(90, self.runner1, self.runner3)
        results = test.start()
        self.__class__.all_results[1] = {place: runner.name for place, runner in results.items()}
        last_place = max(results.keys())
        self.assertTrue(results[last_place].name == 'Ник')

    def test_tournament_2(self):
        test = Tournament(90, self.runner2, self.runner3)
        results = test.start()
        self.__class__.all_results[2] = {place: runner.name for place, runner in results.items()}
        last_place = max(results.keys())
        self.assertTrue(results[last_place].name == 'Ник')

    def test_tournament_3(self):
        test = Tournament(90, self.runner1, self.runner2, self.runner3)
        results = test.start()
        self.__class__.all_results[3] = {place: runner.name for place, runner in results.items()}
        last_place = max(results.keys())
        self.assertTrue(results[last_place].name == 'Ник')


if __name__ == '__main__':
    unittest.main()
