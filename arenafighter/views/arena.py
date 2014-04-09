from django.shortcuts import render, redirect
from arenafighter.models.character import Character
from arenafighter.models.enemy import Enemy, generate_enemy
from arenafighter.models.inventory import Potion
from arenafighter.forms import ContinueFightForm, GetItemForm, EnemyLookupForm

def use_potion(request):
    if request.POST.get('item_id'):
        form = GetItemForm(request.POST)
        if form.is_valid():
            enemy = None
            if request.POST.get('enemy_id'):
                enemy_form = EnemyLookupForm(request.POST)
                print enemy_form
                if enemy_form.is_valid():
                    print enemy_form
                    enemy = Enemy.objects.get(id=enemy_form.cleaned_data['enemy_id'])
            potion = Potion.objects.get(id=form.cleaned_data['item_id'])
            character = Character.objects.get(id=request.user.profile.current_character_id)
            character.use_health_potion(potion)
            if character.dead:
                character.dead = False
                character.current_hp = character.hpmax
                character.save()
            message = "Ya been patched up. Now go get 'em, mate!"
            context = {'enemy': enemy,
                       'message': message,
                       }
            if enemy:
                context['enemy_id'] = enemy.id

            if request.POST.get('enemy_id'):
                return render(request, 'fight_round.html', context)
            else:
                return redirect('player_info', character.id)

def attack(request):
    if request.POST:
        form = EnemyLookupForm(request.POST)
        if form.is_valid():
            enemy = Enemy.objects.get(id=form.cleaned_data['enemy_id'])
            character = Character.objects.get(id=request.user.profile.current_character_id)
            char_initiative = character.initiative_roll()
            enemy_initiative = enemy.initiative_roll()
            if char_initiative >= enemy_initiative:
                character.attack(enemy)
                enemy.attack(character)
            else:
                enemy.attack(character)
                character.attack(enemy)
            message = death_check(character, enemy)
            context = {'enemy': enemy,
                       'message': message,
                       'enemy_id': enemy.id,
                       }
            if character.dead:
                return redirect('player_info', character.id)
            elif enemy.dead:
                return render(request, 'fight.html', context)

    return render(request, 'fight_round.html', context)


def fight(request):
    if request.POST.get('enemy_id'):
        form = ContinueFightForm(request.POST)
        if form.is_valid:
            if request.POST.get('enemy_id'):
                enemy = Enemy.objects.get(id=form.cleaned_data['enemy_id'])
    else:
        enemy = generate_enemy('weak')


    character = Character.objects.get(id=request.user.profile.current_character_id)
    context = {'enemy': enemy,
               'character': character,
               }
    return render(request, 'fight_round.html', context)


def check_for_levelup(character):
    if character.xp >= character.next_levelup:
        character.level += 1
        character.hpmax += int(character.hpmax*.15)
        character.next_levelup = int(character.next_levelup*.2 + character.next_levelup)
        character.xp = 0
        character.save()
        return character
    else:
        return character


def death_check(character, enemy):
    if character.current_hp <= 0:
        character.dead = True
        character.fights_lost += 1
        character.save()
        message = "Ouch, son. Looks like that fella did a number on you. You'll need to get some healin' before you come back."
    elif enemy.current_hp <= 0:
        enemy.dead = True
        character.xp += enemy.xp_value
        character.gold += enemy.gold
        character.renown += enemy.renown_value
        check_for_levelup(character)
        character.fights_won += 1
        character.save()
        enemy.delete()
        message = "Nice fightin' there, fella! Took care of that bout nice and clean-like."
    else:
        message = "Aye, keep at it!! Fight another round ??"
    return message







# This defines an enemy strength definition where the key is the relative strength of the enemy
# and the value is a dict of attributes for that enemy, where the dict key corresponds to an attribute
# of Enemy(), making it easy to create random Enemy objects based on this dict



