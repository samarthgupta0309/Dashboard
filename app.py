from Exploration import ExploratoryAnalysis
import streamlit as st
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

def main():

    st.title('Data Story Teller')

    st.info('''Welcome to EDA dashboard, be a data detective''')
    st.image("cover.png")
    def UploadFile():
        uploaded_file = st.file_uploader("", type='csv')
        if uploaded_file is not None:
            return (pd.read_csv(uploaded_file))
    
    df = UploadFile()

    try:
        EA = ExploratoryAnalysis(df)
        st.success('File uploaded!')

        st.sidebar.title('Setting')

        st.sidebar.subheader('EDA options')
        if st.sidebar.checkbox('Basic information'):
            if st.sidebar.checkbox('Head'):
                st.subheader('Data Frame head')
                st.write(df.head(10))
            
            if st.sidebar.checkbox('Describe'):
                st.subheader('Dataframe description:')
                st.text(df.describe())

            # if st.sidebar.checkbox('Info'):
            #     st.subheader('DataFrame info')
            #     st.text(EA.info())

            if st.sidebar.checkbox('IsNull'):
                st.subheader('Null occurences')
                st.write(df.isnull().sum())
            
            if st.sidebar.checkbox('Unique val & freq'):
                col = st.sidebar.selectbox('Choose a column for see unique values', EA.columns)
                st.subheader('Unique val & freq')
                st.write(EA.info2(col))
            
        st.sidebar.subheader('Data Viz options')

        if st.sidebar.checkbox('Graphics'):
            if st.sidebar.checkbox('Count Plot'):
                st.subheader('Count Plot')
                column_count_plot = st.sidebar.selectbox("Choose a column to plot count",EA.columns)
                hue_opt = st.sidebar.selectbox("Optional categorical variables (countplot hue)",EA.columns.insert(0,None))
                if st.checkbox('Plot Countplot'):
                    fig = EA.CountPlot(column_count_plot, hue_opt)
                    st.pyplot()

            if st.sidebar.checkbox('Scatter Plot'):
                st.subheader('Scatter Plot')
                column_box_plot_X = st.sidebar.selectbox("X (Choose a column):",EA.columns.insert(0,None))
                column_box_plot_Y = st.sidebar.selectbox("Y (Choose a column - only numerical):",EA.numerical_columns)
                hue_box_opt = st.sidebar.selectbox("Optional categorical variables (scatterplot hue)",EA.columns.insert(0,None))            #     if st.checkbox('Plot Distplot'):
                fig = EA.Scatter(column_box_plot_X, column_box_plot_Y, hue_box_opt)
                st.pyplot()
            
            if st.sidebar.checkbox('Heatmap Correlation'):
                st.subheader('Heatmap Correlation Plot')
                fig = EA.HeatMapCorr()
                st.pyplot()

            if st.sidebar.checkbox('Boxplot'):
                st.subheader('Boxplot')
                column_box_plot_X = st.sidebar.selectbox("X (Choose a column):",EA.columns.insert(0,None))
                column_box_plot_Y = st.sidebar.selectbox("Y (Choose a column - only numerical):",EA.numerical_columns)
                hue_box_opt = st.sidebar.selectbox("Optional categorical variables (boxplot hue)",EA.columns.insert(0,None))
                if st.checkbox('Plot Boxplot'):
                    fig = EA.BoxPlot(column_box_plot_X, column_box_plot_Y, hue_box_opt)
                    st.pyplot()
    except:
        st.balloons()
if __name__ == "__main__":
    main()