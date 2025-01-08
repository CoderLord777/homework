import unittest
import module_12_2
import module_12_1

test_runner = unittest.TestSuite()
test_runner.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_1.RunnerTest))
test_runner.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(test_runner)