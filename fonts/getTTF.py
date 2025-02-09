from fontTools.ttLib import TTCollection

# 加载 TTC 文件
ttc = TTCollection('Songti.ttc')

# 提取第一个字体
print(len(ttc.fonts))
font = ttc.fonts[3]

# 保存为 TTF 文件
font.save('Songti0.ttf')

