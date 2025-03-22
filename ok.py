import time
import streamlit as st
st.balloons()

st.title("Python")
st.subheader("Before learning Python , Please enter the following info below:")
name = st.text_input("Enter your name :")
mobile = st.text_input("Enter your mobile number:")
adress = st.text_area("Enter your Address:")
classd = st.selectbox("Choose your STD",(1,2,3,4,5,6,7,8,9,10))

button= st.button("Done!")
with st.spinner('Wait for it...'):
    time.sleep(5)
st.success('Done!')
if button:
    st.markdown(f"""
Name = {name}


Mobile Number = {mobile}


Adresss = {adress}


Class = {classd}

""")

st.subheader("Let's Learn Python !")
st.header("What is Python ?")
st.write("""
Python is a programming language that is used for a variety of tasks, including web development, data science, and software development. It is a general-purpose language that is easy to learn and use. 

         
         """)
st.header("Features of Python :-")
st.write("""
Easy to learn : Python is a beginner-friendly language with easy-to-read syntax. 

Versatile : Python can be used for a variety of tasks, including scientific computing, web development, and automation. 

Open-source : Python is an open-source community language, so many independent programmers are constantly building libraries and functionality for it. 


""")
st.header("Uses of Python:-")
st.write("""


         
Web development : Python is used to create websites and web applications. 

Data science : Python is used for data analysis, data visualization, and machine learning. 

Software development  : Python is used to develop software, including software testing, bug tracking, and build control. 

Automation : Python is used to automate tasks, such as organizing finances. 



""")
st.subheader("Now! we will take a few examples of Python:")
st.code("""
        
        print("Hello World")
        
        """)
st.write("In the above example the statement PRINT is used to display , if we write firstly PRINT and then add brackets , add double quotes and write Hello World in it , it will display Hello World in terminal box ")
st.subheader("Python Indentation")
st.write("""
Indentation refers to the spaces at the beginning of a code line.

Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important.

Python uses indentation to indicate a block of code.

""")
st.code("""

if 5 > 2:
  print("Five is greater than two!")
""")
st.write("Python will give you an error if you skip the indentation:")
st.subheader("Python Syntax")
st.write("""



Comments can be used to explain Python code.

Comments can be used to make the code more readable.

Comments can be used to prevent execution when testing code.
         """)
st.code("""
#This is a comment
print("Hello, World!")


""")
st.subheader("Variable")
st.write("""
Variables are containers for storing data values.

""")
st.subheader("Creating a Variable")
st.write("""
         
Python has no command for declaring a variable.

A variable is created the moment you first assign a value to it. 
         
         """)
