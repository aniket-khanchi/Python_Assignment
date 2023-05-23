from bokeh.plotting import figure, output_file, show, save
from bokeh.layouts import column, grid,row,gridplot
from bokeh.models import Band, ColumnDataSource,FactorRange
from bokeh.palettes import magma
from scipy import stats
import pandas as pd
import sys


class Graph:
    
    def __init__(self,train,ideal,test) -> None:
        self.train_df = train
        self.ideal_df = ideal
        self.test_df = test

    def line_chart(self,dataframe,line_equation_para_dict,df_name=None):
        # Create individual plots
        plots = []
        for column in dataframe.columns:
            if column != 'x':
                
                tmp_df = pd.DataFrame()
                tmp_df['x'] = dataframe['x']
                tmp_df['y'] = dataframe[column]
                slope = line_equation_para_dict[column]['Slope']
                intercept = line_equation_para_dict[column]['Intercept']
                tmp_df['y_predicted'] = (dataframe['x'] * slope) + intercept

                p = figure(title=f'Plot {column}', width=500, height=350)
                p.line(tmp_df['x'], tmp_df['y_predicted'], line_width=2, line_color='blue')
                # Add a scatter plot to the figure
                p.scatter(tmp_df['x'], tmp_df['y'], marker='circle', size=8, fill_color='red')
                plots.append(p)
        

        grid = gridplot([[plots[0], plots[1]], [plots[2], plots[3]]])
        
        show(grid)

        # create name for save html file
        chart_filename = "output/" + str(df_name) + ".html"
        print(chart_filename)
        #save html file
        output_file(filename = chart_filename)
        # save(grid)

    
    def min_deviation_chart(self,train_dataframe,train_line_equation_para_dict,ideal_dataframe,ideal_line_equation_para_dict):
        # Create individual plots
        min_dev_plots = []
 
        for train_column,ideal_column in zip(train_dataframe.columns,ideal_dataframe.columns):
            if train_column and ideal_column != 'x':
                
                train_tmp_df = pd.DataFrame()
                train_tmp_df['x'] = train_dataframe['x']
                train_tmp_df['y'] = train_dataframe[train_column]
                slope = train_line_equation_para_dict[train_column]['Slope']
                intercept = train_line_equation_para_dict[train_column]['Intercept']
                train_tmp_df['y_predicted'] = (train_dataframe['x'] * slope) + intercept
                
                ideal_tmp_df = pd.DataFrame()
                ideal_tmp_df['x'] = ideal_dataframe['x']
                ideal_tmp_df['y'] = ideal_dataframe[ideal_column]
                slope = ideal_line_equation_para_dict[ideal_column]['Slope']
                intercept = ideal_line_equation_para_dict[ideal_column]['Intercept']
                ideal_tmp_df['y_predicted'] = (ideal_dataframe['x'] * slope) + intercept
                
                p = figure(title=f'Plot train_{train_column} vs ideal_{ideal_column}', width=500, height=350)
                
                p.scatter(train_tmp_df['x'], train_tmp_df['y'], marker='circle', size=8, color='red')
                p.line(ideal_tmp_df['x'], ideal_tmp_df['y'],line_width=2, line_color='blue')

                min_dev_plots.append(p)

        grid = gridplot([[min_dev_plots[0], min_dev_plots[1]], [min_dev_plots[2], min_dev_plots[3]]])

        # create name for save html file
        chart_filename = "output/"+"min_dev.html"

        #save html file
        output_file(filename = chart_filename)
        save(grid)

                    
        
                
    

       
        




