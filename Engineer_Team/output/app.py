from accounts import Account, get_share_price
import gradio as gr

# Initialize a default account with some initial deposit
account = Account(username="demo_user", initial_deposit=10000)

def create_account(username, initial_deposit):
    global account
    account = Account(username, initial_deposit)
    return f"Account created for {username} with initial deposit of {initial_deposit}"

def deposit(amount):
    account.deposit(amount)
    return f"Deposited {amount}. Current balance: {account.balance}"

def withdraw(amount):
    if account.withdraw(amount):
        return f"Withdrew {amount}. Current balance: {account.balance}"
    return "Insufficient funds for withdrawal."

def buy_shares(symbol, quantity):
    if account.buy_shares(symbol, quantity):
        return f"Purchased {quantity} shares of {symbol}. Current balance: {account.balance}"
    return "Insufficient funds to buy shares."

def sell_shares(symbol, quantity):
    if account.sell_shares(symbol, quantity):
        return f"Sold {quantity} shares of {symbol}. Current balance: {account.balance}"
    return "Not enough shares to sell."

def get_portfolio_value():
    value = account.get_portfolio_value()
    return f"Total Portfolio Value: {value}"

def get_profit_or_loss():
    pnl = account.get_profit_or_loss()
    return f"Profit/Loss: {pnl}"

def get_holdings():
    holdings = account.get_holdings()
    return f"Current Holdings: {holdings}"

def get_transaction_history():
    history = account.get_transaction_history()
    return f"Transactions: {history}"

with gr.Blocks() as demo:
    gr.Markdown("# Trading Simulation Platform")
    
    with gr.Tab("Account"):
        username_input = gr.Textbox(label="Username")
        deposit_input = gr.Number(label="Initial Deposit", value=10000)
        create_btn = gr.Button("Create Account")
        create_output = gr.Textbox(label="Create Account Output")

    with gr.Tab("Transactions"):
        amount_input = gr.Number(label="Amount")
        deposit_btn = gr.Button("Deposit")
        withdraw_btn = gr.Button("Withdraw")
        transaction_output = gr.Textbox(label="Transaction Output")

    with gr.Tab("Shares"):
        symbol_input = gr.Dropdown(choices=["AAPL", "TSLA", "GOOGL"], label="Share Symbol")
        quantity_input = gr.Number(label="Quantity")
        buy_btn = gr.Button("Buy Shares")
        sell_btn = gr.Button("Sell Shares")
        shares_output = gr.Textbox(label="Shares Transaction Output")
        
    with gr.Tab("Reports"):
        portfolio_btn = gr.Button("Get Portfolio Value")
        portfolio_output = gr.Textbox(label="Portfolio Value")
        pnl_btn = gr.Button("Get Profit/Loss")
        pnl_output = gr.Textbox(label="Profit/Loss")
        holdings_btn = gr.Button("Get Holdings")
        holdings_output = gr.Textbox(label="Holdings")
        history_btn = gr.Button("Get Transaction History")
        history_output = gr.Textbox(label="Transaction History")

    create_btn.click(fn=create_account, inputs=[username_input, deposit_input], outputs=create_output)
    deposit_btn.click(fn=deposit, inputs=amount_input, outputs=transaction_output)
    withdraw_btn.click(fn=withdraw, inputs=amount_input, outputs=transaction_output)
    buy_btn.click(fn=buy_shares, inputs=[symbol_input, quantity_input], outputs=shares_output)
    sell_btn.click(fn=sell_shares, inputs=[symbol_input, quantity_input], outputs=shares_output)
    portfolio_btn.click(fn=get_portfolio_value, outputs=portfolio_output)
    pnl_btn.click(fn=get_profit_or_loss, outputs=pnl_output)
    holdings_btn.click(fn=get_holdings, outputs=holdings_output)
    history_btn.click(fn=get_transaction_history, outputs=history_output)

demo.launch()