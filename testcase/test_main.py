import unittest
from public import HandData, log
from parameterized import parameterized
from keyword_action import KeywordAction
import ast
import traceback


class TestMain(unittest.TestCase):
    logger = log.Log()
    # 读取用例
    case_all = HandData.read_excel('data.xls', 'case data')
    logger.info("用例列表case_all: %s" % case_all)
    # print("case_all:", case_all)

    @classmethod
    def setUpClass(cls, logger=logger):
        # 读取测试步骤
        cls.test_steps = HandData.read_excel('data.xls', 'Test Steps')
        cls.logger = logger
        cls.logger.info("测试步骤test_steps: %s" % cls.test_steps)
        # print("test_steps:", cls.test_steps)
        # 创建KeywordAction对象
        cls.action = KeywordAction.Action()
        cls.logger.info("测试开始...")

    # 设定输出的用例报告中的用例名格式 (这里需要三个传参否则会报错,且第一个必须为test否则加载不到用例)
    def custom_name_func(testcase_func=None, param_num=None, param=None):
        return "%s_%s_%s_%s" % ('test', str(param.args[0]), str(param.args[1]), str(param.args[3]))

    # 参数化数据，将读取的用例参数化；testcase_func_name参数化用例名称
    @parameterized.expand(case_all, testcase_func_name=custom_name_func)
    def test_main(self, TCID, CaseId, Runmode, Summary, Input, Verify_Element, Verify_Type, ErrMsg):
        try:
            case_name = TCID + CaseId
            self.logger.info("开始用例<%s>的测试..." % case_name)

            input_list = ast.literal_eval(Input)       # 将读取到的Input1转化为list
            self.logger.info("输入信息列表input_list: %s" % input_list)
            index = 0

            for step in self.test_steps:
                if TCID == step[0]:
                    if step[3] == 'open_browser':
                        self.action.open_browser(step[4])
                    elif step[3] == 'navigate':
                        self.action.navigate(step[4])
                    elif step[3] == 'input':
                        loc = HandData.get_element_loc(step[4])
                        self.action.input(loc, input_list[index])       # 实现有多个input步骤时，逐一输入list数值
                        self.logger.info("input_list[index]: %s" % input_list[index])
                        index += 1
                    elif step[3] == 'click':
                        loc = HandData.get_element_loc(step[4])
                        self.action.click(loc)
                    elif step[3] == 'click_element':
                        loc = HandData.get_element_loc(step[4])
                        self.action.click_element(loc)
                    elif step[3] == 'verify':
                        loc = HandData.get_element_loc(Verify_Element)
                        self.action.verify(loc, Verify_Type, ErrMsg)
                    elif step[3] == 'close_browser':
                        self.action.close_browser()
        except Exception as e:
            self.logger.error(traceback.format_exc())
            # self.logger.error('traceback.print_exc(): %s,%s' % (traceback.print_exc(), e))
            self.assertTrue(0)  # 此处在用例抛出异常时加入断言，assertTrue(0)必定返回fasle,说明用例失败

    @classmethod
    def tearDownClass(cls):
        cls.logger.info("测试结束")
