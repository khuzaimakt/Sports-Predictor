import tensorflow as tf
import numpy as np


def predict_winning_team_hockey(team, opp_team):
    try:
        with open('team_ids_hockey.txt', 'r') as file:
            content_team = file.read()
            team_ids = eval(content_team)

        model = tf.keras.models.load_model('hockey_team.h5')

        team_id = team_ids[team]
        opp_team_id = team_ids[opp_team]

        input_data = np.array([[team_id, opp_team_id]])
        probability = model.predict(input_data)[0][0]  # Probability of winning

        results= {
            team: probability * 100,
            opp_team: (1 - probability) * 100
        }

        return results


    except KeyError as e:
        return {'Error':f"Error: {e} not found. Please check the team name."}
    except FileNotFoundError:
        return {"Error":"Error: File not found."}
    except Exception as e:
        return {'Error':f"An error occurred: {e}"}



def predict_winning_team_football(team, opp_team):
    try:
        with open('team_ids_football.txt', 'r') as file:
            content_team = file.read()
            team_ids = eval(content_team)

        model = tf.keras.models.load_model('football_team.keras')

        team_id = team_ids[team]
        opp_team_id = team_ids[opp_team]

        input_data = np.array([[team_id, opp_team_id]])
        probability = model.predict(input_data)[0][0]  # Probability of winning

        results= {
            team: probability * 100,
            opp_team: (1 - probability) * 100
        }

        return results

    except KeyError as e:
        return {'Error':f"Error: {e} not found. Please check the team name."}
    except FileNotFoundError:
        return {"Error":"Error: File not found."}
    except Exception as e:
        return {'Error':f"An error occurred: {e}"}



def predict_winning_team_basketball(team, opp_team):
    try:
        with open('team_ids_basketball.txt', 'r') as file:
            content_team = file.read()
            team_ids = eval(content_team)

        model = tf.keras.models.load_model('basketball_team.keras')

        team_id = team_ids[team]
        opp_team_id = team_ids[opp_team]

        input_data = np.array([[team_id, opp_team_id]])
        probability = model.predict(input_data)[0][0]  # Probability of winning

        results= {
            team: probability * 100,
            opp_team: (1 - probability) * 100
        }

        return results

    except KeyError as e:
        return {'Error':f"Error: {e} not found. Please check the team name."}
    except FileNotFoundError:
        return {"Error":"Error: File not found."}
    except Exception as e:
        return {'Error':f"An error occurred: {e}"}
