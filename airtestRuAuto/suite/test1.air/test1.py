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
# 第一场展示战斗
dialogue("蛮族蚁首领")
# 我的对话
wait(Template(r"tpl1637516238137.png", record_pos=(-0.033, 0.165), resolution=(2280, 1080)), timeout=60)
sleep(2)
touch([0.465*w, 0.513*h])

dialogue("蚁后")
# 我的对话
wait(Template(r"tpl1637493999967.png", record_pos=(-0.012, 0.164), resolution=(2280, 1080)), timeout=60)
sleep(2)
touch([0.465*w, 0.513*h])

dialogue("凯撒")
dialogue("图拉真")

# 我的对话
wait(Template(r"tpl1637494066870.png", record_pos=(-0.053, 0.169), resolution=(2280, 1080)), timeout=60)
sleep(2)
touch([0.465*w, 0.513*h])

dialogue("凯撒")

# 我的对话
wait(Template(r"tpl1637516876487.png", record_pos=(-0.096, 0.193), resolution=(2280, 1080)),timeout=60)
sleep(2)
touch([0.465*w, 0.513*h])

# 第一场战斗
novice_battle(1)
# 长按下兵
touch([0.669 * w, 0.681 * h], duration=10)
# 点击统帅和英雄放技能
touch([0.276*w, 0.863*h])
touch([0.196*w, 0.869*h])
novice_battle(2)

dialogue("凯撒")
wait(Template(r"tpl1637517252354.png", record_pos=(-0.081, 0.164), resolution=(2280, 1080)),timeout=60)
sleep(2)
touch([0.465*w, 0.513*h])
sleep(5)
touch([0.465*w, 0.513*h])

dialogue("尤利娅")
wait(Template(r"tpl1637517313031.png", record_pos=(0.169, 0.167), resolution=(2280, 1080)),timeout=60)
sleep(5)
touch([0.465*w, 0.513*h])

dialogue("尤利娅")

wait(Template(r"tpl1637517348506.png", record_pos=(-0.284, 0.178), resolution=(2280, 1080)),timeout=60)
sleep(2)
touch([0.084*w, 0.876*h])

sleep(10)
dialogue("尤利娅")
sleep(2)
dialogue("尤利娅")

# 收集
wait(Template(r"tpl1637518155729.png", record_pos=(-0.325, 0.129), resolution=(2280, 1080)),timeout=60)
sleep(2)
touch([0.067*w, 0.777*h])
wait(Template(r"tpl1637518270815.png", record_pos=(0.001, -0.036), resolution=(2280, 1080)),timeout=60)
sleep(2)
touch([0.373*w, 0.695*h])
sleep(5)
touch([0.56*w, 0.383*h])
wait(Template(r"tpl1637518396919.png", record_pos=(0.001, 0.004), resolution=(2280, 1080)),timeout=60)
sleep(2)
touch([0.494*w, 0.398*h])

dialogue("尤利娅")
wait(Template(r"tpl1637518614324.png", record_pos=(0.325, 0.004), resolution=(2280, 1080)),timeout=60)
sleep(2)
touch([0.933*w, 0.518*h])

sleep(7)
dialogue("尤利娅")
sleep(3)
touch([0.28*w, 0.701*h])
sleep(5)
touch([0.285*w, 0.581*h])

wait(Template(r"tpl1637518833360.png", record_pos=(0.299, -0.053), resolution=(2280, 1080)),timeout=60)
sleep(3)
touch([0.684*w, 0.386*h])
wait(Template(r"tpl1637519096742.png", record_pos=(0.284, 0.125), resolution=(2280, 1080)),timeout=60)
sleep(3)
touch([0.91*w, 0.856*h])
wait(Template(r"tpl1637519173266.png", record_pos=(0.116, -0.05), resolution=(2280, 1080)),timeout=60)
sleep(3)
touch([0.497*w, 0.477*h])

# 第二场战斗
novice_battle(3)
novice_battle(4)
novice_battle(1)
# 下兵
touch([0.669*w, 0.681*h], duration=10)
# 点击统帅和英雄放技能
touch([0.276*w, 0.863*h])
touch([0.196*w, 0.869*h])
novice_battle(2)

# 4级弹窗
wait(Template(r"tpl1637519567283.png", record_pos=(0.006, -0.129), resolution=(2280, 1080)),timeout=60)
sleep(2)
touch([0.139*w, 0.206*h])

dialogue("尤利娅")

