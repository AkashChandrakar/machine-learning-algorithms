def simple_linear_regression(input_feature, output):
    
    n = input_feature.size()
    if n == 0:
        return (None, None)
    
    # compute the sum of input_feature and output
    sum_input_feature = input_feature.sum()
    sum_output = output.sum()
    
    # compute the product of the output and the input_feature and its sum
    product_input_output = input_feature * output
    sum_product_input_output = product_input_output.sum()
    
    # compute the squared value of the input_feature and its sum
    square_input = input_feature * input_feature
    sum_square_input = square_input.sum()
    
    # use the formula for the slope
    slope = ((sum_product_input_output - sum_input_feature * sum_output / n) / 
             ((sum_square_input - sum_input_feature * sum_input_feature / n)) )
    
    # use the formula for the intercept
    intercept = sum_output / n - slope * sum_input_feature / n
    
    return (intercept, slope)
