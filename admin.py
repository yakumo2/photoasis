from flask import Blueprint, render_template, jsonify, request, redirect, url_for, session

import folder_action
import global_variables

admin_bp = Blueprint('admin_bp', __name__)

admin_password = global_variables.password

#route functions start from here ---------------

# Route for admin page
@admin_bp.route('/')
def admin():

    # 检查用户是否已登录
    if 'logged_in' not in session:
        return redirect(url_for('admin_bp.login'))

	# 指定路径和输出文件名
    path = global_variables.path
    output_file = 'folders.json'

    # 列出文件夹并保存到 JSON 文件
    #list_folders_to_json(path, output_file)

    # 读取文件夹信息并排序
    folders = folder_action.get_sorted_folders()
    return render_template("admin.html", folders=folders)

# Route to scan folders
@admin_bp.route('/scan_folders', methods=['POST'])
def scan_folders():
    folder_action.list_folders_to_json(global_variables.path, 'folders.json')
    return jsonify({'success': True}), 200

# Route to toggle display status of a folder
@admin_bp.route('/toggle_display/<int:folder_id>', methods=['POST'])
def toggle_display(folder_id):
    print("Received id", folder_id)
    folders = folder_action.load_folders()
    for folder in folders:
        if folder['id'] == folder_id:
            print("found id, display:", folder['display'])
            folder['display'] = not folder['display']
            print("updated, display:", folder['display']) 
            break
    folder_action.save_folders(folders)
    return jsonify({'success': True}), 200

# Route for login page
@admin_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        request_data = request.json
        password = request_data.get('password')
        if password == admin_password:
            # 设置 session 标志以表示用户已登录
            session['logged_in'] = True
            return jsonify({'success': True}), 200
        else:
            return jsonify({'error': '密码错误，请重试！'}), 401
    else:
        return render_template('login.html')


# Route to logout
@admin_bp.route('/logout')
def logout():
    # 删除 session 中的登录标志
    session.pop('logged_in', None)
    return redirect(url_for('admin_bp.login'))





