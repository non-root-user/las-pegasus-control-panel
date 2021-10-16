from . import ponies
from . import songs
from . import covers


def initialize(app, session, db):

    @app.route('/api')
    def api_index():
        return {'status': 200, 'message': 'I work!'}

    ponies.ponies(app, session, db)
    songs.songs(app, session, db)
    covers.covers(app, session, db)
