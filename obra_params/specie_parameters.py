

specie_params = {'spe1':{
                    'mm':{
                        0:{
                        'individual_timestep':400,
                        'max_indivividual_timestep':800,
                        'min_individual_timestep':100,
                        'max_change_individual_timestep':40
                        },
                        1:{
                        'life_span':10,
                        'max_life_span':25,
                        'min_life_span':5,
                        'max_change_life_span':3,
                        },
                        2:{
                        'individual_timesteps_to_be_more_tired':3,
                        'max_individual_timesteps_to_be_more_tired':5,
                        'min_individual_timesteps_to_be_more_tired':2,
                        'max_change_individual_timesteps_to_be_more_tired':1,
                        },
                        3:{
                        'alpha':0.1,
                        'max_alpha':1,
                        'min_alpha':0.001,
                        'max_change_alpha':0.05,
                        },
                        4:{
                        'epsilon':0.1,
                        'max_epsilon':1,
                        'min_epsilon':0.001,
                        'max_change_epsilon':0.05,
                        },
                        5:{
                        'om':0.9,
                        'max_om':1,
                        'min_om':0.1,
                        'max_change_om':0.01,
                        },
                        #Empieza sin poder reproducirse porque 
                        # el número de pasos necesario para
                        # la reproducción es mayor al del máximo
                        # life_span de esta especie
                        6:{
                        'n_steps_to_reproduce':18,
                        'max_n_steps_to_reproduce':20,
                        'min_n_steps_to_reproduce':6,
                        'max_change_n_steps_to_reproduce':2,
                        },
                        7:{
                        'freq_factor':3,
                        'max_freq_factor':6,
                        'min_freq_factor':1,
                        'max_change_freq_factor':1,
                        },
                        8:{
                        'max_rf_effect_in_timesteps':2,
                        'max_max_rf_effect_in_timesteps':20,
                        'min_max_rf_effect_in_timesteps':1,
                        'max_change_max_rf_effect_in_timesteps':1,
                        },
                        9:{
                        #'current_state':'DEFINE',#necesita ser definido
                        'nHarms':0,
                        'max_nHarms':30,
                        'min_nHarms':0,
                        'max_change_nHarms':2
                        }
                        },
                    #heredables
                    'h':{
                        'n_actions':3,
                        'specie':'spe1',
                        'freq_zone_idx':'DEFINE',#necesita ser definido
                        'inherit_Qs':False,
                
                        },

                    'nn':{
                        'timestep_to_act':0,
                        'life_timestep':0,
                        'timesteps_from_last_meal':0,
                        'steps':0,
                        'states_actions':[],
                        'timesteps_alive':0,
                        'D':0,
                        'K':1,
                        'steps_prereproduction':0,
                        'n_times_actions_taken':'DEFINE',
                        'state_counter':'DEFINE',
                        'last_action':None,
                        'current_action':None,
                        'total_current_state':'DEFINE',
                        'total_next_state':'DEFINE',
                        'pan':'DEFINE',
                        'next_state':'DEFINE',
                        'extrinsic_reward':0,
                        'intrin_reward':0,
                        'kind_of_food':'DEFINE',
                        },
                    
                    'nh':{
                        'idx':'DEFINE',
                        'current_state':'DEFINE',
                        }
                    },
                 'spe2':{
                    'mm':{
                        0:{
                        'individual_timestep':400,
                        'max_indivividual_timestep':800,
                        'min_individual_timestep':100,
                        'max_change_individual_timestep':40,
                        },
                        1:{
                        'life_span':10,
                        'max_life_span':15,
                        'min_life_span':5,
                        'max_change_life_span':3,
                        },
                        2:{
                        'individual_timesteps_to_be_more_tired':3,
                        'max_individual_timesteps_to_be_more_tired':5,
                        'min_individual_timesteps_to_be_more_tired':2,
                        'max_change_individual_timesteps_to_be_more_tired':1,
                        },
                        3:{

                        'alpha':0.1,
                        'max_alpha':1,
                        'min_alpha':0.001,
                        'max_change_alpha':0.05,
                        },
                        4:{
                        'epsilon':0.1,
                        'max_epsilon':1,
                        'min_epsilon':0.001,
                        'max_change_epsilon':0.05,
                        },
                        5:{
                        'om':0.9,
                        'max_om':1,
                        'min_om':0.1,
                        'max_change_om':0.01,
                        },
                        #Empieza sin poder reproducirse porque 
                        # el número de pasos necesario para
                        # la reproducción es mayor al del máximo
                        # life_span de esta especie
                        6:{
                        'n_steps_to_reproduce':18,
                        'max_n_steps_to_reproduce':20,
                        'min_n_steps_to_reproduce':16,
                        'max_change_n_steps_to_reproduce':1,
                        },
                        7:{
                        'freq_factor':3,
                        'max_freq_factor':6,
                        'min_freq_factor':1,
                        'max_change_freq_factor':1,
                        },
                        8:{
                        'max_rf_effect_in_timesteps':2,
                        'max_max_rf_effect_in_timesteps':20,
                        'min_max_rf_effect_in_timesteps':1,
                        'max_change_max_rf_effect_in_timesteps':1,
                        },
                        9:{
                        #'current_state':'DEFINE',#necesita ser definido
                        'nHarms':0,
                        'max_nHarms':30,
                        'min_nHarms':0,
                        'max_change_nHarms':2
                        }
                        },
                    #heredables
                    'h':{
                        'n_actions':3,
                        'specie':'spe2',
                        'freq_zone_idx':'DEFINE',#necesita ser definido
                        'inherit_Qs':False,
                
                        },

                    'nn':{
                        'timestep_to_act':0,
                        'life_timestep':0,
                        'timesteps_from_last_meal':0,
                        'steps':0,
                        'states_actions':[],
                        'timesteps_alive':0,
                        'D':0,
                        'K':1,
                        'steps_prereproduction':0,
                        'n_times_actions_taken':'DEFINE',
                        'state_counter':'DEFINE',
                        'last_action':None,
                        'current_action':None,
                        'total_current_state':'DEFINE',
                        'total_next_state':'DEFINE',
                        'pan':'DEFINE',
                        'next_state':'DEFINE',
                        'extrinsic_reward':0,
                        'intrin_reward':0,
                        'kind_of_food':'DEFINE',
                        },
                    
                    'nh':{
                        'idx':'DEFINE',
                        'current_state':'DEFINE',
                        }
                    },
                 'spe3':{
                    'mm':{
                        0:{
                        'individual_timestep':50,
                        'max_indivividual_timestep':100,
                        'min_individual_timestep':20,
                        'max_change_individual_timestep':10,
                        },
                        1:{
                        'life_span':30,
                        'max_life_span':45,
                        'min_life_span':15,
                        'max_change_life_span':3,
                        },
                        2:{
                        'individual_timesteps_to_be_more_tired':10,
                        'max_individual_timesteps_to_be_more_tired':15,
                        'min_individual_timesteps_to_be_more_tired':5,
                        'max_change_individual_timesteps_to_be_more_tired':1,
                        },
                        3:{
                        'alpha':0.1,
                        'max_alpha':1,
                        'min_alpha':0.001,
                        'max_change_alpha':0.05,
                        },
                        4:{
                        'epsilon':0.1,
                        'max_epsilon':1,
                        'min_epsilon':0.001,
                        'max_change_epsilon':0.05,
                        },
                        5:{
                        'om':0.9,
                        'max_om':1,
                        'min_om':0.1,
                        'max_change_om':0.01,
                        },
                        #Empieza sin poder reproducirse porque 
                        # el número de pasos necesario para
                        # la reproducción es mayor al del máximo
                        # life_span de esta especie
                        6:{
                        'n_steps_to_reproduce':21,
                        'max_n_steps_to_reproduce':25,
                        'min_n_steps_to_reproduce':5,
                        'max_change_n_steps_to_reproduce':1,
                        },
                        7:{
                        'freq_factor':3,
                        'max_freq_factor':6,
                        'min_freq_factor':1,
                        'max_change_freq_factor':1,
                        },
                        8:{
                        'max_rf_effect_in_timesteps':2,
                        'max_max_rf_effect_in_timesteps':20,
                        'min_max_rf_effect_in_timesteps':1,
                        'max_change_max_rf_effect_in_timesteps':1,
                        },
                        9:{
                        #'current_state':'DEFINE',#necesita ser definido
                        'nHarms':0,
                        'max_nHarms':30,
                        'min_nHarms':0,
                        'max_change_nHarms':2
                        }
                        },
                    #heredables
                    'h':{
                        'n_actions':3,
                        'specie':'spe3',
                        'freq_zone_idx':'DEFINE',#necesita ser definido
                        'inherit_Qs':True,
                
                        },

                    'nn':{
                        'timestep_to_act':0,
                        'life_timestep':0,
                        'timesteps_from_last_meal':0,
                        'steps':0,
                        'states_actions':[],
                        'timesteps_alive':0,
                        'D':0,
                        'K':1,
                        'steps_prereproduction':0,
                        'n_times_actions_taken':'DEFINE',
                        'state_counter':'DEFINE',
                        'last_action':None,
                        'current_action':None,
                        'total_current_state':'DEFINE',
                        'total_next_state':'DEFINE',
                        'pan':'DEFINE',
                        'next_state':'DEFINE',
                        'extrinsic_reward':0,
                        'intrin_reward':0,
                        'kind_of_food':'DEFINE',
                        },
                    
                    'nh':{
                        'idx':'DEFINE',
                        'current_state':'DEFINE',
                        }
                    },
                 
                 'spe4':{
                    'mm':{
                        0:{
                        'individual_timestep':20,
                        'max_indivividual_timestep':50,
                        'min_individual_timestep':5,
                        'max_change_individual_timestep':10,
                        },
                        1:{
                        'life_span':70,
                        'max_life_span':200,
                        'min_life_span':40,
                        'max_change_life_span':5,
                        },
                        2:{
                        'individual_timesteps_to_be_more_tired':3,
                        'max_individual_timesteps_to_be_more_tired':5,
                        'min_individual_timesteps_to_be_more_tired':2,
                        'max_change_individual_timesteps_to_be_more_tired':1,
                        },
                        3:{
                        'alpha':0.1,
                        'max_alpha':1,
                        'min_alpha':0.001,
                        'max_change_alpha':0.05,
                        },
                        4:{
                        'epsilon':0.1,
                        'max_epsilon':1,
                        'min_epsilon':0.001,
                        'max_change_epsilon':0.05,
                        },
                        5:{
                        'om':0.9,
                        'max_om':1,
                        'min_om':0.1,
                        'max_change_om':0.01,
                        },
                        #Empieza sin poder reproducirse porque 
                        # el número de pasos necesario para
                        # la reproducción es mayor al del máximo
                        # life_span de esta especie
                        6:{
                        'n_steps_to_reproduce':51,
                        'max_n_steps_to_reproduce':55,
                        'min_n_steps_to_reproduce':10,
                        'max_change_n_steps_to_reproduce':5,
                        },
                        7:{
                        'freq_factor':3,
                        'max_freq_factor':6,
                        'min_freq_factor':1,
                        'max_change_freq_factor':1,
                        },
                        8:{
                        'max_rf_effect_in_timesteps':2,
                        'max_max_rf_effect_in_timesteps':20,
                        'min_max_rf_effect_in_timesteps':1,
                        'max_change_max_rf_effect_in_timesteps':1,
                        },
                        9:{
                        #'current_state':'DEFINE',#necesita ser definido
                        'nHarms':0,
                        'max_nHarms':30,
                        'min_nHarms':0,
                        'max_change_nHarms':2
                        }
                        },
                    #heredables
                    'h':{
                        'n_actions':3,
                        'specie':'spe4',
                        'freq_zone_idx':'DEFINE',#necesita ser definido
                        'inherit_Qs':True,
                
                        },

                    'nn':{
                        'timestep_to_act':0,
                        'life_timestep':0,
                        'timesteps_from_last_meal':0,
                        'steps':0,
                        'states_actions':[],
                        'timesteps_alive':0,
                        'D':0,
                        'K':1,
                        'steps_prereproduction':0,
                        'n_times_actions_taken':'DEFINE',
                        'state_counter':'DEFINE',
                        'last_action':None,
                        'current_action':None,
                        'total_current_state':'DEFINE',
                        'total_next_state':'DEFINE',
                        'pan':'DEFINE',
                        'next_state':'DEFINE',
                        'extrinsic_reward':0,
                        'intrin_reward':0,
                        'kind_of_food':'DEFINE',
                        },
                    
                    'nh':{
                        'idx':'DEFINE',
                        'current_state':'DEFINE',
                        }
                    },
                'spe5':{
                    'mm':{
                        0:{
                        'individual_timestep':500,
                        'max_indivividual_timestep':1500,
                        'min_individual_timestep':400,
                        'max_change_individual_timestep':80,
                        },
                        1:{
                        'life_span':5,
                        'max_life_span':10,
                        'min_life_span':1,
                        'max_change_life_span':3,
                        },
                        2:{
                        'individual_timesteps_to_be_more_tired':3,
                        'max_individual_timesteps_to_be_more_tired':5,
                        'min_individual_timesteps_to_be_more_tired':2,
                        'max_change_individual_timesteps_to_be_more_tired':1,
                        },
                        3:{
                        'alpha':0.1,
                        'max_alpha':1,
                        'min_alpha':0.001,
                        'max_change_alpha':0.05,
                        },
                        4:{
                        'epsilon':0.1,
                        'max_epsilon':1,
                        'min_epsilon':0.001,
                        'max_change_epsilon':0.05,
                        },
                        5:{
                        'om':0.9,
                        'max_om':1,
                        'min_om':0.1,
                        'max_change_om':0.01,
                        },
                        #Empieza sin poder reproducirse porque 
                        # el número de pasos necesario para
                        # la reproducción es mayor al del máximo
                        # life_span de esta especie
                        6:{
                        'n_steps_to_reproduce':5,
                        'max_n_steps_to_reproduce':8,
                        'min_n_steps_to_reproduce':2,
                        'max_change_n_steps_to_reproduce':1,
                        },
                        7:{
                        'freq_factor':2,
                        'max_freq_factor':6,
                        'min_freq_factor':1,
                        'max_change_freq_factor':1,
                        },
                        8:{
                        'max_rf_effect_in_timesteps':2,
                        'max_max_rf_effect_in_timesteps':20,
                        'min_max_rf_effect_in_timesteps':1,
                        'max_change_max_rf_effect_in_timesteps':1,
                        },
                        9:{
                        #'current_state':'DEFINE',#necesita ser definido
                        'nHarms':0,
                        'max_nHarms':30,
                        'min_nHarms':0,
                        'max_change_nHarms':2
                        }
                        },
                    #heredables
                    'h':{
                        'n_actions':3,
                        'specie':'spe5',
                        'freq_zone_idx':'DEFINE',#necesita ser definido
                        'inherit_Qs':False,
                
                        },

                    'nn':{
                        'timestep_to_act':0,
                        'life_timestep':0,
                        'timesteps_from_last_meal':0,
                        'steps':0,
                        'states_actions':[],
                        'timesteps_alive':0,
                        'D':0,
                        'K':1,
                        'steps_prereproduction':0,
                        'n_times_actions_taken':'DEFINE',
                        'state_counter':'DEFINE',
                        'last_action':None,
                        'current_action':None,
                        'total_current_state':'DEFINE',
                        'total_next_state':'DEFINE',
                        'pan':'DEFINE',
                        'next_state':'DEFINE',
                        'extrinsic_reward':0,
                        'intrin_reward':0,
                        'kind_of_food':'DEFINE',
                        },
                    
                    'nh':{
                        'idx':'DEFINE',
                        'current_state':'DEFINE',
                        }
                    },
                 'spe6':{
                    'mm':{
                        0:{
                        'individual_timestep':100,
                        'max_indivividual_timestep':500,
                        'min_individual_timestep':50,
                        'max_change_individual_timestep':20,
                        },
                        1:{
                        'life_span':30,
                        'max_life_span':55,
                        'min_life_span':15,
                        'max_change_life_span':3,
                        },
                        2:{
                        'individual_timesteps_to_be_more_tired':3,
                        'max_individual_timesteps_to_be_more_tired':5,
                        'min_individual_timesteps_to_be_more_tired':2,
                        'max_change_individual_timesteps_to_be_more_tired':1,
                        },
                        3:{
                        'alpha':0.1,
                        'max_alpha':1,
                        'min_alpha':0.001,
                        'max_change_alpha':0.05,
                        },
                        4:{
                        'epsilon':0.1,
                        'max_epsilon':1,
                        'min_epsilon':0.001,
                        'max_change_epsilon':0.05,
                        },
                        5:{
                        'om':0.9,
                        'max_om':1,
                        'min_om':0.1,
                        'max_change_om':0.01,
                        },
                        #Empieza sin poder reproducirse porque 
                        # el número de pasos necesario para
                        # la reproducción es mayor al del máximo
                        # life_span de esta especie
                        6:{
                        'n_steps_to_reproduce':11,
                        'max_n_steps_to_reproduce':15,
                        'min_n_steps_to_reproduce':5,
                        'max_change_n_steps_to_reproduce':1,
                        },
                        7:{
                        'freq_factor':2,
                        'max_freq_factor':4,
                        'min_freq_factor':1,
                        'max_change_freq_factor':1,
                        },
                        8:{
                        'max_rf_effect_in_timesteps':2,
                        'max_max_rf_effect_in_timesteps':20,
                        'min_max_rf_effect_in_timesteps':1,
                        'max_change_max_rf_effect_in_timesteps':1,
                        },
                        9:{
                        #'current_state':'DEFINE',#necesita ser definido
                        'nHarms':0,
                        'max_nHarms':30,
                        'min_nHarms':0,
                        'max_change_nHarms':2
                        }
                        },
                    #heredables
                    'h':{
                        'n_actions':3,
                        'specie':'spe6',
                        'freq_zone_idx':'DEFINE',#necesita ser definido
                        'inherit_Qs':True,
                
                        },

                    'nn':{
                        'env':'DEFINE',
                        'feats':'DEFINE',
                        'timestep_to_act':0,
                        'life_timestep':0,
                        'timesteps_from_last_meal':0,
                        'steps':0,
                        'states_actions':[],
                        'timesteps_alive':0,
                        'D':0,
                        'K':1,
                        'steps_prereproduction':0,
                        'n_times_actions_taken':'DEFINE',
                        'state_counter':'DEFINE',
                        'last_action':None,
                        'current_action':None,
                        'total_current_state':'DEFINE',
                        'total_next_state':'DEFINE',
                        'pan':'DEFINE',
                        'next_state':'DEFINE',
                        'extrinsic_reward':0,
                        'intrin_reward':0,
                        'kind_of_food':'DEFINE',
                        },
                    
                    'nh':{
                        'idx':'DEFINE',
                        'current_state':'DEFINE',
                        }
                    },
                 
                  
                 }




