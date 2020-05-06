'''
Fungsi untuk menghitung nilai fungsi fail (border function)
untuk setiap karakter pada string pattern dan mengembalikan
tabel fail
'''
def computeFail(pattern):
    fail = [0] * len(pattern)
    
    m = len(pattern)
    j = 0;
    k = 1;
    
    while (k < m):
        if (pattern[j] == pattern[k]):
            fail[k] = j + 1
            k += 1
            j += 1
        elif (j > 0):
            j = fail[j-1]
        else: # tidak match sama sekali
            fail[k] = 0
            k += 1
    
    return fail

'''
Fungsi utama dalam pencocokan string menggunakan metode KMP
Mencari patternInput dalam textInput
Jika ditemukan, fungsi mengembalikan indeks pertama letak kemunculan
pattern dalam teks, jika tidak ditemukan, fungsi mengembalikan -1
'''
def kmpAlgorithm(textInput, patternInput):

    text = textInput.upper()
    pattern = patternInput.upper()

    n = len(text)
    m = len(pattern)

    fail = computeFail(pattern)
    
    i = 0
    j = 0

    while (i < n):
        if (pattern[j] == text[i]):
            if (j == m-1): # posisi j sudah di akhir pattern
                return i-m + 1
            i+=1
            j+=1
        elif (j > 0):
            j = fail[j-1] # mulai mencocokan dari nilai fail[j-1]
        else:
            i+=1

    return -1; #tidak match
