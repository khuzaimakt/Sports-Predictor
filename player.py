
import tensorflow as tf
import numpy as np

def predict_player_score_hockey(player_name, team, opp_team):
    try:
        with open('team_ids_hockey.txt', 'r') as file:
            content_team = file.read()
            team_ids = eval(content_team)

        with open('player_ids_hockey.txt', 'r') as file:
            content_player = file.read()
            player_ids = eval(content_player)

        player_id = player_ids[player_name]
        team_id = team_ids[team]
        opp_team_id = team_ids[opp_team]

        

        input_data = np.array([player_id, team_id, opp_team_id])
        input_data = input_data.reshape(1, 3)

        model = tf.keras.models.load_model('hockey_player.h5')
        predicted_score = model.predict(input_data)[0, 0]

        return {'score':str(predicted_score)}
        
    except KeyError as e:
        return {'Error':f"Error: {e} not found. Please check the team name."}
    except FileNotFoundError:
        return {"Error":"Error: File not found."}
    except Exception as e:
        return {'Error':f"An error occurred: {e}"}



def predict_player_score_football(player_name, team, opp_team):
    try:
        with open('team_ids_football.txt', 'r') as file:
            content_team = file.read()
            team_ids = eval(content_team)

        with open('player_ids_football.txt', 'r') as file:
            content_player = file.read()
            player_ids = eval(content_player)

        player_id = player_ids[player_name]
        team_id = team_ids[team]
        opp_team_id = team_ids[opp_team]

        

        input_data = np.array([player_id, team_id, opp_team_id])
        input_data = input_data.reshape(1, 3)

        model = tf.keras.models.load_model('football_player.keras')
        predicted_score = model.predict(input_data)[0, 0]

        return {'score':str(predicted_score)}
        
    except KeyError as e:
        return {'Error':f"Error: {e} not found. Please check the team name."}
    except FileNotFoundError:
        return {"Error":"Error: File not found."}
    except Exception as e:
        return {'Error':f"An error occurred: {e}"}



def predict_player_score_basketball(player_name, team, opp_team):
    try:
        with open('team_ids_basketball.txt', 'r') as file:
            content_team = file.read()
            team_ids = eval(content_team)

        with open('player_ids_basketball.txt', 'r') as file:
            content_player = file.read()
            player_ids = eval(content_player)

        player_id = player_ids[player_name]
        team_id = team_ids[team]
        opp_team_id = team_ids[opp_team]

        

        input_data = np.array([player_id, team_id, opp_team_id])
        input_data = input_data.reshape(1, 3)

        model = tf.keras.models.load_model('basketball_player.keras')
        predicted_score = model.predict(input_data)[0, 0]

        return {'score':str(predicted_score)}
        
    except KeyError as e:
        return {'Error':f"Error: {e} not found. Please check the team name."}
    except FileNotFoundError:
        return {"Error":"Error: File not found."}
    except Exception as e:
        return {'Error':f"An error occurred: {e}"}
