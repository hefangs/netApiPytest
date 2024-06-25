#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Author  : he
@File    : test_album.py
@Date    : 2024/6/24 16:33
@Description: 
"""
import logging
import os
import time

import pytest

import common.operation_file as utils

logger = logging.getLogger(__name__)


@pytest.mark.usefixtures("session", "logs")
class TestAlbum:
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'album', 'comment_album.yaml')))
	def test_comment_album(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		if 'before' in params:
			params['before'] = params.get('before') or int(time.time() * 1000)
		logger.info(f"Testing comment album with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response :{res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'album', 'album_content.yaml')))
	def test_album_content(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		logger.info(f"Testing album content with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response :{res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'album', 'album_dynamic.yaml')))
	def test_album_dynamic(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		logger.info(f"Testing album dynamic with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response :{res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'album', 'album_sub.yaml')))
	def test_album_sub(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		logger.info(f"Testing album sub with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response :{res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'album', 'album_sublist.yaml')))
	def test_album_sublist(self, args, session):
		url = args['request']['url']
		params = args['request'].get('params')
		if params is None:
			res = session.get(url)
			logger.info(f"Testing album sublist with URL: {url}")
		else:
			res = session.get(url, params=params)
			logger.info(f"Testing album sublist with URL: {url} and params: {params}")
		try:
			res.raise_for_status()
			logger.info(f"Response :{res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'album', 'album_top.yaml')))
	def test_album_top(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		logger.info(f"Testing album top with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response :{res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'album', 'album_new.yaml')))
	def test_album_new(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		logger.info(f"Testing album new with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response :{res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'album', 'album_list.yaml')))
	def test_album_list(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		logger.info(f"Testing album list with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response :{res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'album', 'album_songsaleboard.yaml')))
	def test_album_songsaleboard(self, args, session):
		url = args['request']['url']
		params = args['request'].get('params')
		if params is None:
			res = session.get(url)
			logger.info(f"Testing album songsaleboard with URL: {url}")
		else:
			logger.info(f"Testing album songsaleboard with URL: {url} and params: {params}")
			res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response :{res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'album', 'album_list_style.yaml')))
	def test_album_list_style(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		logger.info(f"Testing album list style with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response :{res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'album', 'album_detail.yaml')))
	def test_album_detail(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		logger.info(f"Testing album detail with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response :{res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'album', 'digitalalbum_purchased.yaml')))
	def test_digitalalbum_purchased(self, args, session):
		url = args['request']['url']
		params = args['request'].get('params')
		logger.info(f"Testing digitalAlbum purchased with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response :{res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'album', 'record_recent_album.yaml')))
	def test_record_recent_album(self, args, session):
		url = args['request']['url']
		params = args['request'].get('params')
		logger.info(f"Testing record recent album with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response :{res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
