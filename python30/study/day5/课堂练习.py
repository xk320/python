old_dict = {
    "#1":{ 'hostname':'c1', 'cpu_count': 2, 'mem_capicity': 80 },
    "#2":{ 'hostname':'c1', 'cpu_count': 2, 'mem_capicity': 80 },
    "#3":{ 'hostname':'c1', 'cpu_count': 2, 'mem_capicity': 80 }
}

new_dict = {
    "#1":{ 'hostname':'c1', 'cpu_count': 2, 'mem_capicity': 800 },
    "#3":{ 'hostname':'c1', 'cpu_count': 2, 'mem_capicity': 80 },
    "#4":{ 'hostname':'c2', 'cpu_count': 2, 'mem_capicity': 80 }
}
# 1、 原来没有  -》 插入
# 2、 原来有的 -》 更新
# 3、 原来有，新的没有 -> 原来的删除

# 三个列表
#   要更新的数据
#   要删除的数据
#   要新增的数据

s1_old = set(old_dict)
s1_new = set(new_dict)
li_update = s1_old.intersection(s1_new)
li_add = s1_new.symmetric_difference(s1_old.intersection(s1_new))
li_del = s1_old.symmetric_difference(s1_old.intersection(s1_new))
print(old_dict)
for i in li_add :
    old_dict[i] = new_dict[i]
for i in li_del :
    old_dict.pop(i)
for i in li_update :
    old_dict[i].update(new_dict[i])
print(old_dict)


