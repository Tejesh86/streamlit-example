import streamlit
import pandas
streamlit.title('🥣 My snowflake bedge 2 practice');
streamlit.header('🥗 Snowflake');
# streamlit.text('🐔 streamlit text');
streamlit.text('🥑 trying to resolve error');
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt");
my_fruit_list = my_fruit_list.set_index('Fruit');
# streamlit.dataframe(my_fruit_list);
# Let's put a list here so they can pick the fruit they want to include
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Lemon','Lime','Orange']);
# display the table on the page
fruits_to_show = my_fruit_list.loc[fruits_selected];
streamlit.dataframe(fruits_to_show);
