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
        for i in data:
            st.write(i["utc_datetime"])

    elif choice == "Limp":
        st.subheader("Calc Limp")

    else:
        st.subheader("Calc Dimp")

if __name__ == '__main__':
    main()

                               
