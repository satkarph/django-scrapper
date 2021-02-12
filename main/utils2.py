import pandas
def read_excel(input_file):
    df = pandas.read_excel(input_file)
    list_of_ids = df['id'].tolist()
    return list_of_ids