from django import template

register = template.Library()


@register.tag
def ifpermission(parser, token):
    bits = token.split_contents()[1:]
    permission = bits[0]
    try:
        obj = bits[1]
    except IndexError:
        obj = None

    nodelist_true = parser.parse(('else', 'endifpermission'))
    token = parser.next_token()
    if token.contents == 'else':
        nodelist_false = parser.parse(('endifpermission',))
        parser.delete_first_token()
    else:
        nodelist_false = template.NodeList()

    return IfPermissionNode(permission=permission, obj=obj,
        nodelist_true=nodelist_true, nodelist_false=nodelist_false)


class IfPermissionNode(template.Node):
    def __init__(self, permission, obj, nodelist_true, nodelist_false):
        self.nodelist_true = nodelist_true
        self.nodelist_false = nodelist_false
        self.permission = template.Variable(permission)
        if obj is not None:
            self.obj = template.Variable(obj)
        else:
            self.obj = None

    def render(self, context):
        user = template.Variable('user').resolve(context)
        if self.obj is not None:
            obj = self.obj.resolve(context)
        else:
            obj = None

        if user.has_perm(self.permission.resolve(context), obj):
            return self.nodelist_true.render(context)
        else:
            return self.nodelist_false.render(context)