specie_params2 = {'spe1':{
                    'mm':{
                        0:{
                        'individual_timestep':400,
                        'max_indivividual_timestep':800,
                        'min_individual_timestep':100,
                        'max_change_individual_timestep':40
                        },
                        1:{
                        'life_span':10,
                        'max_life_span':25,
                        'min_life_span':5,
                        'max_change_life_span':3,
                        },
                        2:{
                        'individual_timesteps_to_be_more_tired':3,
                        'max_individual_timesteps_to_be_more_tired':5,
                        'min_individual_timesteps_to_be_more_tired':2,
                        'max_change_individual_timesteps_to_be_more_tired':1,
                        },
                        3:{
                        'alpha':0.1,
                        'max_alpha':1,
                        'min_alpha':0.001,
                        'max_change_alpha':0.05,
                        },
                        4:{
                        'epsilon':0.1,
                        'max_epsilon':1,
                        'min_epsilon':0.001,
                        'max_change_epsilon':0.05,
                        },
                        5:{
                        'om':0.9,
                        'max_om':1,
                        'min_om':0.1,
                        'max_change_om':0.01,
                        },
                        #Empieza sin poder reproducirse porque 
                        # el número de pasos necesario para
                        # la reproducción es mayor al del máximo
                        # life_span de esta especie
                        6:{
                        'n_steps_to_reproduce':18,
                        'max_n_steps_to_reproduce':20,
                        'min_n_steps_to_reproduce':6,
                        'max_change_n_steps_to_reproduce':2,
                        },
                        7:{
                        'freq_factor':3,
                        'max_freq_factor':6,
                        'min_freq_factor':1,
                        'max_change_freq_factor':1,
                        },
                        8:{
                        'max_rf_effect_in_timesteps':2,
                        'max_max_rf_effect_in_timesteps':20,
                        'min_max_rf_effect_in_timesteps':1,
                        'max_change_max_rf_effect_in_timesteps':1,
                        },
                        9:{
                        #'current_state':'DEFINE',#necesita ser definido
                        'nHarms':0,
                        'max_nHarms':30,
                        'min_nHarms':0,
                        'max_change_nHarms':2
                        }
                        },
                    #heredables
                    'h':{
                        'n_actions':3,
                        'specie':'spe1',
                        'freq_zone_idx':'DEFINE',#necesita ser definido
                        'inherit_Qs':False,
                
                        },

                    'nn':{
                        'timestep_to_act':0,
                        'life_timestep':0,
                        'timesteps_from_last_meal':0,
                        'steps':0,
                        'states_actions':[],
                        'timesteps_alive':0,
                        'D':0,
                        'K':1,
                        'steps_prereproduction':0,
                        'n_times_actions_taken':'DEFINE',
                        'state_counter':'DEFINE',
                        'last_action':None,
                        'current_action':None,
                        'total_current_state':'DEFINE',
                        'total_next_state':'DEFINE',
                        'pan':'DEFINE',
                        'next_state':'DEFINE',
                        'extrinsic_reward':0,
                        'intrin_reward':0,
                        'kind_of_food':'DEFINE',
                        },
                    
                    'nh':{
                        'idx':'DEFINE',
                        'current_state':'DEFINE',
                        }
                    },
                 'spe2':{
                    'mm':{
                        0:{
                        'individual_timestep':400,
                        'max_indivividual_timestep':800,
                        'min_individual_timestep':100,
                        'max_change_individual_timestep':40,
                        },
                        1:{
                        'life_span':10,
                        'max_life_span':15,
                        'min_life_span':5,
                        'max_change_life_span':3,
                        },
                        2:{
                        'individual_timesteps_to_be_more_tired':3,
                        'max_individual_timesteps_to_be_more_tired':5,
                        'min_individual_timesteps_to_be_more_tired':2,
                        'max_change_individual_timesteps_to_be_more_tired':1,
                        },
                        3:{

                        'alpha':0.1,
                        'max_alpha':1,
                        'min_alpha':0.001,
                        'max_change_alpha':0.05,
                        },
                        4:{
                        'epsilon':0.1,
                        'max_epsilon':1,
                        'min_epsilon':0.001,
                        'max_change_epsilon':0.05,
                        },
                        5:{
                        'om':0.9,
                        'max_om':1,
                        'min_om':0.1,
                        'max_change_om':0.01,
                        },
                        #Empieza sin poder reproducirse porque 
                        # el número de pasos necesario para
                        # la reproducción es mayor al del máximo
                        # life_span de esta especie
                        6:{
                        'n_steps_to_reproduce':18,
                        'max_n_steps_to_reproduce':20,
                        'min_n_steps_to_reproduce':16,
                        'max_change_n_steps_to_reproduce':1,
                        },
                        7:{
                        'freq_factor':3,
                        'max_freq_factor':6,
                        'min_freq_factor':1,
                        'max_change_freq_factor':1,
                        },
                        8:{
                        'max_rf_effect_in_timesteps':2,
                        'max_max_rf_effect_in_timesteps':20,
                        'min_max_rf_effect_in_timesteps':1,
                        'max_change_max_rf_effect_in_timesteps':1,
                        },
                        9:{
                        #'current_state':'DEFINE',#necesita ser definido
                        'nHarms':0,
                        'max_nHarms':30,
                        'min_nHarms':0,
                        'max_change_nHarms':2
                        }
                        },
                    #heredables
                    'h':{
                        'n_actions':3,
                        'specie':'spe2',
                        'freq_zone_idx':'DEFINE',#necesita ser definido
                        'inherit_Qs':False,
                
                        },

                    'nn':{
                        'timestep_to_act':0,
                        'life_timestep':0,
                        'timesteps_from_last_meal':0,
                        'steps':0,
                        'states_actions':[],
                        'timesteps_alive':0,
                        'D':0,
                        'K':1,
                        'steps_prereproduction':0,
                        'n_times_actions_taken':'DEFINE',
                        'state_counter':'DEFINE',
                        'last_action':None,
                        'current_action':None,
                        'total_current_state':'DEFINE',
                        'total_next_state':'DEFINE',
                        'pan':'DEFINE',
                        'next_state':'DEFINE',
                        'extrinsic_reward':0,
                        'intrin_reward':0,
                        'kind_of_food':'DEFINE',
                        },
                    
                    'nh':{
                        'idx':'DEFINE',
                        'current_state':'DEFINE',
                        }
                    },
                 'spe3':{
                    'mm':{
                        0:{
                        'individual_timestep':50,
                        'max_indivividual_timestep':100,
                        'min_individual_timestep':20,
                        'max_change_individual_timestep':10,
                        },
                        1:{
                        'life_span':20,
                        'max_life_span':25,
                        'min_life_span':5,
                        'max_change_life_span':3,
                        },
                        2:{
                        'individual_timesteps_to_be_more_tired':10,
                        'max_individual_timesteps_to_be_more_tired':15,
                        'min_individual_timesteps_to_be_more_tired':5,
                        'max_change_individual_timesteps_to_be_more_tired':1,
                        },
                        3:{
                        'alpha':0.1,
                        'max_alpha':1,
                        'min_alpha':0.001,
                        'max_change_alpha':0.05,
                        },
                        4:{
                        'epsilon':0.1,
                        'max_epsilon':1,
                        'min_epsilon':0.001,
                        'max_change_epsilon':0.05,
                        },
                        5:{
                        'om':0.9,
                        'max_om':1,
                        'min_om':0.1,
                        'max_change_om':0.01,
                        },
                        #Empieza sin poder reproducirse porque 
                        # el número de pasos necesario para
                        # la reproducción es mayor al del máximo
                        # life_span de esta especie
                        6:{
                        'n_steps_to_reproduce':21,
                        'max_n_steps_to_reproduce':25,
                        'min_n_steps_to_reproduce':5,
                        'max_change_n_steps_to_reproduce':1,
                        },
                        7:{
                        'freq_factor':3,
                        'max_freq_factor':6,
                        'min_freq_factor':1,
                        'max_change_freq_factor':1,
                        },
                        8:{
                        'max_rf_effect_in_timesteps':2,
                        'max_max_rf_effect_in_timesteps':20,
                        'min_max_rf_effect_in_timesteps':1,
                        'max_change_max_rf_effect_in_timesteps':1,
                        },
                        9:{
                        #'current_state':'DEFINE',#necesita ser definido
                        'nHarms':0,
                        'max_nHarms':30,
                        'min_nHarms':0,
                        'max_change_nHarms':2
                        }
                        },
                    #heredables
                    'h':{
                        'n_actions':3,
                        'specie':'spe3',
                        'freq_zone_idx':'DEFINE',#necesita ser definido
                        'inherit_Qs':True,
                
                        },

                    'nn':{
                        'timestep_to_act':0,
                        'life_timestep':0,
                        'timesteps_from_last_meal':0,
                        'steps':0,
                        'states_actions':[],
                        'timesteps_alive':0,
                        'D':0,
                        'K':1,
                        'steps_prereproduction':0,
                        'n_times_actions_taken':'DEFINE',
                        'state_counter':'DEFINE',
                        'last_action':None,
                        'current_action':None,
                        'total_current_state':'DEFINE',
                        'total_next_state':'DEFINE',
                        'pan':'DEFINE',
                        'next_state':'DEFINE',
                        'extrinsic_reward':0,
                        'intrin_reward':0,
                        'kind_of_food':'DEFINE',
                        },
                    
                    'nh':{
                        'idx':'DEFINE',
                        'current_state':'DEFINE',
                        }
                    },
                 
                 'spe4':{
                    'mm':{
                        0:{
                        'individual_timestep':20,
                        'max_indivividual_timestep':50,
                        'min_individual_timestep':5,
                        'max_change_individual_timestep':10,
                        },
                        1:{
                        'life_span':50,
                        'max_life_span':150,
                        'min_life_span':20,
                        'max_change_life_span':5,
                        },
                        2:{
                        'individual_timesteps_to_be_more_tired':3,
                        'max_individual_timesteps_to_be_more_tired':5,
                        'min_individual_timesteps_to_be_more_tired':2,
                        'max_change_individual_timesteps_to_be_more_tired':1,
                        },
                        3:{
                        'alpha':0.1,
                        'max_alpha':1,
                        'min_alpha':0.001,
                        'max_change_alpha':0.05,
                        },
                        4:{
                        'epsilon':0.1,
                        'max_epsilon':1,
                        'min_epsilon':0.001,
                        'max_change_epsilon':0.05,
                        },
                        5:{
                        'om':0.9,
                        'max_om':1,
                        'min_om':0.1,
                        'max_change_om':0.01,
                        },
                        #Empieza sin poder reproducirse porque 
                        # el número de pasos necesario para
                        # la reproducción es mayor al del máximo
                        # life_span de esta especie
                        6:{
                        'n_steps_to_reproduce':51,
                        'max_n_steps_to_reproduce':55,
                        'min_n_steps_to_reproduce':10,
                        'max_change_n_steps_to_reproduce':5,
                        },
                        7:{
                        'freq_factor':3,
                        'max_freq_factor':6,
                        'min_freq_factor':1,
                        'max_change_freq_factor':1,
                        },
                        8:{
                        'max_rf_effect_in_timesteps':2,
                        'max_max_rf_effect_in_timesteps':20,
                        'min_max_rf_effect_in_timesteps':1,
                        'max_change_max_rf_effect_in_timesteps':1,
                        },
                        9:{
                        #'current_state':'DEFINE',#necesita ser definido
                        'nHarms':0,
                        'max_nHarms':30,
                        'min_nHarms':0,
                        'max_change_nHarms':2
                        }
                        },
                    #heredables
                    'h':{
                        'n_actions':3,
                        'specie':'spe4',
                        'freq_zone_idx':'DEFINE',#necesita ser definido
                        'inherit_Qs':True,
                
                        },

                    'nn':{
                        'timestep_to_act':0,
                        'life_timestep':0,
                        'timesteps_from_last_meal':0,
                        'steps':0,
                        'states_actions':[],
                        'timesteps_alive':0,
                        'D':0,
                        'K':1,
                        'steps_prereproduction':0,
                        'n_times_actions_taken':'DEFINE',
                        'state_counter':'DEFINE',
                        'last_action':None,
                        'current_action':None,
                        'total_current_state':'DEFINE',
                        'total_next_state':'DEFINE',
                        'pan':'DEFINE',
                        'next_state':'DEFINE',
                        'extrinsic_reward':0,
                        'intrin_reward':0,
                        'kind_of_food':'DEFINE',
                        },
                    
                    'nh':{
                        'idx':'DEFINE',
                        'current_state':'DEFINE',
                        }
                    },
                'spe5':{
                    'mm':{
                        0:{
                        'individual_timestep':500,
                        'max_indivividual_timestep':1500,
                        'min_individual_timestep':400,
                        'max_change_individual_timestep':80,
                        },
                        1:{
                        'life_span':10,
                        'max_life_span':12,
                        'min_life_span':1,
                        'max_change_life_span':3,
                        },
                        2:{
                        'individual_timesteps_to_be_more_tired':3,
                        'max_individual_timesteps_to_be_more_tired':5,
                        'min_individual_timesteps_to_be_more_tired':2,
                        'max_change_individual_timesteps_to_be_more_tired':1,
                        },
                        3:{
                        'alpha':0.1,
                        'max_alpha':1,
                        'min_alpha':0.001,
                        'max_change_alpha':0.05,
                        },
                        4:{
                        'epsilon':0.1,
                        'max_epsilon':1,
                        'min_epsilon':0.001,
                        'max_change_epsilon':0.05,
                        },
                        5:{
                        'om':0.9,
                        'max_om':1,
                        'min_om':0.1,
                        'max_change_om':0.01,
                        },
                        #Empieza sin poder reproducirse porque 
                        # el número de pasos necesario para
                        # la reproducción es mayor al del máximo
                        # life_span de esta especie
                        6:{
                        'n_steps_to_reproduce':5,
                        'max_n_steps_to_reproduce':6,
                        'min_n_steps_to_reproduce':2,
                        'max_change_n_steps_to_reproduce':1,
                        },
                        7:{
                        'freq_factor':2,
                        'max_freq_factor':6,
                        'min_freq_factor':1,
                        'max_change_freq_factor':1,
                        },
                        8:{
                        'max_rf_effect_in_timesteps':2,
                        'max_max_rf_effect_in_timesteps':20,
                        'min_max_rf_effect_in_timesteps':1,
                        'max_change_max_rf_effect_in_timesteps':1,
                        },
                        9:{
                        #'current_state':'DEFINE',#necesita ser definido
                        'nHarms':0,
                        'max_nHarms':30,
                        'min_nHarms':0,
                        'max_change_nHarms':2
                        }
                        },
                    #heredables
                    'h':{
                        'n_actions':3,
                        'specie':'spe5',
                        'freq_zone_idx':'DEFINE',#necesita ser definido
                        'inherit_Qs':False,
                
                        },

                    'nn':{
                        'timestep_to_act':0,
                        'life_timestep':0,
                        'timesteps_from_last_meal':0,
                        'steps':0,
                        'states_actions':[],
                        'timesteps_alive':0,
                        'D':0,
                        'K':1,
                        'steps_prereproduction':0,
                        'n_times_actions_taken':'DEFINE',
                        'state_counter':'DEFINE',
                        'last_action':None,
                        'current_action':None,
                        'total_current_state':'DEFINE',
                        'total_next_state':'DEFINE',
                        'pan':'DEFINE',
                        'next_state':'DEFINE',
                        'extrinsic_reward':0,
                        'intrin_reward':0,
                        'kind_of_food':'DEFINE',
                        },
                    
                    'nh':{
                        'idx':'DEFINE',
                        'current_state':'DEFINE',
                        }
                    },
                 'spe6':{
                    'mm':{
                        0:{
                        'individual_timestep':100,
                        'max_indivividual_timestep':500,
                        'min_individual_timestep':50,
                        'max_change_individual_timestep':20,
                        },
                        1:{
                        'life_span':10,
                        'max_life_span':15,
                        'min_life_span':5,
                        'max_change_life_span':3,
                        },
                        2:{
                        'individual_timesteps_to_be_more_tired':3,
                        'max_individual_timesteps_to_be_more_tired':5,
                        'min_individual_timesteps_to_be_more_tired':2,
                        'max_change_individual_timesteps_to_be_more_tired':1,
                        },
                        3:{
                        'alpha':0.1,
                        'max_alpha':1,
                        'min_alpha':0.001,
                        'max_change_alpha':0.05,
                        },
                        4:{
                        'epsilon':0.1,
                        'max_epsilon':1,
                        'min_epsilon':0.001,
                        'max_change_epsilon':0.05,
                        },
                        5:{
                        'om':0.9,
                        'max_om':1,
                        'min_om':0.1,
                        'max_change_om':0.01,
                        },
                        #Empieza sin poder reproducirse porque 
                        # el número de pasos necesario para
                        # la reproducción es mayor al del máximo
                        # life_span de esta especie
                        6:{
                        'n_steps_to_reproduce':11,
                        'max_n_steps_to_reproduce':15,
                        'min_n_steps_to_reproduce':5,
                        'max_change_n_steps_to_reproduce':1,
                        },
                        7:{
                        'freq_factor':2,
                        'max_freq_factor':4,
                        'min_freq_factor':1,
                        'max_change_freq_factor':1,
                        },
                        8:{
                        'max_rf_effect_in_timesteps':2,
                        'max_max_rf_effect_in_timesteps':20,
                        'min_max_rf_effect_in_timesteps':1,
                        'max_change_max_rf_effect_in_timesteps':1,
                        },
                        9:{
                        #'current_state':'DEFINE',#necesita ser definido
                        'nHarms':0,
                        'max_nHarms':30,
                        'min_nHarms':0,
                        'max_change_nHarms':2
                        }
                        },
                    #heredables
                    'h':{
                        'n_actions':3,
                        'specie':'spe6',
                        'freq_zone_idx':'DEFINE',#necesita ser definido
                        'inherit_Qs':True,
                
                        },

                    'nn':{
                        'env':'DEFINE',
                        'feats':'DEFINE',
                        'timestep_to_act':0,
                        'life_timestep':0,
                        'timesteps_from_last_meal':0,
                        'steps':0,
                        'states_actions':[],
                        'timesteps_alive':0,
                        'D':0,
                        'K':1,
                        'steps_prereproduction':0,
                        'n_times_actions_taken':'DEFINE',
                        'state_counter':'DEFINE',
                        'last_action':None,
                        'current_action':None,
                        'total_current_state':'DEFINE',
                        'total_next_state':'DEFINE',
                        'pan':'DEFINE',
                        'next_state':'DEFINE',
                        'extrinsic_reward':0,
                        'intrin_reward':0,
                        'kind_of_food':'DEFINE',
                        },
                    
                    'nh':{
                        'idx':'DEFINE',
                        'current_state':'DEFINE',
                        }
                    },
                 
                  
                 }



