from pprint import pp

from src.text_component.components import *
from src.text_component.parser import Parser

rawtext = Parser.parse_file(".json")
# pp(rawtext)

# create a new raw
raw = Rawtext()
#header
raw.add(
    Text("§l§e［§4狂§e］§r§e总战力:"),
    Score.s("总战力"),
    Text("    道龄§r§e["),
)

raw.adx(
    "@s*[]时",
    ":",
    "@s*[]分",
    ":",
    "@s*[]秒"
)

#translate
raw.translate("%4").build(
    Selector("@s[scores={境界=!2,境界层数=!10}]"),
    Selector("@s[scores={境界=!2,境界层数=10}]"),
    Selector("@s[scores={境界=2,境界层数=12}]"),
    Selector("@s[scores={境界=2,境界层数=10}]"),
    Text("§e未到瓶颈 还可提升"),
    Text("§l到达瓶颈 请先渡劫"),
    Text("§r§e未到瓶颈 还可提升"),
    Text("§e§l到达瓶颈 请先渡劫")
)
#menu
raw.add(
    Text("］\n§l§e［§4癫§e］  §r§a血量§b:§a"),
    Score.s("血量"),
    Text("§b‖§a"),
    Score.s("满血量"),
    Text("  §e练气§6"),
    Score.s("境界层数"),
    Text("§e层§a§l[§r§a"),
    Score.s("感悟进度"),
    Text("§b‖§a"),
    Score.s("感悟进度满"),
    Text("§a§l]§r§a"),
    Score.s("感悟进度百分比"),
    Text("%  §a护甲值§b:§a"),
    Score.s("防御"),
    Text("   \n§l§e［§4逆§e］  §r§c攻击力§a:"),
    Score.s("功击"),
    Text("  §c暴击§b:§a"),
    Score.s("暴击"),
    Text("§b%   §c爆伤§b:§a"),
    Score.s("爆伤"),
    Text("  §a闪避§b:§a"),
    Score.s("闪避")
)

pp(raw)