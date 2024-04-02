import os
from tqdm import tqdm
from PIL import Image
from pillow_heif import register_heif_opener
import global_variables

register_heif_opener()

# 压缩图片并保存
def compress_image(input_path, output_path, quality=60, max_size=400, crop_to_square=False):
    try:
        # 如果输出文件已存在，则跳过压缩
        if os.path.exists(output_path):
            return False
        
        # 打开图片
        image = Image.open(input_path)
        
        # 如果是 HEIC 格式，则转换为 JPEG 格式
        if image.format == 'HEIC':
            output_path = output_path.replace('.jpeg', '.png')  # 修改输出路径为 PNG 格式
            image = image.convert("RGB")
        
        # 获取原始图片尺寸
        width, height = image.size
        
        # 计算调整后的尺寸
        if width >= height:
            new_width = min(width, max_size)
            new_height = int(height * (new_width / width))
        else:
            new_height = min(height, max_size)
            new_width = int(width * (new_height / height))
        
        # 调整尺寸
        resized_image = image.resize((new_width, new_height), Image.LANCZOS)
        
        # 如果需要裁切成正方形
        if crop_to_square:
            # 计算裁切后的区域
            left = (new_width - min(new_width, new_height)) / 2
            top = (new_height - min(new_width, new_height)) / 2
            right = (new_width + min(new_width, new_height)) / 2
            bottom = (new_height + min(new_width, new_height)) / 2
            
            # 进行裁切
            resized_image = resized_image.crop((left, top, right, bottom))
        
        # 保存图片
        resized_image.save(output_path, quality=quality)  # 设置压缩质量
        
        return True
    except Exception as e:
        print(f"Failed to compress {input_path}: {e}")
        return False

# 遍历文件夹中的图片并压缩保存
def compress_images_in_folder(input_folder, output_folder, high_quality=False):
    max_size = 800 if high_quality else 400
    max_quality = 100 if high_quality else 60
    crop_to_square = False if high_quality else True
    
    for root, dirs, files in os.walk(input_folder):
        # 生成对应的输出文件夹结构
        rel_path = os.path.relpath(root, input_folder)
        output_root = os.path.join(output_folder, rel_path)
        os.makedirs(output_root, exist_ok=True)
        
        # 遍历文件夹中的文件
        for file in tqdm(files, desc=f'Compressing images in {root}'):
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.heic')):
                input_path = os.path.join(root, file)
                output_path = os.path.join(output_root, file.split('.')[0] + '.jpeg')  # 添加 -small 后缀
                compress_image(input_path, output_path, quality=max_quality, max_size=max_size, crop_to_square=crop_to_square)

# 主函数
if __name__ == "__main__":
    input_folder = global_variables.original #'photo/photo_original'
    output_folder = global_variables.path #'photo/photo_small'
    output_folder_high_quality = global_variables.big #'photo/photo_big'
    
    if not os.path.exists(input_folder):
        print("Can't find input folder:", input_folder)
        exit()

    compress_images_in_folder(input_folder, output_folder)
    compress_images_in_folder(input_folder, output_folder_high_quality, high_quality=True)
