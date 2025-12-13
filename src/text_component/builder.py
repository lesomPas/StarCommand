# create by lesomras on 2025-12-14
from .components import TextComponent, Rawtext, Translate
from ..core.exceptions import UnsupportedArgument, MissingArgument, MalformedArgument

class TranslateBuilder(object):
    def __init__(self, raw: Rawtext, translate: str) -> None:
        if not isinstance(raw, Rawtext) or not isinstance(translate, str):
            raise UnsupportedArgument("build failed")

        self.raw = raw
        self.translate = translate

    def build(self, *args) -> Rawtext:
        if args == ():
            return self.raw.add(Translate(self.translate))

        if any(not isinstance(i, TextComponent) for i in args):
            raise UnsupportedArgument("build failed")

        withraw = Rawtext().add_sequence(list(args))
        return self.raw.add(Translate(self.translate, with_content = withraw))

    def string_build(self, *args) -> Rawtext:
        if args == ():
            return self.raw.add(Translate(self.translate))

        if any(not isinstance(i, str) for i in args):
            raise UnsupportedArgument("build failed")

        return self.raw.add(Translate(self.translate, string_sequence = list(args)))

    def sequence_build(self, sequence: list[TextComponent]) -> Rawtext:
        return self.build(*sequence)

    def sequence_str_build(self, sequence: list[str]) -> Rawtext:
        return self.string_build(*sequence)
