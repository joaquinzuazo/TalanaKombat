# Talana Kombat JRPG

Talana Kombat is a game where 2 characters  _Tonyn Stallone_ and _Arnaldor Shuatseneguer_ fight each other to the death. Each character has 2 special hits that are executed with a combination of moves + 1 hit button.
This application is for the challenge of [Talana](https://web.talana.com/).

## The game:

- Each player starts with 6 health points.
- Each player has 2 special attacks (dealing 2 and 3 damage each) and 2 basic attacks (dealing 1 damage each).
- Each player submits their moves for the entire game as a "list" of "sequences".
- The game is played in turns, and the turn order is determined by the duration of each player's move (shortest first). If the moves are the same duration, player one goes first.
- The game ends when any player loses all his health points. In the event that this does not happen, at the end of the rounds, the player with the most health points at that time wins or a tie may also occur.
- Moves will only be `W`, `A`, `S` or `D` for movement, and `P` or `K` for attacks

## Dependencies:

The API is developed in with the following dependencies:

-   Django
-   djangorestframework
-   pytest
-   black

## Prerequisites:
-   Docker
-   Postman or similar
-   A copy of this project on your computer


How can I install and use it? I recommend downloading and installing the desktop version for its simplicity
[Docker desktop](https://www.docker.com/products/docker-desktop/).
In Postman's case, [Postman](https://www.postman.com/).


## How to run this project?
Once you have the prerequisites, you must execute the following commands in the root of the project:
```sh
docker-composer build
```
subsequently
```sh
docker-composer up
```

If you receive the following messages, you are ready to run:
```sh
web_1  | Django version 4.1, using settings 'kombat.settings'
web_1  | Starting development server at http://0.0.0.0:8000/
```

Once the project is executed, you must send a request to the following url: http://127.0.0.1:8000/ of type POST with the information of the corresponding fight.
```sh
POST http://127.0.0.1:8000/
```
### Request structure:
The structure of the information must travel in the body of the request as json raw type.
```json
{
    "player1":{
        "movimientos":["D","DSD","S","DSD","SD"],
        "golpes":["K","P","","K","P"]
    },
    "player2":{
        "movimientos":["SA","SA","SA","ASA","SA"],
        "golpes":["K","","K","P","P"]
    }
}
```
another example:
```json
{
    "player1":{
        "movimientos":["SDD", "DSD", "SA", "DSD"],
        "golpes":["K", "P", "K", "P"]
    },
    "player2":{
        "movimientos":["DSD", "WSAW", "ASA", "", "ASA", "SA"],
        "golpes":["P", "K", "K", "K", "P", "k"]
    }
}
```

### Response structure:
If the request is correct, you will receive a status 200 and the following response:
```json
{
    "combat": [
        "Tonyn se mueve y lanza un golpe de puño",
        "Arnaldor lanza un golpe de puño",
        "Tonyn se mueve",
        "Arnaldor se mueve",
        "Arnaldor se mueve",
        "Arnaldor se mueve",
        "Arnaldor se mueve",
        "Arnaldor se mueve",
        "Terminaron las rondas y hay un empate, al finalizar las rondas ambos tienen 5 puntos de salud"
    ]
}
```
If any data in the request is wrong, you will receive a status 400 and the following response:
```json
{
    "message": "Alguna dato se encuentra vacío o incorrecto"
}
```
