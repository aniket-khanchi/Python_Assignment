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
        
        # show(grid)

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

    def generate_mapper_graph(self,mapper_point_data,max_deviation_train_ideal_dict):
        """
        Generate mapped chart for test dataset, within range of max deviation 
        """
        df_in_range_point = pd.DataFrame()
        x = []
        y = []
        mapper_point_data_tag  = ""
        # mapper_point_data contains information related to mapping points on chart
        # {'y2_y44': [{'x': -9.8, 'y': 0.04520088, 'ideal_column': 'y44', 'y_upperband': 0.059579999999999994, 'y_lowerband': -0.07782},
        # {'x': -0.3, 'y': -0.026510444, 'ideal_column': 'y44', 'y_upperband': 0.05863, 'y_lowerband': -0.07876999999999999},
        # {'x': 3.5, 'y': -0.012937355, 'ideal_column': 'y44', 'y_upperband': 0.058249999999999996, 'y_lowerband': -0.07915}]}
        for mapper_point_data_idx,mapper_point_data_value in mapper_point_data.items():
            mapper_point_data_tag = mapper_point_data_idx
            # mapper_point_data[mapper_point_data_idx] contains dict of tester points and repective info about band and ideal function
            #[{'x': -9.8, 'y': 0.04520088, 'ideal_column': 'y44', 'y_upperband': 0.059579999999999994, 'y_lowerband': -0.07782},
            # {'x': -0.3, 'y': -0.026510444, 'ideal_column': 'y44', 'y_upperband': 0.05863, 'y_lowerband': -0.07876999999999999},
            # {'x': 3.5, 'y': -0.012937355, 'ideal_column': 'y44', 'y_upperband': 0.058249999999999996, 'y_lowerband': -0.07915}]
            for in_range_idx in mapper_point_data[mapper_point_data_idx]:
                # test data points
                x.append(in_range_idx['x'])
                y.append(in_range_idx['y'])
                #ideal column
                ideal_column_y = in_range_idx['ideal_column']
        #create a dict of tester data points
        dict = {'x':x,'y':y}
        
        df_in_range_point = pd.DataFrame(dict)
        
        #all the test data points
        """
             x         y
        0 -9.8  0.045201
        1 -0.3 -0.026510
        2  3.5 -0.012937
        """
        x =  df_in_range_point['x'].to_numpy()
        y =  df_in_range_point['y'].to_numpy()
        
        ideal_col_y = 0
        max_deviation = 0
        max_deviation_tag = ''
        
        #iterate through dict of max deviation calcuated
        for map_idx in max_deviation_train_ideal_dict:
            #iterate through dict of ideal function and its max dec=viation
            for ideal_idx in max_deviation_train_ideal_dict[map_idx]:
                #ideal function for max deviation
                ideal_col_y = ideal_idx 
                #max deviation
                max_deviation = max_deviation_train_ideal_dict[map_idx][ideal_idx]
                #generate train and ideal function pair(y1_y40)
                max_deviation_tag = f'{map_idx}_{ideal_idx}'
                
                
            #copy independent and dependent variables from ideal dataset
            x_data_pt = self.ideal_df['x'].to_numpy()
            y_data_pt = self.ideal_df[ideal_col_y].to_numpy()
              
            if (mapper_point_data_tag == max_deviation_tag):
        
                df = pd.DataFrame()
                #copy independent and dependent variables
                df['x'] = x_data_pt
                df['y'] = y_data_pt
                #regression parameter
                ideal_slope, ideal_intercept, r_value, p_value, std_err = stats.linregress( df['x'], df['y'])
     
                #generate best fit line for ideal function
                # df['y_bestfit'] = (ideal_slope * df['x']) + ideal_intercept
                df['y_bestfit'] = df['y']
                #dataframe for upper and lower band
                df['y_upperband'] = df['y_bestfit'] + max_deviation
                df['y_lowerband'] = df['y_bestfit'] - max_deviation
                
                # Create a Bokeh figure
                p = figure(title="Deviation", x_axis_label="X", y_axis_label="Y")

                # Plot the upper and lower bands
                p.line(df['x'], df['y_upperband'], line_color="blue", line_width=2, legend_label="Upper Band")
                p.line(df['x'], df['y_lowerband'], line_color="red", line_width=2, legend_label="Lower Band")

                # Create a shaded region between the upper and lower bands
                p.varea(x=df['x'], y1=df['y_upperband'], y2=df['y_lowerband'], fill_color="gray", fill_alpha=0.5)
                
                #create scatter plot
                p.scatter(x=df['x'], y=df['y_bestfit'], line_color=None, fill_alpha=0.5, size=5, )
                #create upper and lowe band
                # band = Band(base=df['x'], lower=df['y_lowerband'], upper=df['y_upperband'],  level='underlay',fill_alpha=1.0, line_width=1, line_color='black')
                
                #graph features 
                # p.add_layout(band)
                p.title.text = f"x vs {ideal_col_y}, max deviation :{max_deviation}"
                p.xgrid[0].grid_line_color=None
                p.ygrid[0].grid_line_alpha=0.5
                p.xaxis.axis_label = 'X'
                p.yaxis.axis_label = 'Y'
                size = 10
                color = magma(256)
                file_header = f"mapped_testdata_train_function_{map_idx}_ideal_function_{ideal_col_y}"
                #generate legend for 
                p.scatter(x, y,size = size, color = "red",legend_label="Mapped testdata within max deviation") 
                #file path to save graph 
                chart_filename = "output/"+ file_header +".html"
                #save graph in save path
                output_file(filename=chart_filename, title=file_header )
                #show the graph in browser.    
                try:  
                    # show(row(p)) 
                    pass
                except Exception as _error:
                    print(f"Error: GRAPH GENERATED UNSUCCESSFUL: {_error}")
                    
        
    def generate_map_test_data_chart(self,map_data_set_dict,max_deviation_train_ideal_dict):
        """
        calculate max deviation for ideal and train data
        """ 
        max_deviation_tag_list = []
        #iterate dict of deviation of ideal and train 
        for train_col_y in max_deviation_train_ideal_dict:
            for ideal_col_y in max_deviation_train_ideal_dict[train_col_y]:
                #create a tag list for train and respective pair of ideal function
                max_deviation_tag_list.append(f"{train_col_y}_{ideal_col_y}")
        
        #iterate through the deviation tag example '0.0085(deviation) : 19.9(test point)'
        for max_deviation_idx in max_deviation_tag_list:
        
            in_range_data_points_list = []
            in_range_data_points_dict = {}
            #iterate through the dict containing test dataset, alonf side ideal function and band dataset
            #3.5: {'x': 3.5, 'y': -0.012937355, 'ideal_column': 'y44', 'y_upperband': 0.04925, 'y_lowerband': -0.07015}
            for in_range_max_max_deviation in map_data_set_dict[max_deviation_idx]:
                in_range_data_points = (map_data_set_dict[max_deviation_idx][in_range_max_max_deviation])
                in_range_data_points_list.append(in_range_data_points)
            #list consist of points with in range of upper and lower limit
            in_range_data_points_dict[max_deviation_idx] = in_range_data_points_list
            #generate the test datapoint graph
            self.generate_mapper_graph(in_range_data_points_dict,max_deviation_train_ideal_dict)

       
        




