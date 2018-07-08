import openpyxl
import pyperclip
from os import chdir
import datetime
import schedule
import win32com.client as win32


def Emailer():
    # Copy and format data from Excel Sheet
    #chdir('/users/ryanhsu/desktop')   # change to match icap's working dir
    chdir('C:\\Users\\Hyori\\Desktop')
    wb = openpyxl.load_workbook('RTD_Tutorial.xlsx')
    sheet = wb['Sheet1']            # change to match RTD sheet's name
    snapshot = ''
    for cell in sheet['A1':'D13']:   # change to match RTD sheet's data area
        for data in cell:
            snapshot += data.value
    pyperclip.copy(snapshot)
    
    # Paste data into Outlook email and send to distribution list in BCC
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.BCC = 'ryanyc@gmail.com' # Change to BCC list
    mail.Subject = 'Market Update'
    mail.HtmlBody = pyperclip.paste()
    mail.send

    # Set up periodic email timer
    currentTime = datetime.datetime.now().time()
    if currentTime.hour >= 7 and currentTime.hour < 18:
        schedule.every(15).minutes.do(Emailer)
    else:
        schedule.every(25).minutes.do(Emailer)
        

#TODO: Add a GUI
