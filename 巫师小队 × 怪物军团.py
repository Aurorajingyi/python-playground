# 实现一个包含巫师小队、怪物队列、技能概率、回魔机制的回合制战斗系统
import random

# ====================
# 🧙 巫师类定义 #win+. 输入emoji（wins）
# ====================
class Wizard:
    def __init__(self, name):
        self.name = name
        self.hp = 100    # 初始生命值
        self.mp = 50     # 初始魔法值

    def cast_spell(self, spell_name, target):
        # 释放火球术
        if spell_name == "fireball":
            if self.mp >= 10:
                self.mp -= 10
                target.take_damage(30)
                print(f"{self.name}对{target.name}发起{spell_name}攻击，伤害值为30")
            else:
                print(f"{self.name}的魔力值不足以发起{spell_name}攻击")

        # 释放冰冻术
        elif spell_name == "ice":
            if target.frozen:
                target.unfreeze()  # 如果目标已经被冻结，先解冻
            elif self.mp >= 15:
                self.mp -= 15
                target.take_damage(20)
                target.frozen = True
                print(f"刚刚，{self.name}对{target.name}发起了{spell_name}攻击，冻结一回合")
            else:
                print(f"{self.name}的魔力值不足以发起{spell_name}攻击")

    def recover(self):
        # 回魔，最多恢复到50
        if self.mp < 50:
            self.mp += 10
            if self.mp > 50:
                self.mp = 50
            print(f"{self.name}的魔力值恢复10点，现在魔力值为{self.mp}")

    def is_alive(self):
        return self.hp > 0

    def status(self):
        print(f"{self.name}当前的Hp={self.hp}, 当前的Mp={self.mp}")

# ====================
# 👾 怪物类定义
# ====================
class Monster:
    def __init__(self, name):
        self.name = name
        self.hp = 80
        self.frozen = False  # 初始未被冻结

    def take_damage(self, amount):
        # 10% 概率闪避技能
        if random.random() < 0.1:
            print(f"{self.name}成功躲避攻击，技能Miss了！")
        else:
            self.hp -= amount
            if self.hp < 0:
                self.hp = 0
            print(f"{self.name}受到{amount}点伤害，当前HP为{self.hp}")
            if self.hp == 0:
                print(f"{self.name}倒下了！")

    def unfreeze(self):
        self.frozen = False
        print(f"{self.name}使用解冻技能")

    def is_alive(self):
        return self.hp > 0

    def status(self):
        print(f"{self.name}当前的Hp={self.hp}")

    def attack(self, target):
        # 怪物攻击玩家，若被冻结则跳过
        if self.frozen:
            print(f"{self.name}被冻结，无法攻击")
            return
        damage = random.randint(5, 10)  # 造成随机伤害
        target.hp -= damage
        if target.hp < 0:
            target.hp = 0
        print(f"{self.name}反击造成{damage}点伤害，{target.name}剩余HP为{target.hp}")
        if target.hp <= 0:
            print(f"{target.name}被击倒！")

# ====================
# ⚔️ 主战斗系统
# ====================
# 巫师小队 & 怪物军团初始化
party = [Wizard("Harry"), Wizard("Snape")]
monsters = [Monster("哥布林"), Monster("狼人")]

# 主战斗循环：只要有巫师活着 且 有怪物活着
while any(wizard.is_alive() for wizard in party) and any(monster.is_alive() for monster in monsters):
    for wizard in party:
        if not wizard.is_alive():  # 巫师已死亡则跳过
            continue

        # 找到第一个存活的怪物作为当前目标
        current_monster = None
        for m in monsters:
            if m.is_alive():
                current_monster = m
                break
        if not current_monster:
            print("所有怪物已经被消灭，巫师团胜利！")
            break

        # 展示当前状态
        print(f"\n=== {wizard.name} 的回合 ===")
        wizard.status()
        current_monster.status()

        # 自动技能选择策略：
        # 冰冻优先，火球其次，不行就回魔
        if wizard.mp >= 15 and not current_monster.frozen:
            spell = "ice"
        elif wizard.mp >= 10:
            spell = "fireball"
        else:
            spell = "recover"

        # 执行操作
        if spell in ["fireball", "ice"]:
            wizard.cast_spell(spell, current_monster)
            # 怪物存活才能反击
            if current_monster.is_alive():
                current_monster.attack(wizard)
        elif spell == "recover":
            wizard.recover()

# ====================
# 💥 战斗结果
# ====================
if any(w.is_alive() for w in party):
    print("\n🎉 战争胜利，怪物军团全军覆灭！")
else:
    print("\n💀 巫师小队全灭")
