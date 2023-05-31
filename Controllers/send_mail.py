import smtplib
from email.message import EmailMessage
import pandas as pd

def sendmail():
    with open('senha.txt') as f:
        senha = f.readlines()
        f.close()
    senha_do_email = senha[0]

    df = pd.read_csv('destinatarios.csv', sep= ',')
    df = df.loc[0:(len(df)), 'destinatarios']
    destinatarios  = []
    for i in df:
        destinatarios.append(i)
        
    email = ''
    msg = EmailMessage()
    msg['Subject']  = ''
    msg['From'] = ''
    msg['To'] = destinatarios
    msg.set_content("Segue o relatório diário")

    with open('Relatorio_diario.pdf', 'rb') as content_file:
        content = content_file.read()
        msg.add_attachment(content, maintype='application', subtype='pdf', filename='Relatorio_diario.pdf')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:     
        smtp.login(email, senha_do_email)
        smtp.send_message(msg)
