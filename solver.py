# Countdown solver module


def canItBeDone(numbers,target,hint,solution):  # returns boolean
    # numbers is a list of numbers, originally 6 numbers but we'll recursively reduce it to length 2
    # target is the integer we are aiming for
    # hint is a boolean used to decide if we just display the last step or the whole solution
    # solution is the string we are building up step by step
    itCan = False
    for i1 in range(len(numbers)):
        for i2 in range(len(numbers)):
            if i1 != i2: # we are not allowed to combine a number with itself
                # combine i1 and i2 in 4 ways: + * - /
                # +
                if i1 > i2: # avoid doing it twice a+b == b+a
                    r=numbers[i1]+numbers[i2]
                    step=str(numbers[i1])+' + '+str(numbers[i2])+' = '+str(r)
                    if r == target:
                        itCan= True
                        if hint:
                           print('hint last step: ',step)
                        else:
                           print(solution+'\n'+step)
                    elif len(numbers) > 2: # keep going if we didn't reach target and there is more to combine
                        nestedNumbers=numbers.copy()
                        nestedNumbers.remove(numbers[i1])
                        nestedNumbers.remove(numbers[i2])
                        nestedNumbers.append(r)
                        itCan=itCan or canItBeDone(nestedNumbers,target,hint,solution+'\n'+step)

                # *
                if i1 > i2: # avoid doing it twice: a*b == b*a
                    r=numbers[i1]*numbers[i2]
                    step=str(numbers[i1])+' * '+str(numbers[i2])+' = '+str(r)
                    if r == target:
                        itCan= True
                        if hint:
                           print('hint last step: ',step)
                        else:
                           print(solution+'\n'+step)
                    elif len(numbers) > 2: # keep going if we didn't reach target and there is more to combine
                        nestedNumbers=numbers.copy()
                        nestedNumbers.remove(numbers[i1])
                        nestedNumbers.remove(numbers[i2])
                        nestedNumbers.append(r)
                        itCan=itCan or canItBeDone(nestedNumbers,target,hint,solution+'\n'+step)
                    
                # -
                if numbers[i1] - numbers[i2] > 0:   # intermediate negative results not allowed
                   r=numbers[i1]-numbers[i2]
                   step=str(numbers[i1])+' - '+str(numbers[i2])+' = '+str(r)
                   if r == target:
                        itCan= True
                        if hint:
                           print('hint last step: ',step)
                        else:
                           print(solution+'\n'+step)
                   elif len(numbers) > 2: # keep going if we didn't reach target and there is more to combine
                            nestedNumbers=numbers.copy()
                            nestedNumbers.remove(numbers[i1])
                            nestedNumbers.remove(numbers[i2])
                            nestedNumbers.append(r)
                            itCan=itCan or canItBeDone(nestedNumbers,target,hint,solution+'\n'+step)
                            
                # /
                if numbers[i1] % numbers[i2] == 0:
                   r=int(numbers[i1]/numbers[i2])
                   step=str(numbers[i1])+' / '+str(numbers[i2])+' = '+str(r)
                   if r == target:
                      itCan= True
                      if hint:
                           print('hint last step: ',step)
                      else:
                           print(solution+'\n'+step)
                   elif len(numbers) > 2: # keep going if we didn't reach target and there is more to combine
                      nestedNumbers=numbers.copy()
                      nestedNumbers.remove(numbers[i1])
                      nestedNumbers.remove(numbers[i2])
                      nestedNumbers.append(r)
                      itCan=itCan or canItBeDone(nestedNumbers,target,hint,solution+'\n'+step)                     
           
    return itCan

  

