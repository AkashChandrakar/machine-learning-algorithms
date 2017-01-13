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
    


def get_regression_predictions(input_feature, intercept, slope):
    # calculate the predicted values:
    predicted_values = intercept + slope*input_feature
    return predicted_values
    
    

def get_residual_sum_of_squares(input_feature, output, intercept, slope):
    # First get the predictions
    predicted_values = get_regression_predictions(input_feature,intercept,slope)
    # then compute the residuals (since we are squaring it doesn't matter which order you subtract)
    residuals = output - predicted_values
    # square the residuals and add them up
    residuals_square = residuals * residuals
    RSS = residuals_square.sum()
    return(RSS)
    


def inverse_regression_predictions(output, intercept, slope):
    # solve output = intercept + slope*input_feature for input_feature. Use this equation to compute the inverse predictions:
    estimated_feature = (output - intercept) / slope
    return estimated_feature

