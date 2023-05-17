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
        save(grid)
        

                    
        
                
    

       
        




