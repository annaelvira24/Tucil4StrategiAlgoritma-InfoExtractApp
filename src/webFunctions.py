import util
import KMP
import BM
import regularExpression as regexp

'''
File berisi kumpulan fungsi untuk back-end website
'''

tglBerita = ""
source = []
datesResult = []
numsResult = []
sntcResult = []

'''
Fungsi untuk mengekstraksi berita dengan mengambil tanggal berita
dan melakukan dekomposisi text berita dari source menjadi kalimat-kalimat
'''
def extractBerita(source) :
    global tglBerita

    f = open(source)
    text = f.read()

    sentences = util.splitText(text)
    headerBerita = sentences[0].split("\n")
    tglBerita = headerBerita[2]
    kalimatBerita = []
    for sentence in headerBerita:
        kalimatBerita.append(sentence)
    for i in range (1, len(sentences)):
        kalimatBerita.append(sentences[i])
    
    return kalimatBerita

'''
Prosedur untuk memproses sebuah kalimat pada berita dengan memeriksa
apakah pada kalimat terdapat angka dan tanggal lalu memsaukkan angka
dan tanggal yang ditemukan serta kalimat tersebut dan sumber berikta
ke array hasil yang sesuai
'''
def prosesKalimat(kalimat, berita, foundIndex):
    global source
    global datesResult
    global numsResult
    global sntcResult
    global tglBerita


    numsTemp = util.findNum(kalimat)
    if(len(numsTemp)>0):
        numsResult.append(util.searchClosestNum(numsTemp, kalimat, foundIndex))
        source.append(berita)
        sntcResult.append(kalimat)
                    
        datesTemp = util.findDate(kalimat)
        lenAwal = len(datesResult)
        if(len(datesTemp) > 0):
            for i in range (len(datesTemp)):
                if(len(datesTemp[i])>=8):
                    datesResult.append(datesTemp[i])
            
            if(len(datesResult) == lenAwal):
                datesResult.append(tglBerita)
        else:
            datesResult.append(tglBerita)

'''
Prosedur untuk melakukan pencocokan string text pada setiap filesOfBerita
dengan pattern keyword menggunakan method algoritma tertentu
'''
def extractKalimat(filesOfBerita, keyword, method):
    global source
    global datesResult
    global numsResult
    global sntcResult

    source.clear()
    datesResult.clear()
    numsResult.clear()
    sntcResult.clear()

    for berita in filesOfBerita:
        kalimatBerita = extractBerita("../test/"+berita)

        if (method == "kmp"):
            for kalimat in kalimatBerita :
                foundIndex = KMP.kmpAlgorithm(kalimat, keyword)
                if (foundIndex != -1):
                    prosesKalimat(kalimat, berita, foundIndex)

        elif(method == "bm"):
            for kalimat in kalimatBerita :
                foundIndex = BM.bmAlgorithm(kalimat, keyword)
                if (foundIndex != -1):
                    prosesKalimat(kalimat, berita, foundIndex)
        else : #method == "regex"
            for kalimat in kalimatBerita :
                foundIndex = KMP.kmpAlgorithm(kalimat, keyword)
                if (foundIndex != -1):
                    prosesKalimat(kalimat, berita, foundIndex)
                