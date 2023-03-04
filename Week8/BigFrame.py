"""BigFrame"""
def frame():
    """_"""
    txt_1 = input().rstrip()
    txt_2 = input().rstrip()
    txt_3 = input().rstrip()
    txt_4 = input().rstrip()
    txt_5 = input().rstrip()
    member_txt = max(len(txt_1), len(txt_2), len(txt_3), len(txt_4), len(txt_5))
    print('*'*(member_txt+4))
    print('* %s%s *'%(txt_1, ' '*(member_txt-len(txt_1))))
    print('* %s%s *'%(txt_2, ' '*(member_txt-len(txt_2))))
    print('* %s%s *'%(txt_3, ' '*(member_txt-len(txt_3))))
    print('* %s%s *'%(txt_4, ' '*(member_txt-len(txt_4))))
    print('* %s%s *'%(txt_5, ' '*(member_txt-len(txt_5))))
    print('*'*(member_txt+4))

frame()
