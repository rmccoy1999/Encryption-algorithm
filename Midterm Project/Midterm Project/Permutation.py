from KeySchedule import key_expansion

def rockin_dat_perm(sp, key):

    #did it manually because its late and im tired, think of equation later, it also combines shiftrows and mixcolumns steps
    party_in_da_back = [sp[len(sp)-6], sp[len(sp)-9], sp[len(sp)-4], sp[len(sp)-2], sp[len(sp)-10], 
                            sp[len(sp)-1], sp[len(sp)-3], sp[len(sp)-5], sp[len(sp)-7], sp[len(sp)-8]]
    
    print("Permuted dutch array is: ", party_in_da_back)
    return(how_bout_no(key_expansion(party_in_da_back, key, 2)))
    
    

def how_bout_no(no):
    #simply the reverse step for rockin_dat_perm
    freaky_dutch_bastard = [no[len(no)-6], no[len(no)-9], no[len(no)-1], no[len(no)-2], no[len(no)-10],
                            no[len(no)-3], no[len(no)-8], no[len(no)-4], no[len(no)-7], no[len(no)-5]]
    print("Un-permuted freaky deaky dutch is: ", freaky_dutch_bastard)
    return(freaky_dutch_bastard)

    #perm = np.roll(data, 3)
    #print("Permuted elements is: ", perm)
    
    #for shit in sp:
        #party_in_da_back = np.concatenate((shit[:2], shit[-2:], shit[2:-3]))
        #party_in_da_back
    
    #party_in_da_back.append()
        
    #party_in_da_back = np.array(sp).reshape(4,4)-2
    #print(party_in_da_back)
    
    #for p in range(0, 2):
        #party_in_da_back[p] = np.roll(party_in_da_back[p], -p)
    #print(party_in_da_back)

