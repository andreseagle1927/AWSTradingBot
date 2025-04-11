import json

def lambda_handler(event, context):
    toBuy = none
    toSell = none
    try:
        close = event.get('close')
        rsi = event.get('rsi')
        cci = event.get('cci')
        sma1 = event.get('sma1')
        sma2 = event.get('sma2')

        # Imprimir los datos recibidos para verificación (opcional)
        print(f"Received data: close={close}, rsi={rsi}, cci={cci}, sma1={sma1}, sma2={sma2}")

        if rsi <= 30 and cci <= -120 and sma1 == sma2:
            toBuy = true
            ## invocar el lambda del order core con la ticket , y la orden de comprar
        if rsi >= 70 and cci >= 110 and sma1 == sma2:
            toSell = true

            ## invocar el lambda del order core con la ticket , y la orden de vender

        # TODO implement

        return {
            'statusCode': 200,
            'body': json.dumps('Hello from Lambda!')
        }

    except Exception as e:
        print(f"Error processing data: {str(e)}")
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'Error processing data'})
        }
