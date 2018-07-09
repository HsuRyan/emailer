import schedule
import win32com.client as win32
import pandas as pd
import time

from config import *
import logging

def create_dataframe(file_location, file_name, sheet_name):
    try:
        df = pd.read_excel(file_location + file_name, sheet_name)
        return df
    except FileNotFoundError:
        logging.error("File or sheet not found + [" + file_location + file_name, sheet_name + "]")

def send_email(BCC, subject, body):
    # Paste data into Outlook email and send to distribution list in BCC
    outlook = win32.Dispatch('outlook.application')
    body = body.to_html()
    mail = outlook.CreateItem(0)
    mail.BCC = BCC # Change to BCC list
    mail.Subject = subject
    mail.HtmlBody = body
    mail.send
    
def market_update_mailer(BCC_email):
    global market_update_file_location
    global market_update_file_name
    global market_update_sheet_name
    global primary_begin_time
    global primary_end_time
    
    market_update = create_dataframe(market_update_file_location, market_update_file_name, market_update_sheet_name)
    send_email(BCC_email, market_update_subject, market_update)