# from bokeh.plotting import figure, show

# # Example data
# x_data = [1, 2, 3, 4, 5]
# y_upper = [5, 6, 7, 8, 9]
# y_lower = [3, 4, 5, 6, 7]

# # Create a Bokeh figure
# p = figure(title="Deviation", x_axis_label="X", y_axis_label="Y")

# # Plot the upper and lower bands
# p.line(x_data, y_upper, line_color="blue", line_width=2, legend_label="Upper Band")
# p.line(x_data, y_lower, line_color="red", line_width=2, legend_label="Lower Band")

# # Create a shaded region between the upper and lower bands
# p.varea(x=x_data, y1=y_upper, y2=y_lower, fill_color="gray", fill_alpha=0.5)

# # Add a legend
# p.legend.location = "top_left"

# # Display the graph
# show(p)



import csv
from sqlalchemy import create_engine, Column, Integer, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create an engine to connect to the SQLite database
engine = create_engine('sqlite:///mydatabase.db', echo=True)

# Create a base class for declarative models
Base = declarative_base()

# Define your model as a subclass of Base
class Train(Base):
    __tablename__ = 'TRAIN_DATA'
    # id = Column(Integer, primary_key=True)
    x = Column(Float,primary_key=True)
    y1 = Column(Float)
    y2 = Column(Float)
    y3 = Column(Float)
    y4 = Column(Float)


class Ideal(Base):
    __tablename__ = 'IDEAL_DATA'
    x = Column(Float,primary_key=True)
    y1 = Column(Float)
    y2 = Column(Float)
    y3 = Column(Float)
    y4 = Column(Float)
# Create the database schema
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Read data from the CSV file and insert into the table
csv_file = 'data\\train.csv'
with open(csv_file, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        record = Train(
            x=float(row['x']),
            y1=float(row['y1']),
            y2=float(row['y2']),
            y3=float(row['y3']),
            y4=float(row['y4'])
        )
        session.add(record)

# Commit the changes and close the session
session.commit()
session.close()