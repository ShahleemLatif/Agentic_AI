import unittest

class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account = Account(user_id=1)

    def test_initial_balance(self):
        self.assertEqual(self.account.balance, 0.0)
        
    def test_deposit_funds(self):
        self.account.deposit_funds(100.0)
        self.assertEqual(self.account.balance, 100.0)
        self.assertEqual(self.account.transactions, [{'type': 'deposit', 'amount': 100.0}])
    
    def test_deposit_negative_amount(self):
        with self.assertRaises(ValueError):
            self.account.deposit_funds(-50.0)
        
    def test_withdraw_funds(self):
        self.account.deposit_funds(200.0)
        self.account.withdraw_funds(50.0)
        self.assertEqual(self.account.balance, 150.0)
        self.assertEqual(self.account.transactions, [{'type': 'deposit', 'amount': 200.0}, {'type': 'withdraw', 'amount': 50.0}])
    
    def test_withdraw_negative_amount(self):
        with self.assertRaises(ValueError):
            self.account.withdraw_funds(-30.0)

    def test_withdraw_insufficient_funds(self):
        with self.assertRaises(ValueError):
            self.account.withdraw_funds(10.0)

    def test_buy_shares(self):
        self.account.deposit_funds(1000.0)
        self.account.buy_shares('AAPL', 5)
        self.assertEqual(self.account.holdings, {'AAPL': 5})
        self.assertAlmostEqual(self.account.balance, 250.0)
        self.assertEqual(len(self.account.transactions), 2)

    def test_buy_shares_insufficient_funds(self):
        with self.assertRaises(ValueError):
            self.account.buy_shares('TSLA', 1)

    def test_sell_shares(self):
        self.account.deposit_funds(5000.0)
        self.account.buy_shares('GOOGL', 1)
        self.account.sell_shares('GOOGL', 1)
        self.assertEqual(self.account.holdings, {})
        self.assertAlmostEqual(self.account.balance, 5000.0)
        self.assertEqual(len(self.account.transactions), 3)

    def test_sell_insufficient_shares(self):
        with self.assertRaises(ValueError):
            self.account.sell_shares('AAPL', 3)

    def test_calculate_portfolio_value(self):
        self.account.deposit_funds(1500.0)
        self.account.buy_shares('AAPL', 5)
        expected_value = self.account.calculate_portfolio_value()
        self.assertAlmostEqual(expected_value, 1500.0)

    def test_report_holdings(self):
        self.account.deposit_funds(1000.0)
        self.account.buy_shares('TSLA', 10)
        self.assertEqual(self.account.report_holdings(), {'TSLA': 10})

    def test_report_profit_loss(self):
        self.account.deposit_funds(1500.0)
        self.account.buy_shares('AAPL', 5)
        profit_loss = self.account.report_profit_loss()
        self.assertAlmostEqual(profit_loss, 0.0)

    def test_list_transactions(self):
        self.account.deposit_funds(1000.0)
        self.account.withdraw_funds(500.0)
        transactions = self.account.list_transactions()
        self.assertEqual(len(transactions), 2)
        self.assertEqual(transactions[0]['type'], 'deposit')
        self.assertEqual(transactions[1]['type'], 'withdraw')

if __name__ == '__main__':
    unittest.main()