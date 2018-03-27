from flask import Flask, render_template, request
import jwt
from jwt.contrib.algorithms.pycrypto import RSAAlgorithm

app = Flask(__name__)

jwt.register_algorithm('RS256', RSAAlgorithm(RSAAlgorithm.SHA256))


def is_token_valid(token):
    pems_dict = {
        'kid1': 'pem1',
        'kid2': 'pem2'
    }

    kid = jwt.get_unverified_header(token)['kid']
    pem = pems_dict.get(kid, None)

    if pem is None:
        print 'kid false'
        return False

    try:
        decoded_token = jwt.decode(token, pem, algorithms=['RS256'])
        iss = 'https://cognito-idp.us-east-2.amazonaws.com/us-east-2_I1ZQrSsWb'
        if decoded_token['iss'] != iss:
            print 'iss false'
            return False
        elif decoded_token['token_use'] != 'access':
            print 'access false'
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
