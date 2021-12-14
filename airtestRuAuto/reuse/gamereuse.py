import calendar

from airtest.core.api import *
from airtest.cli.parser import cli_setup
import os

if not cli_setup():
    auto_setup(__file__, logdir='./reuse/log')

# 当前时间戳
currentTimestamp = str(calendar.timegm(time.gmtime()))


# 适配
def shipei():
    # 获取设备的宽度和高度
    w, h = device().get_current_resolution()
    return w, h


# 应用权限
def popup():
    w, h = shipei()
    # 识别文字：电话
    wait(Template(os.getcwd()+"\\reuse\\img\\tpl1637488379134.png", record_pos=(-0.105, -0.027), resolution=(2280, 1080)), timeout=10)
    # 点击确定按钮
    touch(Template(os.getcwd()+"\\reuse\\img\\tpl1637488412189.png", record_pos=(0.107, 0.073), resolution=(2280, 1080)))


# 账号登录
def login():
    w, h = shipei()
    sleep(6)
    touch([0.453 * w, 0.634 * h])
    text(currentTimestamp)
    print(currentTimestamp)
    sleep(2)
    # 点击进入游戏
    touch(Template(os.getcwd()+"\\reuse\\img\\tpl1637491173439.png", record_pos=(-0.002, 0.15), resolution=(2280, 1080)))
    sleep(5)  # 加载


# 创建角色（跳过CG-创角完成）
def createRole():
    w, h = shipei()
    # 等跳过按钮
    wait(Template(os.getcwd()+"\\reuse\\img\\tpl1637517719300.png", record_pos=(0.401, -0.205), resolution=(2280, 1080)), timeout=60)
    sleep(2)
    # 点击跳过
    touch([0.938 * w, 0.06 * h])
    # 等待创角按钮
    wait(Template(os.getcwd()+"\\reuse\\img\\tpl1637491382786.png", record_pos=(0.251, 0.154), resolution=(2280, 1080)), timeout=60)
    # 选择女统帅
    touch(Template(os.getcwd()+"\\reuse\\img\\tpl1637491961100.png", record_pos=(0.306, -0.031), resolution=(2280, 1080)))
    # 点击输入框
    touch([0.718 * w, 0.613 * h])
    # 删除默认名字
    for i in range(10):
        keyevent("67")
    text(currentTimestamp)
    sleep(2)
    # 点击创角按钮
    touch(Template(os.getcwd()+"\\reuse\\img\\tpl1637491382786.png", record_pos=(0.252, 0.155), resolution=(2280, 1080)))


# 对话
def dialogue(name):
    w, h = shipei()
    if name == "蛮族蚁首领":
        wait(Template(os.getcwd()+"\\reuse\\img\\tpl1637516135918.png", record_pos=(0.064, 0.111), resolution=(2280, 1080)), timeout=60)
        sleep(3)
        touch([0.465 * w, 0.513 * h])
        sleep(3)
    elif name == "蚁后":
        wait(Template(os.getcwd()+"\\reuse\\img\\tpl1637516522093.png", record_pos=(0.064, 0.111), resolution=(2280, 1080)), timeout=60)
        sleep(3)
        touch([0.465 * w, 0.513 * h])
        sleep(3)
    elif name == "凯撒":
        wait(Template(os.getcwd()+"\\reuse\\img\\tpl1637516731604.png", record_pos=(-0.125, 0.114), resolution=(2280, 1080)), timeout=60)
        sleep(7)
        touch([0.465 * w, 0.513 * h])
    elif name == "图拉真":
        wait(Template(os.getcwd()+"\\reuse\\img\\tpl1637516765379.png", record_pos=(-0.12, 0.112), resolution=(2280, 1080)), timeout=60)
        sleep(3)
        touch([0.465 * w, 0.513 * h])
        sleep(3)
    elif name == "弓骑蚁":
        wait(Template(os.getcwd()+"\\reuse\\img\\tpl1637520746949.png", record_pos=(-0.117, 0.114), resolution=(2280, 1080)), timeout=60)
        sleep(3)
        touch([0.51 * w, 0.843 * h])
        sleep(3)
    elif name == "苏拉":
        wait(Template(os.getcwd()+"\\reuse\\img\\tpl1637521786242.png", record_pos=(0.035, 0.11), resolution=(2280, 1080)), timeout=60)
        sleep(3)
        touch([0.51 * w, 0.843 * h])
        sleep(3)
    elif name == "尤利娅":
        wait(Template(os.getcwd() + "\\reuse\\img\\tpl1637520332110.png", record_pos=(0.035, 0.11), resolution=(2280, 1080)), timeout=60)
        sleep(3)
        touch([0.51 * w, 0.843 * h])
        sleep(3)


# 新手真实战斗
def novice_battle(step):
    w, h = shipei()
    # 识别可获取的资源
    if step == 1:
        wait(Template(os.getcwd()+"\\reuse\\img\\tpl1637494225002.png", record_pos=(-0.405, -0.099), resolution=(2280, 1080)), timeout=60)
        sleep(3)
    # 识别结算
    elif step == 2:
        wait(Template(os.getcwd()+"\\reuse\\img\\tpl1637494770260.png", record_pos=(-0.386, 0.196), resolution=(2280, 1080)), timeout=60)
        sleep(7)   # 优化
        touch(Template(os.getcwd()+"\\reuse\\img\\tpl1637494818625.png", record_pos=(0.0, 0.202), resolution=(2280, 1080)))
        sleep(3)
    # 识别历史按钮
    elif step == 3:
        wait(Template(os.getcwd()+"\\reuse\\img\\tpl1637519309012.png", record_pos=(0.035, 0.107), resolution=(2280, 1080)), timeout=60)
        sleep(3)
    # 点击出战
    elif step == 4:
        touch(Template(os.getcwd()+"\\reuse\\img\\tpl1637519377151.png", record_pos=(0.216, 0.106), resolution=(2280, 1080)))
        sleep(5)
        touch([0.52 * w, 0.879 * h])
        sleep(10)


# 抽卡
def hero_draw(step):
    w, h = shipei()
    if step == "免费":
        wait(Template(os.getcwd()+"\\reuse\\img\\tpl1637521039934.png", record_pos=(-0.06, 0.177), resolution=(2280, 1080)), timeout=60)
        sleep(3)
        touch([0.441 * w, 0.869 * h])
    elif step == "跳过":
        wait(Template(os.getcwd()+"\\reuse\\img\\tpl1637521204399.png", record_pos=(0.402, -0.205), resolution=(2280, 1080)), timeout=60)
        sleep(2)
        touch([0.465 * w, 0.513 * h])
    elif step == "继续进化":
        wait(Template(os.getcwd()+"\\reuse\\img\\tpl1637521250730.png", record_pos=(0.119, 0.187), resolution=(2280, 1080)), timeout=60)
        sleep(2)
        touch([0.369 * w, 0.891 * h])
