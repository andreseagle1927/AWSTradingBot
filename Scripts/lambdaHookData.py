import json
import yfinance as yf
import pandas as pd
import pandas_ta as ta
import boto3

def lambda_handler(event, context):
    # Extraer los valores del payload enviado por la primera Lambda
    ticker = event.get('ticker')
    timeframe = event.get('timeframe')
    ma1 = event.get('ma1')
    ma2 = event.get('ma2')
    rsi = event.get('rsi')
    cci = event.get('cci')
        # Imprimir los datos recibidos para verificación (opcional)
    print(f"Received data: Ticker={ticker}, Timeframe={timeframe}, MA1={ma1}, MA2={ma2}, RSI={rsi}, CCI={cci}")

    tickerData = yf.Ticker(ticker)
        #historic_ticker = tickerData.history(period="max", interval = timeframe)

   #print(historic_ticker["Close"].head(10))

       # Descargar los datos históricos

    data = tickerData.history(period="max", interval=timeframe)

        # Calcular RSI

    data['RSI'] = ta.rsi(data['Close'], length=14)

        # Calcular CCI

    data['CCI'] = ta.cci(data['High'], data['Low'], data['Close'], length=30)

        # Calcular la SMA (por ejemplo, 50 días)

    data['sma1'] = ta.sma(data['Close'], length=50)

        # Calcular la SMA (por ejemplo, 50 días)

    data['sma2'] = ta.sma(data['Close'], length=10)

        # Mostrar las primeras filas con los cálculos

    print(data[['Close', 'RSI', 'CCI', 'sma1','sma2']].tail(1))

    payload = {

        'close': float(data['Close'].tail(1).values[0]),  # Convertir a float para evitar problemas de serialización
        'rsi': float(data['RSI'].tail(1).values[0]),
        'cci': float(data['CCI'].tail(1).values[0]),
        'sma1': float(data['sma1'].tail(1).values[0]),
        'sma2': float(data['sma2'].tail(1).values[0])
    }

         # Invocar la segunda Lambda de manera asíncrona

    lambda_client = boto3.client('lambda')
    lambda_client.invoke(
        FunctionName='arn:aws:lambda:us-east-1:490193484081:function:tradingRule',
        InvocationType='Event',  # Asíncrono
        Payload=json.dumps(payload)
    )

  

  

    return {
        'statusCode': 200,
        'body': json.dumps({

            'message': 'Data processed successfully in lambdaHookdata!',

            'processedData': payload

        })

    }

  
  
  

def bringDataFromYahooFinance(ticker , timeframe):

    tickerData = yf.Ticker(ticker)
    historic_ticker = apple.history(period="max", interval = timeframe)

    print(historic_ticker["Close"].head(10))
