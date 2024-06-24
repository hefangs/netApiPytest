#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Author  : he
@File    : test_playlist.py
@Date    : 2024/6/22 11:45
@Description:
"""
import logging
import os
import random
import time

import pytest
from jsonpath_ng import parse

import common.operation_file as utils

logger = logging.getLogger(__name__)


@pytest.mark.usefixtures("session", "logs")
class TestPlayList:
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'playlist', 'user_playlist.yaml')))
	def test_user_playlist(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		# 提取数据 uid
		data = utils.read_file(os.path.join(os.getcwd(), 'extract.yaml'))
		logger.info(f"from extract get data: {data}")
		uid = data.get('uid')
		logger.info(f"from extract get uid: {uid}")
		# 替换参数
		for key, value in params.items():
			if value == "${extract(uid)}":
				params[key] = uid
				logger.info(f"Testing user playlist with URL: {url} and params: {params}")
				res = session.get(url, params=params)
				try:
					res.raise_for_status()
					logger.info(f"Response :{res.json()}")
				except Exception as e:
					logger.error(f"Request failed: {e}")
					raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'playlist', 'update_playlist.yaml')))
	def test_update_playlist(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		name = f"我的新歌单{random.randint(1000, 9999)}"
		desc = f"我的新歌单yeah!{random.randint(1000, 9999)}"
		tags = random.sample(["流行", "民谣", "摇滚", "电子", "说唱", "爵士", "金属", "古风", "轻音乐", "华语", "欧美", "日系", "粤语"], 3)
		all_params = {
			'id': params['id'],
			'name': name,
			'desc': desc,
			'tags': tags
		}
		logger.info(f"Testing update playlist with URL: {url} and params: {all_params}")
		res = session.get(url, params=all_params)
		try:
			res.raise_for_status()
			logger.info(f"Response :{res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'playlist', 'update_playlist_desc.yaml')))
	def test_update_playlist_desc(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		desc = f"我的新歌单yeah!{random.randint(1000, 9999)}"
		all_params = {
			'id': params['id'],
			'desc': desc,
		}
		logger.info(f"Testing update playlist desc with URL: {url} and params: {all_params}")
		res = session.get(url, params=all_params)
		try:
			res.raise_for_status()
			logger.info(f"Response :{res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'playlist', 'update_playlist_name.yaml')))
	def test_update_playlist_name(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		name = f"我的新歌单{random.randint(1000, 9999)}"
		all_params = {
			'id': params['id'],
			'name': name,
		}
		logger.info(f"Testing update playlist name with URL: {url} and params: {all_params}")
		res = session.get(url, params=all_params)
		try:
			res.raise_for_status()
			logger.info(f"Response :{res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'playlist', 'update_playlist_tags.yaml')))
	def test_update_playlist_tags(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		tags = f"我的新歌单{random.randint(1000, 9999)}"
		all_params = {
			'id': params['id'],
			'tags': tags,
		}
		logger.info(f"Testing update playlist tags with URL: {url} and params: {all_params}")
		res = session.get(url, params=all_params)
		try:
			res.raise_for_status()
			logger.info(f"Response :{res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'playlist', 'update_playlist_order.yaml')))
	def test_update_playlist_order(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		logger.info(f"Testing update playlist order with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response :{res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'playlist', 'share_playlist.yaml')))
	def test_playlist_share(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		all_params = {
			'id': params['id'],
			'type': params['type'],
			'msg': params.get('msg') or f"playlist{int(random.randint(1000, 9999))}"
		}
		logger.info(f"Testing share playlist with URL: {url} and params: {all_params}")
		res = session.get(url, params=all_params)
		try:
			res.raise_for_status()
			logger.info(f"Response :{res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise e
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'playlist', 'category_playlist.yaml')))
	def test_category_playlist(self, args, session):
		url = args['request']['url']
		logger.info(f"Testing category playlist with URL: {url} ")
		res = session.get(url)
		try:
			res.raise_for_status()
			logger.info(f"Response :{res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'playlist', 'hot_playlist.yaml')))
	def test_hot_playlist(self, args, session):
		url = args['request']['url']
		logger.info(f"Testing hot playlist with URL: {url} ")
		res = session.get(url)
		try:
			res.raise_for_status()
			logger.info(f"Response :{res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'playlist', 'top_playlist.yaml')))
	def test_top_playlist(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		logger.info(f"Testing top playlist with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response :{res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'playlist', 'tag_playlist.yaml')))
	def test_tag_playlist(self, args, session):
		url = args['request']['url']
		logger.info(f"Testing tag_playlist with URL: {url}")
		res = session.get(url)
		try:
			res.raise_for_status()
			logger.info(f"Response :{res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'playlist', 'related_playlist.yaml')))
	def test_related_playlist(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		logger.info(f"Testing related playlist with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response :{res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'playlist', 'detail_playlist.yaml')))
	def test_detail_playlist(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		logger.info(f"Testing detail playlist  with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response :{res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'playlist', 'all_track_playlist.yaml')))
	def test_track_playlist(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		logger.info(f"Testing all track playlist with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response :{res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'playlist', 'dynamic_playlist.yaml')))
	def test_dynamic_playlist(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		logger.info(f"Testing dynamic playlist  with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response :{res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'playlist', 'update_playcount_playlist.yaml')))
	def test_update_playcount_playlist(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		logger.info(f"Testing update playcount playlist  with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response :{res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'playlist', 'create_playlist.yaml')))
	def test_create_playlist(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		logger.info(f"Testing create playlist  with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response :{res.json()}")
			# 提取新生成的歌单 id 再写入extract.yaml
			jsonpath_expression_id = parse('$.id')
			match = jsonpath_expression_id.find(res.json())
			if match:
				data = {
					'id': match[0].value
				}
				logger.info(f"extract id: {match[0].value}")
				utils.write_file(os.path.join(os.getcwd(), 'extract.yaml'), data)
		except Exception as e:
			logger.error(f"Request failed:{e}")
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'playlist', 'delete_playlist.yaml')))
	def test_delete_playlist(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		# 获取id
		data = utils.read_file(os.path.join(os.getcwd(), 'extract.yaml'))
		ids = data.get('id')
		logger.info(f"from extract get id: {ids}")
		# 替换id为实际的值
		for key, value in params.items():
			if value == "${extract(id)}":
				params[key] = ids
				logger.info(f"Testing delete playlist with URL: {url} and params: {params}")
				res = session.get(url, params=params)
				try:
					res.raise_for_status()
					logger.info(f"Response :{res.json()}")
				except Exception as e:
					logger.error(f"Request failed: {e}")
					raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'playlist', 'subscribe_playlist.yaml')))
	def test_subscribe_playlist(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		logger.info(f"Testing subscribe playlist  with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response :{res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'playlist', 'subscribers_playlist.yaml')))
	def test_subscribes_playlist(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		logger.info(f"Testing subscribers playlist  with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response :{res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'playlist', 'tracks_playlist.yaml')))
	def test_tracks_playlist(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		logger.info(f"Testing tracks playlist  with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response :{res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'playlist', 'comment_playlist.yaml')))
	def test_comment_playlist(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		if 'before' in params:
			params['before'] = params.get('before') or int(time.time() * 1000)
		logger.info(f"Testing comment playlist  with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response :{res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'playlist', 'simi_playlist.yaml')))
	def test_simi_playlist(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		logger.info(f"Testing simi playlist  with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response :{res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
