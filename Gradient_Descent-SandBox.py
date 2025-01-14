# only for for Linear Regression animolz!
# yhat = wx + b 
# loss = (y-yhat)**2 / N 
import numpy as np
# initialise  parameters
x = np.random.randn(10,1)
y = 5*x + np.random.rand()
# Parameters
w = 0.0 
b = 0.0 
# hyperparameter 
learning_rate = 0.01

# gradient descent function
def descend(x, y, w, b, learning_rate): 
    dldw = 0.0 
    dldb = 0.0 
    N = x.shape[0]
    # loss = (y-(wx+b)))**2
    for xi, yi in zip(x,y): 
       dldw += -2*xi*(yi-(w*xi+b))
       dldb += -2*(yi-(w*xi+b))
    
    # update the weight parameter 
    w = w - learning_rate*(1/N)*dldw
    b = b - learning_rate*(1/N)*dldb
    return w, b 

# make updates (iteratively)
for epoch in range(800): 
    w,b = descend(x,y,w,b,learning_rate)
    yhat = w*x + b
    loss = np.divide(np.sum((y-yhat)**2, axis=0), x.shape[0]) 
    print(f'{epoch} loss is {loss}, paramters w:{w}, b:{b}')
print(x,y)

