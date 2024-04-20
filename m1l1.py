meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "AFK": "klavyeden uzakta",
            "NT": "iyi deneme",
            "BTW": "bu arada",
            "idk": "Bilmiyorum",
            "knk": "kanka",
            "mb": "benim hatam",
            "gg": "iyi oyun"
            }


word = input("kelimeyi yazın")

if word in meme_dict.keys():
    # Kelime eşleşiyorsa ne yapmalıyız?
    print(meme_dict[word])
else:
    # Kelime eşleşmiyorsa ne yapmalıyız?
    print("kelime yok....")
