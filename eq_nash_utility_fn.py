#Edgar Tobon Sosa
#18.01.2026

#Program to calculate de utility function in a climate strategy domain problem

#CONSTANTS
EMISION_CITIES_VALUES = [0.9, 0.7, 0.4, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ]
RISK_CITIES_VALUES = [0.6, 0.4, 0.6, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ]
TECHNOLOGICAL_CITIES_VALUES = [0.4, 0.8, 0.3, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ]

#OBJECTIVE: Calculate the scalar value of the Benifit in the city_i
#PARAMETERS: 
	# DELTA: constant value emission reduction weight
	# ei: emission reduction of the city
	# e_max: maximum emissions of the cities 
	# THETA: the cooperation benefit weight
	# coop: binary operator (1: cooperate, 0: no cooperate)
def benefit_city (DELTA, ei, e_max, THETA, coop):
	B = DELTA[ 1 - ( ei/e_max ) ] + THETA(coop)
	return (B)

#OBJECTIVE: Calculate the scalar value of the Cost in the city_i
#PARAMETERS: 
	# GAMMA: constant value of cost weight
	# ti: smart score of the city
	# t_max: highest score 
def cost_city (GAMMA,ti, t_max):
	C = GAMMA[ 1 - ( ti/t_max ) ]
	return (C)

#OBJECTIVE: Calculate the utility funciont; U(X) -> R
	# i: The selectect city, i -> {1,2,3,4,...,n}
	# ei: emission reduction of the city
	# e_max: maximum emissions of the cities 
	# coop: binary operator (1: cooperate, 0: no cooperate)
	# t_max: highest score
	# ALPHA, BETHA, GAMMA : constant values 
def utility_city (i, e_max, coop, t_max, ALPHA, BETHA, GAMMA):
	ei = EMISION_CITIES_VALUES[i]
	ri = RISK_CITIES_VALUES[i]
	ti = TECHNOLOGICAL_CITIES_VALUES[i]

	B = benefit_city (DELTA, ei, e_max, THETA, coop)
	C = cost_city (GAMMA, ti, t_max)
	
	U = [ALPHA * B] - [BETHA * C]  - [GAMMA * ri]

	return (U)


 
