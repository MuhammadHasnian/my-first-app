import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo=st.session_state["new_todo"]
    todos.append(todo+"\n")
    functions.write_todos(todos)



st.title("My Todo App")
st.subheader("This is my todo App. ")
st.write("This app is to increase your productivity."
         "You can use this app to save your daily goals and "
         "you can double press check box if goal is completed.")


for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        st.session_state["new_todo"] = ""


st.text_input(label="add new todo...",
              placeholder="add a new todo...",
              on_change=add_todo,key="new_todo")

