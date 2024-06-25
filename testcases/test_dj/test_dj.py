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
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'dj', 'banner.yaml')))
	def test_banner(self, args, session):
		url = args['request']['url']
		logger.info(f"Testing banner with URL: {url}")
		res = session.get(url)
		try:
			res.raise_for_status()
			logger.info(f"Response : {res.json()}")
		except Exception as e:
			logger.error(f"Request Failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'dj', 'personalize_recommend.yaml')))
	def test_personalize_recommend(self, args, session):
		url = args['request']['url']
		params = args['request'].get('params')
		if params is None:
			res = session.get(url)
			logger.info(f"Testing personalized_recommend with URL: {url}")
		else:
			logger.info(f"Testing personalized_recommend with URL: {url} and params: {params}")
			res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response : {res.json()}")
		except Exception as e:
			logger.error(f"Request Failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'dj', 'dj_subscriber.yaml')))
	def test_dj_subscriber(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		if 'time' in params:
			params['time'] = params.get('time') or int(time.time() * 1000)
		logger.info(f"Testing dj_subscriber with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response : {res.json()}")
		except Exception as e:
			logger.error(f"Request Failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'dj', 'dj_hot.yaml')))
	def test_dj_hot(self, args, session):
		url = args['request']['url']
		params = args['request'].get('params')
		if params is None:
			res = session.get(url)
			logger.info(f"Testing dj_hot with URL: {url}")
		else:
			res = session.get(url, params=params)
			logger.info(f"Testing dj_hot with URL: {url} and params: {params}")
		try:
			res.raise_for_status()
			logger.info(f"Response : {res.json()}")
		except Exception as e:
			logger.error(f"Request Failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'dj', 'dj_program_toplist.yaml')))
	def test_dj_program_toplist(self, args, session):
		url = args['request']['url']
		params = args['request'].get('params')
		if params is None:
			res = session.get(url)
			logger.info(f"Testing dj_program_toplist with URL: {url}")
		else:
			res = session.get(url, params=params)
			logger.info(f"Testing dj_program_toplist with URL: {url} and params: {params}")
		try:
			res.raise_for_status()
			logger.info(f"Response : {res.json()}")
		except Exception as e:
			logger.error(f"Request Failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'dj', 'pay_dj_toplist.yaml')))
	def test_pay_dj_toplist(self, args, session):
		url = args['request']['url']
		params = args['request'].get('params')
		if params is None:
			res = session.get(url)
			logger.info(f"Testing pay_dj_toplist with URL: {url}")
		else:
			res = session.get(url, params=params)
			logger.info(f"Testing pay_dj_toplist with URL: {url} and params: {params}")
		try:
			res.raise_for_status()
			logger.info(f"Response : {res.json()}")
		except Exception as e:
			logger.error(f"Request Failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'dj', '24h_program_toplist.yaml')))
	def test_24h_program_toplist(self, args, session):
		url = args['request']['url']
		params = args['request'].get('params')
		if params is None:
			res = session.get(url)
			logger.info(f"Testing 24h_program_toplist with URL: {url}")
		else:
			res = session.get(url, params=params)
			logger.info(f"Testing 24h_program_toplist with URL: {url} and params: {params}")
		try:
			res.raise_for_status()
			logger.info(f"Response : {res.json()}")
		except Exception as e:
			logger.error(f"Request Failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'dj', '24h_dj_toplist.yaml')))
	def test_24h_dj_toplist(self, args, session):
		url = args['request']['url']
		params = args['request'].get('params')
		if params is None:
			res = session.get(url)
			logger.info(f"Testing 24h_dj_toplist with URL: {url}")
		else:
			res = session.get(url, params=params)
			logger.info(f"Testing 24h_dj_toplist with URL: {url} and params: {params}")
		try:
			res.raise_for_status()
			logger.info(f"Response : {res.json()}")
		except Exception as e:
			logger.error(f"Request Failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'dj', 'newcomer_dj_toplist.yaml')))
	def test_newcomer_dj_toplist(self, args, session):
		url = args['request']['url']
		params = args['request'].get('params')
		if params is None:
			res = session.get(url)
			logger.info(f"Testing newcomer_dj_toplist with URL: {url}")
		else:
			res = session.get(url, params=params)
			logger.info(f"Testing newcomer_anchor_toplist with URL: {url} and params: {params}")
		try:
			res.raise_for_status()
			logger.info(f"Response : {res.json()}")
		except Exception as e:
			logger.error(f"Request Failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'dj', 'popular_dj_toplist.yaml')))
	def test_popular_dj_toplist(self, args, session):
		url = args['request']['url']
		params = args['request'].get('params')
		if params is None:
			res = session.get(url)
			logger.info(f"Testing newcomer_dj_toplist with URL: {url}")
		else:
			res = session.get(url, params=params)
			logger.info(f"Testing newcomer_anchor_toplist with URL: {url} and params: {params}")
		try:
			res.raise_for_status()
			logger.info(f"Response : {res.json()}")
		except Exception as e:
			logger.error(f"Request Failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'dj', 'dj_toplist.yaml')))
	def test_dj_toplist(self, args, session):
		url = args['request']['url']
		params = args['request'].get('params')
		if params is None:
			res = session.get(url)
			logger.info(f"Testing dj_toplist with URL: {url}")
		else:
			res = session.get(url, params=params)
			logger.info(f"Testing dj_toplist with URL: {url} and params: {params}")
		try:
			res.raise_for_status()
			logger.info(f"Response : {res.json()}")
		except Exception as e:
			logger.error(f"Request Failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'dj', 'dj_radio_hot.yaml')))
	def test_dj_radio_hot(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		res = session.get(url, params=params)
		logger.info(f"Testing dj_radio_hot with URL: {url} and params: {params}")
		try:
			res.raise_for_status()
			logger.info(f"Response : {res.json()}")
		except Exception as e:
			logger.error(f"Request Failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'dj', 'dj_recommend.yaml')))
	def test_dj_recommend(self, args, session):
		url = args['request']['url']
		res = session.get(url)
		logger.info(f"Testing dj_recommend with URL: {url}")
		try:
			res.raise_for_status()
			logger.info(f"Response : {res.json()}")
		except Exception as e:
			logger.error(f"Request Failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'dj', 'dj_catelist.yaml')))
	def test_dj_catelist(self, args, session):
		url = args['request']['url']
		logger.info(f"Testing dj_catelist with URL: {url}")
		res = session.get(url)
		try:
			res.raise_for_status()
			logger.info(f"Response : {res.json()}")
		except Exception as e:
			logger.error(f"Request Failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'dj', 'dj_recommend_type.yaml')))
	def test_dj_recommend_type(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		res = session.get(url, params=params)
		logger.info(f"Testing dj_recommend_type with URL: {url} and params: {params}")
		try:
			res.raise_for_status()
			logger.info(f"Response : {res.json()}")
		except Exception as e:
			logger.error(f"Request Failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'dj', 'dj_sub.yaml')))
	def test_dj_sub(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		res = session.get(url, params=params)
		logger.info(f"Testing dj_sub with URL: {url} and params: {params}")
		try:
			res.raise_for_status()
			logger.info(f"Response : {res.json()}")
		except Exception as e:
			logger.error(f"Request Failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'dj', 'dj_sublist.yaml')))
	def test_dj_sublist(self, args, session):
		url = args['request']['url']
		logger.info(f"Testing dj_sublist with URL: {url}")
		res = session.get(url)
		try:
			res.raise_for_status()
			logger.info(f"Response : {res.json()}")
		except Exception as e:
			logger.error(f"Request Failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'dj', 'dj_paygift.yaml')))
	def test_dj_paygift(self, args, session):
		url = args['request']['url']
		params = args['request'].get('params')
		if params is None:
			res = session.get(url)
			logger.info(f"Testing dj_paygift with URL: {url}")
		else:
			res = session.get(url, params=params)
			logger.info(f"Testing dj_paygift with URL: {url} and params: {params}")
		try:
			res.raise_for_status()
			logger.info(f"Response : {res.json()}")
		except Exception as e:
			logger.error(f"Request Failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'dj', 'category_excludehot.yaml')))
	def test_category_excludehot(self, args, session):
		url = args['request']['url']
		logger.info(f"Testing category_excludehot with URL: {url}")
		res = session.get(url)
		try:
			res.raise_for_status()
			logger.info(f"Response : {res.json()}")
		except Exception as e:
			logger.error(f"Request Failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'dj', 'dj_recommend_category.yaml')))
	def test_dj_recommend_category(self, args, session):
		url = args['request']['url']
		logger.info(f"Testing dj_category_recommend with URL: {url}")
		res = session.get(url)
		try:
			res.raise_for_status()
			logger.info(f"Response : {res.json()}")
		except Exception as e:
			logger.error(f"Request Failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'dj', 'jd_today_perfered.yaml')))
	def test_dj_today_perfered(self, args, session):
		url = args['request']['url']
		logger.info(f"Testing dj_today_perfered with URL: {url}")
		res = session.get(url)
		try:
			res.raise_for_status()
			logger.info(f"Response : {res.json()}")
		except Exception as e:
			logger.error(f"Request Failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'dj', 'dj_detail.yaml')))
	def test_dj_detail(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		res = session.get(url, params=params)
		logger.info(f"Testing dj_detail with URL: {url} and params: {params}")
		try:
			res.raise_for_status()
			logger.info(f"Response : {res.json()}")
		except Exception as e:
			logger.error(f"Request Failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'dj', 'dj_programs.yaml')))
	def test_dj_programs(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		res = session.get(url, params=params)
		logger.info(f"Testing dj_programs with URL: {url} and params: {params}")
		try:
			res.raise_for_status()
			logger.info(f"Response : {res.json()}")
		except Exception as e:
			logger.error(f"Request Failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'dj', 'dj_program_detail.yaml')))
	def test_dj_program_detail(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		res = session.get(url, params=params)
		logger.info(f"Testing dj_program_detail with URL: {url} and params: {params}")
		try:
			res.raise_for_status()
			logger.info(f"Response : {res.json()}")
		except Exception as e:
			logger.error(f"Request Failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'dj', 'record_recent_dj.yaml')))
	def test_record_recent_dj(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		res = session.get(url, params=params)
		logger.info(f"Testing record_recent_dj with URL: {url} and params: {params}")
		try:
			res.raise_for_status()
			logger.info(f"Response : {res.json()}")
		except Exception as e:
			logger.error(f"Request Failed: {e}")
			raise
