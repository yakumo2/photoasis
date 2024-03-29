from flask import Blueprint, render_template, request, abort
import global_variables
from folder_action import load_folders

album_bp = Blueprint('album_bp', __name__)



# Route for album page
@album_bp.route('/<album_name>')
def album(album_name):
    path = global_variables.path
    page = int(request.args.get('page', 1))
    photos = get_photos(path, album_name)
    num_photos = len(photos)
    per_page = 20
    num_pages = (num_photos + per_page - 1) // per_page
    if page < 1 or page > num_pages:
        abort(404)
    start_idx = (page - 1) * per_page
    end_idx = min(start_idx + per_page, num_photos)
    paginated_photos = photos[start_idx:end_idx]

    albums=load_folders();
    name = 'Default'
    # 在 JSON 数据中查找 path 等于 album_name 的块，并将其 name 赋值给 name 变量
    for block in albums:
        if block.get('path') == album_name:
            name = block.get('name')
            print("found "+name)
            break

    print("album executed")
    return render_template('album.html',name=name, big=global_variables.big, path=path, album_name=album_name, photos=paginated_photos, page=page, num_pages=num_pages)

# Helper function to get list of photos in an album
def get_photos(path, album_name):
    import os
    photos = []
    album_path = os.path.join(path, album_name)
    if not os.path.exists(album_path):
        abort(404)
    for root, dirs, files in os.walk(album_path):
        for file in files:
            if file.endswith(('jpg', 'jpeg', 'png', 'gif')):
                photos.append(file)
    return photos