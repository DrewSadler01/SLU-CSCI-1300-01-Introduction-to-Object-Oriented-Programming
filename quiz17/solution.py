####################################
# Students: drew.sadler@slu.edu , derek.mccarty@slu.edu 
####################################

from data import zip2state, zip2pop

state2pop={}
for zipcode,state in zip2state.items():
    if state in state2pop:
        state2pop[state]+=(zip2pop[zipcode])
    else:
        state2pop[state]=zip2pop[zipcode]
        
print(state2pop)


