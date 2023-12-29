

# 密碼工程 Quiz 3

[![hackmd-github-sync-badge](https://hackmd.io/qsQ5mABDQ2eaZWrAsU61Tg/badge)](https://hackmd.io/qsQ5mABDQ2eaZWrAsU61Tg)

解決 Polyalphabetic Substitution Ciphers  
這個程式有以下功能  
1. determine the keyword length of these two encrypted messages using I.C. 
2. Then solve the encryption keyword letters 
3. Finally, break this ciphertext and recover the plaintext.
- Note: The programs will need to read the message from stdin and output 
the result followed by a newline to stdout.
## How to use?
### Exercise
在終端機輸入```python .\110550164.py```進行編譯  

將透過 Monoalphabetic Substitution Ciphers 所加密的密文輸入並按下 Enter，明文就會被寫入 message_out.txt 之中。  

### Bonus 1
在終端機輸入```python .\110550164_bonus_1.py```進行編譯就可以看到解碼後的明文了
## Source Code
以下是我程式在執行時主要的code
```python=
ciphertext = get_from_stdin()
guess_max_key_size = 6
key_size = get_key_size(ciphertext, guess_max_key_size)
# print("The key size is:", key_size)
split_text = split_with_keysize(ciphertext, key_size)
#print_chi(split_text, key_size)
key = generate_key(split_text)
# print("The key is:", key)
plain_text = decrypt(split_text, key)
plain_text = rearrange_plaintext(plain_text)
# print("The plaintext is:")
# print(plain_text)

fp = open("message_out.txt", "w")
fp.write(plain_text)
fp.close()
```
接下來我會將我的程式碼分成幾個部分:  
1. 從 stdin 讀檔
2. 找到 key_size
3. 產生 key
4. 用 key 將明文找出來
### 從 stdin 讀檔
```python=
def get_from_stdin():
    message = ""
    for line in fileinput.input():
        if(line == '\n'):
            break
        message += line.rstrip()
    message = ''.join(message.split())
    #print("the ciphertext is:", ciphertext)
    return message
```
其實沒有什麼好說的，就是用fileinput這個函式庫把整個message讀進來然後回傳而已
### 找到 key_size
在主要程式碼中 call 了以下這幾行:
```python=
guess_max_key_size = 6
key_size = get_key_size(ciphertext, guess_max_key_size)
print("The key size is:", key_size)
```
這段程式碼意思是:  

我先猜 key_size 的最大可能大小為 6，並把這整個 ciphertext 加上猜的大小丟到 get_key_size 裡面找出最有可能的 key_size。   

最後再將結果印出來。

以下將會介紹整個 get_key_size 是怎麼運作的。
#### get_key_size
```python=
def get_key_size(message, guess_max_key_size):
    max_IC = -1
    for i in range(1, guess_max_key_size + 1):
        IC_keys = calculate_IC_keys(message, i)
        #print(IC_keys)
        if (max_IC < IC_keys):
            max_IC = IC_keys
            key_size = i
    return key_size
```
這段程式碼是將密文和所猜想到的最大 key_size 傳進來以後，利用 IC 來計算出最有可能的鑰匙大小。  

如果是加密的所使用 key_size 的話，IC 會是所有 key_size 裡面最大的，所以可以利用這點將 key_size 從1遍歷所猜想到的最大範圍(這裡是到6)，將平均 IC 最大的 key_size 記錄下來並回傳
#### calculate_IC_keys
```python=
def calculate_IC_keys(message, key_size):
    Incidence_of_coincidence = [0 for i in range(key_size)]
    for key_row in range(key_size):
        message_jump = ""
        for i in range(key_row, len(message), key_size):
            message_jump += message[i]
        #print("=======")
        #print(message_jump)
        #print("=======")
        Incidence_of_coincidence[key_row] = calculate_IC(message_jump)
    average_IC = statistics.mean(Incidence_of_coincidence)
    #print("The average IC of the ciphertext is:", average_IC)
    return average_IC
```
這段程式碼是將密文切割後，計算出每段切割後密文的 IC ，並將平均IC回傳  

例如密文是 ABCDEFGH, 且 key_size 為 2, 那麼就會將整段訊息切成 ACEG 以及 BDFH, 並呼叫 calculate_IC 將 ACEG 以及 BDFH 的 IC 算出來，最後再回傳這兩個切割過後密文的 IC 平均
#### calculate_IC
```python=
def calculate_IC(message):
    alphebets = [0 for i in range(26)]
    for ch in message:
        alphebets[ord(ch) - ord("A")] += 1
    f_sum = 0
    for i in range(26):
        f_sum += alphebets[i] * (alphebets[i] - 1)
        #print(chr(ord("A") + i), ": ", alphebets[i], sep = "")
    return (f_sum / (len(message) * (len(message) - 1)))
```
這段程式碼是利用 IC 的公式算出傳入的字串的 IC

公式如下:
![](https://i.imgur.com/YDxilkP.png)

### 產生 key
接著跟產生 key 有關的程式碼是以下幾行:
```python=
split_text = split_with_keysize(ciphertext, key_size)
#print_chi(split_text, key_size)
key = generate_key(split_text)
print("The key is:", key)
```
有兩步驟，分別是:  
1. 將 ciphertext 透過預測出的最有可能 key_size 切割
2. 將切割過後的 ciphertext 丟進 generate_key 裡面產生 key  
#### split_with_keysize
```python=
def split_with_keysize(message, key_size):
    split_texts = ["" for i in range(key_size)]
    for key_row in range(key_size):
        for i in range(key_row, len(message), key_size):
            split_texts[key_row] += message[i]
    return split_texts
```
在產生key之前，我先寫了一個 split_with_keysize，用途是將傳入的 message 分開  

其實做法跟上方的 calculate_IC_keys 幾乎一樣，差別只是split_with_keysize的功能只有透過 key_size 把整個 message 並回傳回去一個 2 維陣列 (key_size x split_text 長度)就是了。
#### generate_key
```python=
def generate_key(split_text):
    key = ""
    for i in range(len(split_text)):
        letters = count_letters(split_text[i])
        key += find_chi(letters, split_text)
    return key
```
generate_key 的在做的事情其實很簡單，就是透過  
1. 計算 split_text 每個 row 中的所有字母出現個數，也就是算出每段被切割過後的密文所出現過後的字母次數  

- Example: 像是ABCDEFGH, 被切割成 ACEG 和 BDFH，那麼 count_letters 會把 ACEG 以及 BDFH 的字母出現次數算出來。

2. 利用所有字母出現個數以及 split_text 傳入 find_chi 裡面，並透過 find_chi 計算出每個 row 的切割過後密文的 key 為何  

透過這兩步驟就能把 key 找出來了    
#### count_letters
```python=
def count_letters(message):
    letters = [0 for i in range(26)]
    for ch in message:
        letters[ord(ch) - ord("A")] += 1
    return letters
```
沒什麼好說的，就是把一段 message 的 A ~ Z 字母出現次數算出來並回傳
#### find_chi
```python=
def find_chi(letters, split_text):
    letter_happen_rate = [0.082, 0.015, 0.028, 0.043, 0.13,
                      0.022, 0.02, 0.061, 0.07, 0.0015,
                      0.0077, 0.04, 0.024, 0.067, 0.075,
                      0.019, 0.00095, 0.06, 0.063, 0.091, 
                      0.028, 0.0098, 0.024, 0.0015, 0.02, 
                      0.00074]
    letter_expected = [letter_happen_rate[i] * len(split_text) for i in range(26)]
    #print(len(split_text))
    letters = deque(letters)
    min_chi_square = float("inf")
    for j in range(26):
        chi_square = sum([(letters[i] - letter_expected[i]) * (letters[i] - letter_expected[i]) / letter_expected[i] for i in range(26)])
        #print("chi of", chr(j + ord('A')), ":", chi_square)
        if min_chi_square > chi_square:
            key = chr(j + ord('A'))
            min_chi_square = min(min_chi_square, chi_square)
        letters.rotate(-1)
    #print(letters)
    #print(letter_expected)
    #print(chi_square)
    return key
```
這段程式碼在做兩件事: 
1. 計算期望值: 我先去 [wiki](https://en.wikipedia.org/wiki/Letter_frequency) 裡面將英文字母出現機率輸入到 letter_happen_rate 中，並將其和 split_text 的長度相乘得到每個字母的出現次數期望值。
2. 透過 chi test 的公式，也就是![](https://i.imgur.com/BZ7Gzva.png)
將最有可能的 key 計算出來，並回傳最可能的 key (也就是最小的 chi square 值所對應到的英文字母)  

值得一提的是，我將這段 message 原本的字母出現次數變成deque，就能透過 deque 的 rotate 將整串陣列往左移一格，這樣就能很方便的計算所有 26 種可能的 key 值。
#### print_chi
```python=
def print_chi(split_text, key_size):
    for i in range(key_size):
        print("==============")
        print("chi for the", i,"th key is:")
        letters = count_letters(split_text[i])
        find_chi(letters, split_text[i])
        print("==============")
```
用來 Debug chi test 用的而已
### 用 key 將明文找出來
跟找出明文有關的 code 是底下幾行:  
```python=
plain_text = decrypt(split_text, key)
plain_text = rearrange_plaintext(plain_text)
print("The plaintext is:")
print(plain_text)
```
分成兩個部分:
1. 將切割過後的密文透過 key 解碼
2. 將明文重新排列，因為 decrypt 回傳的是很多 row 的 矩陣，要從上往下讀很麻煩
#### decrypt
```python=
def decrypt(split_text, key):
    #print(key[0])
    plain_text = [restore_with_each_key(split_text[i], key[i]) for i in range(len(split_text))]
    return plain_text
```
將每段 split_text 用 key 還原
#### restore_with_each_key
```python=
def restore_with_each_key(message, shift_letter):
    shifted_message =""
    for ch in message:
        #print(ch)
        #print(shift_letter)
        #print(chr((ord(ch) - ord("A") + ord(shift_letter) - ord("A")) % 26 + ord("A")))
        shifted_message += chr((ord(ch) - ord("A") - ord(shift_letter) - ord("A")) % 26 + ord("A"))
        #print(ch)
    #print(shifted_message)
    return shifted_message
```
將所有密文位移 ( key - 密文英文字母 )，回推出明文
#### rearrange_plaintext
```python=
def rearrange_plaintext(plain_text):
    rearranged = ""
    for j in range(len(plain_text[0])):
        for i in range(len(plain_text)):
            if (j >= len(plain_text[i])):
                return rearranged
            rearranged += plain_text[i][j]
    return rearranged
```
從 column 開始讀明文並把他合到字串上回傳
## Source Code for Bonus 1
```python=
import hashlib
PASSLIST = [
        'test',
        'name',
        'hello',
        'password',
        'goodbye',
        '12345',
        '123456',
        '123456789',
        'test1'
]
def solve_hash(hash):
    print("Solving hash:", hash)
    for word in PASSLIST:
        guess = hashlib.md5(word.encode('utf-8')).hexdigest()
        if guess.upper() == hash or guess.lower() == hash:
                print(f'[+] Password found: {word}')
                return
        else:
                print(f'[-] Guess: {word} incorrect...')
    print('Password not found in wordlist...')

hash1 = '5f4dcc3b5aa765d61d8327deb882cf99'
hash2 = '5a105e8b9d40e1329780d62ea2265d8a'

solve_hash(hash1)
solve_hash(hash2)
```
PASSLIST中放入猜的字串，並將 hash values 放入 hash1, hash2，最後再丟到 solve_hash 裡面跑
### solve_hash
其實就是利用 ```hashlib.md5(word.encode('utf-8')).hexdigest()``` 將所猜的字串一一跑過，如果猜的字串的 md5 加密相同就知道明文是那個猜的字串了。
## Test Results
我有將解碼過後的明文放在 message1_out.txt 以及 message2_out.txt
### Encrypt message 1
將 Encrypted message 1
```
ZQQTK PQUWD PGMWD BQTXY LFQWL SHAJB UCIPV KUQEJ RBAAC LRSIZ ZCRWT LDFMT PGYXF ISOSE ASZXN PHTAY HHIIR ADDIJ LBFO
E VKUWW VFFLV TCEXG HFFXF ZVGXF BFQEI ZOSEZ UGFGF UJUGK PCZWZ UQQJI VAFLV CSDCX YOPYR SQTEI HQFII VTAYI LRGGR AWAR
N LAGWK JCZXZ UIMPC FTAVX LHMRU LAMRT PDMXV VIDWV SJQWW YCYOE VKXIU NSBVV CWAYJ SMMGH BWDIU DSYYJ AGQXR ZWP
IF SRZSK PCZWR URQQS YOOIW YSELF USEEE KOEAV SSMVE DSYYJ APQHR PZKYE SSMVE PBSWF TSFLZ UUILZ JVUXY HGOSJ AIERF ZAMP
C SONSL YOZHR ULUIK FHAET XIUVV HBPXY PGPMW MWOYC AMMXK HQTIJ PHEIC MAAVV JZAWV SMFSR UOSIZ UKTMT ODDSX YSEW
Y HGSEZ USPEJ AFARX HGOIE KSZGP VJQVG YSVYU PQQEE KWZAY PQTTV YGARJ HBPXY PBSWR YSPEP IMPEP MWZHZ UUFLV PFDIR SZQ
ZV SWZPZ LIAJK OSUVT VBHIE AWARR SJMPL LHTIJ HAQTI PBOMG SSEAY PQTLR CSEAV WHMAR FHDEU PHUSE HZMFL ZSEEE KKTMT O
ODID HYURX YOBMU OOHST HAARX AVQVV CSZYV ZCRWZ USOYI PGFWR UREXI PDBME NHTIK OWZXR DRDCM LWXJI VAMXK YOOXZ C
SEYG LFEXZ AWARJ HFQAF YYURX HGMGK PJQPP PBXMK LFMXL YSMWZ UGAGZ LHKXY LQDIU BZUXP VTARV DFUXV YCDXY LDMVK POX
MK FCREE VHTII MWZHJ HGBSN LFRYC HHAYT OGFSE LOZHR ZKTSC LGAQV HQTEJ AWEID LBFME AVQLV HZFLP ZQQTK PQUWD VTMXV
TDQVR ASOPR ZGAJR UHMKF UWEXJ HGFLV KFQED ZCRGF UGQVM HHUWD VFFLV PABSJ AIDIJ VTBPL YOXMJ AGURV JIDIJ PBFLV JVGVT
OVUWK VFKEE KHDEU PHUSE DVQXY LFAJR UQUIE ACDGF TDMVR AWHIC FFQGV UHFMD LGMVV ZINNV JHQHK VJQVP KWRJV YSZXY
HBPPZ UURVF THTEK DVUGY AVQME KIXKV UQQSI JFQHL SWFCF MTAVD LFMKV ZQAYC KOXPF DAQVV ZHMXV TSZXJ HFQNV HZAYJ SM
IEK JVQHR URFLV TCFMM LGAJK OSIVZ ASDJF YAMWZ TDAVK HBFEE PBSVV KWQRK PBFLV HBMPP ZWESW OWELZ ZHAVP HGFLV MOO
XJ OSDIT VFPWG YCNES PZUXP PGMTF DSDJL SOZHK YCGFC LGAQV ASEXR URUXZ ZPKXY PGFVF BPXIJ VAQWK HBPEI KHTEK HZMVX LD
AVK PCZSW OWEXF YWOEC LJUHV UQQMJ ZWRXV KQARJ PGFIE JMUWE VZQWJ WSDXZ UOOMF BGMRU LLMGK PBSME PHEHV TOZHJ
PBNVZ LTFSN YWFIR OWEXF YMIID BGFOE VKYSI LHTEE TSDIW HQFWY BAMRE HHGVV CWQAV KIZHV YOZME KIOXZ VBAJV EHQRU LRQ
BG LFUIE JSUWK OSNIJ AVQPG ACFLV JFUXZ JWEQF MVGQR UVUWK VFKLZ ZHAVZ JOXGY HFMGK LFEGR UCZPP ISQWK PAMXV KPKXY L
GFEE KODHN OWOLY BAMRV EDQVZ LBOIN OSFLV YOOXL HZAVK YOPMK PCZEI FVMWW BFZMJ OSPXF MCDQT VFDIT AJUIN ZCRME K
WHMU BOXWN LAGWK YSSEI KHTID HGRSI TWZKG HFFWF MOSVV HHILF SSIID BGFQV HGGVV AVQQS FHTIZ YFQPR AWARK VHTID HGE
SW ISURX ZPKAY VAFLV FODIJ BFDSL URQHR URURT VBFID WZMXZ UUFLV PBOMU LBFWZ UHTIZ YZUZV ZCDGF URUXZ VBILZ JVFVR KW
FMF UVMWY HBPIU KCIRK VIEAV TIEXI HHTII JCZWZ KSDXY LUQRV YOXFV HFURX VTFLV DVAPV UODVR AWHIK OOZXY LFQWG LQFMM
LDDSS HPUPZ AMAJZ AGPIK HWX
```
輸入並按下 Enter ，可以得到以下輸出: 
```
The key size is: 5
The key is: HOMER
The plaintext is:
SCEPTICISMISASMUCHTHERESULTOFKNOWLEDGEASKNOWLEDGEISOFSCEPTICISMTOBECONTENTWITHWHATWEATPRESENTKNOWISFORTHEMOSTPARTTOSHUTOUREARSAGAINSTCONVICTIONSINCEFROMTHEVERYGRADUALCHARACTEROFOUREDUCATIONWEMUSTCONTINUALLYFORGETANDEMANCIPATEOURSELVESFROMKNOWLEDGEPREVIOUSLYACQUIREDWEMUSTSETASIDEOLDNOTIONSANDEMBRACEFRESHONESANDASWELEARNWEMUSTBEDAILYUNLEARNINGSOMETHINGWHICHITHASCOSTUSNOSMALLLABOURANDANXIETYTOACQUIREANDTHISDIFFICULTYATTACHESITSELFMORECLOSELYTOANAGEINWHICHPROGRESSHASGAINEDASTRONGASCENDENCYOVERPREJUDICEANDINWHICHPERSONSANDTHINGSAREDAYBYDAYFINDINGTHEIRREALLEVELINLIEUOFTHEIRCONVENTIONALVALUETHESAMEPRINCIPLESWHICHHAVESWEPTAWAYTRADITIONALABUSESANDWHICHAREMAKINGRAPIDHAVOCAMONGTHEREVENUESOFSINECURISTSANDSTRIPPINGTHETHINTAWDRYVEILFROMATTRACTIVESUPERSTITIONSAREWORKINGASACTIVELYINLITERATUREASINSOCIETYTHECREDULITYOFONEWRITERORTHEPARTIALITYOFANOTHERFINDSASPOWERFULATOUCHSTONEANDASWHOLESOMEACHASTISEMENTINTHEHEALTHYSCEPTICISMOFATEMPERATECLASSOFANTAGONISTSASTHEDREAMSOFCONSERVATISMORTHEIMPOSTURESOFPLURALISTSINECURESINTHECHURCHHISTORYANDTRADITIONWHETHEROFANCIENTORCOMPARATIVELYRECENTTIMESARESUBJECTEDTOVERYDIFFERENTHANDLINGFROMTHATWHICHTHEINDULGENCEORCREDULITYOFFORMERAGESCOULDALLOWMERESTATEMENTSAREJEALOUSLYWATCHEDANDTHEMOTIVESOFTHEWRITERFORMASIMPORTANTANINGREDIENTINTHEANALYSISOFHISHISTORYASTHEFACTSHERECORDSPROBABILITYISAPOWERFULANDTROUBLESOMETESTANDITISBYTHISTROUBLESOMESTANDARDTHATALARGEPORTIONOFHISTORICALEVIDENCEISSIFTEDCONSISTENCYISNOLESSPERTINACIOUSANDEXACTINGINITSDEMANDSINBRIEFTOWRITEAHISTORYWEMUSTKNOWMORETHANMEREFACTSHUMANNATUREVIEWEDUNDERANINDUCTIONOFEXTENDEDEXPERIENCEISTHEBESTHELPTOTHECRITICISMOFHUMANHISTORYHISTORICALCHARACTERSCANONLYBEESTIMATEDBYTHESTANDARDWHICHHUMANEXPERIENCEWHETHERACTUALORTRADITIONARYHASFURNISHEDTOFORMCORRECTVIEWSOFINDIVIDUALSWEMUSTREGARDTHEMASFORMINGPARTSOFAGREATWHOLEWEMUSTMEASURETHEMBYTHEIRRELATIONTOTHEMASSOFBEINGSBYWHOMTHEYARESURROUNDEDANDINCONTEMPLATINGTHEINCIDENTSINTHEIRLIVESORCONDITIONWHICHTRADITIONHASHANDEDDOWNTOUSWEMUSTRATHERCONSIDERTHEGENERALBEARINGOFTHEWHOLENARRATIVETHANTHERESPECTIVEPROBABILITYOFITSDETAILS
```
### Encrypted message 2
將 Encrypted message 2
```
IVIKDKDQMJGLPWLZGMPFBJIIDBBYSLJDXFGBIWWEHAPHEYSGNCCYOOTSTZABCOBVRTAZEYWVWWAZAIDGAZ
PETHPVBPWOBVJXGFMDOBCGPFKXKSZZAIGCJRPETACJHUTHPVHKJHPZHFPMEVZEQSBYOMHSDVFTASFGZTC
OBZCGHFMDOBCWVNVBRVKRGXDBMKFBTGBVGMPTBVFMTGBLBMXZWESHGCBYSKDTBYSFWOARQHCJQEQBC
UIDCNCHWWGNEDWIHPTKQCZGDKIGDENHPZGIGWVTWIASBFHATQIJSBCDWZBMPGQKKTHTQIGMEFMJSGISLK
CFTHPVFXLSZVHAGSMGCLHWJCSXMDTRBTIWWEGHUHPVGXRZCJWHCCZZBVPFKVFTIWWECYIVQJUXCHTVAT
CWVRBHJHPFILTCNYWLUOBYSKHAIEGBDBBYSKTKIJHATSFGZTCOBZCGIVIKVXLOAZBAXRQEUYDFITFBBSWIHA
PHPVKTHAIUOGSHPRHMWSGNWLWSLKCTKCQUOGPGGCIFDFBYOMWSPRRLDAMUWLTOAVKAXQPTONHSLYWL
HSOISZPHQFBBRCCCRMWWVBCYCCWKVXGOLVENPHMJCEJHQFBLIVMJSMWSVYOWICJVGBUHMUOGSPICOGR
SLRUTXBAKSTRVWKVXG
```
輸入並按下 Enter ，可以得到以下輸出:
```
The key size is: 6
The key is: POIROT
The plaintext is:
THATPROCESSSAIDISTARTSUPONTHESUPPOSITIONTHATWHENYOUHAVEELIMINATEDALLWHICHISIMPOSSIBLETHENWHATEVERREMAINSHOWEVERIMPROBABLEMUSTBETHETRUTHITMAYWELLBETHATSEVERALEXPLANATIONSREMAININWHICHCASEONETRIESTESTAFTERTESTUNTILONEOROTHEROFTHEMHASACONVINCINGAMOUNTOFSUPPORTWEWILLNOWAPPLYTHISPRINCIPLETOTHECASEINPOINTASITWASFIRSTPRESENTEDTOMETHEREWERETHREEPOSSIBLEEXPLANATIONSOFTHESECLUSIONORINCARCERATIONOFTHISGENTLEMANINANOUTHOUSEOFHISFATHERSMANSIONTHEREWASTHEEXPLANATIONTHATHEWASINHIDINGFORACRIMEORTHATHEWASMADANDTHATTHEYWISHEDTOAVOIDANASYLUMORTHATHEHADSOMEDISEASEWHICHCAUSEDHISSEGREGATIONICOULDTHINKOFNOOTHERADEQUATESOLUTIONSTHESETHENHADTOBESIFTEDANDBALANCEDAGAINSTEACHOTHER
```
### Bonus 1
```
Solving hash: 5f4dcc3b5aa765d61d8327deb882cf99
[-] Guess: test incorrect...
[-] Guess: name incorrect...
[-] Guess: hello incorrect...
[+] Password found: password
Solving hash: 5a105e8b9d40e1329780d62ea2265d8a
[-] Guess: test incorrect...
[-] Guess: name incorrect...
[-] Guess: hello incorrect...
[-] Guess: password incorrect...
[-] Guess: goodbye incorrect...
[-] Guess: 12345 incorrect...
[-] Guess: 123456 incorrect...
[-] Guess: 123456789 incorrect...
[+] Password found: test1
```
```5f4dcc3b5aa765d61d8327deb882cf99```對應到的明文是```password```  

```5a105e8b9d40e1329780d62ea2265d8a```對應到的明文是```test1```
## Reference


https://nicholasmordecai.co.uk/programming/creating-simple-python-md5-cracker/  

https://s1.nordcdn.com/nord/misc/0.55.0/nordpass/200-most-common-passwords-en.pdf  


https://stackoverflow.com/questions/17350330/python-array-rotation

# Answer to Bonus 2
>Perfect secrecy achieved with RSA?  
>Give your answer and reasons in README by creating a 
separated subdirectory apart from the program code 
explanation

我認為 RSA 沒有辦法達成 Perfect Secrecy  

RSA 是透過 receiver 的 public key 和 sender 的 private key 進行加密，而 Perfect secrecy 是指就算給 attacker 不管多少計算資源都沒辦法從 ciphertext 得到任何有關 plaintext 的訊息，也就是老師上課講的：「亂的可以。」  

但是 RSA 卻沒辦法達到 Perfect Secrecy，原因是透過 RSA 加密過後的 ciphertext 還是可以得到一些有關 plaintext 的訊息。  

因為 public key 是固定的，如果相同的 plaintext 透過相同的 public key 加密，得到的 ciphertext 也會是相同的，而且 ciphertext 的長度會和 plaintext 的長度有相關，所以加密過後的 ciphertext 還是可以得到有關 plaintext 的訊息，也就是代表 RSA 並沒有辦法達到 perfect secrecy。  

但 RSA 還是能廣泛應用的原因是因為電腦算力還不夠在有限的時間內暴力破解，如果未來電腦算力足夠的話就會被淘汰了。