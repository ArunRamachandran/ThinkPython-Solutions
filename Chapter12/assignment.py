# to split an email id into a user and a domain

addr = 'arunkramachandran92@gmail.com'

uname, domain = addr.split('@')

print uname
print domain

# The return value from split is a list with two elements; the first element
# is assigned to uname, the second to domain


