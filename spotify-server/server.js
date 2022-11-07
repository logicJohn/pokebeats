
const express = require('express')
const app = express()

const request = require('request');

const port = 5111

const dict = {
    "fire": "rock",
    "electric": "dubstep",
    "water": "blues"
}

// res.json({spotifyuri: ''})

app.get('/', (req, res) => {
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

function checkSpotify(genre) {
    let url = "https://api.spotify.com" 

}


app.listen(port, () => {
    console.log(`Spotify server is listening on port ${port}`)
})