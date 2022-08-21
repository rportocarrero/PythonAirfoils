import random
import struct

rand_min = 1
rand_max = 10

# initialization

def generateChromosome():
    ch = []
    s = struct.Struct('fffffffff')
    for i in range(9):
        ch.append(random.uniform(rand_min,rand_max))
        
    return s.pack(ch[0],ch[1],ch[2],ch[3],ch[4],ch[5],ch[6],ch[7],ch[8])

# fitness function

# selection

# crossover

def crossover(ch1, ch2):
    index = random.randrange(min(len(ch2),len(ch1)))
    newCh1 = ch1[:index]+ch2[index:]
    newCh2 = ch2[:index]+ch1[index:]
    
    return newCh1, newCh2

# mutation

# termination criterion

# display individual

def decodeChromosome(ch):
    chromlist = struct.unpack('fffffffff',ch)
    
    w_half_span = chromlist[0]
    w_sweep = chromlist[1]
    w_root_chord = chromlist[2]
    w_tip_chord = chromlist[3]
    ht_dist = chromlist[4]
    ht_half_span = chromlist[5]
    ht_sweep = chromlist[6]
    ht_root_chord = chromlist[7]
    ht_tip_chord = chromlist[8]
    
    return w_half_span, w_sweep, w_root_chord, w_tip_chord, ht_dist, ht_half_span, ht_sweep, ht_root_chord, ht_tip_chord
    
    
#DEBUG
ch1 = generateChromosome()
print(decodeChromosome(ch1))



