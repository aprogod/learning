import pandas as pd

class Class_1():
    
    def __init__(self, input_url):
        self.sales_df = pd.read_csv(input_url)
        ### self.columns_list = []
    
    def sort_1(self, input):
        self.sales_df.sort_values(input, inplace = True)
        self.sales_df.reset_index(drop=True, inplace = True)
        return self.sales_df

    def drop_1(self, *input_columns):
        
        self.input = list(set(input_columns))
        self.sales_df.drop(self.input, axis = "columns", inplace = True)
        
        return self.sales_df
