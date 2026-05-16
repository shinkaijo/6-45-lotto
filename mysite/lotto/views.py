from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from .models import Ticket, Draw
import random

def buy_auto(request):
    # 1부터 45까지의 숫자 중 6개를 중복 없이 무작위로 선택합니다.
    lotto_numbers = random.sample(range(1, 46), 6)
    lotto_numbers.sort() # 번호를 오름차순으로 정렬합니다.

    # 생성된 번호를 Ticket 모델에 저장합니다.
    # 인덱스는 0부터 시작하며, 총 6개(0~5)를 사용해야 합니다.
    ticket = Ticket(
        num1=lotto_numbers[0],
        num2=lotto_numbers[1],
        num3=lotto_numbers[2],
        num4=lotto_numbers[3],
        num5=lotto_numbers[4],
        num6=lotto_numbers[5]
    )
    ticket.save() # 데이터베이스(Model)에 반영합니다. [10]

    # 구매가 완료되면 결과를 보여줄 화면(Template)으로 데이터를 보냅니다. [10]
    return render(request, 'lotto/buy_result.html', {'numbers': lotto_numbers})

def home(request):
    return render(request, 'lotto/home.html')

def buy_manual(request):

    if request.method == 'POST':

        numbers = [
            int(request.POST['num1']),
            int(request.POST['num2']),
            int(request.POST['num3']),
            int(request.POST['num4']),
            int(request.POST['num5']),
            int(request.POST['num6']),
        ]

        numbers.sort()

        ticket = Ticket(
            num1=numbers[0],
            num2=numbers[1],
            num3=numbers[2],
            num4=numbers[3],
            num5=numbers[4],
            num6=numbers[5],
        )

        ticket.save()

        return render(request, 'lotto/buy_result.html', {
            'numbers': numbers
        })

    return render(request, 'lotto/buy_manual.html')

from .models import Ticket, WinningNumber

def check_result(request):
    tickets = Ticket.objects.all().order_by('-created_at')
    winning = Draw.objects.order_by('-round_number').first()

    results = []

    if winning:
        winning_numbers = set(winning.get_numbers())
        bonus = winning.bonus_num

        for ticket in tickets:
            ticket_numbers = set(ticket.get_numbers())
            match_count = len(ticket_numbers & winning_numbers)
            bonus_match = bonus in ticket_numbers

            if match_count == 6:
                rank = '1등'
            elif match_count == 5 and bonus_match:
                rank = '2등'
            elif match_count == 5:
                rank = '3등'
            elif match_count == 4:
                rank = '4등'
            elif match_count == 3:
                rank = '5등'
            else:
                rank = '낙첨'

            results.append({
                'ticket': ticket,
                'numbers': ticket.get_numbers(),
                'match_count': match_count,
                'bonus_match': bonus_match,
                'rank': rank,
            })

    return render(request, 'lotto/check_result.html', {
        'winning': winning,
        'results': results,
    })
@staff_member_required
def admin_sales(request):
    tickets = Ticket.objects.all().order_by('-created_at')

    return render(request, 'lotto/admin_sales.html', {
        'tickets': tickets
    })


@staff_member_required
def admin_draw(request):
    if request.method == 'POST':
        numbers = random.sample(range(1, 46), 7)
        win_numbers = sorted(numbers[:6])
        bonus_num = numbers[6]

        last_draw = Draw.objects.order_by('-round_number').first()

        if last_draw:
            next_round = last_draw.round_number + 1
        else:
            next_round = 1

        Draw.objects.create(
            round_number=next_round,
            win_num1=win_numbers[0],
            win_num2=win_numbers[1],
            win_num3=win_numbers[2],
            win_num4=win_numbers[3],
            win_num5=win_numbers[4],
            win_num6=win_numbers[5],
            bonus_num=bonus_num
        )

        return redirect('admin_draw_results')

    return render(request, 'lotto/admin_draw.html')


@staff_member_required
def admin_draw_results(request):
    draws = Draw.objects.all().order_by('-round_number')

    return render(request, 'lotto/admin_draw_results.html', {
        'draws': draws
    })