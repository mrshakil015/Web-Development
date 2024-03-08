import random
import string

def generateid():
    # Generate a random ID
    randomid = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    return randomid

userid = generateid()
print(userid)
