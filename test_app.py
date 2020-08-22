import streamlit as st
import streamlit.components.v1 as stc
import requests

st.title(" SLEEPY fun")

st.success("Successful")


def main():
    menu = ["Simp", "Limp", "Dimp"]
    choice = st.sidebar.selectbox("Menu",menu)

    if choice == "Simp":
        st.subheader("Calc Simp")
        r = requests.get('http://worldtimeapi.org/api/ip')
        data = r.json()
        time_data = data["utc_datetime"]
        st.write(time_data)

    elif choice == "Limp":
        st.subheader("Calc Limp")
        r = requests.get('http://worldtimeapi.org/api/ip')
        data = r.json()
        st.write(data)


    else:
        st.subheader("Calc Dimp")

if __name__ == '__main__':
    main()

                               
