# 你是魔法学院的校长（恭喜你），要管理巫师（Wizard）报名参加魔法课程（Course）。
class Wizard:
    def __init__(self,name,level):
        self.name=name
        self.level=level
        self.courses=[]
    def enroll(self,course):
        course.add_student(self) # 传进wizard，判断是否能add
    """
    你是一个 巫师对象 wizard，你说：“我要报名 course 这门课。”
    所以你就调用了：这门课程的 .add_student() 方法
    self  是 Wizard 对象本体（你自己）
    你传自己进去，交给课程来判断你能不能报名
    """
    def list_courses(self): # 打印当前报名的课程名
        if self.courses:
            print(f"{self.name}的课程名单：")
            for course in self.courses:
                print(f"- 《{course.title}》")
        else:
            print(f"{self.name}当前还没有选课")

class Course:
    def __init__(self,title,required_level):
        self.title=title
        self.required_level=required_level
        self.enrolled_wizards=[]
    def add_student(self,wizard):
        """
        你现在变成了课程 course 视角
        它收到一个 wizard（你传进去的那个自己）
        然后它检查：这个巫师 wizard.level >= self.required_level
        """
        if wizard.level>=self.required_level:
            wizard.courses.append(self)
            self.enrolled_wizards.append(wizard)
            print(f"{wizard.name}成功报名了{self.title}")
        else:
            print(f"{wizard.name}你的等级{wizard.level}不够选{self.title}")
    # 打印选了某门课的学生
    def list_students(self):
        if self.enrolled_wizards:
            print(f"选中{self.title}这门课的学生名单是：")
            for wizard in self.enrolled_wizards:
                print(f"- {wizard.name}")
        else:
            print(f"当前{self.title}这门课还没有学生选")

# 交互
harry = Wizard("Harry", 2)
snape = Wizard("Snape", 10)

alchemy = Course("炼金术", 5)
herb = Course("草药学", 1)

harry.enroll(alchemy)    # 打印：等级不足，无法报名
harry.enroll(herb)       # 报名成功
snape.enroll(alchemy)    # 报名成功

herb.list_students()     # 草药学名单
harry.list_courses()     # 哈利的课程列表

