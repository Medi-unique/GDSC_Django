def basic_operations(a, b):

    try:
        result = {
            'addition': a + b,
            'subtraction': a - b,
            'multiplication': a * b,
            'division': a / b
        }
    except ZeroDivisionError:
        result = {
            'addition': None,
            'subtraction': None,
            'multiplication': None,
            'division': 'Error: Division by zero'
        }
    except Exception as e:
        result = {
            'addition': None,
            'subtraction': None,
            'multiplication': None,
            'division': f'Error: {str(e)}'
        }
    return result


def power_operation(base, exponent, **kwargs):
    
    try:
        result = base ** exponent
        if 'modulo' in kwargs:
            modulo = kwargs['modulo']
            result = result % modulo
    except Exception as e:
        result = f'Error: {str(e)}'
    return result


def apply_operations(operation_list):
    
    results = []
    for operation, args in operation_list:
        try:
            result = operation(*args)
        except Exception as e:
            result = f'Error: {str(e)}'
        results.append(result)
    return results