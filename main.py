from flask import *

app = Flask(__name__)
def wordsfinder(char_esp,charStr):
    matchWords=[]
    char_list=[]
    char_list[:0]=charStr
    char_list.append(char_esp)
    for l in lines:
        l=l.rstrip().lower()
        find=False
        if char_esp in l:
            allchars=[]
            for c in l:
                if c not in char_list:
                    allchars.append(False)
                else:
                    allchars.append(True)
            find=all(allchars)
            if(find):matchWords.append(l)
    return matchWords


@app.route("/",methods=['GET','POST'])
def index():
    if request.method=='POST':
        esp= request.form['esp']
        list= request.form['list']
        matchWords=wordsfinder(esp,list)
        return render_template('index.html', your_list=matchWords,title="home")
    else:
        return render_template('index.html',title="home")


if __name__ == "__main__":
    file1 = open('net.txt', 'r')
    lines = file1.readlines()
    app.run(debug=True)
#/html/body/script[7]/text()
