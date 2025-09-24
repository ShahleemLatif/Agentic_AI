import gradio as gr
from accounts import Account, get_share_price

# Create an instance of the Account class for the user with user_id 1
user_account = Account(user_id=1)

def create_account(initial_deposit):
    try:
        user_account.deposit_funds(initial_deposit)
        return f"Account created with initial deposit of ${initial_deposit}."
    except ValueError as e:
        return str(e)

def deposit_funds(amount):
    try:
        user_account.deposit_funds(amount)
        return f"Deposited ${amount} successfully."
    except ValueError as e:
        return str(e)

def withdraw_funds(amount):
    try:
        user_account.withdraw_funds(amount)
        return f"Withdrew ${amount} successfully."
    except ValueError as e:
        return str(e)

def buy_shares(symbol, quantity):
    try:
        quantity = int(quantity)
        user_account.buy_shares(symbol, quantity)
        return f"Bought {quantity} shares of {symbol}."
    except ValueError as e:
        return str(e)

def sell_shares(symbol, quantity):
    try:
        quantity = int(quantity)
        user_account.sell_shares(symbol, quantity)
        return f"Sold {quantity} shares of {symbol}."
    except ValueError as e:
        return str(e)

def calculate_portfolio_value():
    return f"Total portfolio value: ${user_account.calculate_portfolio_value()}"

def calculate_profit_loss():
    return f"Profit/Loss: ${user_account.calculate_profit_loss()}"

def report_holdings():
    holdings = user_account.report_holdings()
    return f"Holdings: {holdings}"

def list_transactions():
    transactions = user_account.list_transactions()
    return f"Transactions: {transactions}"

with gr.Blocks() as demo:
    gr.Markdown("## Trading Simulation Platform")
    
    with gr.Row():
        initial_deposit = gr.Number(label="Initial Deposit", value=0.0)
        create_account_btn = gr.Button("Create Account")
        create_account_output = gr.Textbox(label="Output")

    with gr.Row():
        amount = gr.Number(label="Amount", value=0.0)
        deposit_btn = gr.Button("Deposit Funds")
        deposit_output = gr.Textbox(label="Output")

        withdraw_btn = gr.Button("Withdraw Funds")
        withdraw_output = gr.Textbox(label="Output")

    with gr.Row():
        symbol = gr.Dropdown(choices=["AAPL", "TSLA", "GOOGL"], label="Symbol")
        quantity = gr.Number(label="Quantity", value=0)

    with gr.Row():
        buy_btn = gr.Button("Buy Shares")
        buy_output = gr.Textbox(label="Output")

        sell_btn = gr.Button("Sell Shares")
        sell_output = gr.Textbox(label="Output")

    with gr.Row():
        calculate_portfolio_btn = gr.Button("Calculate Portfolio Value")
        portfolio_output = gr.Textbox(label="Output")
        
        calculate_profit_btn = gr.Button("Calculate Profit/Loss")
        profit_output = gr.Textbox(label="Output")

    with gr.Row():
        holdings_btn = gr.Button("Report Holdings")
        holdings_output = gr.Textbox(label="Output")

        transactions_btn = gr.Button("List Transactions")
        transactions_output = gr.Textbox(label="Output")
    
    create_account_btn.click(create_account, inputs=initial_deposit, outputs=create_account_output)
    deposit_btn.click(deposit_funds, inputs=amount, outputs=deposit_output)
    withdraw_btn.click(withdraw_funds, inputs=amount, outputs=withdraw_output)
    
    buy_btn.click(buy_shares, inputs=[symbol, quantity], outputs=buy_output)
    sell_btn.click(sell_shares, inputs=[symbol, quantity], outputs=sell_output)
    
    calculate_portfolio_btn.click(calculate_portfolio_value, outputs=portfolio_output)
    calculate_profit_btn.click(calculate_profit_loss, outputs=profit_output)
    
    holdings_btn.click(report_holdings, outputs=holdings_output)
    transactions_btn.click(list_transactions, outputs=transactions_output)

if __name__ == "__main__":
    demo.launch()