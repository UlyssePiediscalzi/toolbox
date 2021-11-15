import seaborn as sns
def heatmap(df):
    '''takes a DataFrame'''
    corr = df.corr()
    sns.heatmap(corr,
                xticklabels=corr.columns,
                yticklabels=corr.columns,
                cmap="YlGnBu")
