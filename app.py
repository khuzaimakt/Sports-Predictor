from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from player import predict_player_score_hockey,predict_player_score_football,predict_player_score_basketball
from team import predict_winning_team_hockey,predict_winning_team_football,predict_winning_team_basketball

app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
def read_root():
    return "Welcome to my predictor"


@app.post('/api/predict_hockey')
async def predict_hockey(data: dict):
    num_params = len(data)

    # Check if the number of parameters is not 2 or 3
    if num_params < 2 or num_params > 3:
        raise HTTPException(status_code=400, detail='Invalid number of parameters.')

    # Extract the parameters
    if num_params == 3:
        player = data.get('player')
        team = data.get('team')
        opp_team = data.get('opp_team')

        results = predict_player_score_hockey(player, team, opp_team)

        return results

    if num_params == 2:
        team = data.get('team')
        opp_team = data.get('opp_team')

        results = predict_winning_team_hockey(team, opp_team)

        return results


@app.post('/api/predict_football')
async def predict_football(data: dict):
    num_params = len(data)

    # Check if the number of parameters is not 2 or 3
    if num_params < 2 or num_params > 3:
        raise HTTPException(status_code=400, detail='Invalid number of parameters.')

    # Extract the parameters
    if num_params == 3:
        player = data.get('player')
        team = data.get('team')
        opp_team = data.get('opp_team')

        results = predict_player_score_football(player, team, opp_team)

        return results

    if num_params == 2:
        team = data.get('team')
        opp_team = data.get('opp_team')

        results = predict_winning_team_football(team, opp_team)

        return results
    


@app.post('/api/predict_basketball')
async def predict_basketball(data: dict):
    num_params = len(data)

    # Check if the number of parameters is not 2 or 3
    if num_params < 2 or num_params > 3:
        raise HTTPException(status_code=400, detail='Invalid number of parameters.')

    # Extract the parameters
    if num_params == 3:
        player = data.get('player')
        team = data.get('team')
        opp_team = data.get('opp_team')

        results = predict_player_score_basketball(player, team, opp_team)

        return results

    if num_params == 2:
        team = data.get('team')
        opp_team = data.get('opp_team')

        results = predict_winning_team_basketball(team, opp_team)

        return results
    



