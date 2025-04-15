# join() - Concatenate any number of strings.
# The string whose method is called is inserted in between each given string.
# The result is returned as a new string.
s1 = 'Python Developer'
s2 = "-".join(s1)
print(s2)
# P-y-t-h-o-n- -D-e-v-e-l-o-p-e-r

s3 = ".".join(s1)
print(s3)
# P.y.t.h.o.n. .D.e.v.e.l.o.p.e.r

str1 = 'Hello'
s4 = str1.join(s1)
print(s4)
# PHelloyHellotHellohHellooHellonHello HelloDHelloeHellovHelloeHellolHellooHellopHelloeHellor


