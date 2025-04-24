#Inequalities selected for V of FermionRepresentation type with dimensions [8]with number of particules = 4
 
G=LinearGroup([8]) 
V = FermionRepresentation(G, 4 )
 
brut_inequations=[(0, 0, 0, 0, 0, 0, 0, -1), 
(3, -1, -1, -1, -1, -1, -1, -1), 
(1, -1, 0, 0, 0, 0, -1, -1), 
(1, 0, -1, 0, 0, -1, 0, -1), 
(1, 0, 0, -1, -1, 0, 0, -1), 
(1, 0, 0, -1, 0, -1, -1, 0), 
(0, 1, 0, -1, 0, -1, 0, -1), 
(0, 0, 1, -1, 0, 0, -1, -1), 
(0, 0, 0, 0, 1, -1, -1, -1), 
(1, 1, 1, -3, -1, -1, -1, -1), 
(1, 1, -1, -1, 1, -3, -1, -1), 
(1, -1, 1, -1, 1, -1, -3, -1), 
(-1, 1, 1, -1, 1, -1, -1, -3), 
(1, -1, -1, 1, 1, -1, -1, -3), 
(1, -1, 1, -1, -1, 1, -1, -3), 
(1, 1, -1, -1, -1, -1, 1, -3), 
 ] 

#inequalities in our formated type Inequality 
inequalities=[Inequality.from_tau(Tau.from_flatten(brut_ineq,G)) for brut_ineq in brut_inequations] 
 
 