import boto3
import json

# Crear un cliente para EventBridge
client = boto3.client('events')

def modify_event_rule_and_target(rule_name, target_lambda_arn, new_schedule_expression, new_input_string):
    # Modificar la expresión de tiempo de la regla
    response_rule = client.put_rule(
        Name=rule_name,
        ScheduleExpression=new_schedule_expression,  # Nueva expresión de tiempo, e.g., 'rate(15 minutes)'
        State='ENABLED'
    )
    
    # Modificar el input constante del target
    response_target = client.put_targets(
        Rule=rule_name,
        Targets=[
            {
                'Id': '1',
                'Arn': target_lambda_arn,
                'Input': json.dumps({"message": new_input_string})
            }
        ]
    )
    
    print(f"Regla modificada: {rule_name} con nueva expresión de tiempo: {new_schedule_expression}")
    print(f"Input modificado para Lambda: {new_input_string}")

# Llamar a la función para modificar la regla
modify_event_rule_and_target(
    rule_name='InvokeMyLambdaEvery30Minutes',
    target_lambda_arn='arn:aws:lambda:us-east-1:123456789012:function:MySecondLambda',
    new_schedule_expression='rate(15 minutes)',  # Cambiar la frecuencia a 15 minutos
    new_input_string='Nuevo mensaje de ejemplo'
)
