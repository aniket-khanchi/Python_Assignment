def squared_error(first_df, second_df):
    """
    Calculates the squared error to another function
    :param other_function:
    :return: the squared error
    """
    distances = second_df - first_df
    distances["y"] = distances["y"] ** 2
    total_deviation = sum(distances["y"])
    return total_deviation



def minimise_loss(training_df,ideal_fun_df,loss_function):
    function_with_smallest_error = None
    smallest_error = None
    for function in ideal_fun_df.df_dict.keys():
        error = loss_function(training_df, ideal_fun_df.df_dict[function])
        if ((smallest_error == None) or error < smallest_error):
            smallest_error = error
            function_with_smallest_error = function

    ideal_function = function_with_smallest_error
    return ideal_function

