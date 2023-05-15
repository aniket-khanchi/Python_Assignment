from bokeh.plotting import figure, output_file, show, save
from bokeh.layouts import column, grid,row
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


    def train_line_chart(self,dataframe,line_equation_para_dict):
        for column in dataframe.columns:
            if column != 'x':
                
                tmp_df = pd.DataFrame()
                tmp_df['x'] = dataframe['x']
                tmp_df['y'] = dataframe[column]
                slope = line_equation_para_dict[column]['Slope']
                intercept = line_equation_para_dict[column]['Intercept']
                tmp_df['y_predicted'] = (dataframe['x'] * slope) + intercept
                p = figure(title='Line and Scatter Plot' + str(column), x_axis_label='X', y_axis_label='Y')
                # print(column)
                # Add a line plot to the figure
                p.line(tmp_df['x'], tmp_df['y_predicted'], line_width=2, line_color='blue')

                # Add a scatter plot to the figure
                p.scatter(tmp_df['x'], tmp_df['y'], marker='circle', size=8, fill_color='red')

                # Show the figure
                # show(p)
                # create name for save html file
                train_chart_filename = "output/" + f"train_{column}.html"
                print(train_chart_filename)
                #save html file
                output_file(filename = train_chart_filename, title=f"Train data({column}) ")
                

    # def create_chart(self, tmp_df):
        
        # if column == 'y2': 
        #     sys.exit()   
                    
        
                
    

       
        




