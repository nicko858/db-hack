
import random

from datacenter.models import (Chastisement, Commendation, Lesson, Mark,
                               Schoolkid)


def get_schoolkid(schoolkid_name):
    try:
        return Schoolkid.objects.get(full_name=schoolkid_name)
    except Schoolkid.DoesNotExist:
        print('Нет ученика с именем - {} !'.format(schoolkid_name))
        print('Проверьте, что указали полное ФИО!')


def fix_marks(schoolkid):
    bad_points = [2, 3]
    good_point = 5
    bad_marks = Mark.objects.filter(schoolkid=schoolkid, points__in=bad_points)
    for mark in bad_marks:
        mark.points = good_point
        mark.save()


def remove_chastisements(schoolkid):
    for chastisement in Chastisement.objects.filter(schoolkid=schoolkid):
        chastisement.delete()


def create_commendation(subject, schoolkid):
    year_of_study, group_letter = 6, 'А'
    commendations_text = [
        'Молодец!',
        'Отлично!',
        'Хорошо!',
        'Гораздо лучше, чем я ожидал!',
        'Ты меня приятно удивил!',
        'Великолепно!',
        'Прекрасно!',
        'Ты меня очень обрадовал!',
        'Именно этого я давно ждал от тебя!',
        'Сказано здорово – просто и ясно!',
        'Ты, как всегда, точен!',
        'Очень хороший ответ!',
        'Талантливо!',
        'Ты сегодня прыгнул выше головы!',
        'Я поражен!',
        'Уже существенно лучше!',
        'Потрясающе!',
        'Замечательно!',
        'Прекрасное начало!',
        'Так держать!',
        'Ты на верном пути!',
        'Здорово!',
        'Это как раз то, что нужно!',
        'Я тобой горжусь!',
        'С каждым разом у тебя получается всё лучше!',
        'Мы с тобой не зря поработали!',
        'Я вижу, как ты стараешься!',
        'Ты растешь над собой!',
        'Ты многое сделал, я это вижу!',
        'Теперь у тебя точно все получится!',
    ]
    commendation = random.choice(commendations_text)
    lessons = Lesson.objects.filter(
        year_of_study=year_of_study,
        group_letter=group_letter,
        subject__title=subject,
        )
    lesson = random.choice(lessons)
    Commendation.objects.create(
        schoolkid=schoolkid,
        subject=lesson.subject,
        teacher=lesson.teacher,
        created=lesson.date,
        text=commendation,
        )
