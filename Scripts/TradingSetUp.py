import json

import boto3

def lambda_handler(event, context):
    try:
        # El cuerpo está en formato JSON, así que lo parseamos
        body = json.loads(event['body'])
        # Extraer los valores del JSON enviado
        ticker = body.get('ticker')  # Valor predeterminado si no se envía
        timeframe = body.get('timeframe')
        ma1 = body.get('ma1')
        ma2 = body.get('ma2')
        rsi = body.get('rsi')
        cci = body.get('cci')
        
        payload = {
            'ticker': ticker,
            'timeframe': timeframe,
            'ma1': ma1,
            'ma2': ma2,
            'rsi': rsi,
            'cci': cci
        }
         # Invocar la segunda Lambda de manera asíncrona
        lambda_client = boto3.client('lambda')
        '''response = lambda_client.invoke(

            FunctionName='arn:aws:lambda:us-east-1:490193484081:function:lamdaHookData',  # Nombre de la segunda Lambda

            InvocationType='Event',  # 'Event' para invocación asíncrona

            Payload=json.dumps(payload)  # Enviar los datos como JSON

        )'''

        lambda_client.invoke(
            FunctionName='arn:aws:lambda:us-east-1:490193484081:function:lamdaHookData',
            InvocationType='Event',  # Asíncrono
            Payload=json.dumps(payload)
        )


        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Trading setup received successfully!',
                'receivedData': payload
            })
        }

    except Exception as e:
        print(f"Error parsing request body: {str(e)}")
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'Error processing request body'})
        }
