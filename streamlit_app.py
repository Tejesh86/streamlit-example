import streamlit
import pandas
streamlit.title('🥣 My snowflake bedge 2 practice');
streamlit.header('🥗 Snowflake');
streamlit.text('🐔 streamlit text');
streamlit.text('🥑 trying to solve error');
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt");
streamlit.dataframe(my_fruit_list);
