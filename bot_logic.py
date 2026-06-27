import random
def gen_pass(pass_legth):
    elements = "+-/*!&$#?=@<>"
    password =  ""

    for i in range(pass_legth):
        password += random.choice(elements)

        return password