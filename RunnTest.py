import unittest
from Running import Runner

class RunnerTest(unittest.TestCase):

    def setUp(cls):
        print('setUp')
    @classmethod
    def tearDownClass(cls):
        print('setUpClass')

    def test_wallk(self):

        runner = Runner('wallk')
        for _ in range(10):
            runner.walk()
        self.assertEqual(50, runner.distance)
    def test_run(self):
        runner = Runner('run')

        for _ in range(10):
            runner.run()
        self.assertEqual(100, runner.distance)


    def test_challenge(self ):
        runner1 = Runner('challenge')
        runner2 = Runner('challenge2')
        for _ in range(10):
            runner1.walk()
        for _ in range(10):
            runner2.run()
        self.assertNotEqual(runner2.distance, runner1.distance)




