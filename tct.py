from src.text_component.components import *
from pprint import pp

print(Rawtext)
p = Rawtext()

print(repr(p))
p.add(Text("a"), Selector("b"), Score("along", "objective"))
pp(p)
pp(p.to_dictionary())

p.translate("%%9").build(Text("1"), Text("2"), Text("3"), Text("1"))
pp(p)