
class Account:
    def __init__(self, user_id: int) -> None:
        self.user_id = user_id
        self.balance = 0.0
        self.initial_deposit = 0.0
        self.holdings = {}
        self.transactions = []

    def deposit_funds(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError('Deposit amount must be positive.')
        self.balance += amount
        if self.initial_deposit == 0:
            self.initial_deposit += amount
        self.transactions.append({'type': 'deposit', 'amount': amount})

    def withdraw_funds(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError('Withdrawal amount must be positive.')
        if amount > self.balance:
            raise ValueError('Insufficient balance.')
        self.balance -= amount
        self.transactions.append({'type': 'withdraw', 'amount': amount})

    def buy_shares(self, symbol: str, quantity: int) -> None:
        if quantity <= 0:
            raise ValueError('Quantity must be positive.')
        price_per_share = get_share_price(symbol)
        total_price = price_per_share * quantity
        if total_price > self.balance:
            raise ValueError('Insufficient funds to buy shares.')
        self.balance -= total_price
        if symbol in self.holdings:
            self.holdings[symbol] += quantity
        else:
            self.holdings[symbol] = quantity
        self.transactions.append({'type': 'buy', 'symbol': symbol, 'quantity': quantity})

    def sell_shares(self, symbol: str, quantity: int) -> None:
        if quantity <= 0:
            raise ValueError('Quantity must be positive.')
        if symbol not in self.holdings or self.holdings[symbol] < quantity:
            raise ValueError('Insufficient shares to sell.')
        price_per_share = get_share_price(symbol)
        total_value = price_per_share * quantity
        self.balance += total_value
        self.holdings[symbol] -= quantity
        if self.holdings[symbol] == 0:
            del self.holdings[symbol]
        self.transactions.append({'type': 'sell', 'symbol': symbol, 'quantity': quantity})

    def calculate_portfolio_value(self) -> float:
        total_value = self.balance
        for symbol, quantity in self.holdings.items():
            total_value += get_share_price(symbol) * quantity
        return total_value

    def calculate_profit_loss(self) -> float:
        return self.calculate_portfolio_value() - self.initial_deposit

    def report_holdings(self) -> dict:
        return self.holdings.copy()

    def report_profit_loss(self) -> float:
        return self.calculate_profit_loss()

    def list_transactions(self) -> list:
        return self.transactions.copy()

# Mock implementation of `get_share_price` function

def get_share_price(symbol: str) -> float:
    prices = {
        'AAPL': 150.0,
        'TSLA': 800.0,
        'GOOGL': 2750.0
    }
    return prices.get(symbol, 0.0)