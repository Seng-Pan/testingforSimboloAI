import streamlit as st

st.title("TO-Do List")

task = st.text_input("Enter your task")

if "task_list" not in st.session_state:
    st.session_state["task_list"] = []

if st.button("Add Task"):
    if task:    # only add task if the input is not empty
        st.session_state["task_list"].append(task)

for i,t in enumerate(st.session_state["task_list"]):
    st.write(f"{i+1}. {t}")

for i, key_val in enumerate(st.session_state["task_list"]):
    if st.checkbox(f"Done: {key_val}"):
        st.session_state["task_list"].remove(key_val)







