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
import random
import time

import pytest

import common.operation_file as utils

logger = logging.getLogger(__name__)


@pytest.mark.usefixtures("session", "logs")
class TestArtist:
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'artist', 'artist_list.yaml')))
	def test_artist_list(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		types = random.choice([[-1, 1, 2, 3]])
		areas = random.choice([[-1, 7, 96, 8, 16, 0]])
		all_params = {
			'limit': params['limit'],
			'offset': params['offset'],
			'initial': params['initial'],
			'type': params.get('type') or random.choice(types),
			'area': params.get('area') or random.choice(areas),
		}
		logger.info(f"Testing artist_list with URL: {url} and params: {all_params}")
		res = session.get(url, params=all_params)
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'artist', 'artist_sub.yaml')))
	def test_artist_sub(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		logger.info(f"Testing artist_sub with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'artist', 'artist_top.yaml')))
	def test_artist_top(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		logger.info(f"Testing artist_top with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'artist', 'artist_songs.yaml')))
	def test_artist_songs(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		logger.info(f"Testing artist_songs with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'artist', 'artist_sublist.yaml')))
	def test_artist_sublist(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		logger.info(f"Testing artist_sublist with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'artist', 'topic_sublist.yaml')))
	def test_artist_topic_sublist(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		logger.info(f"Testing artist_topic_sublist with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'artist', 'artist.yaml')))
	def test_artist(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		logger.info(f"Testing artist with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'artist', 'artist_mv.yaml')))
	def test_artist_mv(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		logger.info(f"Testing artist mv with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'artist', 'artist_album.yaml')))
	def test_artist_album(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		logger.info(f"Testing artist album with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'artist', 'artist_desc.yaml')))
	def test_artist_desc(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		logger.info(f"Testing artist desc with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'artist', 'artist_detail.yaml')))
	def test_artist_detail(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		logger.info(f"Testing artist detail with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'artist', 'artist_simi.yaml')))
	def test_artist_simi(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		logger.info(f"Testing artist simi with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'artist', 'artist_hot.yaml')))
	def test_artist_hot(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		logger.info(f"Testing artist hot with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'artist', 'artist_new_songs.yaml')))
	def test_artist_new_songs(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		if 'before' in params:
			params['before'] = params.get('before') or int(time.time() * 1000)
		logger.info(f"Testing artist new songs with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'artist', 'artist_new_mvs.yaml')))
	def test_artist_new_mvs(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		if 'before' in params:
			params['before'] = params.get('before') or int(time.time() * 1000)
		logger.info(f"Testing artist new mvs with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'artist', 'artist_fans.yaml')))
	def test_artist_fans(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		logger.info(f"Testing artist fans with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'artist', 'artist_follow_count.yaml')))
	def test_artist_follow_count(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		logger.info(f"Testing artist follow count with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'artist', 'digitalAlbum_detail.yaml')))
	def test_digital_album_detail(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		logger.info(f"Testing digitalAlbum detail with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'artist', 'digitalAlbum_sales.yaml')))
	def test_digital_album_sales(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		logger.info(f"Testing digitalAlbum sales with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
	
	@pytest.mark.parametrize('args', utils.read_file(os.path.join(os.getcwd(), 'data', 'artist', 'artist_video.yaml')))
	def test_artist_video(self, args, session):
		url = args['request']['url']
		params = args['request']['params']
		logger.info(f"Testing artist video with URL: {url} and params: {params}")
		res = session.get(url, params=params)
		try:
			res.raise_for_status()
			logger.info(f"Response: {res.json()}")
		except Exception as e:
			logger.error(f"Request failed: {e}")
			raise
