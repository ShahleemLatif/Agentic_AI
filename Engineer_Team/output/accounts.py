class Account:
    def __init__(self, username, initial_deposit):
        self.username = username
        self.balance = initial_deposit
        self.transactions = []
        self.holdings = {}
        self.initial_deposit = initial_deposit

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append({'type': 'deposit', 'amount': amount})

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append({'type': 'withdrawal', 'amount': amount})
            return True
        return False

    def buy_shares(self, symbol, quantity):
        price = get_share_price(symbol)
        cost = price * quantity
        if cost <= self.balance:
            self.balance -= cost
            self.holdings[symbol] = self.holdings.get(symbol, 0) + quantity
            self.transactions.append({'type': 'buy', 'symbol': symbol, 'quantity': quantity, 'price': price})
            return True
        return False

    def sell_shares(self, symbol, quantity):
        if symbol in self.holdings and self.holdings[symbol] >= quantity:
            price = get_share_price(symbol)
            revenue = price * quantity
            self.balance += revenue
            self.holdings[symbol] -= quantity
            if self.holdings[symbol] == 0:
                del self.holdings[symbol]
            self.transactions.append({'type': 'sell', 'symbol': symbol, 'quantity': quantity, 'price': price})
            return True
        return False

    def get_portfolio_value(self):
        total = self.balance
        for symbol, quantity in self.holdings.items():
            price = get_share_price(symbol)
            total += price * quantity
        return total

    def get_profit_or_loss(self):
        return self.get_portfolio_value() - self.initial_deposit

    def get_holdings(self):
        return self.holdings

    def get_transaction_history(self):
        return self.transactions

# Sample test get_share_price function
def get_share_price(symbol):
    prices = {
        'AAPL': 150.0,
        'TSLA': 750.0,
        'GOOGL': 2800.0
    }
    return prices.get(symbol, 0.0)