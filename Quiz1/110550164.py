cypher_text = """T ZJDMBYFS VZRFGYRVY  DBVY JIYFG
FKMFSRFGZF T IFFARGL JI GJY
ITS SFDJEFC ISJD TATSD JG
TGTANQRGL TGC FKMAJSF
YOF IAJJC JI TCETGZFC XGJHAFCLF HORZO
FTZO NFTS WSRGLV HRYO RY"""
alphebets = [0 for i in range(26)]
for ch in cypher_text:
    if ch == " " or ch == "\n":
        continue
    alphebets[ord(ch) - ord("A")] += 1
for i in range(26):
    print(chr(ord("A") + i), ": ", alphebets[i], sep = "")