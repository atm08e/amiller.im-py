import logging

def setup_routes(app, handler, project_root=None):
    logging.info("Setting up routes!")
    app.router.add_route('GET', '/', handler.index)
    # app.router.add_route('GET', '/blog', self.blog)
    # app.router.add_route('GET', '/favorites', self.favorites)
    # app.router.add_route('GET', '/resume', self.resume)
    # app.router.add_route('GET', '/fishing', self.fishing)
    # app.router.add_route('GET', '/snow', self.snow)
    # app.router.add_route('GET', '/about', self.about)