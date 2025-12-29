def lambda_handler(event, context):
    numbers = event["numbers"]
    result = []

    for n in numbers:
        sqrt_value = n ** 0.5   # square root
        result.append(sqrt_value)

    return result