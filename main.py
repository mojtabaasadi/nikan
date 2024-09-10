import easyocr,os,sqlite3,sys
from PIL import Image
import base64
from io import BytesIO
from utils import  make_four_point_box


con = sqlite3.connect('./extractions.db')
reader = easyocr.Reader(['fa'])
files = os.listdir('./files')
cur = con.cursor()
tablename = 'clips' 
cur.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name=? ", (tablename, ))

if cur.fetchone()[0] ==1 : 
    print('Table exists. ')
    pass
else: 
    cur.execute("""
            CREATE TABLE clips  (
                image TEXT,
                predicted TEXT,
                prediction_engine TEXT,
                first_correction TEXT,
                second_correction TEXT,
                reference TEXT,
                prediction_score REAL,
                id INTEGER PRIMARY KEY AUTOINCREMENT
            );
            """)
    con.commit()

for file in files:
    result = reader.readtext('./files/'+file)
    image = Image.open('./files/'+file)
    content = ""
    for (bbox, text, prob) in result:
        box = make_four_point_box(bbox)
        clip = image.crop(box=box)
        buffered = BytesIO() 
        
        clip.save(buffered, format=image.format)
        img_bytes = base64.b64encode(buffered.getvalue())
        img_str = 'data:image/'+image.format.lower()+';base64,' + img_bytes.decode('utf-8')
        cur.execute("""
                    insert into clips  (image,predicted,prediction_engine,prediction_score,reference) values (
"{0}",
"{1}",
"EasyOcr-arabic",
{2},
"{3}");
                    """.format(img_str,text,prob,file))
        con.commit()

cur.close()
con.close()