import unittest
from flask import current_app
from app import create_app, db


class BasicsTestCase(unittest.TestCase):
    # 测试开始前,初始化环境
    def setUp(self):
        self.app = create_app('testing')  # 创建测试app
        self.app_context = self.app.app_context()
        self.app_context.push()  # 激活上下文
        db.create_all()  # 创建数据库

    # 测试结束后,移除所有改变
    def tearDown(self):
        db.session.remove()
        db.drop_all()  # 移除数据库
        self.app_context.pop()  # 关闭上下文

    def test_app_exists(self):
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])
