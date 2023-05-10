import pandas as pd
import scipy as sp
import math


def line_eqn_para(dataframe):
        """
        This function will provide us the Line equation parameters e.g., slope, intercept...
        """
        line_eqn_para = {}
        for col_name in dataframe.columns[:]:
            if col_name != 'x':
                line_eqn_para_dict = {}
                independent_var = dataframe['x']
                dependent_var = dataframe[col_name]
                #copy slope, intercept, r_value, p_value, std_err
                slope, intercept, r_value, p_value, std_err = sp.stats.linregress(independent_var, dependent_var)
            
                line_eqn_para_dict["Slope"] = slope
                line_eqn_para_dict["Intercept"] = intercept
                line_eqn_para_dict["r_value"] = r_value
                line_eqn_para_dict["p_value"] = p_value
                line_eqn_para_dict["std_err"]=std_err

                line_eqn_para[col_name] = line_eqn_para_dict
        line_eqn_para_df = pd.DataFrame(line_eqn_para)

        return line_eqn_para_df

def least_squares(ideal_df,test_df):              #change this at later some point of time
    """
    This function will calculate the lease square method
    """
    #iterate over training functions to the find the matching ideal function
    least_squares_dict = {}
    test_line_eqn_para = line_eqn_para(test_df)
    for function in test_line_eqn_para:
        intercept = test_line_eqn_para.loc['Intercept', function]
        slope = test_line_eqn_para.loc['Slope', function]

        ideal_least_square_dict = {}
        for col_name in ideal_df.columns[:]:
            least_square_df = pd.DataFrame() 
            least_square_df['x'] = ideal_df['x']
            if col_name != 'x':
                least_square = 0
                least_square_df['y_actual'] = ideal_df[col_name]
                least_square_df['y_predicted'] = (least_square_df['x'] * slope) + intercept
                least_square_df['Residual_err'] = least_square_df['y_actual'] - least_square_df['y_predicted']
                least_square_df['Residual_err_square'] = least_square_df['Residual_err'] * least_square_df['Residual_err']
                least_square = least_square_df['Residual_err_square'].sum()
                Mean_least_square = least_square/len(least_square_df['y_actual'])
                Root_mean_square_error = math.sqrt(Mean_least_square)
                ideal_least_square_dict[col_name] = Root_mean_square_error
        least_squares_dict[function] = ideal_least_square_dict

    return least_squares_dict


def best_fit_line_ideal_func(least_square_dict):
        """
        Function to identifiy best fit ideal function w.r.t train function
        """
        best_fit_line = {}
        #iterate through the list of square error 
        for train_line in least_square_dict:
            # find the minimum from the list of square error  
            least_square = min(least_square_dict[train_line].values())
            # loop through ideal function to find match for train function
            least_square_key_value = {key:value for key, value in least_square_dict[train_line].items() if value == least_square}
            #create dict of all the min square error for graph creation
            best_fit_line[train_line] = least_square_key_value

        return best_fit_line


             



    
