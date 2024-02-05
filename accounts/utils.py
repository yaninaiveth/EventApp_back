import jwt

def generateToken(JSONtoken):

    encoded = jwt.encode(JSONtoken, "secret", algorithm="HS256")
    decoded = jwt.decode(encoded, "secret", algorithms=["HS256"])

    return decoded
