from PIL import Image
from math import floor
import numpy as np
import time

SIZE = 101  # board will be SIZE by SIZE pixels
SAND_GRAINS = 10000  # grains of sand to start with

start_time = time.time()

board = np.zeros((SIZE, SIZE))  # 2d array filled with 0s
board[floor(SIZE/2)][floor(SIZE/2)] = SAND_GRAINS  # put all the grains in the middle



# THIS IS THE ONLY PART YOU NEED TO WRITE!
# the code here should loop through iterations of the fractal, toppling the sand
# you'll need this to happen in a loop until all the pixels have <4 grains of sand
# as long as there are still any with at least 4, topple 1 onto each neighboring pixel






# finish timing
end_time = time.time()
print("Generation took: ",  end_time-start_time)

# display board
coloredBoard = np.zeros( (2*SIZE, 2*SIZE, 3), dtype=np.uint8)

for i in range(SIZE):
  for j in range(SIZE):
    if board[i][j] == 0:
      coloredBoard[2*i:2*i+2,2*j:2*j+2] = [255,255,255]
    elif board[i][j] == 1:
      coloredBoard[2*i:2*i+2,2*j:2*j+2] = [150,150,255]
    elif board[i][j] == 2:
      coloredBoard[2*i:2*i+2,2*j:2*j+2] = [50,50,200]
    else:
      coloredBoard[2*i:2*i+2,2*j:2*j+2] = [0,0,255]

img = Image.fromarray(coloredBoard, 'RGB')
#img.save('my.png')
img.show()

end_time = time.time()
print("Program took: ",  end_time-start_time)