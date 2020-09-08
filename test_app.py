import streamlit as st
import streamlit.components.v1 as stc
import requests
import paramiko


st.title("Troubleshooting Command Center")


def sshConnection(nixCommand): 
    formatHostname = f"Connected to: soa-{options1}-{options2}.uhc.com " 
    if customSearch:
        st.write(f'Custom shell search [ {sentence} ]')
    else:
        st.write(f'Shell search: [ {nixCommand} ]')
    try:
        client = paramiko.SSHClient()
        client.load_system_host_keys() # this loads any local ssh keys #BEST to add specific host keys
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname='192.168.1.88', username='t', password='/home/t/.ssh/id_rsa', timeout=10)
        _, ss_stdout, ss_stderr = client.exec_command(nixCommand)
        r_out, r_err = ss_stdout.readlines(), ss_stderr.read()
        if len(r_err) < 5:
            st.success(formatHostname)
            st.write(r_out)
        else:
            st.error('Stderr returned')
        client.close()
    except:
        st.write("Code Exception Error...")
        st.warning("Bad code, SSH Timeout, check connection, or DNS issue")



def main():
    global options1
    global options2
    global customSearch

    systemCheck = ["","Auth", "Syslog" ]
    choice3 = st.sidebar.selectbox("Log Checks",systemCheck, key='3333')
    systemAPI = ["","Alarms", "Updates" ]
    choice4 = st.sidebar.selectbox("API Checks",systemAPI, key='4444')

    # pick server
    options1 = st.selectbox('Pick server type',('cm', 'lda', 'gda'))
    options2 = st.selectbox('Pick server location',('ctc','elr'))
    
    customSearch = st.text_input('Enter custom bash command: ') 
    
    if st.button('run'):
        st.write('')
    else:
        st.write('Click to Run')
        st.stop()

    if choice3 == "Syslog":
        st.subheader("Check Type: Syslog")
        if customSearch:
            sshConnection(customSearch)
        else:
           # sshConnection(linuxCommand())
            sshConnection('tail -n 10 /var/log/syslog')

    if choice3 == "Auth":
        st.subheader("Check Type: Authentication")
        if customSearch:
            sshConnection(customSearch)
        else:
            sshConnection('grep "Accepted publickey" /var/log/auth.log')


if __name__ == '__main__':
    main()
