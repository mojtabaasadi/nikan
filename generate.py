import codecs
sql = "SELECT  first_correction  from clips c WHERE  first_correction is NOT  NULL ;"
from utils import db_action

if __name__ == '__main__':    
    (res,closer) = db_action(sql,True)
    closer()
    txt= ""
    for item in res:
        txt += item['first_correction'] + '\n'
    
    with codecs.open('outFa.txt','w+','utf-8') as file:
        file.write(txt)
        file.close()
    
    print("saved to outFa.txt")