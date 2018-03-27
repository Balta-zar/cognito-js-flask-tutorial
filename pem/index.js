var request = require('request');
var jwkToPem = require('jwk-to-pem');

//url: 'https://cognito-idp.{region}.amazonaws.com/{userPoolId}/.well-known/jwks.json'
request({
    url: 'https://cognito-idp.us-east-2.amazonaws.com/us-east-2_I1ZQrSsWb/.well-known/jwks.json',
    json: true
}, function (error, response, body) {
    if (!error && response.statusCode === 200) {
        pems = {};
        var keys = body['keys'];
        for(var i = 0; i < keys.length; i++) {
            //Convert each key to PEM
            var key_id = keys[i].kid;
            var modulus = keys[i].n;
			var exponent = keys[i].e;
            var key_type = keys[i].kty;
            var jwk = { kty: key_type, n: modulus, e: exponent};
            var pem = jwkToPem(jwk);
            pems[key_id] = pem;
        }
        console.log(pems);
    } else {
        console.error("error");
    }
});
