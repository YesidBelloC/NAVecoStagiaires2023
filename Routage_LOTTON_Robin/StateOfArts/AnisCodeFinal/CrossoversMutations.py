"""
    Auteur : Anis SALHI
    Date : 06/2022
    
    * Script qui contient 3 opérateurs de croisement et 1 de mutation 
     ==> qui permettent la reproduction et la diversification à travers les générations.
    
    Modifie par: Anis SALHI
"""
#==============================================================================

import random

""" croisement 1: la moyenne des vitesses en gardant les accelerations du parent 1 (meilleur parent)
    ainsi que les vitesses si la moyenne n'est pas possible """

def crossover_speed_mean(chromosome_1 , chromosome_2):
    print(" ********** 333333333333333333333 ***********")
    chromosome_result = []
   
    for i in range(len(chromosome_1)):
        
        if(i%2 == 0): 
            chromosome_result.append(chromosome_1[i]) 
        
        else:
            if( i > 1 and ( chromosome_1[i-1] > 0 and chromosome_2[i-1] >= 0 ) and chromosome_result[i-2] < (chromosome_1[i] + chromosome_2[i])/2 ):
                if round((chromosome_1[i] + chromosome_2[i])/2  ,2 ) != 0 :
                    chromosome_result.append( round((chromosome_1[i] + chromosome_2[i])/2  ,2 ) )
                else:
                    chromosome_result.append( (chromosome_1[i] + chromosome_2[i])/2  )
            
            elif( i > 1 and ( chromosome_1[i-1] < 0 and chromosome_2[i-1] <= 0 ) and chromosome_result[i-2] > (chromosome_1[i] + chromosome_2[i])/2 ):   
                if round((chromosome_1[i] + chromosome_2[i])/2  ,2 ) != 0 :
                    chromosome_result.append( round((chromosome_1[i] + chromosome_2[i])/2  ,2 ) )
                else : 
                    chromosome_result.append( (chromosome_1[i] + chromosome_2[i])/2   )
                
            
            else:
                chromosome_result.append( chromosome_1[i] )
           
                     
    return chromosome_result 



""" croisement 2: la moyenne des vitesses et des accelerations en gardant les accelerations et les vitesses
    du parent 1 si la moyenne n'est pas possible """
    # en gardant ceux du "MEILLEUR" parent

def crossover_speed_and_acceleration_mean(chromosome_1 , chromosome_2):
    chromosome_result = []
    
    for i in range(len(chromosome_1)):
        print(" ********** 00000000000000000000000000000 ********** ")
        if (i == 0): # accel et vitesse de la premiere phase (tjrs les memes qlq le chrom) 
            chromosome_result.append( (chromosome_1[i] + chromosome_2[i])/2  )
            chromosome_result.append( (chromosome_1[i+1] + chromosome_2[i+1])/2  )
                
        elif(i%2 == 0): 
            
            if( ( chromosome_1[i] > 0 and chromosome_2[i] >= 0 ) and chromosome_result[i-1] < (chromosome_1[i+1] + chromosome_2[i+1])/2 ):
                chromosome_result.append( (chromosome_1[i] + chromosome_2[i])/2 )
                chromosome_result.append( (chromosome_1[i+1] + chromosome_2[i+1])/2 )
            
            elif( ( chromosome_1[i] < 0 and chromosome_2[i] <= 0 ) and chromosome_result[i-1] > (chromosome_1[i+1] + chromosome_2[i+1])/2 ):
                chromosome_result.append( (chromosome_1[i] + chromosome_2[i])/2 )
                chromosome_result.append( (chromosome_1[i+1] + chromosome_2[i+1])/2 )
            
            elif( ( chromosome_1[i] < 0 and chromosome_2[i] <= 0 ) and chromosome_result[i-1] <= (chromosome_1[i+1] + chromosome_2[i+1])/2 ):
                chromosome_result.append( (chromosome_1[i] + chromosome_2[i])/2 )
                chromosome_result.append( chromosome_1[i+1] )
                
            elif( ( chromosome_1[i] > 0 and chromosome_2[i] >= 0 ) and chromosome_result[i-1] >= (chromosome_1[i+1] + chromosome_2[i+1])/2 ):
                chromosome_result.append( (chromosome_1[i] + chromosome_2[i])/2 )
                chromosome_result.append( chromosome_1[i+1]  )
                
            # on garde ceux du parent 1 (le meilleur)    
            elif( chromosome_1[i] == 0) :  
                chromosome_result.append( chromosome_1[i] )   
                chromosome_result.append( chromosome_result[i-1] )                                 
            else:
                chromosome_result.append( chromosome_1[i] )   
                chromosome_result.append( chromosome_1[i+1] )   
                
    return chromosome_result 


"""
    Entrée :  [Chromosome], [Chromosome]    
    Sortie :  [Chromosome], bool use_this_one_point_crossover (Operation used?)
"""
""" croisement 3: echange en un point random, cad qu'avant ce point random on garde la prtie du parent 1
    et apres, la partie du parent 2. Si ce n'est pas possible on applique le croisement 2 (juste au dessus) """
    

