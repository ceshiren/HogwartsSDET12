import importlib
import re
import types

import yaml

from requests_wework.core.content import Content


class BaseAction:
    depends = []
    local_variable = {}

    def __init__(self, content: Content):
        self.data = content.get_data()
        # 扫描函数，把函数存入局部变量表
        self.parse_content()

    def parse_content(self):
        for command_name, command_content in self.data.items():
            if "depend" == command_name:
                for depend in command_content:
                    self.depends.append(importlib.import_module(depend))
            elif command_name.startswith('def_'):
                fun_name = command_name[4:]

                def __init__(s, int_command_content, in_fun_name):
                    s.fun_name = in_fun_name
                    s.command_content = int_command_content

                def run(s):
                    for in_command_name, in_command_content in s.command_content.items():
                        if in_command_name.startswith('run_'):
                            in_fun_name = in_command_name[4:]
                            try:
                                return self.local_variable[in_fun_name].run()
                            except KeyError:
                                for import_mod in self.depends:
                                    if hasattr(import_mod, in_fun_name):
                                        content_format = self.parse_value(in_command_content)
                                        return getattr(import_mod, in_fun_name)\
                                            (**content_format).json()

                cls_dict = {
                    '__init__': __init__,
                    'run': run
                }
                tmp_class = types.new_class('tmp_class', (), {}, lambda ns: ns.update(cls_dict))
                self.local_variable[fun_name] = tmp_class(command_content, fun_name)

    def parse_value(self, content):
        raw = yaml.dump(content)
        functions = re.findall(r"\$\((.*)\)", raw)
        for function in functions:
            parse_res = self.run_fun(function)
            if "access_token" in parse_res.keys():
                raw = raw.replace(f"$({function})", repr(parse_res["access_token"]))
            else:
                raw = raw.replace(f"$({function})", repr(parse_res))
        return yaml.load(raw)

    def run_fun(self, fun_name):
        return self.local_variable[fun_name].run()
