import streamlit as st
import streamlit.components.v1 as stc
import requests

st.title("Application Data Check")

st.success("Successful")
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
                )

def main():
    system = ["Issues", "Systems", "API" ]
    choice = st.sidebar.selectbox("System Check",system)
    firewall = ["firewalls", "pano", "syslog"]
    choice2 = st.sidebar.markdown("firewall data", firewall)

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

                               
