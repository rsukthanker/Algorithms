import numpy as np
def find_peak_2d(matrix):
    nrows=matrix.shape[0]
    ncols=matrix.shape[1]
    peak=[]
    for i in range(nrows):
        for j in range(ncols):
            val=matrix[i,j]
            if i==0:
               if j==0:
                  bottom=matrix[i+1,j]
                  right=matrix[i,j+1]
                  if val>=bottom and val>=right:
                     peak.append(val)
                     #break
               elif j==ncols-1:
                 bottom=matrix[i+1,j]
                 left=matrix[i,j-1]
                 if val>=bottom and val>=left:
                    peak.append(val)
                    #break
               else:
                  bottom=matrix[i+1,j]
                  right=matrix[i,j+1]
                  left=matrix[i,j-1]
                  if val>=bottom and val>=right and val>=left:
                     peak.append(val)
                     #break
            elif i==nrows-1:
               if j==0:
                  top=matrix[i-1,j]
                  right=matrix[i,j+1]
                  if val>=top and val>=right:
                     peak.append(val)
                     #break
               elif j==ncols-1:
                 top=matrix[i-1,j]
                 left=matrix[i,j-1]
                 if val>=top and val>=left:
                    peak.append(val)
                    #break
               else:
                  top=matrix[i-1,j]
                  right=matrix[i,j+1]
                  left=matrix[i,j-1]
                  if val>=top and val>=right and val>=left:
                     peak.append(val)
                     #break 
            elif j==0:
                 top=matrix[i-1,j]
                 bottom=matrix[i+1,j]
                 right=matrix[i,j+1]
                 if val>=top and val>=bottom and val>=right:
                    peak.append(val)
                    #break
            elif j==ncols-1:
               top=matrix[i-1,j]
               bottom=matrix[i+1,j]
               left=matrix[i,j-1]
               if val>=top and val>=bottom and val>=left:
                  peak.append(val)
                  #break
            else:
               top=matrix[i-1,j]
               bottom=matrix[i+1,j]
               left=matrix[i,j-1]
               right=matrix[i,j+1]
               if val>=top and val>=bottom and val>=left and val>=right:
                  peak.append(val)
                  #break
    return peak
def find_peak_2d_logn(mat,cstart,cend):
    midcol=int(cstart+(cend-cstart)/2)
    b=np.argmax(mat[:,midcol])
    max=mat[b,midcol]
    if max<mat[b,midcol-1] and midcol-1>=0:
       return find_peak_2d_logn(mat,cstart,midcol-1)
    elif  midcol+1<=cend and max<mat[b,midcol+1]:
       return find_peak_2d_logn(mat,midcol+1,cend) 
    else:
      return max
