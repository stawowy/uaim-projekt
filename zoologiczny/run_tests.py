import unittest

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.defaultTestLoader.discover(start_dir='tests', pattern='test*.py')

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
