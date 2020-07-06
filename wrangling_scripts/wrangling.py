def data_wrangling(columns):

    from wrangling_scripts.functions.functions import ranking
    import pandas as pd

    # Importing Data

    df_2019 = pd.read_csv('data/survey_results_public_2019.csv')

    # Cleaning Data

    df_2019_clean = df_2019.dropna(subset=['DevType'])
    df_2019_clean_DS = df_2019_clean[df_2019_clean['DevType'].str.contains('Data scientist or machine learning specialist')]

    # Plotting Data

    column_names = columns
    legends=['Used in 2019', 'Desired for 2020']

    plot = ranking(df_2019_clean_DS, column_names, legends)
    
    return plot