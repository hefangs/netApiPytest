#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Author  : he
@File    : test_song.py
@Date    : 2024/6/22 下午6:57
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
class TestSong:
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'song', 'update_song_order.yaml')))
	def test_song_order(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		logger.info(f"Testing update song order with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response :{res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise e
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'song', 'share_song.yaml')))
	def test_song_share(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		all_params = {
			'id': params['id'],
			'type': params['type'],
			'msg': params.get('msg') or f"song{int(random.randint(1000, 9999))}"
		}
		logger.info(f"Testing share song with URL: {url} and params: {all_params}")
		res = session.get(url, params=all_params)
		try:
			res.raise_for_status()
			logger.info(f"Response :{res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise e
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'song', 'url_song.yaml')))
	def test_song_url(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		logger.info(f"Testing song url with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response :{res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'song', 'check_song.yaml')))
	def test_check_song(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		logger.info(f"Testing check song with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response :{res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'song', 'lyric_song.yaml')))
	def test_lyric_song(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		logger.info(f"Testing lyric song with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response :{res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'song', 'lyric_new_song.yaml')))
	def test_lyric_new_song(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		logger.info(f"Testing lyric new song with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response :{res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'song', 'top_song.yaml')))
	def test_top_song(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		logger.info(f"Testing top song with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response :{res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'song', 'comment_music.yaml')))
	def test_comment_music(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		if 'before' in params:
			params['before'] = params.get('before') or int(time.time() * 1000)
		logger.info(f"Testing comment music with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response :{res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'song', 'comment_floor.yaml')))
	def test_comment_floor(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		if 'time' in params:
			params['time'] = params.get('time') or int(time.time() * 1000)
		logger.info(f"Testing comment floor with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response :{res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'song', 'song_detail.yaml')))
	def test_song_detail(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		logger.info(f"Testing song detail with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response :{res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'song', 'song_simi.yaml')))
	def test_song_simi(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		logger.info(f"Testing song simi with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response :{res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'song', 'recommend_songs.yaml')))
	def test_recommend_songs(self, args, session):
		url = args['request']['url']
		logger.info(f"Testing recommend songs with URL: {url}")
		res = session.get(url)
		try:
			res.raise_for_status()
			logger.info(f"Response :{res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'song', 'recommend_songs_dislike.yaml')))
	def test_recommend_songs_dislike(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		logger.info(f"Testing recommend songs dislike with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response :{res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'song', 'history_recommend_songs.yaml')))
	def test_history_recommend_songs(self, args, session):
		url = args['request']['url']
		logger.info(f"Testing history recommend songs with URL: {url}")
		res = session.get(url)
		try:
			res.raise_for_status()
			logger.info(f"Response :{res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'song', 'history_recommend_songs_detail.yaml')))
	def test_history_recommend_songs_detail(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		logger.info(f"Testing history recommend songs detail with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response :{res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'song', 'personalized_new_song.yaml')))
	def test_personalized_new_song(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		logger.info(f"Testing personalized new song with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response :{res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
