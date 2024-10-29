
import os,re,codecs


regex = r"_(\d{1,})\.jpg"

def generate():
    files = os.listdir('./out')
    txt= "filename,words\n"
    for filename in files:
        new_file = filename.split("_")[-1]
        label = "_".join(filename.split("_")[:-1])
        real_name= label[::-1]
        os.rename('./out/'+filename,'./out/'+new_file)
        txt += new_file+','+real_name+'\n'
    with codecs.open('./out/labels.csv','w+','utf-8') as csv:
        csv.write(txt)
        csv.close()
        

if __name__ == '__main__':
    generate()