from flask import Flask, render_template, request
import jwt
from jwt.contrib.algorithms.pycrypto import RSAAlgorithm

app = Flask(__name__)

jwt.register_algorithm('RS256', RSAAlgorithm(RSAAlgorithm.SHA256))

def is_token_valid(token):
    pem = '-----BEGIN RSA PUBLIC KEY-----\nMIIBCgKCAQEAk1dH4Dyl4o3asYqguy+A+1/bXuPGnMXbj41H9zVTcmTCznW2ajjh\nl7+sBAJWnxsd+z43SlPzQ/EiOd144G37w84xln6VMPsjMgRf0Pwlo9rEsmhTS3ly\npR8eOMrQRN65qqo7z2+xtYwzfb+4F49QTFG18ggFMnbmrCE9LWLEyxIQ7kYwYOw9\nPpVooeSAlD4wXYdYI4pGvqCRtYfVfRbQT5GEmwLALTUvhGMhKZHVlwD4nlSo3kNA\n7VMzfOAAKyiB+lNKFBopL1qwQWC61xPfxNt3O+cSrq4lOBUHHnhNHz7OfVyXj6xx\nBRJziO4Zo9Ve7nxEcRpzK/mlkx7jSdHDNwIDAQAB\n-----END RSA PUBLIC KEY-----\n'
    try:
        decoded_token = jwt.decode(token, pem, algorithms=['RS256'])
        iss = 'https://cognito-idp.us-east-2.amazonaws.com/us-east-2_I1ZQrSsWb'
        if decoded_token['iss'] != iss:
            print 'iss false'
            return False
        elif decoded_token['token_use'] != 'access':
            print 'access false'
            return False
        kid = 'kuyzfrEKql8/C5riRiesrSu1DmCIwtbyW8E5rxNBoDo='
        if jwt.get_unverified_header(token)['kid'] != kid:
            print 'kid false'
            return False
        return True
    except Exception:
        return False


@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/code_registration")
def code_registration():
    return render_template('code_registration.html')


@app.route("/welcome")
def welcome():
    return render_template('welcome.html')


@app.route("/api/protected_api", methods=["POST"])
def protected_api():
    access_token = request.form['access_token']
    if (is_token_valid(access_token)):
        return 'some protected data from api'
    else:
        return 'bad token', 401


if __name__ == '__main__':
    app.run(debug=True)
