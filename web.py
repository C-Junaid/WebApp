import streamlit as st
import functions


todos = functions.get_todos()


def add_todo():
    new_todo = st.session_state['new_todo']
    todos.append(new_todo + '\n')
    functions.write_todos(todos)


st.title("My To Do App")
st.subheader("This is my To Do App")
st.write("This app will increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter a todo", placeholder="Add New To Do",
              on_change=add_todo, key='new_todo')
