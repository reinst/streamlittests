import streamlit as st
import streamlit.components.v1 as stc
import requests

st.title(" SLEEPY fun")

st.success("Successful")


def main():
    menu = ["Issues", "Systems", "API" ]
    choice = st.sidebar.selectbox("Menu",menu)

    if choice == "Issues":
        st.subheader("Issues Center")
        r = requests.get('http://worldtimeapi.org/api/ip')
        data = r.json()
        time_data = data["utc_datetime"]
        st.write(time_data)

    elif choice == "Systems":
        st.subheader("Systems Check")
        r = requests.get('http://worldtimeapi.org/api/ip')
        data = r.json()
        st.write(data)


    else:
        st.subheader("API Check")

if __name__ == '__main__':
    main()

                               
