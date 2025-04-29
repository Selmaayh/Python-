import streamlit as st 

#titre
st.title('Python Learning')

#text
st.write ("hello world")

#user input 
user_input = st.text_input('tapez votre text : ')
st.write(user_input)



#colon 
col1, col2 = st.columns(2)



with col1: 
    #image 
    st.image("https://dessindigo.com/storage/images/posts/pikachu/dessin-pikachu-couleur-marron-marques-queues-dos.jpg")



with col2: 
    #video 
    st.video("https://www.youtube.com/watch?v=RU5-V3XwYjk") 




#menu deroulant
pays_select = st.selectbox("selectionner un pays ", ["fr", "en"])

st.write(pays_select)
st.sidebar.image("https://dessindigo.com/storage/images/posts/pikachu/dessin-pikachu-couleur-marron-marques-queues-dos.jpg")