# coding=gbk
import os, time, pytest,allure

if __name__ == '__main__':

    # ��ȡ��ǰ������ʱ������Ϊ���Ա����ļ��еĺ�׺
    currentTime = time.strftime('%Y-%m-%d-%H-%M-%S')
    # �洢allure��¼��������־
    os.system(r'copy environment.properties D:/Pycharm/UiYunDaiZhang/UI2/class_pytest_webdriver�ĸ���/Users/shs/class_pytest_webdriver/Allure-results')

    # # ����test_caseĿ¼��������test��ͷ���ļ�������������
    # pytest.main(
    #     ['-s', 'D:/Pycharm/UiYunDaiZhang/UI2/class_pytest_webdriver�ĸ���/test_case/', '--alluredir', './Allure-results','--clean-alluredir',
    #      '-W','ignore:Module already imported:pytest.PytestWarning'])


    # ���л�������ģ�����������
    # pytest.main(
    #     ['-s', 'D:/Pycharm/UiYunDaiZhang/UI2/class_pytest_webdriver�ĸ���/test_case/test_case_basic', '--alluredir', './Allure-results','--clean-alluredir',
    #      '-W', 'ignore:Module already imported:pytest.PytestWarning'])

    # ���л�������-��������ģ�����������
    pytest.main(
        ['-s', 'D:/Pycharm/UiYunDaiZhang/UI2/class_pytest_webdriver�ĸ���/test_case/test_case_basic/test_case_basic_basesetting', '--alluredir', './Allure-results','--clean-alluredir',
         '-W', 'ignore:Module already imported:pytest.PytestWarning'])

    # # ���л�������-����۸�����ģ�����������
    # pytest.main(
    #     ['-s',
    #      'D:/Pycharm/UiYunDaiZhang/UI2/class_pytest_webdriver�ĸ���/test_case/test_case_basic/test_case_basic_inventorypricesetting',
    #      '--alluredir', './Allure-results', '--clean-alluredir',
    #      '-W', 'ignore:Module already imported:pytest.PytestWarning'])
    #

    # # #���л�������-�ͻ�ģ�����������
    # pytest.main(
    #     ['-s', 'D:/Pycharm/UiYunDaiZhang/UI2/class_pytest_webdriver�ĸ���/test_case/test_case_basic/test_case_basic_customer.py',
    #      '--alluredir', './Allure-results','--clean-alluredir',
    #      '-W','ignore:Module already imported:pytest.PytestWarning'])


    # # ���л�������-��Ӧ��ģ�����������
    # pytest.main(
    #     ['-s',
    #      'D:/Pycharm/UiYunDaiZhang/UI2/class_pytest_webdriver�ĸ���/test_case/test_case_basic/test_case_basic_supplier.py',
    #      '--alluredir', './Allure-results', '--clean-alluredir',
    #      '-W', 'ignore:Module already imported:pytest.PytestWarning'])



    # ���ɲ��Ա��棬�ҵ��������� ���ɲ��Ա���
    os.system('allure serve ./Allure-results -o ./reports')
    # ���ɲ��Ա��棬�ҵ��������� ���ɲ��Ա��棬�����ļ��к�׺�ϼ���������ʱ����
    os.system(f'allure generate ./Allure-results -o ./Allure-report{currentTime}')
    currentTime1 = time.strftime('%Y-%m-%d-%H-%M-%S')
    print('��ʼʱ�䣺'+currentTime)
    print('����ʱ�䣺' + currentTime1)
    # os.mkdir(path)  # ����pathָ����Ŀ¼���ò�������ʡ��
    # os.rmdir(path)  # ɾ��pathָ����Ŀ¼���ò�������ʡ��
    # os.listdir(path)  # �г�pathĿ¼�����е��ļ���Ŀ¼��
    # os.remove(path)  # ɾ��pathָ�����ļ����ò�������ʡ��
    # os.path.isfile(path)  # �ж�·���Ƿ�Ϊ�ļ�
    # os.path.isdir(path)  # �ж�·���Ƿ�ΪĿ¼
    # os.path.join(path1[, path2[,]])  # ��Ŀ¼���ļ����ϳ�һ��·��

