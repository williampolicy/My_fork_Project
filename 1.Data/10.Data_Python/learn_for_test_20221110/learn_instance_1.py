# Python program to demonstrate
# instance methods
  
  
class shape:
      
    # Calling Constructor
    def __init__(self, edge, color):
        self.edge = edge
        self.color = color
          
    # Instance Method
    def finEdges(self):
        return self.edge
          
    # Instance Method
    def modifyEdges(self, newedge):
        self.edge = newedge
          
# Driver Code
circle = shape(0, 'red')
square = shape(4, 'blue')
  
# Calling Instance Method
print("No. of edges for circle: "+ str(circle.finEdges()))
  
# Calling Instance Method
square.modifyEdges(6)
  
print("No. of edges for square: "+ str(square.finEdges()))
