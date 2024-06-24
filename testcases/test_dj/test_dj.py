#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Author  : he
@File    : test_dj.py
@Date    : 2024/6/22 下午11:10
@Description: 
"""

import logging
import os
import random
import time

import pytest

import common.operation_file as utils

logger = logging.getLogger(__name__)


@pytest.mark.usefixtures("session", "logs")
class TestDj:
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'dj', 'user_dj.yaml')))
	def test_user_dj(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		# 获取uid
		data = utils.read_file(os.path.join(os.getcwd(), 'extract.yaml'))
		uid = data.get('uid')
		logger.info(f'uid: {uid}')
		# 替换 ${extract(uid)}
		for key, value in params.items():
			if value == "${extract(uid)}":
				params[key] = uid
		logger.info(f"替换 ${'extract(uid)'}:{uid}")
		logger.info(f"Testing user_dj  with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'dj', 'share_djradio.yaml')))
	def test_share_djradio(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		all_params = {
			'id': params['id'],
			'type': params['type'],
			'msg': params.get('msg') or f"djradio{int(random.randint(1000, 9999))}"
		}
		logger.info(f"Testing share test_mv with URL: {url} and params: {all_params}")
		res = session.get(url, params=all_params)
		try:
			res.raise_for_status()
			logger.info(f"Response : {res.json()}")
		except Exception as e:
			logger.error(f"Request Failed: {e}")
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'dj', 'share_djprogram.yaml')))
	def test_share_djprogram(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		all_params = {
			'id': params['id'],
			'type': params['type'],
			'msg': params.get('msg') or f"djprogram{int(random.randint(1000, 9999))}"
		}
		logger.info(f"Testing share test_mv with URL: {url} and params: {all_params}")
		res = session.get(url, params=all_params)
		try:
			res.raise_for_status()
			logger.info(f"Response : {res.json()}")
		except Exception as e:
			logger.error(f"Request Failed: {e}")
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'dj', 'comment_dj.yaml')))
	def test_comment_dj(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		if 'before' in params:
			params['before'] = params.get('before') or int(time.time() * 1000)
		logger.info(f"Testing comment_dj with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response : {res.json()}")
		except Exception as e:
			logger.error(f"Request Failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'dj', 'personalized_djprogram.yaml')))
	def test_personalized_djprogram(self, args, session):
		url = args['request']['url']
		logger.info(f"Testing personalized_djprogram with URL: {url}")
		res = session.get(url)
		try:
			res.raise_for_status()
			logger.info(f"Response : {res.json()}")
		except Exception as e:
			logger.error(f"Request Failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'dj', 'recommended_programs.yaml')))
	def test_recommended_programs(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		logger.info(f"Testing recommended programs with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response : {res.json()}")
		except Exception as e:
			logger.error(f"Request Failed: {e}")
			raise
