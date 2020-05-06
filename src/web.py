from flask import Flask, redirect, url_for, render_template, request
import webFunctions
app = Flask(__name__)

'''
File ini berisi fungsi untuk back-end dari website
'''

@app.route("/", methods=["POST", "GET"])
def home():
  if request.method == "POST":
    inputFiles = request.form.getlist("filename")
    inputKeyword = request.form["keyword"]
    #print(isikey == "sedang")
    method = request.form["algorithm"]
    webFunctions.extractKalimat(inputFiles,inputKeyword,method)

    return render_template("homePage.html", algoritma=method, folder=inputFiles, key=inputKeyword, jumlah=webFunctions.numsResult , tanggal=webFunctions.datesResult, kalimat=webFunctions.sntcResult, sumber=webFunctions.source)
  else:
    return render_template("homePage.html", algoritma="", folder="", key = "", number=[] , tanggal=[], result=[], source=[])

if __name__ == "__main__":
    app.static_folder = 'static'
    app.run(debug=True)

