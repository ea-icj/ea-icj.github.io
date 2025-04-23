#Inequalities selected for V of kron type with dimensions [3, 3, 3, 1]
 
G=LinGroup([3, 3, 3, 1]) 
V = Representation(G,'kron' )
 
brut_inequations=[(2, 0, 1, 2, 0, 1, 0, 2, 1, -4), 
(2, 1, 0, 1, 2, 0, 0, 1, 2, -4), 
(2, 1, 0, 2, 0, 1, 0, 1, 2, -4), 
(1, 0, 0, 0, 1, 0, 1, 0, 1, -2), 
(2, 0, 1, 1, 2, 0, 1, 0, 2, -4), 
(1, 0, 0, 1, 0, 0, 0, 1, 1, -2), 
(1, 0, 0, 0, 0, 1, 1, 1, 0, -2), 
(0, 0, 0, 0, 0, 0, 1, 1, 0, -1), 
 ] 

#inequalities in our formated type Inequality 
inequalities=[Inequality.from_tau(Tau.from_flatten(brut_ineq,G)) for brut_ineq in brut_inequations] 
 
 