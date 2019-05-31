import unicodedata

from data import dakuten

if __name__ == '__main__':
    kana = dakuten.DakutenTrans().get()
    print(kana)

    s = '株式会社フィールト゛サーヒ゛ス'
    sm = 'ｲﾜﾞﾌﾞﾁ ﾋｻｵ'
    sn = unicodedata.normalize('NFKC', sm)
    print(sm)
    print(sn)

    for key in kana.keys():
        s = s.replace(key, kana[key])
    print(s)

    s1 = unicodedata.normalize('NFKC', s)
    print(s1)

    print("O46¥;ﾝ7}V3")