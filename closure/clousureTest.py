

def print_msg(msg):
# this is the outside enclosing function
    def printer():
# this is the nested function
        print(msg)
    
    return printer  # this got changed

# Now let's try calling this function.
# Output: Hello
another = print_msg("Hello")
another()

