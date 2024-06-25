#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Author  : he
@File    : test_video.py
@Date    : 2024/6/24 23:22
@Description: 
"""
import logging
import os.path
import time

import pytest

import common.operation_file as utils

logger = logging.getLogger(__name__)


@pytest.mark.usefixtures("session", "logs")
class TestVideo:
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'video', 'sub_video.yaml')))
	def test_sub_video(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		logger.info(f"Testing video_sub with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'video', 'recent_video.yaml')))
	def test_recent_video(self, args, session):
		url = args['request']['url']
		logger.info(f"Testing recent_video with URL: {url}")
		res = session.get(url)
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'video', 'comment_video.yaml')))
	def test_comment_video(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		if 'before' in params:
			params['before'] = params.get('before') or int(time.time() * 1000)
		logger.info(f"Testing comment video with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'video', 'mylike.yaml')))
	def test_mylike(self, args, session):
		url = args['request']['url']
		logger.info(f"Testing mylike with URL: {url}")
		res = session.get(url)
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'video', 'video_group_list.yaml')))
	def test_video_group_list(self, args, session):
		url = args['request']['url']
		logger.info(f"Testing video group list with URL: {url}")
		res = session.get(url)
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'video', 'video_category_list.yaml')))
	def test_video_category_list(self, args, session):
		url = args['request']['url']
		logger.info(f"Testing video category list with URL: {url}")
		res = session.get(url)
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'video', 'video_group.yaml')))
	def test_video_group(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		logger.info(f"Testing video group with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'video', 'video_all.yaml')))
	def test_video_all(self, args, session):
		url = args['request']['url']
		params = args['request'].get('params')
		if params is None:
			res = session.get(url)
			logger.info(f"Testing video all with URL: {url}")
		else:
			res = session.get(url, params=params)
			logger.info(f"Testing video all with URL: {url} and params: {params}")
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'video', 'video_recommend.yaml')))
	def test_video_recommend(self, args, session):
		url = args['request']['url']
		params = args['request'].get('params')
		if params is None:
			res = session.get(url)
			logger.info(f"Testing video all with URL: {url}")
		else:
			res = session.get(url, params=params)
			logger.info(f"Testing video all with URL: {url} and params: {params}")
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'video', 'video_related.yaml')))
	def test_video_related(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		logger.info(f"Testing video related with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'video', 'video_detail.yaml')))
	def test_video_detail(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		logger.info(f"Testing video detail with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'video', 'video_detail_info.yaml')))
	def test_video_detail_info(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		logger.info(f"Testing video detail info with URL: {url} and p arams: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'video', 'video_url.yaml')))
	def test_video_url(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		logger.info(f"Testing video url with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'video', 'record_recent_video.yaml')))
	def test_record_recent_video(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		logger.info(f"Testing record recent video with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
