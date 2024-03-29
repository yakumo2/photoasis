# 使用 Python 3.9 的 Alpine 版本作为基础镜像
FROM python:3.9-alpine

# 设置工作目录
WORKDIR /app

# 将当前目录中的文件复制到工作目录中
COPY . /app

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 安装 bash
RUN apk add --no-cache bash

# 设置环境变量
ENV FLASK_APP=app.py

# 暴露端口
EXPOSE 15001

# 运行应用
# CMD ["python", "app.py"]
CMD ["./run.sh"]
