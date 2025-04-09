# 模拟巫师攻击怪物，每人有 HP 和 MP，释放技能会耗魔，怪物会掉血，代码会爆炸（可能）
class Wizard:
    def __init__(self,name):
        self.name = name
        self.hp = 100
        self.mp = 50
    def cast_spell(self,spell_name,target):
        if spell_name == "火球术":
            if self.mp>=10:
                self.mp-=10
                target.take_damage(30)
                print(f"{self.name}对{target.name}使用火球术，造成30点伤害！")
            else:
                print(f"{self.name}的魔法值不够使用{spell_name}")
        if spell_name == "冰冻术":
            if self.mp>=15:
                self.mp-=15
                target.take_damage(20)
                target.frozen=True
                print(f"{self.name}对{target.name}使用冰冻术，造成15点伤害！")
            else:
                print(f"{self.name}的魔法值不够使用{spell_name}")

    def status(self):
         print(f"{self.name}的生命值为:{self.hp}，魔法值为:{self.mp}")

class Monster:
    def __init__(self,name,frozen=False):
        self.name = name
        self.hp = 80
        self.frozen = frozen
    def take_damage(self,amount):
        self.hp -= amount
        if self.hp <= 0:
            self.hp = 0
            print(f"{self.name}生命值耗尽，game over!")

    def status(self):
        if self.frozen and self.hp >0:
            print(f"{self.name}正在被冻结，生命值为{self.hp}")
        elif not self.frozen and self.hp >0:
            print(f"{self.name}未被冻结，生命值剩余{self.hp}")

# 交互
harry = Wizard("Harry")
slime = Monster("史莱姆")

harry.cast_spell("火球术", slime)
harry.status()
slime.status()

harry.cast_spell("冰冻术", slime)
harry.status()
slime.status()

harry.cast_spell("冰冻术", slime)
harry.cast_spell("冰冻术", slime) # 魔法值不够
