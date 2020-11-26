import pandas as pd 
data_df = pd.read_csv("WebVisualizations/Resources/cities.csv")
data_df.to_html('data_table.html', index=False)