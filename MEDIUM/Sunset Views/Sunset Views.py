def sunsetViews(buildings, direction):
  # Direction EAST means facing right , WEST means facing left.
  # We will traverse the array in reverse direction of the given direction
  # For EAST we will traverse right to left and opposite for the WEST
  start = 0 if direction == "WEST" else len(buildings)-1
  idx = start # For left to right idx is 0 , for right to left idx is len(buildings)-1
  ViewBuildings = [] # Store the indexes of the buildings those are true for sunsetViews
  step = 1 if start == 0 else -1 # Increment or decrement based on direction
  maxHeight = 0
  while idx>= 0 and idx<=len(buildings)-1:
    if buildings[idx]>maxHeight:
      ViewBuildings.append(idx)
      maxHeight = buildings[idx]
    #maxHeight = max(buildings[idx], maxHeight)
    idx+=step

  if direction == "EAST":
    return ViewBuildings[::-1]

  return ViewBuildings
