import streamlit as st
import functions


todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state['new_todo'] = ""     # Added extra, not included in tutorial; clears text input after hitting enter


st.title("The To Do App")
st.subheader("A minimal web app designed to list to-do items")
st.write("Built by Darin Mujeeb")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        print(checkbox)
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add a to-do here",
              on_change=add_todo, key='new_todo')
