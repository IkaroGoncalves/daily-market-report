from bcb import sgs
import mplcyberpunk
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import matplotlib.dates as mdates
from matplotlib.dates import date2num
from datetime import datetime
from datetime import timedelta

def selic():
    selic = sgs.get({'selic':432}, start = '2003-01-01')
    
    plt.style.use("cyberpunk")
    fig, ax = plt.subplots()

    ax.plot(selic.index, selic['selic'])
    ax.yaxis.set_major_formatter(mtick.PercentFormatter())
    ax.grid(False)
    plt.savefig('selic.png', dpi = 300)

def inflacao():
    hoje = datetime.now()
    um_ano_atras = hoje - timedelta(days = 366)

    inflacao = sgs.get({'ipca': 433,
                'igp-m': 189}, start = um_ano_atras + timedelta(180))

    datas_numericas = date2num(inflacao.index)

    plt.style.use("cyberpunk")
    fig, ax = plt.subplots()

    ax.bar(datas_numericas-7, inflacao['ipca'], label = "IPCA", width=7)
    ax.bar(datas_numericas, inflacao['igp-m'], label = "IGP-M", width=7)

    ax.yaxis.set_major_formatter(mtick.PercentFormatter())
    ax.xaxis_date()
    formato_data = mdates.DateFormatter('%b-%y')
    ax.xaxis.set_major_formatter(formato_data)
    ax.grid(False)
    plt.axhline(y=0, color = 'w')
    plt.legend()
    plt.savefig('inflacao.png', dpi = 300)

