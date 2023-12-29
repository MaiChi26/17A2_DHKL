animals = ["ant", "bear", "cat", "dog", "elephant", "fish", "goat", "hippo"]
animal=input('tôi muốn tìm con:')
print('số lượng động vật:',len(animals))
for i in animals:
    if animal==i:
        print('có',animal,'trong danh sách động vật')
        break
else:
    print('không có')
    