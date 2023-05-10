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



def find_classification(point, ideal_functions):
    """
    It computes if a point is within the tolerance of a classification
    :param point: a dict object in there is an "x" and an "y"
    :param ideal_functions: a list of IdealFunction objects
    :return:a tuple containing the closest classification if any, and the distance
    """
    current_lowest_classification = None
    current_lowest_distance = None

    for ideal_function in ideal_functions:
        try:
            locate_y_in_classification = ideal_function.locate_y_based_on_x(point[0])
        except IndexError:
            print("This point is not in the classification function")
            raise IndexError

        # Observe here how the absolute distance is used
        distance = abs(locate_y_in_classification - point[1])

        if (abs(distance < ideal_function.tolerance)):
            # This procedure makes sure there is handling if there are multiple classifcations possible
            # It returns the one with lowest distance
            if ((current_lowest_classification == None) or (distance < current_lowest_distance)):
                current_lowest_classification = ideal_function
                current_lowest_distance = distance

    return current_lowest_classification, current_lowest_distance



