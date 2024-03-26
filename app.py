from flask import Flask, render_template, abort, request

app = Flask(__name__, static_folder='photo')

# Helper function to get list of albums
def get_albums():
    import os
    albums = []
    for root, dirs, files in os.walk('photo'):
        albums.extend(dirs)
        break  # only top-level directories
    return albums

# Helper function to get list of photos in an album
def get_photos(album_name):
    import os
    photos = []
    album_path = os.path.join('photo', album_name)
    if not os.path.exists(album_path):
        abort(404)
    for root, dirs, files in os.walk(album_path):
        for file in files:
            if file.endswith(('jpg', 'jpeg', 'png', 'gif')):
                photos.append(file)
    return photos

# Route for index page
@app.route('/')
def index():
    albums = get_albums()
    return render_template('index.html', albums=albums)

# Route for album page
@app.route('/album/<album_name>')
def album(album_name):
    page = int(request.args.get('page', 1))
    photos = get_photos(album_name)
    num_photos = len(photos)
    per_page = 20
    num_pages = (num_photos + per_page - 1) // per_page
    if page < 1 or page > num_pages:
        abort(404)
    start_idx = (page - 1) * per_page
    end_idx = min(start_idx + per_page, num_photos)
    paginated_photos = photos[start_idx:end_idx]
    return render_template('album.html', album_name=album_name, photos=paginated_photos, page=page, num_pages=num_pages)

if __name__ == '__main__':
    app.run(port=15001)
