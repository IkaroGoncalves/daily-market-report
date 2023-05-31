from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from datetime import datetime

def daily_report():
    date = datetime.today().strftime('%d-%m-%Y')
    cnv = canvas.Canvas('Relatorio_diario.pdf', pagesize= A4)

    cnv.setFont('Helvetica', 10)
    cnv.drawString(10, 830,'Pagina 1 de 2')
    cnv.setFont('Helvetica-Bold', 12)
    cnv.drawString(150, 800, f'RELATÓRIO FECHAMENTO MERCADO {date}')

    cnv.setFont('Helvetica-Bold', 13)
    cnv.drawString(10, 750, '1 - Ações e Câmbio')
    cnv.setFont('Helvetica', 10)
    cnv.drawString(10, 730, '1.1 Fechamento mercado financeiro:')
    cnv.drawImage('table_indices.png', 10, 630, width= 80, height= 80)
    cnv.setFont('Helvetica', 10)
    cnv.drawString(10, 590, '1.2 - Gráficos:')
    cnv.drawString(140, 560, 'IBOVESPA')
    cnv.drawString(430, 560, 'S&P 500')
    cnv.drawImage('ibovespa.png', 10, 290, width= 285, height= 260)
    cnv.drawImage('sp500.png', 300, 290, width= 285, height= 260)
    cnv.drawString(250, 255, 'EURO \ DOLAR')
    cnv.drawImage('cambio.png', 100, 8, width= 360, height= 240)
    cnv.drawString(250, 255, 'EURO \ DOLAR')

    cnv.showPage()
    
    cnv.setFont('Helvetica', 10)
    cnv.drawString(10, 830,'Pagina 2 de 2')
    cnv.drawString(10, 780, '1. 3 Variação preço ações:')
    cnv.drawImage('table_stocks.png', 10, 560, width= 330, height= 190)
    cnv.setFont('Helvetica-Bold', 13)
    cnv.drawString(10, 510,'2 - Dados econômicos:')
    cnv.setFont('Helvetica', 10)
    cnv.drawString(10, 485,'2.1 Selic')
    cnv.drawImage('selic.png', 10, 265, width= 350, height= 210)
    cnv.drawString(10, 240,'2.2 Inflação')
    cnv.drawImage('inflacao.png', 10, 20, width= 350, height= 210)

    cnv.save()