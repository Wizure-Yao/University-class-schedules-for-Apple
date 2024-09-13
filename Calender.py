from datetime import datetime, timedelta


def parse_input(input_string):
    # 拆分输入字符串，以逗号为分隔符
    parts = input_string.split(',')
    result = []

    for part in parts:
        if '-' in part:
            # 处理范围情况
            start, end = part.split('-')
            # 将范围内的数字添加到结果列表
            result.extend(range(int(start), int(end) + 1))

        else:
            # 处理单个数字
            result.append(int(part))

    return result


first_day = datetime.strptime(str(input('输入第一周的第一天(yyyy-mm-dd)：')), '%Y-%m-%d')
task_name = str(input('输入日程名称：'))
task_date = int(input('输入日程星期：'))
task_weeks = parse_input(str(input('输入日程重复周期(1,3-5,9)：')))
task_start_time = str(input('输入日程开始时间(hh:mm)：'))
task_end_time = str(input('输入日程结束时间(hh:mm)：'))

# This file will be used to create a calendar for the user to use
with open('C:\\Users\\13409\\Desktop\\Calendar.txt', 'a') as file:
    for task_week in task_weeks:
        # 计算日程日期
        task_day = first_day + timedelta(weeks=task_week - 1) + timedelta(days=task_date - first_day.weekday() - 1)
        # 将日程写入文件
        file.write(f'{task_name},'
                   f'{task_day.strftime("%Y-%m-%d")} {task_start_time},'
                   f'{task_day.strftime("%Y-%m-%d")} {task_end_time}\n')