import numpy as np

def create_specie(specie,parent_params=None):
        if parent_params is not None:# and parent_params_nonheritable is not None:
                from_parent = True
        else:
                from_parent = False
                
        all_mm_params = []
        #specie = 'spe1'
    #for specie,d_params in specie_params.items():
        params = {specie:[]}
        paramsh = {specie:[]}
        paramsnn = {specie:[]}
        paramsnh = {specie:[]}
        #print('BEFOREEEEE')
        #print(specie_params[specie]['nn'])
        for type_param,d_type_params in specie_params[specie].items():#d_params.items():
            if type_param == 'mm':
                for param,d_values in d_type_params.items():
                    params[specie].append(d_values)
            elif type_param == 'h':
                #for param,d_values in d_type_params.items():
                    paramsh[specie].append(d_type_params)#d_values)
            elif type_param == 'nn':
                #for param,d_values in d_type_params.items():
                    #print('ANTES')
                    #print('d_type_params')
                    #print(d_type_params)
                    paramsnn[specie].append(d_type_params)#d_values)
                    #print('DESPUES')
                    #print(paramsnn[specie])
                    #for arg,val in d_values.items():
                        #pass                
                        #params[specie].append((arg,val))
            elif type_param == 'nh':
                #for param,d_values in d_type_params.items():
                    paramsnh[specie].append(d_type_params)#d_values)
