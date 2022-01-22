import requests

from bs4 import BeautifulSoup

#  https://registration.ueab.ac.ke/ueab/j_security_check
# https://registration.ueab.ac.ke/ueab/a_students.jsp?view=1:0
login_url=('https://registration.ueab.ac.ke/ueab/j_security_check')
dashboard=('https://registration.ueab.ac.ke/ueab/a_students.jsp?view=1:0')
profile=('https://registration.ueab.ac.ke/ueab/a_students.jsp?view=2:0')
school_info=('https://registration.ueab.ac.ke/ueab/a_students.jsp?view=10:0')

username='SKAHMU2011'
#fill out this string to log in
password=''
payload={
    'j_username':username,
    'j_password':password,
}
# dash=requests.post(login_url,data=payload ,verify=False)
# print(dash.text)
with requests.session() as s:
    s.post(login_url,data=payload)
    dashboard_request=s.get(dashboard)
    print(dashboard_request.text)
    profile_request=BeautifulSoup(profile,'lxml')
    school_info_request=BeautifulSoup(school_info,'lxml')
    dash_soup=BeautifulSoup(dashboard_request.content,'lxml')
    profile_soup=BeautifulSoup(profile_request.content,'lxml')
    school_info_soup=BeautifulSoup(school_info_request.content,'lxml')

    
