## this will use matplot lib and plot the data shown


## IMPORTS

import matplotlib.pyplot as plt
import pandas as pd


def plotting_data_main( File ):
    ## create the figures and read the data
    fig, ax = plt.subplots(figsize=(10, 6)) # Define size here
    df = pd.read_csv(File.processed_csv )

    x_col = 'Power-On Hours'
    y_col = 'Life Percentage'
    label_col = 'SSD Serial No.'

    plt.figure(figsize=(12, 7))
    plt.scatter(df[x_col], df[y_col], color='blue')

    # Start the loop from the second row (index 1) to get data from row 0
    for i in range(1, len(df)):
        # Get the label from the row ABOVE (i-1)
        label_text = df[label_col].iloc[i-1] 
        
        # Get the coordinates for the CURRENT dot (i)
        x_val = df[x_col].iloc[i]
        y_val = df[y_col].iloc[i]
        
        plt.annotate(
            label_text, 
            (x_val, y_val),
            textcoords="offset points", 
            xytext=(0, 10), 
            ha='center',
            fontsize=8,
            arrowprops=dict(arrowstyle='->', lw=0.5, color='gray')
        )

    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title('SSD Comparison (Labeled with prior row)')
    plt.grid(True)
    plt.show()