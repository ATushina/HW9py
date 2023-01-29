def complex_operation(a, b, operator):
    c_a = complex(a)    
    c_b = complex(b)    
    return c_a+c_b if operator == '+' else c_a-c_b if operator == '-' \
        else c_a*c_b if operator == '*' else c_a/c_b if operator == '/' else False