import streamlit as st

# Title
st.title("✅ AI Code Debugger")

# Description
st.write("Hello, Bujii! Your AI Debugger is Ready 🚀")

# User Input
code = st.text_area("Enter your Python Code:", "")

# Run Button
if st.button("Run Code"):
    try:
        exec(code)
        st.success("✅ Code executed successfully!")
    except Exception as e:
        st.error(f"❌ Error: {e}")
