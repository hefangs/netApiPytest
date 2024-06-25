#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Author  : he
@File    : test_mv.py
@Date    : 2024/6/23 下午11:10
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
class TestMv:
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'mv', 'mv_share.yaml')))
	def test_mv_share(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		all_params = {
			'id': params['id'],
			'type': params['type'],
			'msg': params.get('msg') or f"mv{int(random.randint(1000, 9999))}"
		}
		logger.info(f"Testing share mv share with URL: {url} and params: {all_params}")
		res = session.get(url, params=all_params)
		try:
			res.raise_for_status()
			logger.info(f"Response : {res.json()}")
		except Exception as e:
			logger.error(f"Request Failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'mv', 'mv_sub.yaml')))
	def test_mv_sub(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		logger.info(f"Testing mv sub with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response : {res.json()}")
		except Exception as e:
			logger.error(f"Request Failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'mv', 'mv_sublist.yaml')))
	def test_mv_sublist(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		logger.info(f"Testing mv sublist with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response : {res.json()}")
		except Exception as e:
			logger.error(f"Request Failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'mv', 'mv_comment.yaml')))
	def test_mv_comment(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		if 'before' in params:
			params['before'] = params.get('before') or int(time.time() * 1000)
		logger.info(f"Testing mv comment with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response : {res.json()}")
		except Exception as e:
			logger.error(f"Request Failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'mv', 'mv_simi.yaml')))
	def test_mv_simi(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		logger.info(f"Testing mv simi with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response : {res.json()}")
		except Exception as e:
			logger.error(f"Request Failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'mv', 'mv_all.yaml')))
	def test_mv_all(self, args, session):
		url = args['request']['url']
		params = args['request'].get('params')
		if params is None:
			res = session.get(url)
			logger.info(f"Testing mv all with URL: {url}")
		else:
			logger.info(f"Testing mv url with URL: {url} and params: {params}")
			res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response : {res.json()}")
		except Exception as e:
			logger.error(f"Request Failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'mv', 'mv_latest.yaml')))
	def test_mv_latest(self, args, session):
		url = args['request']['url']
		params = args['request'].get('params')
		if params is None:
			res = session.get(url)
			logger.info(f"Testing mv latest with URL: {url}")
		else:
			logger.info(f"Testing mv latest with URL: {url} and params: {params}")
			res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response : {res.json()}")
		except Exception as e:
			logger.error(f"Request Failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'mv', 'mv_exclusive_rcmd.yaml')))
	def test_mv_exclusive_rcmd(self, args, session):
		url = args['request']['url']
		params = args['request'].get('params')
		logger.info(f"Testing mv exclusive rcmd with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response : {res.json()}")
		except Exception as e:
			logger.error(f"Request Failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'mv', 'mv_personalized.yaml')))
	def test_mv_personalized(self, args, session):
		url = args['request']['url']
		logger.info(f"Testing mv personalized with URL: {url}")
		res = session.get(url)
		try:
			res.raise_for_status()
			logger.info(f"Response : {res.json()}")
		except Exception as e:
			logger.error(f"Request Failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'mv', 'mv_top.yaml')))
	def test_mv_top(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		logger.info(f"Testing mv top with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response : {res.json()}")
		except Exception as e:
			logger.error(f"Request Failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'mv', 'mv_detail.yaml')))
	def test_mv_detail(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		logger.info(f"Testing mv detail with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response : {res.json()}")
		except Exception as e:
			logger.error(f"Request Failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'mv', 'mv_detail_info.yaml')))
	def test_mv_detail_info(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		logger.info(f"Testing mv detail info with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response : {res.json()}")
		except Exception as e:
			logger.error(f"Request Failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'mv', 'mv_url.yaml')))
	def test_mv_url(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		logger.info(f"Testing mv url with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response : {res.json()}")
		except Exception as e:
			logger.error(f"Request Failed: {e}")
			raise
