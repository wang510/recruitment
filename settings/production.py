import os
from .base import *

# 从环境变量获取 SECRET_KEY，及其它敏感数据；
# 容器化的环境下，这些数据保存在专用的 secret 存储，或者 KMS 系统中
# 如 Kubernetes Secret中，云厂商的 KMS 服务，或者开源的 Vault 服务中

ALLOWED_HOSTS = ["127.0.0.1", "host.docker.internal", "*"]

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'w$46iie+a8-7f(13#i%v@pa@+fbm^t@fofizy1^m69r8(-h16o3s882')

DEBUG = False
INSTALLED_APPS += (
	# 'debug_toolbar', # and other apps for local development
)

INTERNAL_IPS = [
	# ...
	'127.0.0.1',
	# ...
]

## 如果仅使用数据库中的账号，以下 LDAP 配置可忽略
## 替换这里的配置为正确的域服务器配置，同时可能需要修改 base.py 中的 LDAP 服务器相关配置:
LDAP_AUTH_URL = os.environ.get('LDAP_AUTH_URL', 'ldap://localhost:389')
LDAP_AUTH_CONNECTION_USERNAME = os.environ.get('LDAP_AUTH_CONNECTION_USERNAME')
LDAP_AUTH_CONNECTION_PASSWORD = os.environ.get('LDAP_AUTH_CONNECTION_PASSWORD')

STATIC_URL = 'http://icdn.ihopeit.com/static/'
# STATIC_URL = '/static/'

DEFAULT_FILE_STORAGE = 'django_oss_storage.backends.OssMediaStorage'

# AliCloud access key ID
OSS_ACCESS_KEY_ID = os.environ.get('OSS_ACCESS_KEY_ID', '')
# AliCloud access key secret
OSS_ACCESS_KEY_SECRET = os.environ.get('OSS_ACCESS_KEY_SECRET', '')
# The name of the bucket to store files in
OSS_BUCKET_NAME = 'djangorecruit'

# The URL of AliCloud OSS endpoint
# Refer https://www.alibabacloud.com/help/zh/doc-detail/31837.htm for OSS Region & Endpoint
OSS_ENDPOINT = 'oss-cn-beijing.aliyuncs.com'

DINGTALK_WEB_HOOK_TOKEN = os.environ.get('DINGTALK_WEB_HOOK_TOKEN', '')
DINGTALK_WEB_HOOK = "https://oapi.dingtalk.com/robot/send?access_token=%s" % DINGTALK_WEB_HOOK_TOKEN

##########################