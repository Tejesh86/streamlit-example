import streamlit
import pandas
import requests
streamlit.title('🥣 My snowflake bedge 3 practice');
streamlit.header('🥗 Snowflake');
# streamlit.text('🐔 streamlit text');
streamlit.text('🥑 trying to solve error');
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt");
my_fruit_list = my_fruit_list.set_index('Fruit');
# streamlit.dataframe(my_fruit_list);
# Let's put a list here so they can pick the fruit they want to include
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Lemon']); #,'Lime'
# display the table on the page
fruits_to_show = my_fruit_list.loc[fruits_selected];
streamlit.dataframe(fruits_to_show);


fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response);
streamlit.header("Fruityvice Fruit Advice!");

