import yfinance as yf
import pandas as pd
from datetime import datetime
from datetime import timedelta
import mplcyberpunk
import matplotlib.pyplot as plt
from bcb import currency
import dataframe_image as dfi

def variations():
    start_dia = datetime.now()
    start_dia = start_dia - timedelta(days= 7)
    start_dia = datetime.strftime(start_dia, '%Y-%m-%d')
    
    sp500 = yf.download('^GSPC', start= start_dia)['Adj Close']

    df_sp500 = pd.DataFrame(sp500)
    df_sp500.to_csv('s&p500.csv', index= True)

    df_sp500 = pd.read_csv('s&p500.csv', sep = ',')
    df_sp500 ['Indice'] = df_sp500 ['Adj Close']
    df_sp500 = df_sp500 [['Date','Indice']]

    close_sp500 = df_sp500.loc[len(sp500) -1,['Indice']]
    close_sp500 = float(close_sp500)
    variation_sp500 = df_sp500.loc[len(sp500) -1,['Indice']] - df_sp500.loc[len(sp500) -2,['Indice']] 
    variation_sp500 = float(variation_sp500)
    variation_sp500 = variation_sp500 / close_sp500
    variation_sp500 = "{:.2%}".format(variation_sp500)

    plt.style.use("cyberpunk")
    df_sp500.plot(kind= 'line',
    x = 'Date',
    y = 'Indice', grid = False)
    plt.savefig('sp500.png', dpi= 300)

    ibov = yf.download('^BVSP', start= start_dia)['Adj Close']

    df_ibov = pd.DataFrame(ibov)
    df_ibov.to_csv('ibovespa.csv', index= True)
    df_ibov = pd.read_csv('ibovespa.csv', sep = ',')
    df_ibov ['Indice'] = df_ibov ['Adj Close']
    df_ibov = df_ibov [['Date','Indice']]

    close_ibov = df_ibov.loc[len(ibov) -1, ['Indice']]
    close_ibov = float(close_ibov)
    variation_ibov = df_ibov.loc[len(ibov) -1, ['Indice']] - df_ibov.loc[len(ibov) -2, ['Indice']] 
    variation_ibov = float(variation_ibov)
    variation_ibov = variation_ibov / close_ibov
    variation_ibov = "{:.2%}".format(variation_ibov)

    plt.style.use("cyberpunk")
    df_ibov.plot(kind='line',
    x= 'Date',
    y= 'Indice', grid= False)
    plt.savefig('ibovespa.png', dpi= 300)

    list_stocks = ['ITUB4.SA', 'ITSA4.SA', 'BBDC4.SA', 'BBAS3.SA', 'MGLU3.SA', 'B3SA3.SA']
    stocks = yf.download(list_stocks, start= start_dia)['Adj Close']

    def formatar(data):
        return "{:.2f}".format(data)
    
    df_stocks = pd.DataFrame(stocks)
    df_stocks.to_csv('stocks.csv', index= True)
    df_stocks = pd.read_csv('stocks.csv', sep = ',')
    
    df_stocks['B3SA3.SA'] = df_stocks['B3SA3.SA'].apply(formatar)
    df_stocks['BBAS3.SA'] = df_stocks['BBAS3.SA'].apply(formatar)
    df_stocks['BBDC4.SA'] = df_stocks['BBDC4.SA'].apply(formatar)
    df_stocks['ITSA4.SA'] = df_stocks['ITSA4.SA'].apply(formatar)
    df_stocks['ITUB4.SA'] = df_stocks['ITUB4.SA'].apply(formatar)
    df_stocks['MGLU3.SA'] = df_stocks['MGLU3.SA'].apply(formatar)

    df_styled = df_stocks.style.background_gradient()
    dfi.export(df_styled,"table_stocks.png")
 
    hoje = datetime.today().strftime('%Y-%m-%d')
    df = currency.get(['USD', 'EUR'],
                    start='2010-01-01',
                    end= hoje,
                    side='ask')

    plt.style.use("cyberpunk")
    df.plot(figsize=(12, 6,))
    plt.savefig('cambio.png', dpi = 300)
    
    df.to_csv('cambio.csv', index = True)
    cambio = pd.read_csv('cambio.csv', sep= ',')

    current_index = len(cambio.index) - 1
    previous_index = current_index - 1
    
    cambio_usd = cambio.loc[current_index, ['USD']]
    cambio_usd = float(cambio_usd)
    variation_usd = cambio.loc[current_index, ['USD']] - cambio.loc[previous_index, ['USD']]
    variation_usd = float(variation_usd)
    variation_usd = variation_usd / cambio_usd
    variation_usd = "{:.2%}".format(variation_usd)

    list_variation = [variation_ibov, variation_sp500, variation_usd]
    list_name = ['Ibovespa', 'S&P 500', 'Dolar']
    df_variation = pd.DataFrame(list_variation, columns= ['Variação'])
    df_index = pd.DataFrame(list_name, columns= ['Indice'])
    df_variation.to_csv('df_variations.csv', index = True)
    df_index.to_csv('df_indice.csv', index = True)
    df_variation = pd.read_csv('df_variations.csv', sep = ',')
    df_index = pd.read_csv('df_indice.csv', sep = ',')
    df_compiled_variation = pd.merge(df_index, df_variation)
    df_compiled_variation = df_compiled_variation [['Indice', 'Variação']]

    df_styled = df_compiled_variation.style.background_gradient()
    dfi.export(df_styled,"table_indices.png")