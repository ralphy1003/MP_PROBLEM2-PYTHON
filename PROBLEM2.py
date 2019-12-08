#PROBLEM 2-PYTHON
import numpy as np
from math import sqrt
print ("please enter 3  points in (x,y) form:")
A = int(input ("1st point x: "))
B = int(input ("2nd point x: "))
C = int(input ("3rd point x: "))
D = int(input ("1st point y: "))
E = int(input ("2nd point y: "))
F = int(input ("3rd point y: "))
uno = (A^2)+(D^2)
dos = (B^2)+(E^2)
tres = (C^2)+(F^2)
 
AB = A - B;  
AC = A - C;  
  
DE = D - E;  
DF = D - F;  
  
FD = F - D;  
ED = E - D;  
  
CA = C - A;  
BA = B - A; 
    
X13 = pow(A, 2) - pow(C, 2);  

Y13 = pow(D, 2) - pow(F, 2);  
  
X21 = pow(B, 2) - pow(A, 2);  
Y21 = pow(E, 2) - pow(D, 2);  
  
f = (((X13) * (AB) + (Y13) * 
    (AB) + (X21) * (AC) + 
    (Y21) * (AC)) // (2 * 
    ((FD) * (AB) - (ED) * (AC)))); 
              
g = (((X13) * (DE) + (Y13) * (DE) + 
      (X21) * (DF) + (Y21) * (DF)) // 
      (2 * ((CA) * (DE) - (BA) * (DF))));  
      
c = (-pow(A, 2) - pow(D, 2) - 
     2 * g * A - 2 * f * D);  
  
   
h = -g;
    
k = -f;  
sqr_of_r = h * h + k * k - c;  
   
r = sqrt(sqr_of_r); 

a = np.array([[A,D,1],[B,D,1],[E,F,1]])
b = np.array([uno,dos,tres])
x = np.linalg.solve(a,b)
print ('The Vector of DEF are:',x)
print ('The center is:','(',h,')','(',k,')')
print ('The radius is:',r)30
55