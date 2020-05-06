import re
import nltk
nltk.download('punkt')


'''
Fungsi untuk memisahkan text panjang yang terdiri dari banyak kalimat menjadi
list of kalimat
'''
def splitText(text):
    sentences = nltk.sent_tokenize(text)
    return sentences

'''
Fungsi untuk mencari seluruh angka dengan fomrat tertentu
pada kalimat sentence
'''
def findNum(sentence):
    nums =  re.findall(r'(?:\d{1,}[,.]?\d{1,}%?)[\s]?(?:juta|ribu)?[\s]?(?:orang|jiwa|penduduk|kasus|pasien)?', sentence)
    return nums

'''
Fungsi untuk mencari seluruh tanggal dengan fomrat tertentu
pada kalimat sentence
'''
def findDate(sentence):
    dates = re.findall(r'(?:Senin|Selasa|Rabu|Kamis|Jumat|Sabtu|Minggu)?[,]?[\s]?[(]?(?:\d{1,2})[-/\s](?:Jan(?:uari)?|Feb(?:ruari)?|Mar(?:et)?|Apr(?:il)?|Mei|Jun(?:i)?|Jul(?:i)?|Agustus|Sep(?:tember)?|Okt(?:ober)?|Nov(?:ember)?|Des(?:ember)?)?[\s]?(?:\d{1,2})?[-/)\s,]?(?:\d{2,4})?[)\s]?(?:pukul\s)?(?:\d{1,2}[:.\s])?(?:\d{1,2})?(?:\sWIB)?', sentence)
    return dates

'''
Fungsi untuk mencari angka pada list nums yang terdekat jaraknya dengan kata berindkes awal idx
pada kalimat sentence
'''
def searchClosestNum(nums, sentence, idx):
    min = len(sentence)
    closestNum = nums[0]
    for num in nums:
        occ = [m.end() for m in re.finditer(num, sentence)]
        print(occ)
        if(abs(int(occ[0]) - idx) < min and num != '19' and num != '19 '):
            min = abs(int(occ[0])-idx)
            closestNum = num
    
    return closestNum

