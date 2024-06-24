#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Author  : he
@File    : test_search.py
@Date    : 2024/6/24 10:00
@Description: 
"""
import logging
import os

import pytest

import common.operation_file as utils

logger = logging.getLogger(__name__)


@pytest.mark.usefixtures("session", "logs")
class TestSearch:
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'search', 'search.yaml')))
	def test_search(self, args, session, logs):
		url = args['request']['url']
		params = args['request']['params']
		res = session.get(url, params=params)
		logger.info(f"Testing search with URL: {url} and params: {params}")
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'search', 'cloud_search.yaml')))
	def test_cloud_search(self, args, session, logs):
		url = args['request']['url']
		params = args['request']['params']
		res = session.get(url, params=params)
		logger.info(f"Testing cloud search with URL: {url} and params: {params}")
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'search', 'default_search.yaml')))
	def test_default_search(self, args, session, logs):
		url = args['request']['url']
		res = session.get(url)
		logger.info(f"Testing default search with URL: {url}")
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'search', 'hot_search.yaml')))
	def test_hot_search(self, args, session, logs):
		url = args['request']['url']
		res = session.get(url)
		logger.info(f"Testing hot search with URL: {url}")
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'search', 'hot_detail_search.yaml')))
	def test_hot_detail_search(self, args, session, logs):
		url = args['request']['url']
		res = session.get(url)
		logger.info(f"Testing hot detail search with URL: {url}")
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'search', 'suggest_search.yaml')))
	def test_suggest_search(self, args, session, logs):
		url = args['request']['url']
		params = args['request']['params']
		res = session.get(url, params=params)
		logger.info(f"Testing suggest search with URL: {url} and params: {params}")
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'search', 'multimatch_search.yaml')))
	def test_multimatch_search(self, args, session, logs):
		url = args['request']['url']
		params = args['request']['params']
		res = session.get(url, params=params)
		logger.info(f"Testing multimatch search with URL: {url} and params: {params}")
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
