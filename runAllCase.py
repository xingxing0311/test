# coding:utf-8
import unittest
from zhangxun.common import HTMLTestRunner
import os

case_path=os.path.join(os.getcwd(),"report")
report_path=case_path+"\\report.html"

discover=unittest.defaultTestLoader.discover(start_dir=case_path,pattern='test*.py')

fp=open(report_path,'wb')


runner=HTMLTestRunner.HTMLTestRunner(stream=fp)
runner.run(discover)
fp.close()