from numpy import *

def trid(n, diag, diag1, diag2):
    if n==len(diag):
        if len(diag1)==len(diag2):
            if len(diag1)==n-1:
                
                M=(n,n)
                M=zeros(M)
                
                for i in range(n):
                    
                    M[i,i]=diag[i]
                    
                    if i < n-1:
                        
                        M[i, i+1]=diag2[i]
                        M[i+1, i]=diag1[i]
                        
                return M
            else:
                print 'La longitud de las diagonales laterales no coincide con la correcta ('+str(n-1)+' )'
        else:
             print 'La longitud de las diagonales laterales no es igual'
        
    else:
        print 'La longitud de la diagonal principal no es la especificada'