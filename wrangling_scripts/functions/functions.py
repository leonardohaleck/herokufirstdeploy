import pandas as pd
import plotly.graph_objs as go
import plotly, json

def ranking(df_original, columns, legends):
    
    '''
    This function splits the data of a column and calculates de percentage of each string appearance

    INPUT:
    df_original - dataframe that contains a column that you want to analyze
    columns - column that you want to analyze -> LanguageWorkedWith for example
    legends - the name you want to show in plot
    
    OUTPUT:
    A top 10 ranking bar plot
    '''
    
    for i in range(len(columns)):
    
        # Cleaning missing data of column1

        lg_series = df_original[columns[i]].dropna().reset_index().drop('index', axis=1)
        lg_df = pd.DataFrame(lg_series)

        lg = []

        # Separating the column1 information -> Example: 'Python; C' to 'Python' and 'C'

        for j in range(lg_df.shape[0]):
            lgs = lg_df[columns[i]][j].split(';')
            for k in range(len(lgs)):
                lg.append(lgs[k])

        # Counting values of each option

        if i == 0:
            df_language1 = pd.DataFrame(round(pd.DataFrame(lg)[0].value_counts() / len(lg_df), 4))
            df_language1.columns = [legends[i]]
        else:
            df_language2 = pd.DataFrame(round(pd.DataFrame(lg)[0].value_counts() / len(lg_df), 4))
            df_language2.columns = [legends[i]]

    return df_language1, df_language2





def sort_graph_values(df, column):

    '''
    This function sorts the index and one choosen column of a dataframe 
    
    INPUT:
    df - the dataframe that contais the column you want to sort
    column - the column you want to sort

    OUTPUT:
    sorty - the index sorted list
    sortx - the column sorted list
    '''

    sorty = [x for _,x in sorted(zip(df[column][:10],df.index[:10]))]
    sortx = sorted(df[column][:10])

    return sorty, sortx




def make_graph_layout(sortx, sorty, title, xaxis, yaxis):

    graph = [go.Bar(
        x = sortx,
        y = sorty,
        orientation='h',
        text=sortx,
        textposition='outside',
        texttemplate='%{text:.1%f}',
        marker_color='lightblue',
        hoverinfo='skip'
    )]

    layout = dict(title=title,
                  xaxis=dict(title=xaxis, tickformat=".1%", range=[0, 1], visible=False),
                  yaxis=dict(ticklen=10)
                    )

    return graph, layout