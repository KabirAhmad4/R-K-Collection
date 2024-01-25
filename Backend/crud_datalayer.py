import pandas as pd
data_file_name = "products.csv"
def add_product(pid,name,description,price,image,rating):
    df = pd.read_csv(data_file_name)
    values = [pid,name,description,price,image,rating]
    print(values)
    df.loc[len(df.index)]=values
    df.to_csv(data_file_name,index=False)
   
def get_products():
    df = pd.read_csv(data_file_name)
    return df

def get_product(pid):
    df = pd.read_csv(data_file_name)
    product = df[df['pid']==pid]
    return product

def update_rating(pid,new_rating_value):
    df = pd.read_csv(data_file_name)
    idx = df[df['pid']==pid].index
    df.loc[idx,'rating'] = new_rating_value
    df.to_csv(data_file_name,index=False)

def delete_product(pid):
    df = pd.read_csv(data_file_name)
    idx = df[df['pid']==pid].index
    df = df.drop(idx)
    df.to_csv(data_file_name,index=False)

def update_product(pid,name,description,price,rating):
    df = pd.read_csv(data_file_name)
    idx = df[df['pid']==pid].index
    df.loc[idx,'name'] = name
    df.loc[idx,'description'] = description
    df.loc[idx,'price'] = price
    df.loc[idx,'rating'] = rating
    df.to_csv(data_file_name,index=False)