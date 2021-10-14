a='PY TH ON Z'
a1=''
a2=a
a3=a
for i in a:
    x=chr(ord(i)+1)
    a1+=x
    y=a1.replace('!',' ')
    z=y.replace('[','A')
print('sirul 1:',z)
for i in a2:
    w=a2.replace(('Z'), ('A'))
print('sirul 2:', w) 
for i in a3:
    n=a3.replace((' '),('-'))
print('sirul 3:', n)