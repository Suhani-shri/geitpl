from menus.base import Menu, NavigationNode
from menus.menu_pool import menu_pool
from django.utils.translation import gettext_lazy as _


class TestMenu(Menu):

    def get_nodes(self, request):
        nodes = []
        n = NavigationNode(_('Technology'), "/", 1)
       	nodes.append(n)
       
        return nodes

menu_pool.register_menu(TestMenu)