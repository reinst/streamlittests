import streamlit as st
import streamlit.components.v1 as stc
import requests
import paramiko


st.title("Application Data Check")

def sshConnection(nixCommand): 
    formatHostname = f"Connected to: soa-{options1}-{options2}.uhc.com " 
    if sentence:
        st.write(f'Using custom search [ {sentence} ]')

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
    global sentence

    systemCheck = ["","Auth", "Syslog" ]
    choice3 = st.sidebar.selectbox("Log Checks",systemCheck, key='3333')
    systemAPI = ["","Alarms", "Updates" ]
    choice4 = st.sidebar.selectbox("API Checks",systemAPI, key='4444')

    # pick server
    options1 = st.selectbox('pick server type',('cm', 'lda', 'gda'))
    options2 = st.selectbox('pick server location',('ctc','elr'))
    
    sentence = st.text_input('Enter custum bash command: ') 
    
    if st.button('run'):
        st.write('')
    else:
        st.write('Click to Run')
        st.stop()

    if choice3 == "Syslog":
        st.subheader("Check Type: Syslog")
        if sentence:
            sshConnection(sentence)
        else:
            sshConnection('tail -n 10 /var/log/syslog')

    if choice3 == "Auth":
        st.subheader("Check Type: Authentication")
        if sentence:
            sshConnection(sentence)
        else:
            sshConnection('grep "Accepted publickey" /var/log/auth.log')

if __name__ == '__main__':
    main()

                               
