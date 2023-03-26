#Author : Tống Diệu Hương
#Program : Hoi quy tuyen tinh

import numpy as np 
import matplotlib.pyplot as plt 
  
#Tim trong so
def estimate_coef(x, y): 
    n = np.size(x) 
    m_x, m_y = np.mean(x), np.mean(y) 
    SS_xy = np.sum(y*x) - n*m_y*m_x 
    SS_xx = np.sum(x*x) - n*m_x*m_x 
    a = m_y - b*m_x 
    b = SS_xy / SS_xx 
    return(a, b)

#Du bao cho X
def forecast(x,a,b):
    return print("Du doan gia tri Y khi X = ",x," la ",a*x+b)

#Ham chinh
def main(): 
    x = np.array([1, 2, 4, 6, 8]) 
    y = np.array([5, 7, 11, 15, 19])
    X = np.array([7, 11])
    b = estimate_coef(x, y) 
    print("Gia tri cua a = {}  \nGia tri cua b = {}".format(b[0], b[1]))
    for i in X:
        forecast(i,b[0],b[1])
 
if __name__ == "__main__": 
    main() 
