import random
import re

category = ['黑桃', '红桃', '梅花', '方块']
nums = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


# 牌堆
class Poker:
    def __init__(self):
        self.cards = []
        self.length = 0
        self.new_cards()

    # 新的一副牌
    def new_cards(self):
        self.cards = [f'{item}{i}' for item in category for i in nums]
        self.length = len(self.cards)
        random.shuffle(self.cards)  # 随机打乱

    # 发牌
    def pop(self):
        self.length -= 1
        card = self.cards.pop(random.randint(0, self.length))  # 随机出一张牌

        # 确保牌堆中始终有牌
        if self.is_empty():
            print('对不起，牌堆已空!\n正在重新洗牌。。。')
            self.new_cards()
            print('重新洗牌完毕，继续开始游戏')

        return card

    # 判断牌堆是否为空
    def is_empty(self):
        return self.length == 0

    # 剩下牌中牌值出现小于n的概率
    def get_probability(self, n):
        card_nums = [0] * 13
        for card in self.cards:
            card_nums[nums.index(re.sub('[^0-9JQKA]', '', card))] += 1

        res = 0
        for i in range(n):
            res += card_nums[i]

        return res / self.length


# 玩家
class Player:
    def __init__(self):
        self.cards = []
        self.score = 0
        self.points = 0

    def init(self):
        self.points = 0
        self.cards = []

    # 要牌
    def receive_card(self, *cards):
        for card in cards:
            self.cards.append(card)
        self.points = self.cal_score()

    # 计算点数
    def cal_score(self):
        score = 0
        count_of_A = 0
        # 先略过A计算点数
        for card in self.cards:
            t = re.sub('[^0-9JQKA]', '', card)
            if t in ['J', 'Q', 'K']:
                score += 10
            elif t == 'A':
                count_of_A += 1
            else:
                score += int(t)
        # 再加上A的点数
        for i in range(count_of_A):
            if score + 11 <= 21:
                score += 11
            else:
                score += 1
        return score


# 玩家要牌策略
def method_for_human(num, poker, human, computer):
    # 人工要牌
    if num == 0:
        while True:
            res = input('是否继续要牌？(y/n): ')
            if res in ['y', 'Y']:
                return True
            elif res in ['n', 'N']:
                return False
            else:
                print('输入错误，请重新输入')
    # 自动要牌
    elif num == 1:
        return True if poker.get_probability(5) > 0.4 else False
    # 其他策略
    else:
        if human.points == 9 and 2 <= computer.points <= 6:
            return True
        elif human.points == 10 and 2 <= computer.points <= 9:
            return True
        elif human.points == 11 and 2 <= computer.points <= 10:
            return True
        elif human.points == 12 and 2 <= computer.points <= 11:
            return True
        elif human.points < 17:
            return True

        return False


def main(poker: Poker, computer: Player, human: Player):
    while True:
        n = input('输入游戏回合数(q退出)：')
        if n in ['q', 'Q']:
            return
        else:
            try:
                n = int(n)
                break
            except ValueError as e:
                print('输入错误，请输入数字或q退出！')

    for i in range(1, n + 1):
        human.init()
        computer.init()
        print('\n{:*^30}'.format(f'第{i}轮游戏开始！'))

        flag = False  # 是否提前结束的标志
        human.receive_card(poker.pop(), poker.pop())
        computer.receive_card(poker.pop(), poker.pop())
        print(f'你得到的牌是: {human.cards[-2]}, {human.cards[-1]}, 点数为{human.points}')
        print(f'电脑得到的牌是: {computer.cards[-2]}, ?')
        print('-' * 20)
        if human.points == 21 == computer.points:
            print('太巧了，你和电脑的点数都为21点，平局！')
        elif human.points == 21:
            print('你当前点数刚好为21点, 恭喜你，你赢了')
            human.score += 1
        elif computer.points == 21:
            print('电脑当前点数刚好为21点, 很遗憾，你输了')
            computer.score += 1
        else:
            # 玩家要牌
            print('-->轮到玩家要牌：')
            while True:
                if method_for_human(2, poker, human, computer):
                    human.receive_card(poker.pop())
                    print(f'你得到了一张{human.cards[-1]}, 当前牌堆是{human.cards}, 当前点数为 {human.points}')
                    if human.points > 21:
                        computer.score += 1
                        flag = True
                        print(f'你当前点数为{human.points} > 21, 很遗憾，你输了')
                        print(f'电脑手中的牌是： {computer.cards}, 点数为{computer.points}')
                        break
                else:
                    break

            # 电脑要牌
            if not flag:
                print('\n-->轮到电脑要牌：')
                while human.points > computer.points:
                    computer.receive_card(poker.pop())
                    print(f'电脑得到了一张{computer.cards[-1]}, 当前牌堆是{computer.cards}, 当前点数为 {computer.points}')
                    if computer.points > 21:
                        human.score += 1
                        flag = True
                        print(f'电脑手中的牌是: {computer.cards}')
                        print(f'电脑当前点数为 {computer.points} > 21, 恭喜你，你赢了')

                        break
            # 结算
            if not flag:
                print('电脑要牌结束！')
                res = human.points > computer.points
                if res:
                    human.score += 1
                    print('恭喜你，你赢了！')
                else:
                    computer.score += 1
                    print('很遗憾，你输了！')

                print(f'你的牌为{human.cards}, 点数为{human.points}')
                print(f'电脑的牌为{computer.cards}, 点数为{computer.points}')

        print(f'本轮结束，当前比分是(电脑 vs 玩家): {computer.score} : {human.score}\n')

    print('\n{:*^30}'.format(f'游戏结束！'))
    print(f'最后的比分是(电脑 vs 玩家)：{computer.score} : {human.score}')
    print('{} 胜！'.format('电脑' if computer.score > human.score else '玩家'))


if __name__ == '__main__':
    poker = Poker()
    computer = Player()
    human = Player()
    main(poker, computer, human)
