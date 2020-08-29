import streamlit as st
import streamlit.components.v1 as stc
import requests
import paramiko
import json


if st.button("start"):
    st.write("starting")
else:
    st.write("stopping")

# pick server
options1 = st.selectbox('pick server type',('cm', 'lda', 'gda'))
options2 = st.selectbox('pick server location',('ctc','elr'))

st.title("Application Data Check")

def sshConnection(nixCommand):
    formatHostname = f"Connecting to [ soa-{options1}-{options2}.uhc.com ]" 
    st.write(formatHostname)

    try:
        client = paramiko.SSHClient()
        client.load_system_host_keys() # this loads any local ssh keys #BEST to add specific host keys
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname='192.168.11.88', username='t', password='/home/t/.ssh/id_rsa', timeout=10)
        _, ss_stdout, ss_stderr = client.exec_command(nixCommand)
        r_out = ss_stdout.readlines()
        st.write(r_out)
        client.close()
        st.success("Command Executed")
    except:
        st.write("Connection Error...")
        st.warning("SSH Timeout, check connection or DNS")

def main():
    systemCheck = ["","Auth", "Syslog" ]
    choice3 = st.sidebar.selectbox("Log Checks",systemCheck, key='3333')
    systemAPI = ["","Alarms", "Updates" ]
    choice4 = st.sidebar.selectbox("API Checks",systemAPI, key='4444')

    if choice3 == "Syslog":
        st.subheader("Syslog check")
        sshConnection('tail -n 10 /var/log/syslog')

    if choice3 == "Auth":
        st.subheader("Accepted publickey check")
        sshConnection('grep "Accepted publickey" /var/log/auth.log')


if __name__ == '__main__':
    main()

                               
