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
