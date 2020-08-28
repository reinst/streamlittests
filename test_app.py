import streamlit as st
import streamlit.components.v1 as stc
import requests
import paramiko

st.title("Application Data Check")
dataCenter = [ "CTC", "ELR" ]
defaultDataCenter = 'ctc'
choice1 = st.sidebar.selectbox("Select Data Center",dataCenter, key='1111')
if choice1 == "ELR":
    defaultDataCenter = 'elr'

serverType = [ "GDA","CM", "LDA" ]
defaultServerType = 'gda'
choice2 = st.sidebar.selectbox("Select Server Type",serverType, key='2222')
if choice2 == "CM":
    defaultServerType = 'cm'
elif choice2 == "LDA":
    defaultServerType = 'lda'


def sshConnection(nixCommand):
    formatHostname = f"soa-{defaultDataCenter}-{defaultServerType}.uhc.com" 
    st.write(formatHostname)

    try:
        client = paramiko.SSHClient()
        client.load_system_host_keys() # this loads any local ssh keys
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname='192.168.1.88', username='t', password='/home/t/.ssh/id_rsa')
        _, ss_stdout, ss_stderr = client.exec_command(nixCommand)
        r_out = ss_stdout.readlines()
        st.write(r_out)
        client.close()
        st.success("Command Executed")
    except:
        st.write("Connection Error")
        st.warning("Error")

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

                               
