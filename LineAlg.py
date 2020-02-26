from bresenham import bresenham

U = 0
D = 1
L = 2
R = 3

def drawLine(curr_x, curr_y, x, y):
  
  instructions = []

  # returns list of new coordinates in order they would be visited
  # a la [(-1, -4), (0, -3), (0, -2), (1, -1), (2, 0), (2, 1), (3, 2)]
  coords = bresenham(curr_x, curr_y, int(x), int(y))
  
  for i in coords[1:]: # start at second index
    
    # horizontal movement
    if coords[i][0] > coords[i-1][0]:
      instructions.append(R)
    elif coords[i][0] < coords[i-1][0]:
      instructions.append(L)
      
    # vertical movement
    if coords[i][1] > coords[i-1][1]:
      instructions.append(U)
    elif coords[i][1] < coords[i-1][1]:
      instructions.append(D)
    
    
  return instructions
 