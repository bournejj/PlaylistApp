"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Playlist(db.Model):
    """Playlist."""

    # ADD THE NECESSARY CODE HERE

    __tablename__='playlists'

    id = db.Column(db.Integer, primary_key=True, unique=True,)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.Text, nullable=False)
    
    songs = db.relationship('Song', backref='playlist')

    playlist_song = db.relationship('PlaylistSong', backref='playlist')




class Song(db.Model):
    """Song."""

    # ADD THE NECESSARY CODE HERE

    __tablename__= 'songs'

    id = db.Column(db.Integer, primary_key=True, unique=True,)
    title = db.Column(db.String, nullable=False)
    artist = db.Column(db.String, nullable=False)
    playlist_id = db.Column( db.Integer, db.ForeignKey('playlists.id'))
    
    playists = db.relationship('Playlist', backref='song')
 
 
    playlist_song = db.relationship('PlaylistSong', backref='song')



class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""

    # ADD THE NECESSARY CODE HERE

    __tablename__= 'playlist_songs'

    id = db.Column(db.Integer, primary_key=True, unique=True,)
    playlist_id = db.Column( db.Integer, db.ForeignKey('playlists.id'))
    song_id = db.Column( db.Integer, db.ForeignKey('songs.id'))

    songs = db.relationship('Song', backref='playlistSong')
    playlists = db.relationship('Playlist', backref='playlist_Song')

    



# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
