import unittest

if __name__ == "__main__":
    suite = unittest.TestLoader().discover(start_dir='../', pattern='test_*.py')
    unittest.TextTestRunner(verbosity=2).run(suite)
