__all__ = ['temp']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['wish'])
@Js
def PyJsHoisted_wish_(name, this, arguments, var=var):
    var = Scope({'name':name, 'this':this, 'arguments':arguments}, var)
    var.registers(['name'])
    var.get('console').callprop('log', ((Js('Hello, ')+var.get('name'))+Js('!')))
PyJsHoisted_wish_.func_name = 'wish'
var.put('wish', PyJsHoisted_wish_)
pass
pass


# Add lib to the module scope
temp = var.to_python()