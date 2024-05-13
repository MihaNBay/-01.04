N, M = map(int, input().split())
ani_colors = {int(input()) for _ in range(N)}
borya_colors = {int(input()) for _ in range(M)}

common_colors = sorted(ani_colors & borya_colors)
ani_only_colors = sorted(ani_colors - borya_colors)
borya_only_colors = sorted(borya_colors - ani_colors)

print(f"Выводим номера цветов, которые есть в обоих наборах: ", len(common_colors), *common_colors, sep='\n')
print(f"Выводим номера цветов, которые есть только у Ани: ", len(ani_only_colors), *ani_only_colors, sep='\n')
print(f"Выводим номера цветов, которые есть только у Бори: ", len(borya_only_colors), *borya_only_colors, sep='\n')
