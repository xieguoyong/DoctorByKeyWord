import os
import unittest
from public import HTMLTestRunner, send_email

cur_path = os.path.dirname(os.path.realpath(__file__))


def add_case(case_name="testcase", rule="test_*.py"):
    case_path = os.path.join(cur_path, case_name)
    if not os.path.exists(case_path):os.mkdir(case_path)
    discover = unittest.defaultTestLoader.discover(case_path, pattern=rule, top_level_dir=None)
    # print(discover)
    return discover


def run_case(case, report_name="result"):
    report_dir = os.path.join(cur_path, report_name)
    if not os.path.exists(report_dir):os.mkdir(report_dir)
    report_path = os.path.join(report_dir, "result.html")

    fp = open(report_path, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"自动化测试报告", description=u"用例执行情况")
    runner.run(case)
    fp.close()


if __name__ == '__main__':
    all_case = add_case()
    # 运行用例
    run_case(all_case)
    send = send_email.sendemail()
    # 发送邮件
    send.send_mail()