#        print('paramsnn')
 #       print(paramsnn)
        all_mm_params.append((params,paramsh,paramsnn,paramsnh))
        #all_mm_params.append(paramsh)
        #all_mm_params.append(paramsnn)

    #for i in range(len(specie_params)):
     #   print(30*'*')
      #  print(all_mm_params[i])

    #for i in all_mm_params[0][0].values()
      
        spe_params = {}
        spa_nonvar_params = {}
        for i in range(4):
            for value in all_mm_params[0][i].values():
                for element in value:
#                    print(10*'-')
 #                   print(element)
                    #for key,value in element.items():
                    keys = list(element.keys())
                    values = list(element.values())
                    #if i == 2:
                     #       print('i==2')
                      #      print(values)
                    if i == 0:
                        if from_parent == True:
                                #print('**')
                                #print(parent_params)
                                min_v = parent_params[keys[0]] - element[keys[3]]
                                max_v = parent_params[keys[0]] + element[keys[3]]
                        else:
                                min_v = element[keys[0]] - element[keys[3]]
                                max_v = element[keys[0]] + element[keys[3]]

                        if min_v < element[keys[2]]:
                            min_v = element[keys[2]]
                        elif max_v > element[keys[1]]:
                            max_v = element[keys[1]]
  #                      print('keys[0]',keys[0])
                        if keys[0] in ['alpha','epsilon','om']:
                            spe_params[keys[0]] = np.random.uniform(min_v,max_v)
                        else:
                            try:
                                    spe_params[keys[0]] = np.random.randint(min_v,max_v+1)
                            except:
                                    import time
                                    #time.sleep(1)
                                    #print('min_v',min_v)
                                    #print('max_v',max_v)
   #                     print(spe_params[keys[0]])
                    else:
                        for i,key in enumerate(keys):
                            #if from_parent == True:
                             #   parent_params_nonheritable[key] = values[i]
                            #else:
                                #print('key',key)
                                #if key == 'states_actions':
                                 #       print('values[i]')
                                  #      print(values[i])
                                spa_nonvar_params[key] = values[i]
        return spe_params,spa_nonvar_params

spe_params,spa_nonvar_params = create_specie('spe3')
#print(spe_params,spa_nonvar_params)
parent_params = spe_params
parent_nonheritable_params = spa_nonvar_params

cps,cnhps = create_specie('spe3',parent_params)
#print(cps,cnhps)                    #spe_params[]
                        #print(key,' - ',value)
                    
    #print(spe_params)           
        




