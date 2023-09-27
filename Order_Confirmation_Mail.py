import smtplib
from email.message import EmailMessage


def order_confirmation_email(email_addr,user_name,total_cost,rest_choice):
    HOST = "smtp.gmail.com"
    PORT = 587

    print(email_addr)
    FROM_EMAIL = "testyummyeats@gmail.com"
    TO_EMAIL = email_addr
    PASSWORD = "docpbogmikycxuwe"

    # Create an EmailMessage object
    msg = EmailMessage()

    # Set the sender and recipient
    msg.set_content(f"Yummy_Eats: Hi {user_name}, your Order from {rest_choice} is on the way and total cost is ${total_cost}")
    msg["Subject"] = "Yummy_Eats: Order Confirmation"
    msg["From"] = FROM_EMAIL
    msg["To"] = TO_EMAIL

    smtp = smtplib.SMTP(HOST, PORT)

    status_code, response = smtp.ehlo()
    print(f"[*] Echoing the server: {status_code} {response}")

    status_code, response = smtp.starttls()
    print(f"[*] Starting TLS connection: {status_code} {response}")

    status_code, response = smtp.login(FROM_EMAIL, PASSWORD)
    print(f"[*] Logging in: {status_code} {response}")

    smtp.send_message(msg)
    smtp.quit()