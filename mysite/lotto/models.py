from django.db import models

# Create your models here.
class Ticket(models.Model):

    num1 = models.IntegerField()
    num2 = models.IntegerField()
    num3 = models.IntegerField()
    num4 = models.IntegerField()
    num5 = models.IntegerField()
    num6 = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    def get_numbers(self):
        return [
            self.num1,
            self.num2,
            self.num3,
            self.num4,
            self.num5,
            self.num6,
        ]

    def __str__(self):
        return (
            f"{self.num1}, {self.num2}, {self.num3}, "
            f"{self.num4}, {self.num5}, {self.num6}"
        )
    
    
    
class Draw(models.Model):

    # 회차 번호
    round_number = models.IntegerField(unique=True)

    # 당첨 번호
    win_num1 = models.IntegerField()
    win_num2 = models.IntegerField()
    win_num3 = models.IntegerField()
    win_num4 = models.IntegerField()
    win_num5 = models.IntegerField()
    win_num6 = models.IntegerField()

    # 보너스 번호
    bonus_num = models.IntegerField(default=0)

    # 추첨 날짜
    draw_date = models.DateTimeField(auto_now_add=True)

    def get_numbers(self):
        return [
            self.win_num1,
            self.win_num2,
            self.win_num3,
            self.win_num4,
            self.win_num5,
            self.win_num6,
        ]

    def __str__(self):
        return (
            f"{self.round_number}회차 | "
            f"{self.win_num1}, {self.win_num2}, "
            f"{self.win_num3}, {self.win_num4}, "
            f"{self.win_num5}, {self.win_num6} "
            f"+ Bonus {self.bonus_num}"
        )
class WinningNumber(models.Model):
    round_number = models.IntegerField(default=1)

    num1 = models.IntegerField()
    num2 = models.IntegerField()
    num3 = models.IntegerField()
    num4 = models.IntegerField()
    num5 = models.IntegerField()
    num6 = models.IntegerField()

    bonus = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    def numbers(self):
        return [self.num1, self.num2, self.num3, self.num4, self.num5, self.num6]