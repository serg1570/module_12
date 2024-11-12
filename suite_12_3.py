import unittest
import tests_12_3

runTS = unittest.TestSuite()
runTS.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
runTS.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

testy_runner = unittest.TextTestRunner(verbosity=2)
testy_runner.run(runTS)