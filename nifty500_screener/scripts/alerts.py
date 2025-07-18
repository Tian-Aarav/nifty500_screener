import smtplib
from email.mime.text import MIMEText

def send_buy_alerts(stocks):
    buys = [s for s in stocks if s['Signal'] == 'BUY']
    if not buys:
        return

    message = "Buy Alerts:\n\n"
    for stock in buys:
        message += f"{stock['Symbol']} - Close: {stock['Close']} - Score: {stock['Score']}\n"

    msg = MIMEText(message)
    msg['Subject'] = "Daily Nifty 500 Buy Alerts"
    msg['From'] = "your_email@gmail.com"
    msg['To'] = "your_email@gmail.com"

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login("your_email@gmail.com", "your_app_password")
            server.send_message(msg)
        print("Email alerts sent.")
    except Exception as e:
        print(f"Failed to send email: {e}")