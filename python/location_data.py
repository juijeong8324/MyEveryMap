# 각 경로의 좌표를 반환하는 함수입니다
def Coordinate(location_set):
        if location_set == ('미래','어의'):
                return [[37.629286, 127.081490],[37.629425, 127.080756],[37.629594, 127.080184],[37.630340, 127.080323],[37.630607, 127.080163],[37.630717, 127.079558],
            [37.631077, 127.079594],[37.631306, 127.079534],[37.631390, 127.079543],[37.631645, 127.079073],[37.631854, 127.078558],[37.632300, 127.078679],[37.633242, 127.079031],
            [37.633543, 127.078950],[37.633686, 127.078769],[37.634036, 127.078152],[37.634160, 127.077995],[37.634518, 127.078125],[37.634906, 127.076848],[37.635185, 127.076917],
            [37.635350, 127.076836]] 
        elif location_set == ('미래', '혜성'):
                return [[37.629294, 127.081457],[37.629398, 127.081063],[37.629732, 127.081042],[37.630291, 127.081182],[37.630212, 127.081781],[37.630964, 127.081977],[37.631012, 127.081840],[37.631434, 127.081827],[37.631532, 127.082011]]
        elif location_set == ('어의','혜성'): 
                return [[37.635229, 127.076885],[37.634936, 127.076815], [37.634565, 127.078109],[37.634101, 127.077949],[37.633625, 127.078836],[37.633343, 127.079018],[37.633228, 127.079009],[37.631866, 127.078526],
                [37.631713, 127.079056],[37.631390, 127.079548],[37.631290, 127.079661],[37.631387, 127.080908],[37.631446, 127.081953],[37.631557, 127.081944]]
        else:
                return


