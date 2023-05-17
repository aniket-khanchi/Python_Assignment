#importing necessary modules

import math
import pandas as pd
from function_inventory import DataframeFunction
from regression import Regression
from data_visualization import Graph
import sys
# from loss_function import squared_error, minimise_loss, find_classification


if __name__ == '__main__':

    #Define the paths of input & output files
    ideal_csv = "data\\ideal.csv"
    test_csv = "data\\test.csv"
    train_csv = "data\\train.csv"


    test = DataframeFunction(test_csv)
    train = DataframeFunction(train_csv)
    ideal = DataframeFunction(ideal_csv)

    # print(line_eqn_para(train._df).head())
    Reg = Regression(train=train._df,test=test._df,ideal=ideal._df)
    chart = Graph(train=train._df,test=test._df,ideal=ideal._df)

    # for columns in train._df.columns:
    #     if columns != 'x':
    #         tmp_df = pd.DataFrame()
    #         tmp_df['x'] = train._df['x']
    #         tmp_df['y'] = train._df[columns]
    #         chart.line_chart(tmp_df)
            # print(tmp_df)

    


    
    dic = Reg.least_squares(ideal._df,train._df)
    # print(line_equ_train_data_df)
    
    
    best_fit_line_dict = Reg.best_fit_line_ideal_func(dic)
    line_equ_train_data_df = Reg.line_eqn_para(train._df)
    line_equ_train_data_dict = line_equ_train_data_df.to_dict()
    line_qeu_ideal_data_df = Reg.line_eqn_para(ideal._df)
    line_equ_ideal_data_dict = line_qeu_ideal_data_df.to_dict()
    print(line_equ_ideal_data_dict)
    # sys.exit()
    train_chart_df = chart.line_chart(train._df,line_equ_train_data_dict,'train')
    ideal_fn_df  =  pd.DataFrame()
    ideal_fn_df['x'] = ideal._df['x']
    for column in best_fit_line_dict:
        first_key = next(iter(best_fit_line_dict[column]))
        print(first_key)
        ideal_fn_df[first_key] = ideal._df[first_key]
    print(ideal_fn_df)
    ideal_chart_df = chart.line_chart(ideal_fn_df,line_equ_ideal_data_dict,'ideal')
    sys.exit()
    # print(best_fit_line_dict)
    # {'y1': {'y42': 0.3580520323154257}, 'y2': {'y44': 0.02840899369639279}, 'y3': {'y21': 1209.5656806100142}, 'y4': {'y3': 0.7011397050168394}}
    sys.exit()
    # calculate the max deviation for ideal dataset with respect to train dataset
    max_deviation_train_ideal_dict = Reg.max_deviation_train_ideal_data(best_fit_line_dict,line_equ_train_data_dict)
    # print(max_deviation_train_ideal_dict)
    # {'y1': {'y42': 0.8249}, 'y2': {'y44': 0.0764}, 'y3': {'y21': 4514.0375}, 'y4': {'y3': 1.5463}}
    #validate the test data with in range of max deviation
    map_test_dataset_dict = Reg.validate_max_deviation_test_data(max_deviation_train_ideal_dict)
    print(map_test_dataset_dict)
        #Map the test data in chart
        # self.chart.generate_map_test_data_chart(map_test_dataset_dict,max_deviation_train_ideal_dict,mapping_chart_save_path)



    



    















           
            
        

