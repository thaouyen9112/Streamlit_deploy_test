import streamlit as st

st.set_page_config(layout="wide")

st.title('How to layout your Streamlit app')

with st.expander('About this app'):
  st.write('This app shows the various ways on how you can layout your Streamlit app.')
  st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)

st.sidebar.header('Input')
user_name = st.sidebar.text_input('What is your name?')
user_emoji = st.sidebar.selectbox('Choose an emoji', ['','😄', '😆', '😊', '😍', '😴', '😕', '😱'])
user_food = st.sidebar.selectbox('What is your favorite food?', ['', 'Tom Yum Kung', 'Burrito', 'Lasagna', 'Hamburger', 'Pizza'])

tab1, tab2, tab3 = st.tabs(['Name', 'Emoji', 'Food'])

with tab1:
  if user_name != '':
    st.write(f'hello {user_name}')
  else:
    st.write ('Enter your name')

with tab2:
  if user_emoji != '':
    st.write(f"{user_emoji} is {user_name}'s favorite emoji")
  else:
    st.write ('Cloose an emoji')

with tab3:
  if user_food != '':
    st.write(f"{user_food} is {user_name}'s favorite food")
  else:
    st.write ('Enter your favorite food')
