import streamlit
import pandas
streamlit.title('🥣 My snowflake bedge 2 practice');
streamlit.header('🥗 Snowflake');
streamlit.text('🐔 streamlit text');
streamlit.text('🥑 trying to solve error');
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt");
# streamlit.dataframe(my_fruit_list);
# Let's put a list here so they can pick the fruit they want to include
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index));
# display the table on the page
streamlit.dataframe(my_fruit_list);
