#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Author  : he
@File    : test_message.py
@Date    : 2024/6/21 18:25
@Description:
"""
import logging
import os.path
import random
import time

import pytest
from jsonpath_ng import parse

import common.operation_file as utils

logger = logging.getLogger(__name__)


@pytest.mark.usefixtures("session", "logs")
class TestUser:
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'user', 'status.yaml')))
	def test_login_status(self, args, session):
		url = args['request']['url']
		res = session.get(url)
		logger.info(f"Testing login status with URL: {url}")
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Testing login status with URL: {e} failed")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'user', 'detail.yaml')))
	def test_user_detail(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		# 从 extract 提取数据 uid
		data = utils.read_file(os.path.join(os.getcwd(), 'extract.yaml'))
		logger.info(f"from extract get data: {data}")
		uid = data.get('uid')
		
		# 替换 params 中的 ${extract(id)} 为实际的 id 值
		for key, value in params.items():
			if value == "${extract(uid)}":
				logger.info(f"Replacing {params[key]}")
				params[key] = uid
				logger.info(f"Testing user detail with URL: {url} and params: {params}")
				res = session.get(url, params=params)
				try:
					res.raise_for_status()
					logger.info(f"Response: {res.json()}")
				except Exception as e:
					logger.error(f"Request failed: {e}")
					raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'user', 'account.yaml')))
	def test_user_account(self, args, session):
		url = args['request']['url']
		logger.info(f"Testing user account with URL: {url}")
		res = session.get(url)
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'user', 'subcount.yaml')))
	def test_user_subcount(self, args, session):
		url = args['request']['url']
		logger.info(f"Testing user subcount with URL: {url}")
		res = session.get(url)
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'user', 'level.yaml')))
	def test_user_level(self, args, session):
		url = args['request']['url']
		logger.info(f"Testing user level with URL: {url}")
		res = session.get(url)
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'user', 'binding.yaml')))
	def test_user_binding(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		
		# 从 extract 文件中获取 uid
		data = utils.read_file(os.path.join(os.getcwd(), 'extract.yaml'))
		uid = data.get('uid')
		logger.info(f"from extract get uid: {uid}")
		# 替换 params 中的 ${extract(id)} 为实际的 id 值
		for key, value in params.items():
			if value == "${extract(uid)}":
				logger.info(f"Replacing {params[key]}")
				params[key] = uid
				logger.info(f"Testing user binding with URL: {url} and params: {params}")
				res = session.get(url, params=params)
				try:
					res.raise_for_status()
					logger.info(f"Response: {res.json()}")
				except Exception as e:
					logger.error(f"Request failed: {e}")
					raise
	
	@pytest.mark.skipif(True, reason="skip")
	# update user info 每天限制2次
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'user', 'update.yaml')))
	def test_user_update(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		gender = random.choice([0, 1, 2])
		time_stamp = int(time.time())
		name = f"he_{random.randint(1000, 9999)}"
		signature = f"music_{random.randint(1000, 9999)}"
		all_params = {
			"gender": gender,
			"birthday": time_stamp,
			"nickname": name,
			"city": params['city'],
			"province": params['province'],
			"signature": signature
		}
		logger.info(f"Testing user update with URL: {url} and params: {all_params}")
		res = session.get(url, params=all_params)
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'user', 'comment_history.yaml')))
	def test_comment_history(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		# 从 extract 文件中获取 uid
		data = utils.read_file(os.path.join(os.getcwd(), 'extract.yaml'))
		uid = data.get('uid')
		logger.info(f"from extract get uid: {uid}")
		# 替换 params 中的 ${extract(id)} 为实际的 id 值
		for key, value in params.items():
			if value == "${extract(uid)}":
				logger.info(f"Replacing {params[key]}")
				params[key] = uid
				time_stamp = int(time.time())
				all_params = {
					'uid': params['uid'],
					'limit': params.get('limit') or 10,
					'time': params.get('time') or time_stamp
				}
				logger.info(f"Testing comment history with URL: {url} and params: {all_params}")
				res = session.get(url, params=all_params)
				try:
					res.raise_for_status()
					logger.info(f"Response: {res.json()}")
				except Exception as e:
					logger.error(f"Request failed: {e}")
					raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'user', 'follows.yaml')))
	def test_user_follows(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		# 从 extract 文件中获取 uid
		data = utils.read_file(os.path.join(os.getcwd(), 'extract.yaml'))
		uid = data.get('uid')
		logger.info(f"from extract get uid: {uid}")
		# 替换 params 中的 ${extract(id)} 为实际的 id 值
		for key, value in params.items():
			if value == "${extract(uid)}":
				params[key] = uid
				logger.info(f"Replacing {params[key]}")
				logger.info(f"Testing user follows with URL: {url} and params: {params}")
				res = session.get(url, params=params)
				try:
					res.raise_for_status()
					logger.info(f"Response: {res.json()}")
				except Exception as e:
					logger.error(f"Request failed: {e}")
					raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'user', 'followeds.yaml')))
	def test_user_follows(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		# 从 extract 文件中获取 uid
		data = utils.read_file(os.path.join(os.getcwd(), 'extract.yaml'))
		uid = data.get('uid')
		logger.info(f"from extract get uid: {uid}")
		# 替换 params 中的 ${extract(id)} 为实际的 id 值
		for key, value in params.items():
			if value == "${extract(uid)}":
				params[key] = uid
				logger.info(f"Replacing {params[key]}")
				all_params = {
					'uid': params['uid'],
					'limit': params.get('limit') or 30,
					'offset': params.get('offset') or 0
				}
				logger.info(f"Testing user followeds with URL: {url} and params: {all_params}")
				res = session.get(url, params=all_params)
				try:
					res.raise_for_status()
					logger.info(f"Response: {res.json()}")
				except Exception as e:
					logger.error(f"Request failed: {e}")
					raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'user', 'event.yaml')))
	def test_user_event(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		# 从 extract 文件中获取 uid
		data = utils.read_file(os.path.join(os.getcwd(), 'extract.yaml'))
		uid = data.get('uid')
		logger.info(f"from extract get uid: {uid}")
		# 替换 params 中的 ${extract(id)} 为实际的 id 值
		for key, value in params.items():
			if value == "${extract(uid)}":
				params[key] = uid
				logger.info(f"Replacing {params[key]}")
				all_params = {
					'uid': params['uid'],
					'limit': params.get('limit') or 30,
					'lasttime': params.get('lasttime') or int(time.time() * 1000)
				}
				logger.info(f"Testing user event with URL: {url} and params: {all_params}")
				res = session.get(url, params=all_params)
				
				try:
					res.raise_for_status()
					logger.info(f"Response: {res.json()}")
					
					# 获取 events 列表长度并生成随机索引
					events = res.json().get('events', [])
					logger.info(f"events length: {len(events)}")
					if not events:
						logger.error("No events found in the response.")
						raise Exception("No events found")
					random_index = random.randint(0, len(events) - 1)
					logger.info(f"Random index selected: {random_index}")
					
					# 写入 resource_id & thread_id
					jsonpath_expression_resource_id = parse(f'$.events[{random_index}].info.resourceId')
					jsonpath_expression_thread_id = parse(f'$.events[{random_index}].info.threadId')
					match_resource_id = jsonpath_expression_resource_id.find(res.json())
					match_thread_id = jsonpath_expression_thread_id.find(res.json())
					if match_resource_id and match_thread_id:
						logger.info(f"extract resource_id: {match_resource_id[0].value}")
						logger.info(f"extract thread_id: {match_thread_id[0].value}")
						data = {
							'resource_id': match_resource_id[0].value,
							'thread_id': match_thread_id[0].value
						}
						utils.write_file(os.path.join(os.getcwd(), 'extract.yaml'), data)
						logger.info(f"write resource_id & thread_id to extract data:{data}")
				except Exception as e:
					logger.error(f"Request failed: {e}")
					raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'user', 'event_forward.yaml')))
	def test_user_event_forwards(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		# 从 extract 文件中获取 uid & resource_id
		data = utils.read_file(os.path.join(os.getcwd(), 'extract.yaml'))
		uid = data.get('uid')
		resource_id = data.get('resource_id')
		logger.info(f"from extract get uid: {uid}")
		logger.info(f"from extract get resource_id: {resource_id}")
		
		# 替换 params 中的 ${extract(uid)} 和 ${extract(resource_id)} 为实际的值
		for key, value in params.items():
			if value == "${extract(uid)}":
				params[key] = uid
				logger.info(f"Replacing {key} with {params[key]}")
			elif value == "${extract(resource_id)}":
				params[key] = resource_id
				logger.info(f"Replacing {key} with {params[key]}")
		
		# 构建请求参数
		all_params = {
			'uid': params['uid'],
			'evId': params['evId'],
			'forwards': params.get('forwards') or f"share_resource{random.randint(1000, 9999)}"
		}
		
		logger.info(f"Testing user event forwards with URL: {url} and params: {all_params}")
		res = session.get(url, params=all_params)
		
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
			
			# 写入 eventId
			jsonpath_expression_event_id = parse('$.data.eventId')
			match = jsonpath_expression_event_id.find(res.json())
			if match:
				event_id = match[0].value
				logger.info(f"extract eventId: {event_id}")
				data = {'event_id': event_id}
				utils.write_file(os.path.join(os.getcwd(), 'extract.yaml'), data)
				logger.info(f"write eventId to extract, data: {data}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'user', 'event_delete.yaml')))
	def test_user_event_delete(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		# 从 extract 文件中获取 event_id
		data = utils.read_file(os.path.join(os.getcwd(), 'extract.yaml'))
		event_id = data.get('event_id')
		logger.info(f"from extract get event_id: {event_id}")
		
		# 替换 params 中的 ${extract(event_id)} 为实际的值
		for key, value in params.items():
			if value == "${extract(event_id)}":
				params[key] = event_id
				logger.info(f"Replacing {key} with {params[key]}")
		
		# 构建请求参数
		all_params = {
			'evId': params['evId']
		}
		
		logger.info(f"Testing user event delete with URL: {url} and params: {all_params}")
		res = session.get(url, params=all_params)
		
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'user', 'event_comment.yaml')))
	def test_user_event_comment(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		# 从 extract 文件中获取 thread_id
		data = utils.read_file(os.path.join(os.getcwd(), 'extract.yaml'))
		thread_id = data.get('thread_id')
		logger.info(f"from extract get thread_id: {thread_id}")
		# 替换 params 中的 ${extract(thread_id)} 为实际的值
		for key, value in params.items():
			if value == "${extract(thread_id)}":
				params[key] = thread_id
				logger.info(f"Replacing {key} with {params[key]}")
				logger.info(f"Testing user event comment with URL: {url} and params: {params}")
				res = session.get(url, params=params)
				try:
					res.raise_for_status()
					logger.info(f"Response: {res.json()}")
				except Exception as e:
					logger.error(f"Request failed: {e}")
					raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'user', 'follow.yaml')))
	def test_user_follow(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		logger.info(f"Testing user follow with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			if res.status_code != 200 or 'code' in res.json() and res.json()['code'] != 200:
				# logger.error(f"HTTPError: Status Code {res.status_code}")
				logger.error(f"Response: {res.json()}")
			else:
				# Log the successful response code and message
				logger.info(f"Response: {res.json()}")
		
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'user', 'record.yaml')))
	def test_user_record(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		# 从 extract 文件中获取 uid
		data = utils.read_file(os.path.join(os.getcwd(), 'extract.yaml'))
		uid = data.get('uid')
		logger.info(f"from extract get uid: {uid}")
		
		# 替换 params 中的 ${extract(uid)} 为实际的值
		for key, value in params.items():
			if value == "${extract(uid)}":
				params[key] = uid
				logger.info(f"Replacing {key} with {params[key]}")
		logger.info(f"Testing user record with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'user', 'hot_topic.yaml')))
	def test_user_hot_topic(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		logger.info(f"Testing user hot topic with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
			
			# 写入 actid
			jsonpath_expression_actId = parse('$.hot[0].actId')
			match = jsonpath_expression_actId.find(res.json())
			if match:
				actId = match[0].value
				logger.info(f"extract actid: {actId}")
				
				# 检查actId 是否存在
				extract_data = utils.read_file(os.path.join(os.getcwd(), 'extract.yaml'))
				if 'actid' in extract_data:
					logger.info(f"actId already exists in extract.yaml, skip writing")
					return
				data = {'actid': actId}
				utils.write_file(os.path.join(os.getcwd(), 'extract.yaml'), data)
				logger.info(f"write actid to extract, data: {data}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'user', 'topic_detail.yaml')))
	def test_user_topic_detail(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		# 从 extract 文件中获取 actId
		data = utils.read_file(os.path.join(os.getcwd(), 'extract.yaml'))
		actId = data.get('actid')
		logger.info(f"from extract get actid: {actId}")
		# 替换 params 中的 ${extract(actid)} 为实际的值
		for key, value in params.items():
			if value == "${extract(actid)}":
				params[key] = actId
				logger.info(f"Replacing {key} with {params[key]}")
				logger.info(f"Testing user topic detail with URL: {url} and params: {params}")
				res = session.get(url, params=params)
				try:
					res.raise_for_status()
					logger.info(f"Response: {res.json()}")
				except Exception as e:
					logger.error(f"Request failed: {e}")
					raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'user', 'hot_event.yaml')))
	def test_user_hot_event(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		# 从 extract 文件中获取 actId
		data = utils.read_file(os.path.join(os.getcwd(), 'extract.yaml'))
		actId = data.get('actid')
		logger.info(f"from extract get actid: {actId}")
		for key, value in params.items():
			if value == "${extract(actid)}":
				params[key] = actId
				logger.info(f"Replacing {key} with {params[key]}")
				logger.info(f"Testing user hot event with URL: {url} and params: {params}")
				res = session.get(url, params=params)
				try:
					res.raise_for_status()
					logger.info(f"Response: {res.json()}")
				except Exception as e:
					logger.error(f"Request failed: {e}")
					raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'user', 'playmode.yaml')))
	def test_user_playmode(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		logger.info(f"Testing user playmode with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'user', 'event_msg.yaml')))
	def test_user_event_msg(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		logger.info(f"Testing user event msg with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
