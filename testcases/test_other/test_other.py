#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Author  : he
@File    : test_other.py
@Date    : 2024/6/22 14:13
@Description: 
"""

import logging
import os
import time

import pytest

import common.operation_file as utils

logger = logging.getLogger(__name__)


@pytest.mark.usefixtures("session", "logs")
class TestOther:
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'other', 'countries.yaml')))
	def test_countries(self, args, session):
		url = args['request']['url']
		logger.info(f"Testing  countries with URL: {url}")
		res = session.get(url)
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'other', 'homepage_info.yaml')))
	def test_homepage_info(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		logger.info(f"Testing  homepage info with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'other', 'homepage_dragon.yaml')))
	def test_homepage_dragon(self, args, session):
		url = args['request']['url']
		logger.info(f"Testing  homepage dragon with URL: {url} ")
		res = session.get(url)
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'other', 'comment_hot.yaml')))
	def test_comment_hot(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		if 'before' in params:
			params['before'] = params.get('before') or int(time.time() * 1000)
		logger.info(f"Testing  comment hot with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'other', 'comment_new.yaml')))
	def test_comment_new(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		if params['sortType'] == 3:
			params['cursor'] = params.get('cursor') or int(time.time() * 1000)
		logger.info(f"Testing  comment hot with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'other', 'comment_like.yaml')))
	def test_comment_like(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		logger.info(f"Testing  comment like with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			if res.status_code == 250:
				logger.error(f"Request failed: {res.json()}")
				raise Exception(f"Custom error: {res.json()}")
			else:
				res.raise_for_status()
				logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'other', 'comment_hug.yaml')))
	def test_comment_hug(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		# 读取uid
		data = utils.read_file(os.path.join(os.getcwd(), 'extract.yaml'))
		uid = data.get('uid')
		logger.info(f"uid:{uid}")
		# 替换uid 原来的值 ${extract(uid)}
		for key, value in params.items():
			if value == '${extract(uid)}':
				params[key] = uid
		logger.info(f"Testing comment hug with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'other', 'comment_hug_list.yaml')))
	def test_comment_hug_list(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		# 读取uid
		data = utils.read_file(os.path.join(os.getcwd(), 'extract.yaml'))
		uid = data.get('uid')
		logger.info(f"uid:{uid}")
		for key, value in params.items():
			if value == '${extract(uid)}':
				params[key] = uid
		logger.info(f"Testing  comment hug list with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'other', 'banner.yaml')))
	def test_banner(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		logger.info(f"Testing  banner with URL: {url} and params: {params}")
		res = session.get(url)
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'other', 'personal_fm.yaml')))
	def test_personal_fm(self, args, session):
		url = args['request']['url']
		logger.info(f"Testing  personal fm with URL: {url} ")
		res = session.get(url)
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'other', 'daily_signin.yaml')))
	def test_daily_signin(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		logger.info(f"Testing  daily signin with URL: {url} and params: {params}")
		res = session.post(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'other', 'like_music.yaml')))
	def test_like_music(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		logger.info(f"Testing  like music with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'other', 'liked_music_list.yaml')))
	def test_liked_music_list(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		# 读取uid
		data = utils.read_file(os.path.join(os.getcwd(), 'extract.yaml'))
		uid = data.get('uid')
		logger.info(f"uid:{uid}")
		# 取到 uid 值替换 ${extract(uid)}
		for key, value in params.items():
			if value == '${extract(uid)}':
				params[key] = uid
		logger.info(f"Testing  liked music list with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'other', 'fm_trash.yaml')))
	def test_fm_trash(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		logger.info(f"Testing  fm trash with URL: {url} and params: {params}")
		res = session.post(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'other', 'scrobble.yaml')))
	def test_scrobble(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		logger.info(f"Testing  scrobble with URL: {url} and params: {params}")
		res = session.post(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'other', 'personalized_privatecontent.yaml')))
	def test_personalized_privatecontent(self, args, session):
		url = args['request']['url']
		logger.info(f"Testing  personalized privatecontent with URL: {url} ")
		res = session.get(url)
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'other', 'personalized_privatecontent_list.yaml')))
	def test_personalized_privatecontent_list(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		logger.info(f"Testing  personalized privatecontent list with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'other', 'all_toplist.yaml')))
	def test_all_toplist(self, args, session):
		url = args['request']['url']
		logger.info(f"Testing  all toplist with URL: {url}")
		res = session.get(url)
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'other', 'all_toplist_detail.yaml')))
	def test_all_toplist_detail(self, args, session):
		url = args['request']['url']
		logger.info(f"Testing  all toplist detail with URL: {url}")
		res = session.get(url)
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'other', 'toplist_artist.yaml')))
	def test_toplist_artist(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		logger.info(f"Testing  toplist artist with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
