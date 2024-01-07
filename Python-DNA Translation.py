def replicate(dna_strand):
    dna = {
        "A": "T",
        "T": "A",
        "G": "C",
        "C": "G"
    }
    string = ''
    for i in range(len(dna_strand)):
        string = dna[dna_strand[i]] + string
    return string

def transcribe(dna_strand):
    dna = {
        "A": "U",
        "T": "A",
        "G": "C",
        "C": "G"
    }
    string = ''
    for i in range(len(dna_strand)):
        string = dna[dna_strand[i]] + string
    return string
def reverse_transcribe(rna_strand):
    dna = {
        "A": "T",
        "U": "A",
        "G": "C",
        "C": "G"
    }
    string = ''
    for i in range(len(rna_strand)):
        string = dna[rna_strand[i]] + string
    return string

def get_mapping(csv_filename):
    file = read_csv(csv_filename)
    d = {}
    for row in file:
        d[row[0]] = row[3]
    return d
        
    """Your code here"""
'''
def translate(rna_strand):
    ca = get_mapping("codon_mapping.csv")
    string = ''
    lst = []
    while rna_strand:
        lst.append(rna_strand[0:2])
        rna_strand = rna_strand[3:]
    copy = lst.copy()
    if 'AUG' not in lst:
        return None 
        
    for i in range(len(copy)):
        if copy[i] == 'AUG':
            break
        lst.pop(0)
    return lst
    for i in lst:
        if i == "UAA" or i == "UAG" or i == "UGA":
            break 
        else:
            string += ca[i]
    return string + '_'
'''

def translate(rna_strand):
    ca = get_mapping("codon_mapping.csv")
    string = ''
    lst = []
    
    
    if 'AUG' not in rna_strand:
        return None 
    elif 'UAA' not in rna_strand and 'UAG' not in rna_strand and 'UGA' not in rna_strand:
        return None
    while rna_strand[0:3] != 'AUG':
        rna_strand = rna_strand[1:]
    
    while len(rna_strand) >= 3:
        lst.append(rna_strand[0:3])
        rna_strand = rna_strand[3:]
    lst.append(rna_strand)
    for i in lst:
        if i == "UAA" or i == "UAG" or i == "UGA":
            break 
        elif len(i) < 3:
            return None
        else:
            string += ca[i]
    return string + '_'


def tag(tag,data):
    return [tag,data]
def get_tag_type(tag):
    return tag[0]
def get_data(tag):
    return tag[1]

def to_rna(tagged_data):
    tag_type = get_tag_type(tagged_data)
    data = get_data(tagged_data)
    op = get_op("to_rna",(tag_type,))
    return tag("rna", op(data))
def is_same_dogma(tagged_data1, tagged_data2):
    tag_type1 = get_tag_type(tagged_data1)
    tag_type2 = get_tag_type(tagged_data2)
    if tag_type1 == tag_type2:
        if get_data(tagged_data1) == get_data(tagged_data2):
            return True
    elif tag_type1 == "dna" and tag_type2 == "rna":
        get_new_data1 = get_data(to_rna(tagged_data1))
        get_data2 = get_data(tagged_data2)
        if get_new_data1 == get_data2:
            return True
    elif tag_type1 == "rna" and tag_type2 == "dna":
        get_new_data1 = get_data(to_dna(tagged_data1))
        get_data2 = get_data(tagged_data2)
        if get_new_data1 == get_data2:
            return True
    return False

# (a)
def to_protein(tagged_data):
    tag_type = get_tag_type(tagged_data)
    data = get_data(tagged_data)
    if tag_type == "protein":
        data = data
    elif tag_type == "rna":
        data = translate(data)
    elif tag_type == "dna":
        data = translate(transcribe(data))
    return tag("protein", data)
    
# (b)
put_op("to_protein", ("dna","protein"), to_protein) # converts Tagged-DNA to Tagged-Protein
put_op("to_protein", ("rna","protein"), to_protein) # converts Tagged-RNA to Tagged-Protein
put_op("to_protein", ("protein","protein"), to_protein)# converts Tagged-Protein to Tagged-Protein
# (c)
put_op("is_same_dogma", ("protein","protein"), lambda x, y: x == y) # checks Tagged-Protein/Tagged-Protein
put_op("is_same_dogma", ("protein","dna"), lambda x, y: x == translate(transcribe(y))) # checks Tagged-Protein/Tagged-DNA
put_op("is_same_dogma", ("dna","protein"), lambda x, y: translate(transcribe(x)) == y)# checks Tagged-DNA/Tagged-Protein
put_op("is_same_dogma", ("protein","rna"), lambda x, y: x == translate(y)) # checks Tagged-Protein/Tagged-RNA
put_op("is_same_dogma", ("rna","protein"), lambda x, y: translate(x) == y) # checks Tagged-RNA/Tagged-Protein
# (d)
#dna_1 = to_dna(protein)
#dna_2 = to_dna(to_protein(tagged_rna))
dna_3 = to_dna(tagged_rna)
#dna_4 = to_dna(tagged_protein)
#dna_5 = to_dna(to_protein(tagged_dna))
dna_6 = to_dna(to_rna(tagged_dna))
#dna_7 = to_dna(to_rna(tagged_protein))
#dna_8 = to_dna(to_protein(to_rna(tagged_dna)))
#dna_9 = to_dna(to_rna(to_protein(dna_1)))
#dna_10 = ('dna', get_data(dna_6))
# (e)
# Give 6 examples of Tagged-RNAs that will give rise to the Tagged-Protein with data "MYVHAN_"
my_rna_list = [tag("rna","AUGUACGUACACGCAAACUAG"),tag("rna","AUGUACGUACACGCAAACUGA"),
tag("rna","AUGUACGUACACGCAAACUAA"), tag("rna","AUGUAUGUACACGCAAACUAG"), 
tag("rna","AUGUAUGUACACGCAAACUGA"), tag("rna","AUGUAUGUACACGCAAACUAA") ]
# (f)
# Number of Tagged-RNAs that will give rise to the Tagged-Protein with data "MYVHAN_"
num_rnas = 384 # replace with your answer
