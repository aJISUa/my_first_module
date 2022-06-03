def shopping(shop_file):
    shop_dict = {} # 생성할 사전 객체

    with open(f"./data/{shop_file}") as f:
        lines=f.readlines()
    lines=[line.rstrip('\n') for line in lines]
    lines=[line.rstrip('원') for line in lines]
    del lines[0]
    lines.remove('')
    print(lines)
    lines=' '.join(lines)
    lines=list(lines.split(' '))

    str_lines=lines[0::2]
    int_lines=[int(i) for i in lines[1::2]]

    shop_dict=dict(zip(str_lines,int_lines))
    return shop_dict

def item_price(shop_file, item):
  if __name__=='__main__':
    itemprice=shopping(shop_file)
    return itemprice[item]