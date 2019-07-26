import unittest
from public import HandData, ElementLocate
from parameterized import parameterized
from selenium import webdriver
import time
from keyword_action import KeywordAction


class TestMain(unittest.TestCase):
    def setUp(self):
        # self.drself步骤
        self.test_steps = HandData.read_excel('data.xls', 'Test Steps')
        print(self.test_steps)
        # 创建KeywordAction对象
        self.action = KeywordAction.Action()

    # 读取用例
    case_all = HandData.read_excel('data.xls', 'case data')
    print(case_all)

    # 设定输出的用例报告中的用例名格式 (这里需要三个传参否则会报错,且第一个必须为test否则加载不到用例)
    def custom_name_func(testcase_func=None, param_num=None, param=None):
        return "%s_%s_%s_%s" % ('test', str(param.args[0]), str(param.args[1]), str(param.args[3]))

    # 参数化数据，将读取的用例参数化；testcase_func_name参数化用例名称
    @parameterized.expand(case_all, testcase_func_name=custom_name_func)
    def test_main(self, TCID, CaseId, Runmode, Summary, Input1, Input2, Input3, Input4, Input5, ErrMsg, Result):
        for step in self.test_steps:
            if TCID == step[0]:
                if step[3] == 'open_browser':
                    self.action.open_browser(step[4])
                elif step[3] == 'navigate':
                    self.action.navigate(step[4])
                elif step[3] == 'input':
                    loc = HandData.get_element_loc(step[4])
                    self.action.input(loc, Input1)
                elif step[3] == 'click':
                    self.action.click()
                elif step[3] == 'verify':
                    self.action.verify()
                elif step[3] == 'close_browser':
                    self.action.close_browser()
                elif step[3] == 'click_element':
                    self.action.click_element()

    def tearDown(self):
        print("end")
