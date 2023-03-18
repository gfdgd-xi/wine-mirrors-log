#!/usr/bin/env python3
import os
import json
import datetime

programPath = os.path.split(os.path.realpath(__file__))[0]  # 返回 string
lists = []
for i in os.listdir(programPath):
    if i[-3:] == ".md" and i != "README.md":
        print(f"添加 {i}")
        if os.path.exists(f"{programPath}/{os.path.splitext(i)[0]}.txt"):
            print("检测到", f"{programPath}/{os.path.splitext(i)[0]}.txt")
            txt = f"{os.path.splitext(i)[0]}.txt"
        else:
            txt = i
        lists.append([i, txt])
print("列表:", lists)
showString = f"""# 关于 Wine 运行器  
Wine运行器是一个能让Linux用户更加方便地运行Windows应用的程序，内置了对Wine图形化的支持、各种Wine工具、自制的Wine程序打包器和运行库安装工具等。  
它同时还内置了基于VirtualBox制作的、专供小白使用的Windows虚拟机安装工具，可以做到只需下载系统镜像并点击安装即可，无需考虑虚拟机的安装、创建、分区等操作。  

[![star](https://gitee.com/gfdgd-xi/deep-wine-runner/badge/star.svg?theme=dark)](https://gitee.com/gfdgd-xi/deep-wine-runner/stargazers)  

# Wine 更新日志列表（更新时间：{datetime.datetime.now().year}年{datetime.datetime.now().month}月{datetime.datetime.now().day}日 {datetime.datetime.now().hour}:{datetime.datetime.now().minute}:{datetime.datetime.now().second}）  
"""
for i in lists:
    if i[0] == i[1]:
        showString += f"- [{os.path.basename(i[0])}]({os.path.basename(i[0])})  \n"
        continue
    showString += f"- [{i[0]}]({i[0]}) 或 [{i[1]}]({i[1]})  \n"
showString += "\n# ©2020~Now gfdgd xi、为什么您不喜欢熊出没和阿布呢"
print("生成的 markdown:\n" + showString)
with open(f"{programPath}/README.md", "w") as file:
    file.write(showString)
with open(f"{programPath}/LogList.json", "w") as file:
    file.write(json.dumps(lists))
print("写入完成！")