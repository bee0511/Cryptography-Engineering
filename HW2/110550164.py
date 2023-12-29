from pprint import pprint

ciphertext1 = [
"ERASBLE",
"CAMSNAB",
"DUMOLEA",
"TOEDCTA",
"MORYRRE",
"ELNTLII",
"CEENTGH",
"ADNRIAO",
"ESAVQWR",
]
ciphertext1_fake = [
"EALESVTRA",
"CEEROBIIA",
"DRDNDNQGE",
"TASEYLLAI",
"MUANTCAWH",
"EOMANREEO",
"COMSRLTBR",
]
def print_dimension(ciphertext):
    print(f"The dimension of the ciphertext is {len(ciphertext)} x {len(ciphertext[0])}")

def count_vowels(ciphertext):
    sum = 0
    for i in range(len(ciphertext)):
        vowels = 0
        for ch in ciphertext[i]:
            if ch == 'A' or ch =='E' or ch =='I' or ch =='O' or ch =='U':
                vowels += 1
        print("vowels for", ciphertext[i], "is", vowels, ", and differences is", abs(round(vowels - len(ciphertext[0]) * 0.4, 2)))
        sum += abs(round(vowels - len(ciphertext[0]) * 0.4, 2))
    print("The sum of differences for")
    pprint(ciphertext)
    print("is:", sum)
    print("---------------")
    return sum
        
print("Answer to the question 1:")
sum1 = count_vowels(ciphertext1)
sum2 = count_vowels(ciphertext1_fake)
print("Since", sum1, "<", sum2)
print_dimension(ciphertext1)

def column_swap(ciphertext, key):
    tmp = [list(row) for row in ciphertext]
    for i in range(len(ciphertext)):
        for j, k in enumerate(key):
           tmp[i][j] = ciphertext[i][k - 1]
    return tmp
str_array = column_swap(ciphertext1, [6, 3, 4, 1, 2, 5, 7])
ciphertext1 = ["".join(row) for row in str_array]
print("=========================")
print("Answer to the question 2:")
pprint(ciphertext1)


message1 = """CRYPTANALYSIS IN RECENT PUBLICATIONS ALSO CRYPTANALYSIS
REFERS IN THE ORIGINAL SENSE TO THE STUDY OF METHODS AND
TECHNIQUES TO OBTAIN INFORMATION FROM SEALED TEXTS THIS
INFORMATION CAN BE BOTH THE KEY USED AND THE ORIGINAL TEXT
NOWADAYS, THE TERM CRYPTANALYSIS MORE GENERALLY REFERS TO
THE ANALYSIS OF CRYPTOGRAPHIC METHODS NOT ONLY FOR CLOSURE
WITH THE AIM OF EITHER BREAKING THEM I E ABOLISHING THEIR
PROTECTIVE FUNCTION OR OR TO PROVE AND QUANTIFY THEIR
SECURITY CRYPTANALYSIS IS THUS THE COUNTERPART TO
CRYPTOGRAPHY BOTH ARE SUBFIELDS OF CRYPTOLOGY
"""

message2 = """DIE KRYPTOANALYSE IN NEUEREN PUBLIKATIONEN AUCH
KRYPTANALYSE BEZEICHNET IM URSPRUNGLICHEN SINNE DAS STUDIUM
VON METHODEN UND TECHNIKEN UM INFORMATIONEN AUS
VERSCHLUSSELTEN TEXTEN ZU GEWINNEN DIESE INFORMATIONEN
KONNEN SOWOHL DER VERWENDETE SCHLUSSEL ALS AUCH DER
ORIGINALTEXT SEIN HEUTZUTAGE BEZEICHNET DER BEGRIFF
KRYPTOANALYSE ALLGEMEINER DIE ANALYSE VON KRYPTOGRAPHISCHEN
VERFAHREN NICHT NUR ZUR VERSCHLUSSELUNG MIT DEM ZIEL DIESE
ENTWEDER ZU BRECHEN D H IHRE SCHUTZFUNKTION AUFZUHEBEN BZW
ZU UMGEHEN ODER IHRE SICHERHEIT NACHZUWEISEN UND ZU
QUANTIFIZIEREN KRYPTOANALYSE IST DAMIT DAS GEGENSTUCK ZUR
KRYPTOGRAPHIE BEIDE SIND TEILGEBIETE DER KRYPTOLOGIE
"""

