
import pickle
import streamlit as st
import numpy as np


# Opens the deployed model
model = pickle.load(open('deployed_model.pkl', 'rb'))
scaling = pickle.load(open('scalar_model.pkl', 'rb'))

def predict(user_inputs):
    st.title('Player Rating Sports Prediction')

    user_inputs = np.array(user_inputs)

   # scaled_inputs = scaling.transform([user_inputs])

    makeprediction = model.predict([user_inputs])

    return makeprediction

    # Features
def main():
    cf = st.number_input('cf', 0)
    gk = st.number_input('gk', 0)
    lm = st.number_input('lm', 0)
    lcb = st.number_input('lcb', 0)
    rm = st.number_input('rm', 0)
    potential = st.number_input('potential', 0)
    value_eur = st.number_input('value_eur', 0)
    wage_eur = st.number_input('wage_eur', 0)
    release_clause_eur = st.number_input('release_clause_eur', 0)
    movement_reactions = int(st.number_input('movement_reactions', 0))
    age = int(st.number_input('age', 0))

    
    if st.button('Predict', key='predict_button'):
        
        user_inputs = [gk, lcb, cf, lm, rm, potential, value_eur, wage_eur, release_clause_eur, movement_reactions, age]


        output = predict(user_inputs)
        st.success(f"The player's overall rating is {output[0]}")


        #this is the  code that we will use for prediction
    # if st.button('Predict', key='predict_button'):
    #     makeprediction = model.predict([[gk,lcb,cf,lm,rm,potential,value_eur,wage_eur,release_clause_eur,movement_reactions,age]])
    #     output=round(makeprediction[0],2)
    #     st.success('The player overall performance is {}'.format(output))


if __name__ == '__main__':
    main()


#go to terminal and type (streamlit run football_prediction.py)
