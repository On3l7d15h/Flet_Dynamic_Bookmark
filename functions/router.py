from flet import *;

def router(page, route):

    # I didn't what happened but I resolve the problem
    from classes.views.login_view import LoginView
    from classes.views.new_user_view import NewUserView;
    from classes.views.place_view import PlaceView;
    from classes.components.app_bar import TopBar

    # vars
    login_view = LoginView(
            TopBar(page).build(), 
            "/",
            page,
        ).build()
    new_user_view = NewUserView(
        TopBar(page).build(), 
        "/new",
        page
    ).build()
    place_view = PlaceView(
        TopBar(page).build(),
        "/place",
        page
    ).build();

    page.route = route;
    page.window_width = 400;
    page.window_top = 150;
    page.window_left = 580;
    page.views.clear();

    match page.route:
        case "/":
            page.views.append(login_view)
        case "/new":
            if page.client_storage.contains_key("usuario") == False:
                page.views.append(new_user_view)
        case "/place":
            page.window_width = 900;
            page.window_left = 350;
            page.views.append(place_view)

    page.update();