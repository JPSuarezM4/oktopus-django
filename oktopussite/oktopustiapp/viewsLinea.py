from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import pandas as pd
import plotly.express as px
import plotly.io as pio


@login_required
def graficos_linea(request):
    # DataFrame
    df = pd.read_excel('C:/Users/alucp/OneDrive/Desktop/oktopusti/oktopussite/oktopustiapp/storage/CuatroCaminos.xlsx')

    df['date'] = pd.to_datetime(df['date'])
    df['Year'] = df['date'].dt.year
    df['Month'] = df['date'].dt.month
    df['Day'] = df['date'].dt.day
    df['Hour'] = df['date'].dt.hour

    df_parametros = df[['PM10_Reference', 'PM2.5_Reference', 'PM1', 'PM2.5',
                        'PM10', 'TEMPERATURE_INT', 'HUMIDITY_INT', 'TEMPERATURE_AMB', 'HUMIDITY_AMB', 'Day']]

    df_parametros['TEMPERATURE_AMB'] = pd.to_numeric(
        df_parametros['TEMPERATURE_AMB'], errors='coerce')
    df_parametros['HUMIDITY_AMB'] = pd.to_numeric(
        df_parametros['HUMIDITY_AMB'], errors='coerce')

    date_per_day = df_parametros.groupby('Day').agg({
        'TEMPERATURE_AMB': 'mean',
        'HUMIDITY_AMB': 'mean'
    }).reset_index()

    fig = px.histogram(df_parametros, x="PM10_Reference")
    fig.update_layout(
        title="Histograma PM10_Reference",
        xaxis=dict(title="Valores"),
        yaxis=dict(title="Frecuencia"),)
    plotly_html2 = pio.to_html(fig, full_html=False)

    fig = px.histogram(df_parametros, x="PM2.5_Reference")
    fig.update_layout(
        title="Histograma PM2.5_Reference",
        xaxis=dict(title="Valores"),
        yaxis=dict(title="Frecuencia"),)
    plotly_html3 = pio.to_html(fig, full_html=False)

    fig = px.box(df_parametros, x="PM10_Reference")
    fig.update_layout(
        title="Boxplot PM10_Reference",
        xaxis=dict(title="Eje X"),
        yaxis=dict(title="Eje Y"),)
    plotly_html4 = pio.to_html(fig, full_html=False)

    fig = px.box(df_parametros, x="PM2.5_Reference")
    fig.update_layout(
        title="Boxplot PM2.5_Reference",
        xaxis=dict(title="Eje X"),
        yaxis=dict(title="Eje Y"),)
    plotly_html5 = pio.to_html(fig, full_html=False)

    df['TEMPERATURE_AMB'] = pd.to_numeric(
        df['TEMPERATURE_AMB'], errors='coerce')

    top10_temperature = df.groupby('date').agg({'TEMPERATURE_AMB': 'mean'}).reset_index(
    ).sort_values('TEMPERATURE_AMB', ascending=False)

    fig = px.bar(top10_temperature, x='date', y='TEMPERATURE_AMB')
    fig.update_layout(
        title="Top 10 Temperatura Ambiental",
        xaxis=dict(title="Fecha"),
        yaxis=dict(title="Temperatura Promedio"),
    )
    plotly_html6 = pio.to_html(fig, full_html=False)

    df_numeric = df_parametros.select_dtypes(include=['float64', 'int64'])
    correlation = df_numeric.corr(method='pearson').round(2)

    fig = px.imshow(correlation,
                    x=correlation.index,
                    y=correlation.columns,
                    color_continuous_scale='RdBu',
                    labels=dict(color='Correlación'))
    plotly_html = pio.to_html(fig, full_html=False)

    fig = px.line(date_per_day,  x='Day', y='TEMPERATURE_AMB')
    plotly_html7 = pio.to_html(fig, full_html=False)

    fig = px.line(date_per_day,  x='Day', y='HUMIDITY_AMB')
    plotly_html8 = pio.to_html(fig, full_html=False)

    fig = px.bar(date_per_day, x='Day', y='TEMPERATURE_AMB')
    plotly_html9 = pio.to_html(fig, full_html=False)

    fig = px.bar(date_per_day, x='Day', y='HUMIDITY_AMB')
    plotly_html10 = pio.to_html(fig, full_html=False)

    context = {
        'plotly_html2': plotly_html2,
        'plotly_html3': plotly_html3,
        'plotly_html4': plotly_html4,
        'plotly_html5': plotly_html5,
        'plotly_html6': plotly_html6,
        'plotly_html': plotly_html,
        'plotly_html7': plotly_html7,
        'plotly_html8': plotly_html8,
        'plotly_html9': plotly_html9,
        'plotly_html10': plotly_html10,
        'show_navbar': True
        }
    
    return render(request, 'oktopustiapp/graficosLinea.html', context)

