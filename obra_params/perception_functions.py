def get_side_of_nearest_food(env,agent,new_food):
    if agent.nearest_food > abs(agent.current_state - new_food.current_state)\
           and agent.current_state < new_food.current_state:
        return 1
    elif agent.nearest_food > abs(agent.current_state - new_food.current_state)\
           and agent.current_state >= new_food.current_state:
        return -1
    
    return agent.nearest_food

def init_get_side_of_nearest_food(env,agent):
    state = agent.current_state
    if global_poss_food[state] == 1:
        return 0
    for i in range(agent.n_states):
        tmp_state = state - (i+1)
        if tmp_state >= 0:
            if global_poss_food[tmp_state] == 1:
                return -1
        tmp_state = state + (i+1)
        if tmp_state <= agent.n_states - 1:
            if global_poss_food[tmp_state] == 1:
                return 1
                
        
def get_direction_of_nearest_food(actor_current_location,food_locs):
    if len(food_locs) == 0:
        return 0
    
    closest_dist = float('inf')
    
    for food_loc in food_locs:
        if abs(food_loc - actor_current_location) < abs(closest_dist):
            closest_dist = food_loc - actor_current_location
    return 1 if closest_dist < 0 else 2
        


#MEJORAR LA EFICIENCIA
def get_direction_of_most_food(actor_current_location,food_locs):
    if len(food_locs) == 0:
        return 0
    food_locs_c = food_locs.copy()
    food_locs_c.append(actor_current_location)
    food_loc_agent_loc = food_locs_c
##    print('food_locs_c')
##    print(food_locs_c)
##    print('actor_current_location')
##    print(actor_current_location)
##    print('food_loc_agent_loc')
##    print(food_loc_agent_loc)
    
    food_agent_loc_sorted = sorted(food_loc_agent_loc)
    idx_agent_loc = food_agent_loc_sorted.index(actor_current_location)
    how_many_to_left = len(food_agent_loc_sorted[:idx_agent_loc])
    how_many_to_right = len(food_agent_loc_sorted[idx_agent_loc+1:])

    if how_many_to_left > how_many_to_right:
        return 1
    elif how_many_to_left < how_many_to_right:
        return 2
    else:
        return 0

    


    
    






