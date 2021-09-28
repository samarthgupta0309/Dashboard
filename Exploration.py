import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import streamlit as st

class ExploratoryAnalysis:

    def __init__(self, dataframe):
        self.df = dataframe
        self.columns = dataframe.columns
        self.numerical_columns = [name for name in self.columns if (self.df[name].dtype == 'int64') or (self.df[name].dtype == 'float64')]
    
    def info(self):
        buffer = io.StringIO()
        self.df.info(buf = buffer)
        return buffer.getValue()
    
    def info2(self, column_target):
        df = self.df[column_target].value_counts().to_frame().reset_index()
        df.sort_values(by='index', inplace=True, ignore_index=True)
        df.rename(columns={'index':column_target, '{}'.format(column_target):'Values Frequency'}, inplace=True)
        return df
    
    # count plot
    def CountPlot(self, column_target, hue=None):
        sns.set(style="darkgrid")
        return sns.countplot(x=column_target, data=self.df, hue=hue)
    
    # Heat Map - corr
    def HeatMapCorr(self):
        sns.set(style="darkgrid")
        sns.set(font_scale=0.6)
        corr = self.df.corr()
        return sns.heatmap(corr, annot=True, annot_kws={"size": 7}, linewidth=.5)

    #scatter plot
    def Scatter(self, X, y, hue):
        sns.set(style="darkgrid")
        return sns.scatterplot(x = self.df[X], y = self.df[y], hue=hue)
    
    #pairplot
    def PairPlot(self, hue=None):
        sns.set(Style="darkgrid")
        return sns.pairplot(self.df, hue=hue, palette="coolwarm")
    
    #box
    def BoxPlot(self, column_x=None, column_y=None, hue=None):
        sns.set(style="darkgrid")
        return sns.boxplot(x=column_x, y=column_y, hue=hue, data=self.df)
    
    # jointplot - hex
    def Jointplot(self, column_x=None, column_y=None):
        sns.set(style="darkgrid")
        sns.jointplot(x = column_x, y = column_y, kind = 'hex')