import random
def generate_index():
    return '{}{}{}_{}{}{}'.format(chr(random.randint(65,90)), chr(random.randint(65,90)), random.randrange(99), random.randrange(99), chr(random.randint(65,90)), chr(random.randint(65,90)))




