# 你是魔法学院的校长（恭喜你），要管理巫师（Wizard）报名参加魔法课程（Course）。
class Wizard:
    def __init__(self,name,level): # harry = Wizard("Harry", 2)
        self.name = name
        self.level = level
        self.courses = []# 课程列表

    def enroll(self,course): # harry.enroll(alchemy)
        course.add_student(self) # 嵌套使用类，由课程（等级）判断是否能报名

    def list_courses(self): # 打印某个巫师的课程表
        if self.courses: # 如果课程表不为空
            print(f"{self.name}当前课程为：")
            for course in self.courses:
                print(f"- {course.title}")
        else:
            print(f"{self.name}没有报名任何课程")

class Course:
    def __init__(self,title,required_level):
        self.title = title
        self.required_level = required_level
        self.enrolled_wizards = []

    # 要判断等级够不够
    # 将巫师加入课程（要判断等级够不够）
    def add_student(self,wizard): # 这里的这个self是Course（在Course类中）
        if wizard.level >= self.required_level:
            self.enrolled_wizards.append(wizard) # 把巫师的名字放到Courses的系统中
            wizard.courses.append(self) # 更新到Wizard中
            print(f"{wizard.name}成功报名{self.title}")
        else:
            print(f"{wizard.name}等级不足，无法报名{self.title}")
    def list_students(self):
        if self.enrolled_wizards:
            print(f"《{self.title}》这门课报名的巫师有：")
            for wizard in self.enrolled_wizards:
                print(f"- {wizard.name},等级{wizard.level}")
        else:
            print(f"《{self.title}》这门课还没有人报名")



# 交互
harry = Wizard("Harry", 2)
snape = Wizard("Snape", 10)

alchemy = Course("炼金术", 5)
herb = Course("草药学", 1)

harry.enroll(alchemy)    # 打印：等级不足，无法报名
harry.enroll(herb)       # 报名成功

harry.list_courses()     # 打印哈利当前的课程列表