def crossover_exchange_one_point(chromosome_1 , chromosome_2):
    chromosome_result = []
    rand_cut_point = random.randint(2, len(chromosome_1)-2 )
    use_this_one_point_crossover = True
    
    # On tombe sur une acceleration
    if( 
        ( rand_cut_point%2 == 0 and chromosome_1[rand_cut_point] > 0 and chromosome_2[rand_cut_point] > 0 
        and chromosome_2[rand_cut_point+1] > chromosome_1[rand_cut_point-1])
        or
        (rand_cut_point%2 == 0 and chromosome_1[rand_cut_point] < 0 and chromosome_2[rand_cut_point] < 0 
        and chromosome_2[rand_cut_point+1] < chromosome_1[rand_cut_point-1])      
      )  : 
        
        for i in range(len(chromosome_1)):
            
            if i < rand_cut_point :
                chromosome_result.append( chromosome_1[i] )
            else:
                chromosome_result.append( chromosome_2[i] )
        print("********** 11111111111111111111111111111111111111 ********** ")        
                           
    # On tombe sur une vitesse
    elif(
        (rand_cut_point%2 == 1 and chromosome_1[rand_cut_point-1] > 0  
        and chromosome_2[rand_cut_point] > chromosome_1[rand_cut_point-2])
        or
        (rand_cut_point%2 == 1 and chromosome_1[rand_cut_point-1] < 0  
        and chromosome_2[rand_cut_point] < chromosome_1[rand_cut_point-2])            
       ) : # vitesse
        
        for i in range(len(chromosome_1)):
            
            if i < rand_cut_point :
                chromosome_result.append( chromosome_1[i] )
            else:
                chromosome_result.append( chromosome_2[i] )   
        print("********** 1111111111111111111111111111111111111111111111 **********")        
                            

    else :
        use_this_one_point_crossover = False
        print("********** 22222222222222222222222222222222222222222222222222 **********")     
        for i in range(len(chromosome_1)):
 
            if (i == 0): # accel et vitesse de la premiere phase (tjrs les memes qlq le chrom) 
                chromosome_result.append( (chromosome_1[i] + chromosome_2[i])/2 )
                chromosome_result.append(  (chromosome_1[i+1] + chromosome_2[i+1])/2 )
                    
            elif(i%2 == 0): 
                
                if( ( chromosome_1[i] > 0 and chromosome_2[i] >= 0 ) and chromosome_result[i-1] < (chromosome_1[i+1] + chromosome_2[i+1])/2 ):
                    chromosome_result.append( (chromosome_1[i] + chromosome_2[i])/2 )
                    chromosome_result.append( (chromosome_1[i+1] + chromosome_2[i+1])/2 )
                
                elif( ( chromosome_1[i] < 0 and chromosome_2[i] <= 0 ) and chromosome_result[i-1] > (chromosome_1[i+1] + chromosome_2[i+1])/2 ):
                    chromosome_result.append( (chromosome_1[i] + chromosome_2[i])/2 )
                    chromosome_result.append( (chromosome_1[i+1] + chromosome_2[i+1])/2 )
                
                elif( ( chromosome_1[i] < 0 and chromosome_2[i] <= 0 ) and chromosome_result[i-1] <= (chromosome_1[i+1] + chromosome_2[i+1])/2 ):
                    chromosome_result.append( (chromosome_1[i] + chromosome_2[i])/2 )
                    chromosome_result.append( chromosome_1[i+1]  )
                    
                elif( ( chromosome_1[i] > 0 and chromosome_2[i] >= 0 ) and chromosome_result[i-1] >= (chromosome_1[i+1] + chromosome_2[i+1])/2 ):
                    chromosome_result.append( (chromosome_1[i] + chromosome_2[i])/2 )
                    chromosome_result.append( chromosome_1[i+1]  )
                    
                # on garde ceux du parent 1 (le meilleur)    
                else:                
                    if chromosome_1[i] == 0 :
                        chromosome_result.append( chromosome_1[i] )   
                        chromosome_result.append( chromosome_result[i-1] )                                 
                    else:
                        chromosome_result.append( chromosome_1[i] )   
                        chromosome_result.append( chromosome_1[i+1] )   
    
    return chromosome_result, use_this_one_point_crossover 




""" Mutation : on prend une des accelerations du chromosome et on lui donne la plus grande valeur de toutes 
    les accelations possibles (cad: si c une accel negative on lui donne la plus petite et si c une 
                               accel positive on lui donne la plus grande accel PARMIS LES ACCEL DU CHROM)"""

def mutation_chromosome(chromosome_1):
   
    chromosome_result = chromosome_1.copy()
    
    # prendre une acceleration aléatoirement
    gene = random.randrange(0, len(chromosome_1)-1,2)

    # si l'acceleration prise est negative ==> on la remplace avec la plus petite accel du chrom
    if chromosome_result[gene] < 0 :
        # parmis toutes les accel negatives de ce chromosome
        chromosome_result[gene]  = min([i for i in chromosome_result[0:len(chromosome_result):2]])
    
    # si l'acceleration prise est positive ==> on la remplace avec la plus grosse accel du chrom
    elif chromosome_result[gene] > 0 :
        # parmis toutes les accel positives de ce chromosome
        chromosome_result[gene]  = max([i for i in chromosome_result[0:len(chromosome_result):2]])

         
                     
    return chromosome_result 
