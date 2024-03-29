#!/bin/bash

echo "确认要部署到正式吗？ 1: 确认 2: 搞错嘞"
choice=2
read choice

invalid=0

if [ $choice = 1 ]; then
	echo "1: 开始部署 "
	invalid=1
	python3 photo_handler.py
	python3 app.py
fi

if [ $choice = 2 ]; then
	echo "2: 好危险！！！"
	invalid=1
fi

if [ $invalid = 0 ]; then
	echo "无效选择 ( $choice ) "
fi
