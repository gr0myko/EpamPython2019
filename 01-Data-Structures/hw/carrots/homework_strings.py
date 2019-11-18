""""

Задание 1

0) Повторение понятий из биологии (ДНК, РНК, нуклеотид, протеин, кодон)

1) Построение статистики по входящим в последовательность ДНК нуклеотидам 
для каждого гена (например: [A - 46, C - 66, G - 23, T - 34])

2) Перевод последовательности ДНК в РНК (окей, Гугл)

3) Перевод последовательности РНК в протеин*


*В папке files вы найдете файл rna_codon_table.txt - 
в нем содержится таблица переводов кодонов РНК в аминокислоту, 
составляющую часть полипептидной цепи белка.


Вход: файл dna.fasta с n-количеством генов

Выход - 3 файла:
 - статистика по количеству нуклеотидов в ДНК
 - последовательность РНК для каждого гена
 - последовательность кодонов для каждого гена

 ** Если вы умеете в matplotlib/seaborn или еще что, 
 welcome за дополнительными баллами за
 гистограммы по нуклеотидной статистике.
 (Не забудьте подписать оси)

P.S. За незакрытый файловый дескриптор - караем штрафным дезе.

"""

dna = open('./files/dna.fasta')
#creating dictionary for dna names and dna sequences
dna_seqs = {}
for line in dna:
    line = line.rstrip()
    if line[0] == '>':
        name_words = line.split()
        name = name_words[0][1:]
        dna_seqs[name] = ''
    else:
        dna_seqs[name] = dna_seqs[name] + line
dna.close()

def translate_from_dna_to_rna(dna):
    rna = {}
    for dna_id, seq in dna.items():
        rna[dna_id] = seq.replace('T', 'U')
    return rna



def count_nucleotides(dna):
    num_of_nucleotides = []
    for dna_id, seq in dna.items():
        nucleotid_dict = {}
        for nucleotid in seq:
            nucleotid_dict[nucleotid] = seq.count(nucleotid)
        num_of_nucleotides.append(nucleotid_dict)
    return num_of_nucleotides



rna_codon = open('./files/rna_codon_table.txt')
tr_dict = {}
for element in rna_codon.read().split():
    if len(element) == 3:
        name = element
        tr_dict[name] = ''
    else:
        tr_dict[name] += element
rna_codon.close()
rna = translate_from_dna_to_rna(dna_seqs)



def translate_rna_to_protein(rna):
    protein = ''
    for key, rna_seq in rna.items():
        for i in range(0, len(rna_seq), 3):
            if tr_dict[rna_seq[i:i+3]] == 'Stop':
                break
            else:
                protein += tr_dict[rna_seq[i:i+3]]
    return protein
