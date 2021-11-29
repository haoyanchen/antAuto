from airtest.core.api import *
from airtest.cli.parser import cli_setup

from reuse.gamereuse import *
from reuse.initialization import *


# 连接设备
# connect_device("Android://127.0.0.1:5037/FIFIMFFEPVAIWCU8")

if not cli_setup():
    auto_setup(__file__, logdir='./suite/test1.air/log')
init_device("Android", ime_method="ADBIME")
w, h = shipei()
print("执行第一个脚本")
print("新手用例执行开始")

# 初始化环境
initdevice()
# 电话权限
# popup()
# 登录
login()
# 创建角色
createRole()
# -------------------第一场展示战斗-----------------------
dialogue("蛮族蚁首领")
# 我的对话
wait(Template(os.getcwd()+"\\reuse\\img\\tpl1637516238137.png", record_pos=(-0.033, 0.165), resolution=(2280, 1080)), timeout=60)
sleep(2)
touch([0.465*w, 0.513*h])
dialogue("蚁后")
