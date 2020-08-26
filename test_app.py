import streamlit as st
import streamlit.components.v1 as stc
import requests

st.title("Application Data Check")

def main():
    st.sidebar.subheader("Tool checker")
    system = ["","Issues", "Systems", "API" ]
    choice = st.sidebar.selectbox("System Check",system)

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
        st.subheader("Please select check on left screen drop down")
        st.success("System Operational")

    st.sidebar.markdown("---")

if __name__ == '__main__':
    main()

                               
