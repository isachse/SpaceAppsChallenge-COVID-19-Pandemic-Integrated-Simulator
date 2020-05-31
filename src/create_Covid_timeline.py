import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

"""
DESCRIPTION
===========
    Read meta data in OMI NO2 csv file

"""
def read_meta_data(path):
    df_meta = pd.read_csv(path, nrows=7, index_col=0, header =None).transpose()
    meta_dict = {}
    gridBoundaries = [float(num) for num in df_meta['Data Bounding Box:'].values[0].split(',')]
    df = pd.DataFrame()
    meta_dict['x0'] = gridBoundaries[0]
    meta_dict['y0'] = gridBoundaries[1]
    meta_dict['x1'] = gridBoundaries[2]
    meta_dict['y1'] = gridBoundaries[3]
    meta_dict['Start_date'] = df_meta['User Start Date:'].values
    meta_dict['End_date'] = df_meta['User End Date:'].values
    meta_dict['Title'] = df_meta['Title:'].values
    meta_dict['Url'] = df_meta['URL to Reproduce Results:'].values
    meta_dict['fvalue'] = df_meta['Fill Value (mean_OMNO2d_003_ColumnAmountNO2TropCloudScreened):'].values
    
    
    return meta_dict

"""
DESCRIPTION
===========
    Generate interactive html timelines

"""
def gen_html(path2020, path2019, df_flights ,df_movement, title):
    
    meta_dict=read_meta_data(path2020)
    df2020 = pd.read_csv(path2020, skiprows=9, index_col=0, header=None, names=['NO2(1/cm2)'],na_values=meta_dict['fvalue'])
    df2019 = pd.read_csv(path2019, skiprows=9, index_col=0, header=None, names=['NO2(1/cm2)'],na_values=meta_dict['fvalue'])
    #Remove negative values
    df2020 = df2020[df2020['NO2(1/cm2)'] > 0]
    df2019 = df2019[df2019['NO2(1/cm2)'] > 0]

    fig = make_subplots(rows=3, cols=1,shared_xaxes=True, 
                    vertical_spacing=0.08, subplot_titles=('Tropospheric NO2', 'Number of commerical flights'
                                                         ,'Google mobility changes in precent from pre Covid-19')
                       )
    fig.add_trace(go.Scatter(y = df2020['NO2(1/cm2)'],
                            x= df2020.index, name='2020' ,mode='markers')) 

    fig.add_trace(go.Scatter(y = df2019['NO2(1/cm2)'],
                            x= df2020.index, name ='2019', mode='markers')) 
    fig.append_trace(go.Scatter(x=df_flights.index, y=df_flights['Number of flights'],
                 name = 'Daily flights'  ), row=2, col=1) 

    fig.append_trace(go.Scatter(x=df_flights.index, y=df_flights['7-day moving average'],
                            name='7-day moving avarage', line=dict(color ='slateblue'), opacity=0.7,
                              ), row=2, col=1)
    fig.append_trace(go.Scatter(y=df_movement['retail_and_recreation_percent_change_from_baseline'], x= df2020.index
                               ,name='Recreation'), 
                     row=3, col=1)
    
    fig.append_trace(go.Scatter(y=df_movement['grocery_and_pharmacy_percent_change_from_baseline'], x= df2020.index,
                               name='Grocery and Pharmacy'), 
                     row=3, col=1)
    
    fig.append_trace(go.Scatter(y=df_movement['parks_percent_change_from_baseline'], x= df2020.index,
                               name='Parks'), 
                     row=3, col=1)
    
    fig.append_trace(go.Scatter(y=df_movement['transit_stations_percent_change_from_baseline'], x= df2020.index,
                               name='Transit stations'), 
                     row=3, col=1)
    
    fig.append_trace(go.Scatter(y=df_movement['workplaces_percent_change_from_baseline'], x= df2020.index,
                               name='Workplaces'), 
                     row=3, col=1)
    fig.append_trace(go.Scatter(y=df_movement['residential_percent_change_from_baseline'], x= df2020.index,
                               name='Residents'), 
                     row=3, col=1)
    
    
    fig.update_yaxes(title_text='NO2 (1/cm^2)', row=1, col=1)
    fig.update_yaxes(title_text='Number of flights', row=2, col=1)
    fig.update_yaxes(title_text='Precent', row=3, col=1)
    fig.update_layout(
        hovermode="x")
    
    

#     fig.write_html(savefile, include_plotlyjs= 'directory')
    return fig

if __name__ == "__main__":
    pathRome2020 = '../data/omi/OMNO2d_003_20200131-20200524_12E_40N_15E_42N.csv'
    pathRome2019 = '../data/omi/OMNO2d_003_20190131-20190524_12E_40N_15E_42N.csv'

    pathMilan2020 = '../data/omi/OMNO2d_003_20200131-20200524_8E_44N_12E_46N.csv'
    pathMilan2019 = '../data/omi/OMNO2d_003_20190131-20190524_8E_44N_12E_46N.csv'

    pathMadrid2020 = '../data/omi/OMNO2d_003_20200131-20200524_5W_39N_2W_41N.csv'

    pathMadrid2019 = '../data/omi/OMNO2d_003_20190131-20190524_5W_39N_2W_41N.csv'

    df_flights = pd.read_csv('../data/flightradar/number-of-commercial-fli.csv'
                            , index_col = 0)
    df_flights.index = pd.to_datetime(df_flights.index) 

    df = pd.read_csv('../data/google/Global_Mobility_Report__ES_IT_sample.csv')
    df.index = pd.to_datetime(df['date'])
    df_italy = df[df['country_region']=='Italy']
    df_spain = df[df['country_region']=='Spain']



    fig_rome = gen_html(path2020=pathRome2020, path2019=pathRome2019,  df_flights=df_flights,title='OMI Tropospheric NO2 Rome'
                            ,df_movement=df_italy)

    fig_madrid = gen_html(pathMadrid2020, pathMadrid2019,  df_flights=df_flights,title='OMI Tropospheric NO2 Madrid',
            df_movement=df_spain)

    fig_milan = gen_html(pathMilan2020, pathMilan2019, df_flights=df_flights,title='OMI Tropospheric NO2 Milian', 
            df_movement=df_italy)
    fig_milan.update_layout(title_text='Milan Covid-19 Timeline', height=800)
    fig_madrid.update_layout(title_text='Madrid Covid-19 Timeline', height=800)
    fig_rome.update_layout(title_text='Rome Covid-19 Timeline', height=800)

    fig_milan.write_html('../html/MilianCovid-19_timeline.html', include_plotlyjs='directory')
    fig_rome.write_html('../html/RomeCovid-19_timeline.html', include_plotlyjs='directory')
    fig_madrid.write_html('../html/MadridCovid-19_timeline.html', include_plotlyjs='directory')