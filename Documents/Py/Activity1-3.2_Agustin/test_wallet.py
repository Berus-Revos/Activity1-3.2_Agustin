import unittest
from unittest.mock import patch
from wallet import Balance

class testWallet(unittest.TestCase):

    def setUp(self):
        self.acc = Balance(name= "Tin", starting_money=0)

    def test_withdrawSuccess(self):
        self.acc.balance = 100
        with patch("builtins.input", return_value="50"):
            self.acc.withdraw()
        self.assertEqual(self.acc.money, 50)
        self.assertEqual(self.acc.balance, 50)
        self.assertEqual(self.acc.stuff_done, 1)

    def test_withdrawFailed(self):
        self.acc.balance = 10
        with patch("builtins.input", return_value="50"):
            self.acc.withdraw()
        self.assertEqual(self.acc.money, 0)
        self.assertEqual(self.acc.balance, 10)
        self.assertEqual(self.acc.stuff_done, 0)

if __name__ == "__main__":
    unittest.main()