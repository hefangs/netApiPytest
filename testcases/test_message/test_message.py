#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Author  : he
@File    : test_message.py
@Date    : 2024/6/22 11:25
@Description:
"""
import logging
import os
import time

import pytest

import common.operation_file as utils

logger = logging.getLogger(__name__)


@pytest.mark.usefixtures("session", "logs")
class TestMessage:
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'message', 'pl_count.yaml')))
	def test_pl_count(self, args, session):
		url = args['request']['url']
		logger.info(f"Testing user pl_count with URL: {url}")
		res = session.get(url)
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'message', 'private_messages.yaml')))
	def test_private_messages(self, args, session):
		url = args['request']['url']
		params = args['request'].get('params')
		if params is None:
			res = session.get(url)
			logger.info(f"Testing user private_messages with URL: {url}")
		else:
			res = session.get(url, params=params)
			logger.info(f"Testing user private_messages with URL: {url}, params: {params}")
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'message', 'send_private_message.yaml')))
	def test_send_private_message(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		if 'msg' in params:
			params['msg'] = params.get('msg') or f"ok{int(time.time() * 1000)}"
		logger.info(f"Testing user send_private_message with URL: {url}, params: {params}")
		res = session.post(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'message', 'send_private_message_song.yaml')))
	def test_send_private_message_song(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		if 'msg' in params:
			params['msg'] = params.get('msg') or f"ok{int(time.time() * 1000)}"
		logger.info(f"Testing user send_private_message_song with URL: {url}, params: {params}")
		res = session.post(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'message', 'send_private_message_album.yaml')))
	def test_send_private_message_album(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		if 'msg' in params:
			params['msg'] = params.get('msg') or f"ok{int(time.time() * 1000)}"
		logger.info(f"Testing user send_private_message_album with URL: {url}, params: {params}")
		res = session.post(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'message', 'send_private_message_playlist.yaml')))
	def test_send_private_message_playlist(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		if 'msg' in params:
			params['msg'] = params.get('msg') or f"ok{int(time.time() * 1000)}"
		logger.info(f"Testing user send_private_message_playlist with URL: {url}, params: {params}")
		res = session.post(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'message', 'private_message_history.yaml')))
	def test_private_message_history(self, args, session):
		url = args['request']['url']
		params = args['request'].get('params')
		if 'before' in params:
			params['before'] = params.get('before') or int(time.time() * 1000)
		# 从 extract 中获取 uid
		data = utils.read_file(os.path.join(os.getcwd(), 'extract.yaml'))
		uid = data.get('uid')
		logger.info(f"uid:{uid}")
		# ${extract(uid)} 替换为真的uid
		for key, value in params.items():
			if value == '${extract(uid)}':
				params[key] = uid
		logger.info(f"Testing user private_message_history with URL: {url}, params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'message', 'comments.yaml')))
	def test_comments(self, args, session):
		url = args['request']['url']
		params = args['request'].get('params')
		if 'before' in params:
			params['before'] = params.get('before') or int(time.time() * 1000)
		# 从 extract 中获取 uid
		data = utils.read_file(os.path.join(os.getcwd(), 'extract.yaml'))
		uid = data.get('uid')
		logger.info(f"uid:{uid}")
		# ${extract(uid)} 替换为真的uid
		for key, value in params.items():
			if value == '${extract(uid)}':
				params[key] = uid
		logger.info(f"Testing user comments with URL: {url}, params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'message', 'recent_contact.yaml')))
	def test_recent_contact(self, args, session):
		url = args['request']['url']
		logger.info(f"Testing user recent contact with URL: {url}")
		res = session.get(url)
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'message', 'forwards.yaml')))
	def test_forwards(self, args, session):
		url = args['request']['url']
		params = args['request'].get('params')
		logger.info(f"Testing user forwards with URL: {url}, params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'message', 'notices.yaml')))
	def test_notices(self, args, session):
		url = args['request']['url']
		params = args['request'].get('params')
		logger.info(f"Testing user notices with URL: {url}, params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
