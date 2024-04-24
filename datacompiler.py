import os
import glob 
import csv
import pandas as pd

path = "stocks"
files = os.listdir(path) 

snp = pd.read_csv('indexes/snp 500.csv')
nasdaq = pd.read_csv('indexes/nasdaq 100.csv')
dow = pd.read_csv('indexes/dow 30.csv')

content = pd.DataFrame()

for filename in files: 
    df = pd.read_csv(path + '/' + filename, index_col=None)
    
    Low1 = df['Low'][0:-10]
    Low1 = [x for x in Low1 if str(x) != 'nan']

    Low2 = df['Low'][1:-9]
    Low2 = [x for x in Low2 if str(x) != 'nan']

    Low3 = df['Low'][2:-8]
    Low3 = [x for x in Low3 if str(x) != 'nan']

    Low4 = df['Low'][3:-7]
    Low4 = [x for x in Low4 if str(x) != 'nan']

    Low5 = df['Low'][4:-6]
    Low5 = [x for x in Low5 if str(x) != 'nan']

    Low6 = df['Low'][5:-5]
    Low6 = [x for x in Low6 if str(x) != 'nan']

    Low7 = df['Low'][6:-4]
    Low7 = [x for x in Low7 if str(x) != 'nan']

    Low8 = df['Low'][7:-3]
    Low8 = [x for x in Low8 if str(x) != 'nan']

    Low9 = df['Low'][8:-2]
    Low9 = [x for x in Low9 if str(x) != 'nan']

    Low10 = df['Low'][9:-1]
    Low10 = [x for x in Low10 if str(x) != 'nan']

    Low11 = df['Low'][10:]
    Low11 = [x for x in Low11 if str(x) != 'nan']
    
    Volume1 = df['Volume'][0:-10]
    Volume1 = [x for x in Volume1 if str(x) != 'nan']

    Volume2 = df['Volume'][1:-9]
    Volume2 = [x for x in Volume2 if str(x) != 'nan']

    Volume3 = df['Volume'][2:-8]
    Volume3 = [x for x in Volume3 if str(x) != 'nan']

    Volume4 = df['Volume'][3:-7]
    Volume4 = [x for x in Volume4 if str(x) != 'nan']

    Volume5 = df['Volume'][4:-6]
    Volume5 = [x for x in Volume5 if str(x) != 'nan']

    Volume6 = df['Volume'][5:-5]
    Volume6 = [x for x in Volume6 if str(x) != 'nan']

    Volume7 = df['Volume'][6:-4]
    Volume7 = [x for x in Volume7 if str(x) != 'nan']

    Volume8 = df['Volume'][7:-3]
    Volume8 = [x for x in Volume8 if str(x) != 'nan']

    Volume9 = df['Volume'][8:-2]
    Volume9 = [x for x in Volume9 if str(x) != 'nan']

    Volume10 = df['Volume'][9:-1]
    Volume10 = [x for x in Volume10 if str(x) != 'nan']

    Volume11 = df['Volume'][10:]
    Volume11 = [x for x in Volume11 if str(x) != 'nan']

    Dates = df['Date'][0:-10]
    Dates = [x for x in Dates if str(x) != 'nan']

    dict = {'Date' : Dates
    ,'Day -1 Low': Low1
    ,'Day -2 Low': Low2
    ,'Day -3 Low': Low3
    ,'Day -4 Low': Low4
    ,'Day -5 Low': Low5
    ,'Day -6 Low': Low6
    ,'Day -7 Low': Low7
    ,'Day -8 Low': Low8
    ,'Day -9 Low': Low9
    ,'Day -10 Low': Low10
    ,'Day -11 Low': Low11
    ,'Day -1 Volume': Volume1
    ,'Day -2 Volume': Volume2
    ,'Day -3 Volume': Volume3
    ,'Day -4 Volume': Volume4
    ,'Day -5 Volume': Volume5
    ,'Day -6 Volume': Volume6
    ,'Day -7 Volume': Volume7
    ,'Day -8 Volume': Volume8
    ,'Day -9 Volume': Volume9
    ,'Day -10 Volume': Volume10
    ,'Day -11 Volume': Volume11}

    new_df = pd.DataFrame(dict)

    stock = filename.replace('.csv', '')
    new_df['Stock'] = stock

    if stock in list(dow['SYMBOL']):
        isDow = True
        
        ind = dow[dow["SYMBOL"]==stock].index.values[0]
        name = dow.iloc[ind]['NAME']
        high_52 = dow.iloc[ind]['High 52 Weeks']
        low_52 = dow.iloc[ind]['Low 52 Weeks']
        sector = dow.iloc[ind]['Sector']
        if "T" in dow.iloc[ind]['Capitalization']:
            cap = float(dow.iloc[ind]['Capitalization'][:-1]) * 1000000000000
        elif "B" in dow.iloc[ind]['Capitalization']:
            cap = float(dow.iloc[ind]['Capitalization'][:-1]) * 1000000000
        elif "M" in dow.iloc[ind]['Capitalization']:
            cap = float(dow.iloc[ind]['Capitalization'][:-1]) * 1000000
        else:
            cap = dow.iloc[ind]['Capitalization']
    else:
        isDow = False


    if stock in list(nasdaq['SYMBOL']):
        isNas = True
        
        if isDow == False:
            ind = nasdaq[nasdaq["SYMBOL"]==stock].index.values[0]
            name = nasdaq.iloc[ind]['NAME']
            high_52 = nasdaq.iloc[ind]['High 52 Weeks']
            low_52 = nasdaq.iloc[ind]['Low 52 Weeks']
            sector = nasdaq.iloc[ind]['Sector']
            if "T" in str(nasdaq.iloc[ind]['Capitalization']):
                cap = float(nasdaq.iloc[ind]['Capitalization'][:-1]) * 1000000000000
            elif "B" in str(nasdaq.iloc[ind]['Capitalization']):
                cap = float(nasdaq.iloc[ind]['Capitalization'][:-1]) * 1000000000
            elif "M" in str(nasdaq.iloc[ind]['Capitalization']):
                cap = float(nasdaq.iloc[ind]['Capitalization'][:-1]) * 1000000
            else:
                cap = nasdaq.iloc[ind]['Capitalization']
        else:
            pass

    else:
        isNas = False


    if stock in list(snp['SYMBOL']):
        isSnp = True
        
        if (isDow == False) and (isNas == False):
            ind = snp[snp["SYMBOL"]==stock].index.values[0]
            name = snp.iloc[ind]['NAME']
            high_52 = snp.iloc[ind]['High 52 Weeks']
            low_52 = snp.iloc[ind]['Low 52 Weeks']
            sector = snp.iloc[ind]['SECTOR']
            if "T" in str(snp.iloc[ind]['Capitalization']):
                cap = float(snp.iloc[ind]['Capitalization'][:-1]) * 1000000000000
            elif "B" in str(snp.iloc[ind]['Capitalization']):
                cap = float(snp.iloc[ind]['Capitalization'][:-1]) * 1000000000
            elif "M" in str(snp.iloc[ind]['Capitalization']):
                cap = float(snp.iloc[ind]['Capitalization'][:-1]) * 1000000
            else:
                cap = snp.iloc[ind]['Capitalization']
        else:
            pass
    
    else:
        isSnp = False
        if (isDow == False) and (isNas == False):
            name = ''
            cap = ''
            high_52 = ''
            low_52 = ''
            sector = ''
        else:
            pass

    new_df['Name'] = name
    new_df['Sector'] = sector
    new_df['Market Cap'] = cap
    new_df['52 Weeks High'] = high_52
    new_df['52 Weeks Low'] = low_52
    new_df['On S&P500 ?'] = isSnp
    new_df['On Nasdaq 100 ?'] = isNas
    new_df['On Dow 30 ?'] = isDow


    content =  pd.concat([content, new_df])


content.to_csv('Compiled_Data.csv', index=False)