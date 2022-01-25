array1 = [0, 1.2, 1.3, 8]
array2 = [0, 1.2, 1.3, 8]
##array2 = [0, 1.1, 1.2, 8]

def variant(array):
    sigma_sq = 0
    mean = 0
    for i in array:
        mean += i
    mean = mean/len(array)

    for i in array:
        sigma_sq += (i - mean)**2

    sigma_sq /= (len(array))

    print (sigma_sq)

def covariant (array1,array2):
    if len(array1) != len(array2):
        print("Invalid")
   
    sigma = 0

    mean1 = 0
    mean2 = 0
    
    for i in array1:
        mean1 += i
    mean1 = mean1/len(array1)
    
    for i in array2:
        mean2 += i
    mean2 = mean2/len(array2)

    for (i,j) in zip(array1,array2):
        
        sigma += (i - mean1)*(j - mean2)

    sigma /= len(array1)

    print(sigma)

covariant(array1, array2)
