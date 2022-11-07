
const express = require('express')
const app = express()

const request = require('request');

const https = require('https')

const port = 5111

var SpotifyWebApi = require('spotify-web-api-node');

// credentials are optional

let  client_id = 'x'
let  client_secret = 'x'
let  redirectUri = 'http://www.example.com/callback'


var authOptions = {
    url: 'https://accounts.spotify.com/api/token',
    headers: {
      'Authorization': 'Basic ' + (new Buffer(client_id + ':' + client_secret).toString('base64'))
    },
    form: {
      grant_type: 'client_credentials'
    },
    json: true
  };

const dict = {
    "fire": "rock",
    "electric": "dubstep",
    "water": "blues"
}

// res.json({spotifyuri: ''})

app.get('/', (req, res) => {

    request.post(authOptions, function(error, response, body) {
        if (!error && response.statusCode === 200) {
          var token = body.access_token;
          checkSpotify(token, 'rock')
        }
      });

    res.send("spotify api server is listening\n")
})

app.get('/type1/:type1', (req, res) => {
    const type1 = req.params['type1']
    const genre = pickMusic(type1)
    res.send("\nfirst type receieved: " + type1 + " "+  genre + "\n")

})

app.get('/type1/:type1/type2/:type2', (req, res) => {
    
    let genre = pickMusic(req.params[type1])
    let genre2 = pickMusic(req.params[type2])
    res.send("received two types: " + type1 + type2 + genre + genre2)
})

function pickMusic(pokemonType) {

     return dict[pokemonType]
}

function checkSpotify(token, genre) {
    let url = "https://api.spotify.com/v1/" 
    url = url + "recommendations/available-genre-seeds"
    token = "Bearer " + token
    var options = {
        'method': 'GET',
        'url'  : url,
        'headers': {
            'Authorization': token,
            'Content-Type': 'application/json'
        }
    }

    request(options, function (error, response) {
        if (error) throw new Error(error);
        console.log(response.body)
    })
}

app.listen(port, () => {
    console.log(`Spotify server is listening on port ${port}`)
})