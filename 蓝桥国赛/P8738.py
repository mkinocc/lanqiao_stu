if __name__ == '__main__':
    tiangan = ["geng", "xin", "ren", "gui","jia", "yi", "bing", "ding", "wu", "ji"]
    dizhi = ["zi", "chou", "yin", "mao", "chen", "si", "wu", "wei", "shen", "you", "xu", "hai"]
    in_year = int(input())
    s_tiangan = in_year % 10
    # 为什么减4 因为我要凑求余数后是0， 从庚子年开始
    s_dizi = (in_year - 4) % 12
    print("{}{}".format(tiangan[s_tiangan], dizhi[s_dizi]))
