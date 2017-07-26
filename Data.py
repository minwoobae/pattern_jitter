import numpy as np

x_tilde = [10, 15, 22, 29, 34, 40, 45, 51]
# x_tilde = [10, 15, 22, 29, 34, 40, 45, 51, 55]
# L = 5; R = 4

# initDist: p(X_1)
initDist = [5/15, 4/15, 3/15, 2/15, 1/15]

# p(X_2 | X_1)
p2 = np.array([[5/22, 5/22, 5/22, 4/22, 3/22],
               [0, 5/17, 5/17, 4/17, 3/17],
               [0, 0, 5/12, 4/12, 3/12],
               [0, 0, 0, 4/7, 3/7],
               [0, 0, 0, 0, 1]])
# p(X_3 | X_2)
p3 = np.array([[5/22, 5/22, 5/22, 4/22, 3/22],
               [5/22, 5/22, 5/22, 4/22, 3/22],
               [5/22, 5/22, 5/22, 4/22, 3/22],
               [0, 5/17, 5/17, 4/17, 3/17],
               [0, 0, 5/12, 4/12, 3/12]])

# p(X_4 | X_3)
p4 = np.array([[5/15, 4/15, 2/15, 2/15, 1/15],
               [5/15, 4/15, 2/15, 2/15, 1/15],
               [5/15, 4/15, 2/15, 2/15, 1/15],
               [0, 4/10, 3/10, 2/10, 1/10],
               [0, 0, 3/6, 2/6, 1/6]])

# p(X_5 | X_4)
p5 = np.array([[5/19, 5/19, 4/19, 3/19, 2/19],
               [0, 5/14, 4/14, 3/14, 2/14],
               [0, 0, 4/9, 3/9, 2/9],
               [0, 0, 0, 3/5, 2/5],
               [0, 0, 0, 0, 1]])

# p(X_6 | X_5)
p6 = np.array([[5/15, 4/15, 2/15, 2/15, 1/15],
               [5/15, 4/15, 2/15, 2/15, 1/15],
               [0, 4/10, 3/10, 2/10, 1/10],
               [0, 0, 3/6, 2/6, 1/6],
               [0, 0, 0, 2/3, 1/3]])

# p(X_7 | X_6)
p7 = np.array([[5/19, 5/19, 4/19, 3/19, 2/19],
               [0, 5/14, 4/14, 3/14, 2/14],
               [0, 0, 4/9, 3/9, 2/9],
               [0, 0, 0, 3/5, 2/5],
               [0, 0, 0, 0, 1]])
# p(X_8 | X_7)

p8 = np.array([[1/5, 1/5, 1/5, 1/5, 1/5],
               [1/5, 1/5, 1/5, 1/5, 1/5],
               [0, 1/4, 1/4, 1/4, 1/4],
               [0, 0, 1/3, 1/3, 1/3],
               [0, 0, 0, 1/2, 1/2]])
'''
p8 = np.array([[1/4, 1/4, 1/4, 1/4, 0],
               [1/4, 1/4, 1/4, 1/4, 0],
               [0, 1/3, 1/3, 1/3, 0],
               [0, 0, 1/2, 1/2, 0],
               [0, 0, 0, 1, 0]])

# p(X_9 | X_8)
p9 = np.array([[0, 1, 0, 0, 0],
               [0, 0, 1, 0, 0],
               [0, 0, 0, 1, 0],
               [0, 0, 0, 0, 1],
               [0, 0, 0, 0, 0]])
'''

tDistMatrices = np.stack((p2,p3,p4,p5,p6,p7,p8))


tDistMat = np.matrix([[0.20, 0.20, 0.15, 0.20, 0.25],
                      [0.15, 0.25, 0.10, 0.30, 0.20],
                      [0.25, 0.15, 0.20, 0.20, 0.20],
                      [0.10, 0.30, 0.20, 0.10, 0.30],
                      [0.30, 0.20, 0.15, 0.20, 0.15]])