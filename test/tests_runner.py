import unittest
# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.



if __name__ == "__main__":
    suite = unittest.TestLoader().discover(start_dir='../', pattern='test_*.py')
    unittest.TextTestRunner(verbosity=2).run(suite)