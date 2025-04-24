#Inequalities selected for V of FermionRepresentation type with dimensions [7]with number of particules = 3
 
G=LinearGroup([7]) 
V = FermionRepresentation(G, 3 )
 
brut_inequations=[(-2, 1, 1, 1, 1, -2, -2), 
(1, -2, 1, 1, -2, 1, -2), 
(1, 1, -2, -2, 1, 1, -2), 
(1, 1, -2, 1, -2, -2, 1), 
 ] 

#inequalities in our formated type Inequality 
inequalities=[Inequality.from_tau(Tau.from_flatten(brut_ineq,G)) for brut_ineq in brut_inequations] 
 
 