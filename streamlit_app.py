import streamlit
import pandas
import requests
import snowflake.connector

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

streamlit.header("Fruityvice Fruit Advice!");
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon");
# streamlit.text(fruityvice_response.json());

# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+"kiwi");

# take the json version of the response and normalize it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output it the screen as a table
streamlit.dataframe(fruityvice_normalized);

#New section to display fruitvice api response
streamlit.header("Fruityvice Fruit Advice!");
fruit_choice = streamlit.text_input('What fruit would you like information about?','kiwi');
streamlit.write('The user entered', fruit_choice);
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice);