wait(Template(r"tpl1637519641879.png", record_pos=(-0.027, 0.167), resolution=(2280, 1080)),timeout=60)
sleep(2)
touch([0.465*w, 0.513*h])
wait(Template(r"tpl1637519673967.png", record_pos=(0.14, -0.018), resolution=(2280, 1080)),timeout=60)
sleep(2)
touch([0.524*w, 0.477*h])

# 第三场战斗
novice_battle(3)
novice_battle(4)

dialogue("蛮族蚁首领")
wait(Template(r"tpl1637519838312.png", record_pos=(-0.204, 0.13), resolution=(2280, 1080)),timeout=60)
sleep(2)
touch([0.196*w, 0.891*h])
touch([0.669*w, 0.681*h], duration=15)
wait(Template(r"tpl1637519947219.png", record_pos=(-0.04, 0.168), resolution=(2280, 1080)),timeout=60)
sleep(2)
touch([0.465*w, 0.513*h])

dialogue("凯撒")
sleep(2)
touch([0.202*w, 0.871*h])
novice_battle(2)

wait(Template(r"tpl1637520078490.png", record_pos=(-0.161, -0.118), resolution=(2280, 1080)),timeout=60)
sleep(2)
touch([0.498*w, 0.818*h])
wait(Template(r"tpl1637520127862.png", record_pos=(-0.004, -0.104), resolution=(2280, 1080)),timeout=60)
sleep(2)
touch([0.511*w, 0.853*h])

dialogue("尤利娅")

# 浇灌神树
wait(Template(r"tpl1637520195016.png", record_pos=(-0.236, 0.054), resolution=(2280, 1080)),timeout=60)
sleep(2)
touch([0.109*w, 0.619*h])
wait(Template(r"tpl1637520231131.png", record_pos=(0.054, 0.156), resolution=(2280, 1080)),timeout=60)
sleep(2)
touch([0.4*w, 0.828*h])

dialogue("尤利娅")

wait(Template(r"tpl1637520400304.png", record_pos=(0.218, 0.111), resolution=(2280, 1080)),timeout=60)
sleep(2)
touch([0.82*w, 0.742*h])
wait(Template(r"tpl1637520453799.png", record_pos=(-0.0, -0.103), resolution=(2280, 1080)),timeout=60)
sleep(2)
touch([0.51*w, 0.843*h])

dialogue("尤利娅")

wait(Template(r"tpl1637520513113.png", record_pos=(-0.287, -0.168), resolution=(2280, 1080)),timeout=60)
sleep(2)
touch([0.062*w, 0.056*h])
wait(Template(r"tpl1637520579280.png", record_pos=(-0.297, 0.175), resolution=(2280, 1080)),timeout=60)
sleep(2)
touch([0.078*w, 0.879*h])

dialogue("弓骑蚁")
wait(Template(r"tpl1637520795821.png", record_pos=(-0.275, -0.061), resolution=(2280, 1080)),timeout=60)
sleep(2)
touch([0.093*w, 0.378*h])
wait(Template(r"tpl1637520935418.png", record_pos=(-0.005, 0.135), resolution=(2280, 1080)),timeout=60)
sleep(2)
touch([0.594*w, 0.896*h])

dialogue("蚁后")
sleep(3)
touch([0.51*w, 0.843*h])

hero_draw("免费")
hero_draw("跳过")
hero_draw("继续进化")

wait(Template(r"tpl1637521320217.png", record_pos=(-0.325, 0.131), resolution=(2280, 1080)),timeout=60)
sleep(2)
touch([0.062*w, 0.777*h])
sleep(5)
touch([0.52*w, 0.682*h])
sleep(5)
touch([0.553*w, 0.388*h])

dialogue("尤利娅")

wait(Template(r"tpl1637521631141.png", record_pos=(-0.275, -0.05), resolution=(2280, 1080)),timeout=60)
sleep(2)
touch([0.093*w, 0.37*h])

# 五级
wait(Template(r"tpl1637520127862.png", record_pos=(-0.004, -0.104), resolution=(2280, 1080)),timeout=60)
sleep(2)
touch([0.511*w, 0.853*h])
wait(Template(r"tpl1637521764234.png", record_pos=(0.005, -0.13), resolution=(2280, 1080)),timeout=60)
sleep(2)
touch([0.139*w, 0.206*h])

dialogue("苏拉")
dialogue("尤利娅")

wait(Template(r"tpl1637521824350.png", record_pos=(0.125, 0.141), resolution=(2280, 1080)),timeout=60)
sleep(2)
touch([0.713*w, 0.904*h])
wait(Template(r"tpl1637522050432.png", record_pos=(0.291, 0.171), resolution=(2280, 1080)),timeout=60)
sleep(2)
touch([0.908*w, 0.296*h], duration=15)

print("新手用例执行结束")
