'''
Fungsi untuk mencari nilai last occurence bagi setiap
karakter pada string pattern. Fungsi mengembalikan tabel
last
'''
def lastOccurrence(pattern):
    last = [-1] * 128
    for i in range (len(pattern)):
        last[ord(pattern[i])] = i
    
    return last;

'''
Fungsi utama dari algoritma pencocokan string dengan metode BM
Mencari patternInput dalam textInput. Jika ditemukan, fungsi mengembalikan
indeks oertama kemunculan pattern, jika tidak ditemukan, fungsi
mengembalikan -1
'''
def bmAlgorithm(textInput, patternInput) :
    pattern = patternInput.upper()
    text = textInput.upper()

    last = lastOccurrence(pattern)
    n = len(text)
    m = len(pattern)
    i = m-1
    
    if (i > n-1):#pattern lebih panjang dari text
        return -1
    
    j = m-1
    while True:
        if (pattern[j] == text[i]): #jika match
            if (j == 0): #pattern sudah sampai awal
                return i
            else: #pattern belum habis, cocokkan secara mundur (looking glass)
                i-=1
                j-=1
        else: # tidak match, lakukan character jump
            lastOcc = last[ord(text[i])]
            i = i + m - min(j, 1 + lastOcc)
            j = m -1
        
        if(i > n-1):
            break #lakukan selama text belum habis
    
    return -1 #text dan pattern tidak match