import streamlit as st

from src.poem_functions import get_poem

def judge_answer(guess, actual):
    st.session_state.guessed = True
    if guess == actual:
        st.balloons()
        st.session_state.correct_count += 1
    else:
        st.error("Wrong")



if __name__ == '__main__':

    st.title('Poet or GPT?')
    if 'poem' not in st.session_state:
        st.session_state.poem = ""
        st.session_state.real_bool = None
        st.session_state.guessed = False
        st.session_state.correct_count = 0 
    
    st.text(f'Correct Count: {st.session_state.correct_count}')

    poem_btn = st.button('Generate a Poem')
    poem_cont = st.container()

    

    if poem_btn:
        with st.spinner('Wait for it...'):
            poem_info = get_poem("Rupi Kaur")
            st.session_state.poem = poem_info["poem"]
            st.session_state.real_bool = poem_info["real_bool"]
            st.session_state.guessed = False


    with poem_cont:
        st.markdown(st.session_state.poem.replace('\n', '   \n'))

        

    if st.session_state.poem != "" and st.session_state.guessed == False:
        col1, col2  = st.columns(2)
        with col1:
            st.button("That is a Poet", on_click=judge_answer, args=(1, st.session_state.real_bool))

        with col2:
            st.button("That is GPT", on_click=judge_answer, args=(0, st.session_state.real_bool))

    
