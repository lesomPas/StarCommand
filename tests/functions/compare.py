# test_compare.py
import unittest

def compare(dictionary: dict, pattern: dict) -> None:
    if not isinstance(dictionary, dict) or not isinstance(pattern, dict):
        raise TypeError
    # 使用元组 (data, pattern) 确保绑定
    stack = [(dictionary, pattern)]

    while stack:
        data, pat = stack.pop(-1)

        # 检查 data 是否包含 pat 中所有要求的键
        for key, pat_value in pat.items():
            if key not in data:
                raise ValueError(f"missing value: {key}")

            data_value = data[key]

            if isinstance(pat_value, dict) and isinstance(data_value, dict):
                stack.append((data_value, pat_value))
                continue

            if pat_value is str:
                if not isinstance(data_value, str):
                    raise TypeError("str Argument")

            elif pat_value == "number":
                if not isinstance(data_value, (int, float)):
                    raise TypeError("")

            elif pat_value is int:
                if not isinstance(data_value, int):
                    raise TypeError("int Argument")

            elif pat_value is float:
                if not isinstance(data_value, float):
                    raise TypeError("float Argument")

            elif callable(pat_value):
                pat_value(data_value, key)

            elif isinstance(pat_value, list):
                if not isinstance(data_value, list):
                    raise TypeError
                if len(data_value) != len(pat_value):
                    raise ValueError
                for p, d in zip(pat_value, data_value):
                    if isinstance(p, dict) and isinstance(d, dict):
                        stack.append((d, p))
                        continue
                    if not isinstance(d, p):
                        raise TypeError

            elif isinstance(pat_value, tuple):
                if not isinstance(data_value, list):
                    raise TypeError
                if len(pat_value) == 0:
                    raise ValueError
    
                if any(not isinstance(i, pat_value[0]) for i in data_value):
                    raise TypeError

            else:
                raise ValueError("nothing")

        if len(data) != len(pat):
            raise ValueError("too many parameters")

# -------------- 三层/四层嵌套专用用例 --------------
class TestDeepNest(unittest.TestCase):
    """完全按原始 compare 实现测深嵌套"""

    # 1. 三层 dict 全匹配
    def test_depth3_ok(self):
        data = {
            "lv1": {
                "lv2": {
                    "lv3": {"id": 1, "name": "bot"}
                }
            }
        }
        pattern = {
            "lv1": {
                "lv2": {
                    "lv3": {"id": int, "name": str}
                }
            }
        }
        compare(data, pattern)          # 期望：不抛

    # 2. 四层 dict 缺一个 key
    def test_depth4_missing_key(self):
        data = {
            "a": {
                "b": {
                    "c": {
                        "d": {"x": 1}   # 少了一个 "y"
                    }
                }
            }
        }
        pattern = {
            "a": {
                "b": {
                    "c": {
                        "d": {"x": int, "y": str}
                    }
                }
            }
        }
        with self.assertRaises(ValueError) as cm:
            compare(data, pattern)
        # 原始实现只会报 "missing value: y"，不会带路径
        self.assertIn("missing value: y", str(cm.exception))

    # 3. 三层 + list 模式
    def test_depth3_with_list_pattern(self):
        data = {
            "cfg": {
                "layers": [
                    {"units": 128, "act": "relu"},
                    {"units": 64, "act": "tanh"}
                ]
            }
        }
        pattern = {
            "cfg": {
                "layers": [
                    {"units": int, "act": str},
                    {"units": int, "act": str}
                ]
            }
        }
        compare(data, pattern)          # 期望：不抛

    # 4. 三层 + list 模式元素类型错（测原始代码抛什么）
    def test_depth3_list_type_wrong(self):
        data = {
            "cfg": {
                "layers": [
                    {"units": "128", "act": "relu"}  # units 应该是 int
                ]
            }
        }
        pattern = {
            "cfg": {
                "layers": [{"units": int, "act": str}]
            }
        }
        # 原始代码对 list 内元素类型不符时抛的是 ValueError（裸 raise）
        with self.assertRaises(TypeError):
            compare(data, pattern)

    # 5. 四层 + tuple 模式（homogeneous list）
    def test_depth4_tuple_pattern(self):
        data = {
            "pipe": {
                "stage": {
                    "nums": [1.1, 2.2, 3.3]
                }
            }
        }
        pattern = {
            "pipe": {
                "stage": {
                    "nums": (float,)
                }
            }
        }
        compare(data, pattern)          # 期望：不抛

    # 6. 四层 + tuple 模式混入错误类型
    def test_depth4_tuple_type_wrong(self):
        data = {
            "pipe": {
                "stage": {
                    "nums": [1, 2.2, 3]   # 混入 int
                }
            }
        }
        pattern = {
            "pipe": {
                "stage": {
                    "nums": (float,)
                }
            }
        }
        # 原始代码这里也是抛 ValueError
        with self.assertRaises(TypeError):
            compare(data, pattern)


if __name__ == "__main__":
    unittest.main()
