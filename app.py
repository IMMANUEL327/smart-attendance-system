import streamlit as st

# APPLICATION TITLE
st.title("Smart Attendance System")
st.write("welcome to our smart attendance system. Please register to mark your attendance.")

#INITIALIZE STUDENT STORAGE
if "students" not in st.session_state:
    st.session_state.students = []
    
# STUDENT REGISTRATION
st.subheader("Student Registration")
student_name = st.text_input("Enter your full name")
student_id = st.text_input("Enter your student ID")

if st.button("Register"):
    # Validate input fields
    if student_name.strip() == "" or student_id.strip() == "":
        st.error("Please fill in all the fields.")
        
    else:
        #CHECK FOR DUPLICATE STUDENT ID
        duplicate = False
        for existing_student in st.session_state.students:
            if existing_student["student ID"] == student_id.strip():
                duplicate = True
                break
            #Register only if ID is not duplicate
        if duplicate:
            st.error("this student ID is already registered.")
        else:
            student = {
                "name": student_name.strip(), 
                "student ID": student_id.strip()
            }
            
            st.session_state.students.append(student)
            st.success(f"welcome {student_name}, you have been registered successfully!")
            st.info("Registration complete. You can now mark your attendance.")
            
            #DISPLAY REGISTERED STUDENTS
        st.subheader("Registered Students")
        if st.session_state.students:
            st.dataframe(
                         st.session_state.students,
                         use_container_width=True                   
                    )
            st.write(f"Total registered students: {len(st.session_state.students)}")
        else:
            st.write("No students have registered yet.")
            
            #REMOVE A REGISTERED STUDENT
            st.subheader("Remove Registered Student")
            if st.session_state.students:
                student_id = [
                    student["student ID"] 
                    for student in st.session_state.students
                ]
                student_id = st.selectbox("Select student ID to remove", student_id)
                if st.button("Remove Student"):
                    st.session_state.students = [
                        student for student in st.session_state.students 
                        if student["student ID"] != student_id
                    ]
                    st.success("student removed successfully.")
                    st.rerun()
                else:
                    st.write(" there are no students to remove.")
        