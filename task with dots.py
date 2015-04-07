__author__ = 'Agnieszka'
l = ['a', '.', '.', '.', 'd', '.', 'a']

for item in l:
    if l[0] == 'a': continue
    if item == 'd':
        i = l.index('d')


i = l.index('d')

print i

1, i = l.index('d'), l.index('.')
    l[1], l[i] = l[a], l[b]

 #
 # i = ['title', 'email', 'password2', 'password1', 'first_name',
 #         'last_name', 'next', 'newsletter']
 #    a, b = i.index('password2'), i.index('password1')
 #    i[b], i[a] = i[a], i[b]