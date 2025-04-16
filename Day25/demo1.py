# Enclosed scope:
# Nested Functions: The Enclosing Scope
# Enclosing or nonlocal scope is observed when you nest functions inside other functions.
# The enclosing scope was added in Python 2.2. It takes the form of the local scope of any enclosing function’s
# local scopes.
# Names that you define in the enclosing Python scope are commonly known as nonlocal names.

def outer_fn():
    v = 10
    print('Enclosed Var:',v) # Enclosing variable
    def inner_fn():
        v1 = 20
        print('Local Var:',v1)
        print('EV inside inner_fn',v)

    inner_fn()

# print('EV',v)
# NameError: name 'v' is not defined
outer_fn()

# Enclosed Var: 10
# Local Var: 20
# EV inside inner_fn 10