message3 = """MVWZXYXEJIWGC ML BIAORR ZYZVMAKXGYRQ KPQY GPITRKRYVCQSW
POJCBW GX XFO SPSKGXEJ CILCI RY XFO WREHW YJ KOXFYHQ KRB
DIARRGAYCC XM YFRKML SRDYVKKXGYR DBSK CIYVIB DIVDW RRMQ
SRDYVKKXGYR AKR ZO FMDL RRI IOC SCIB KRB DLC YVGQMLKP ROBR
XSUKHYIW, RRI ROVK MVWZXYXEJIWGC QMBI EORCBEJVC POJCBW RY
XFO ELKPWCMQ YJ ABCNDSEBENRMA WIRRSBC RMD SLVC DYV AVSQEVC
GMRR XFO EGW SD OMRRIP LVCKOGXK RRIK S I YLSJSWFSRE DLCSV
NBSROGRSZC PYLMXGYR MB SP DS NBSTO ELN USKRRSJW DLCSV
QOGSBMRI GPITRKRYVCQSW GC XFEW RRI AYYLDIPZEPD XM
MVWZXMQVYZLW LSRR EPO WSLJGOPBC SD MVWZXMVSEI"""

message4 = """FUBSWDQDOBVLV LQ UHFHQW SXEOLFDWLRQV DOVR FUBSWDQDOBVLV
UHIHUV LQ WKH RULJLQDO VHQVH WR WKH VWXGB RI PHWKRGV DQG
WHFKQLTXHV WR REWDLQ LQIRUPDWLRQ IURP VHDOHG WHAWV WKLV
LQIRUPDWLRQ FDQ EH ERWK WKH NHB XVHG DQG WKH RULJLQDO WHAW
QRZDGDBV, WKH WHUP FUBSWDQDOBVLV PRUH JHQHUDOOB UHIHUV WR
WKH DQDOBVLV RI FUBSWRJUDSKLF PHWKRGV QRW RQOB IRU FORVXUH
ZLWK WKH DLP RI HLWKHU EUHDNLQJ WKHP L H DEROLVKLQJ WKHLU
SURWHFWLYH IXQFWLRQ RU RU WR SURYH DQG TXDQWLIB WKHLU
VHFXULWB FUBSWDQDOBVLV LV WKXV WKH FRXQWHUSDUW WR
FUBSWRJUDSKB ERWK DUH VXEILHOGV RI FUBSWRORJB"""

def calculate_IC(message):
    alphebets = [0 for i in range(26)]
    n_sum = 0
    for ch in message:
        if ch == " " or ch == "\n" or ch == ",":
            continue
        alphebets[ord(ch) - ord("A")] += 1
        n_sum += 1
    f_sum = 0
    for i in range(26):
        f_sum += alphebets[i] * (alphebets[i] - 1)
        #print(chr(ord("A") + i), ": ", alphebets[i], sep = "")
    return (f_sum / (n_sum * (n_sum - 1)))
print("=========================")
print("Answer to the question 3:")
print(f"Index of Coincidence for message 1 is {calculate_IC(message1)}.")
print(f"Index of Coincidence for message 2 is {calculate_IC(message2)}.")
print(f"Index of Coincidence for message 3 is {calculate_IC(message3)}.")
print(f"Index of Coincidence for message 4 is {calculate_IC(message4)}.")
print("=========================")
print("Answer to the question 4:")
ciphertext2 = """RHVST TEYSJ KMHUM BBCLC GLKBM HBSJH HDAYC PPWHD UUTAP STJAI
YMXKA OKARN NATNG CVRCH BNGJU EMXWH UERZE RLDMX MASRT LAHRJ
KIILJ BQCTI BVFZW TKBQE OPKEQ OEBMU NUTAK ZOSLD MKXVO YELLX
SGHTT PNROY MORRW BWZKX FFIQJ HVDZZ JGJZY IGYAT KWVIB VDBRM
BNVFC MAXAM CALZE AYAZK HAOAA ETSGZ AAJFX HUEKZ IAKPM FWXTO
EBUGN THMYH FCEKY VRGZA QWAXB RSMSI IWHQM HXRNR XMOEU ALYHN
ACLHF AYDPP JBAHV MXPNF LNWQB WUGOU LGFMO BJGJB PEYVR GZAQW
ANZCL XZSVF BISMB KUOTZ TUWUO WHFIC EBAHR JPCWG CVVEO LSSGN
EFGCC SWHYK BJHMF ONHUE BYDRS NVFMR JRCHB NGJUB TYRUU TYVRG
ZAXWX CSADX YIAKL INGXF FEEST UWIAJ EESFT HAHRT WZGTM CRS
"""
print(f"Index of Coincidence for the ciphertext is {calculate_IC(ciphertext2)}.")
print("It is a polyalphabetic cipher.")