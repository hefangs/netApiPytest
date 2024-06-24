#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Author  : he
@File    : operation_file.py
@Date    : 2024/6/13 15:54
@Description: 
"""

import logging
import os

import yaml

logger = logging.getLogger(__name__)


def read_file(yaml_file):
	if not os.path.exists(yaml_file):
		logger.error(f"The file '{yaml_file}' does not exist")
		raise FileNotFoundError(f"The file '{yaml_file}' does not exist")
	try:
		with open(yaml_file, encoding="utf-8") as f:
			value = yaml.load(f, Loader=yaml.FullLoader)
			return value
	except yaml.YAMLError as e:
		logger.error(f"Error parsing YAML file: {e}")
	except Exception as e:
		logger.error(f"Failed to read file: {e}")


def write_file(yaml_file, data):
	if not isinstance(data, (dict, list)):
		logger.error("Data must be a dictionary or a list")
		raise TypeError("Data must be a dictionary or a list")
	try:
		with open(yaml_file, mode="a", encoding="utf-8") as f:
			yaml.dump(data, f, allow_unicode=True)
	except Exception as e:
		logger.error(f"Failed to write file: {e}")


def clear_file(yaml_file):
	if os.path.exists(yaml_file):
		try:
			with open(yaml_file, encoding="utf-8", mode="w") as f:
				f.truncate()
				logger.info(f"File '{yaml_file}' has been cleared.")
		except Exception as e:
			logger.error(f"Failed to clear file: {e}")
	else:
		logger.error(f"The file '{yaml_file}' does not exist")
		raise FileNotFoundError(f"The file '{yaml_file}' does not exist")
