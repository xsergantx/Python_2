#%
print( "В команде Мастера кода участников: %(team1_num)s" % {'team1_num': 5})
print( "Итого сегодня в командах участников: %(team1_num)s и %(team2_num)s !"% {'team1_num': 5,'team2_num': 6 })

# format()
print( "Команда Волшебники данных решила задач: {score_2} !".format(score_2=42))
print( "Волшебники данных решили задачи за {team1_time} c!".format(team1_time=18015.2))

#f-строк
score_1 = 40
score_2 = 42
challenge_result = 'Победа команды Волшебники данных!'
tasks_total = score_1 + score_2
time_avg = 45.2

print (f'Команды решили {score_1} и {score_2} задач.')
print (f'Результат битвы: {challenge_result} ')
print (f'Сегодня было решено {tasks_total} задач, в среднем по 350.4 секунды на задачу!')