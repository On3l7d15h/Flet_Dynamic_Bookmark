#
from flet import *;

class PlaceView(UserControl):

    def __init__(self, bar, route, page):
        super().__init__();
        self.bar = bar;
        self.route = route;
        self.page = page;

    def build(self):
        from functions.places.home_place import _home_place_;
        from functions.places.setting_place import _setting_place_;
        from functions.places.new_place import _new_place_;

        # Variables
        HomeView = _home_place_(self.page);
        NewPlace = _new_place_(self.page);
        SettingView = _setting_place_(self.page);

        def changetab(e):
            index = e.control.selected_index;
            
            # changing in the view...
            HomeView.visible = True if index == 0 else False;
            NewPlace.visible = True if index == 1 else False;
            SettingView.visible = True if index == 2 else False;

            self.page.update()

        return View(
            appbar=self.bar,
            route=self.route,
            controls=[
                HomeView,
                NewPlace,
                SettingView
            ],
            navigation_bar=NavigationBar(
                bgcolor=colors.PRIMARY_CONTAINER,
                height=60,
                selected_index=0,
                on_change=changetab,
                destinations=[
                    NavigationDestination(label="Hogar", icon=icons.HOME),
                    NavigationDestination(label="Nuevo", icon=icons.CREATE),
                    NavigationDestination(label="Sesión", icon=icons.PERSON),
                ]
            )
        )