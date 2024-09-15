import datetime
import hashlib
import logging
import os
import os.path
from typing import Generator

import pytest
import requests
from jsonpath_ng import parse
from requests import Session
from requests.exceptions import RequestException

import common.operation_file as utils

logger = logging.getLogger(__name__)


def get_md5_hash(password):
	# 计算密码的 MD5 哈希值
	md5 = hashlib.md5()
	md5.update(password.encode('utf-8'))
	return md5.hexdigest()


def use_cached(session, cache) -> bool:
	# 使用缓存的会话信息
	cached_cookies = cache.get("session_cookies", default=None)
	cached_token = cache.get("session_token", default=None)
	cached_uid = cache.get("session_uid", default=None)
	if cached_cookies and cached_token and cached_uid:
		for cookie in cached_cookies:
			session.cookies.set(cookie['name'], cookie['value'], domain=cookie['domain'], path=cookie['path'])
		session.headers['Authorization'] = f'Bearer {cached_token}'
		data = {'uid': cached_uid}
		try:
			
			# 在写入之前清空文件
			utils.clear_file(os.path.join(os.getcwd(), 'extract.yaml'))
			# 将 uid 写到文件
			utils.write_file(os.path.join(os.getcwd(), 'extract.yaml'), data)
			logger.info(f"成功将 UID 写入文件: {data}")
		except Exception as e:
			logger.error(f"写入 UID 到文件失败: {e}")
			pytest.fail(f"写入 UID 到文件失败: {e}")
		return True
	return False


def pytest_configure(config):
	# 配置 pytest，设置日志文件名
	current_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
	log_file = f"./logs/{current_time}.log"
	config.option.log_file = log_file


@pytest.fixture(scope='function')
def logs():
	logger.info(f"--------------------------------Start testing----------------------------------")
	yield
	logger.info(f"---------------------------------End testing-------------------------- --------")


@pytest.fixture(scope="session")
def session(request: pytest.FixtureRequest) -> Generator[Session, None, None]:
	session = requests.Session()
	cache = request.config.cache
	
	# 使用缓存
	if use_cached(session, cache):
		yield session
		return
	
	# 重新登录，获取新的token和cookie
	base_url = 'http://106.15.79.229:3000'
	url = base_url + '/login/cellphone'
	phone = 15000840699
	password = 'hf15000840699'
	md5_password = get_md5_hash(password)
	params = {'phone': phone, 'md5_password': md5_password}
	
	try:
		res = session.get(url, params=params)
		res.raise_for_status()
	except RequestException as e:
		pytest.fail(f"请求登录接口失败: {e}")
	
	jsonpath_expression_token = parse('$.token')
	jsonpath_expression_cookie = parse('$.cookie')
	jsonpath_expression_uid = parse('$.account.id')
	match_token = jsonpath_expression_token.find(res.json())
	match_cookie = jsonpath_expression_cookie.find(res.json())
	match_uid = jsonpath_expression_uid.find(res.json())
	# 获取uid 写到extract.yaml文件
	if match_token and match_cookie and match_uid:
		data = {
			'uid': match_uid[0].value,
		}
		try:
			# 在写入之前清空文件
			utils.clear_file(os.path.join(os.getcwd(), 'extract.yaml'))
			# 将uid写到文件
			utils.write_file(os.path.join(os.getcwd(), 'extract.yaml'), data)
			logger.info(f"成功将 UID 写入文件: {data}")
		except Exception as e:
			logger.error(f"写入 UID 到文件失败: {e}")
		uid = match_uid[0].value
		token = match_token[0].value
		cookie = match_cookie[0].value
		session.cookies.set('Set-Cookie', cookie)
		session.headers['Authorization'] = f'Bearer {token}'
		# 将登录信息存入缓存（包括uid）
		cookies_list = [{'name': c.name, 'value': c.value, 'domain': c.domain, 'path': c.path} for c in session.cookies]
		cache.set("session_cookies", cookies_list)
		cache.set("session_token", token)
		cache.set("session_uid", uid)
	
	# print("New session created:")
	# print("New Cookies:", cookies_list)
	# print("New Token:", token)
	else:
		pytest.fail("无法从响应中找到token或cookie")
	
	yield session
