# Updating the global variable
var = 10
print('GV:',var)
def outer_fn():
    global var
    var = 20
    print('EV:',var)
    def inner_fn():
        global var
        var = 30
        print('Local Var:',var)
    print('before inner',var)
    inner_fn()
    print('after inner', var)

print('Before calling',var)
outer_fn()
print('After calling',var)

# GV 10
# Before calling 10
# EV 20
# before inner 20
# Local Var: 30
# after inner 30
# After calling 30



