import pandas as pd
from scipy import stats
import scipy as sp
import math



class Regression:

    def __init__(self,train,ideal,test) -> None:
        self.train_df = train
        self.ideal_df = ideal
        self.test_df = test

    def line_eqn_para(self,dataframe):
            """
            This function will provide us the Line equation parameters e.g., slope, intercept...
            """
            line_eqn_para = {}
            for col_name in dataframe.columns[:]:
                if col_name != 'x':
                    line_eqn_para_dict = {}
                    x_col = dataframe['x']
                    y_col = dataframe[col_name]
                    slope, intercept, r_value, p_value, std_err = sp.stats.linregress(x_col, y_col)
                
                    line_eqn_para_dict["Slope"] = slope
                    line_eqn_para_dict["Intercept"] = intercept
                    line_eqn_para_dict["r_value"] = r_value
                    line_eqn_para_dict["p_value"] = p_value
                    line_eqn_para_dict["std_err"]=std_err

                    line_eqn_para[col_name] = line_eqn_para_dict
            line_eqn_para_df = pd.DataFrame(line_eqn_para)

            return line_eqn_para_df

    def least_squares(self,ideal_df,train_df):              #change this at later some point of time
        """
        This function will calculate the lease square method
        """
        #iterate over training functions to the find the matching ideal function
        least_squares_dict = {}
        for function in train_df.columns[:]:
            if function != 'x':
            # intercept = test_line_eqn_para.loc['Intercept', function]
            # slope = test_line_eqn_para.loc['Slope', function]

                ideal_least_square_dict = {}
                for col_name in ideal_df.columns[:]:
                    least_square_df = pd.DataFrame() 
                    least_square_df['x'] = ideal_df['x']
                    if col_name != 'x':
                        least_square = 0
                        least_square_df['y_ideal'] = ideal_df[col_name]
                        least_square_df['y_train'] = train_df[function]
                        least_square_df['Residual_err'] = least_square_df['y_ideal'] - least_square_df['y_train']
                        least_square_df['Residual_err_square'] = least_square_df['Residual_err'] * least_square_df['Residual_err']
                        least_square = least_square_df['Residual_err_square'].sum()
                        Mean_least_square = least_square/len(least_square_df['y_ideal'])
                        Root_mean_square_error = math.sqrt(Mean_least_square)
                        ideal_least_square_dict[col_name] = Root_mean_square_error
                least_squares_dict[function] = ideal_least_square_dict

        return least_squares_dict


    def best_fit_line_ideal_func(self,least_square_dict):
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

    def max_deviation_train_ideal_data(self,best_fit_line_dict,line_equ_train_data_dict):
            """
            calculate max deviation in ideal dataset 
            """
            #save dict of max deviation
            max_deviation_train_ideal_dict = {}
            #iterate for ideal test dataset which has a match in train dataset
            #best_fit_line_dict :{'y1': {'y40': 119.1491}, 'y2': {'y44': 0.0249}, 'y3': {'y3': 0.7004}, 'y4': {'y44': 0.0221}}
            for train_y_idx in best_fit_line_dict:
                #copy selected train colunm for each iteration
                train_column_y = train_y_idx
                #iterate for ideal test dataset 
                for ideal_y_idx in best_fit_line_dict[train_y_idx]:
                    max_deviation_dict = {}
                    #copy selected ideal colunm w.r.t given train column
                    ideal_column_y = ideal_y_idx
                    #copy respective train data line equation 
                    #{'intercept': 233.28429, 'slope': -20.099, 'r_value': -0.8895, 'p_value': 1.598e-137, 'std_err': 0.517}
                    train_line_eq = line_equ_train_data_dict[train_column_y]
                    
                    #calculate max deviation for the given train and ideal dataset
                    max_deviation = self.max_deviation_calc(train_column_y,ideal_column_y,train_line_eq)
                    #calculate final max deviation by multiply square root with priviously calculate max deviation 
                    max_deviation_train_ideal = max_deviation * math.sqrt(2)
                    #rounding off to 4 decimal points
                    max_deviation_dict[ideal_y_idx] = round(max_deviation_train_ideal,4)
                    #create a dict of max deviation for respective selected ideal dataset
                    max_deviation_train_ideal_dict[train_column_y] = max_deviation_dict
            
            return max_deviation_train_ideal_dict

    def max_deviation_calc(self,train_column_y,ideal_column_y,train_line_eq):
            """
            calculate max deviation between ideal and train dataset
            """
            #create init max deviation dataframe
            self.max_deviation_df = pd.DataFrame()
            #copy independent variable data from 'X' column from train dataset
            
            self.max_deviation_df['x'] = self.train_df['x']
            #copy dependent variable data from 'Y' train dataset
            self.max_deviation_df[train_column_y] = self.train_df[train_column_y]
            #copy dependent variable data from 'Y' ideal dataset
            self.max_deviation_df[ideal_column_y] = self.ideal_df[ideal_column_y]
            # calculate 'Y' best fit line using slope and intercept from train dataset
            self.max_deviation_df['y(bestfit)']   = (train_line_eq['Slope'] * self.train_df['x']) + train_line_eq['Intercept']

            # calculate deviation/ difference of best fit line(train data) and ideal dataset pair
            self.max_deviation_df['deviation']    =  round(abs( self.ideal_df[ideal_column_y] - self.train_df[train_column_y]),4)
            #calculate max deviation from list of deviation
            max_deviation = self.max_deviation_df['deviation'].max()
            #rounding off to 4 decimal point
            max_deviation = round(max_deviation,4)
            
            return max_deviation
    
    def validate_max_deviation_test_data(self,max_deviation_train_ideal_dict):
        """
        function calclates the test data within the range of max deviation 
        """
        mapping_test_data_dict = {}
        #iterate for dict of max deviation
        #max_deviation_train_ideal_dict : {'y1': {'y42': 0.7037}, 'y2': {'y35': 0.7056}, 'y3': {'y21': 0.7027}, 'y4': {'y31': 0.702}}
        for max_deviation_idx in max_deviation_train_ideal_dict:
            #iterate for all the selcted ideal dataset 
            for ideal_col_y_idx in (max_deviation_train_ideal_dict[max_deviation_idx]):
                mapping_data_set_dict = {}
                ideal_col_y = ideal_col_y_idx
                # copy max deviation
                max_deviation = max_deviation_train_ideal_dict[max_deviation_idx][ideal_col_y]
                
                max_deviation_mapper_df = pd.DataFrame() 
            
                ideal_x = self.ideal_df['x'].to_numpy()
                ideal_y = self.ideal_df[ideal_col_y].to_numpy()
                #generate all linear regression parmater
                ideal_slope, ideal_intercept, r_value, p_value, std_err = stats.linregress(ideal_x, ideal_y)

                ideal_intercept = round(ideal_intercept,4)
                ideal_slope = round(ideal_slope,4)
                # copy independent and dependent variables
                max_deviation_mapper_df['x'] = self.ideal_df['x']
                max_deviation_mapper_df[ideal_col_y] = self.ideal_df[ideal_col_y]
                # generate best fit line with ideal function
                max_deviation_mapper_df['y_bestfit'] = (ideal_slope*self.ideal_df['x']) + ideal_intercept
                #create upper and lower band with support of max deviation
                max_deviation_mapper_df['y_upperband'] = max_deviation_mapper_df[ideal_col_y] + max_deviation
                max_deviation_mapper_df['y_lowerband'] = max_deviation_mapper_df[ideal_col_y] - max_deviation
                
                max_deviation_mapper_df.set_index('x', inplace = True)
                
                for index, test_data_row in self.test_df.iterrows():
                    # test data points
                    x_index =test_data_row['x']
                    y_value =test_data_row['y']
                    ideal_data = (max_deviation_mapper_df.loc[x_index])
                    #mapping test data with in range of max deviation
                    if (y_value >= ideal_data['y_lowerband'] and y_value <= ideal_data['y_upperband']):
                        mapping_data_point_dict = {}
                        mapping_data_point_dict["x"] = x_index
                        mapping_data_point_dict["y"] = y_value
                        mapping_data_point_dict["ideal_column"] = ideal_col_y_idx
                        mapping_data_point_dict["y_upperband"] = ideal_data['y_upperband']
                        mapping_data_point_dict["y_lowerband"] = ideal_data['y_lowerband']
                        #create a dict of test data with in range of max deviation
                        mapping_data_set_dict[x_index] = mapping_data_point_dict
            #dict of all the test data point for all ideal functions
            mapping_test_data_dict[max_deviation_idx+"_"+ideal_col_y_idx] = mapping_data_set_dict
                
        return mapping_test_data_dict




             



    
