restaurantsInOurTown = [
    'La Madeleine',
    'Pont Blanc',
    'Olive Garden',
    'Pommes de Terre',
    'Jean"s''LaBoca', 
    'Pont Blanc', 
    'La Madeleine', 
    'Berliner Kueche', 
    'La Madeleine',
    'Olive Garden']
    

setFrench = set(['La Madeleine','Pont Blanc','Jean"s'])
setPark = set(['LaBoca', 'Pont Blanc', 'La Madeleine', 'Berliner Kueche', 'Olive Garden'])

    
# Is the restaurant 'Madeleine' located near a park?
'La Madeleine' in setPark

# Are french restaurants a category of park restaurants?
setFrench < setPark

# Are park restaurants a category of french restaurants?
setFrench > setPark

# We are just hungry, any restaurant is fine!
setFrench | setPark

# Find a french restaurant near a park!
setFrench & setPark

# Find a restaurant that is near a park but not french style!
setPark - setFrench