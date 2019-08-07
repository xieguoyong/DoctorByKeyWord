import xlrd
import os

excel_dir = r'E:\PycharmProjects\DoctorByKeyWord\dataEngine'


# 根据sheetname读取excel数据，并保存为list
def read_excel(excel_name, sheetname):
    excel_path = os.path.join(excel_dir, excel_name)
    file = xlrd.open_workbook(excel_path)
    # print(file.sheet_names())             # 打印sheet列表
    table = file.sheet_by_name(sheetname)
    rows = table.nrows          # 行数
    table_data = []
    # 将table中每行数据插入列表，并去掉第一行（即标题行）以及第三列为N的行 以及空行
    for i in range(rows):
        if i != 0 and table.cell(i, 2).value != 'N' and table.cell(i, 0).value != '':
            table_data.append(table.row_values(i))

    return table_data


# 根据excel表Test Steps标签中element字段 找到Element Loc标签中对应的元素
def get_element_loc(element):
    """
    :param element: 元素标志
    :return: 返回值从list转化为tuple，方便元素定位时直接以参数传入
    返回值格式如 ('xpath', "//*[@id='app']/div/div/div/div/div[3]/form/div[1]/div/div/input")
    """
    table_data = read_excel('data.xls', 'Element Loc')
    for data in table_data:
        if element in data:
            return tuple(data[1:3])


# 调试用
if __name__ == '__main__':
    excel_path = r"E:\PycharmProjects\DoctorByKeyWord\dataEngine\data.xls"
    sheet_name = 'Test Cases'
    print(read_excel(excel_path, sheet_name))

    get_element_loc('login_001')
