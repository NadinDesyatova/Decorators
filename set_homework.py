# Применение логгера к приложению из домашнего задания по теме "Коллекции данных. Множества".
import os
from logger_2 import logger


def calc_namecode(name):
	letters = ["", "А", "Б", "В", "Г", "Д", "Е", "Ё", "Ж", "З", "И", "Й", "К",
               "Л", "М", "Н", "О", "П", "Р", "С", "Т", "У", "Ф", "Х", "Ц", "Ч",
               "Ш", "Щ", "Ъ", "Ы", "Ь", "Э", "Ю", "Я"]

	name = name.upper()
	code = 0
	for letter in name:
		try:
			ltr_code = letters.index(letter) % 9
		except:
			continue
		if ltr_code == 0:
			ltr_code = 9
		code += ltr_code

	while code > 9:
		curr = code // 10 + code % 10
		code = curr

	return code


if __name__ == '__main__':
	path = 'set_hm.log'

	if os.path.exists(path):
		os.remove(path)

	@logger(path)
	def get_namecodes_information(mentors, codes_info):
		all_list = []
		[all_list.extend(x) for x in mentors]
		# Отделить имя от фамилии
		all_names_list = [x.split(" ")[0].strip() for x in all_list]
		# Убрать дубли при помощи множеств
		all_names_set = set(all_names_list)

		names_codes = [[] for n in range(10)]

		for name in all_names_set:
			code = calc_namecode(name)
			names_codes[code].append(name)

		namecodes_information = []

		for id, _ in enumerate(names_codes):
			if id == 0:
				continue
			# Сортируем имена по алфавиту
			all_names_sorted = sorted(list(names_codes[id]))
			namecodes_information.append(
				f"{codes_info[id]}. Этому коду соответствуют: {', '.join(all_names_sorted)}"
			)

		return namecodes_information

	current_mentors = [
		["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев",
		 "Александр Бардин", "Александр Иванов"],
		["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев",
		 "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев"],
		["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский",
		 "Александр Ульянцев", "Роман Гордиенко"],
		["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин",
		 "Александр Шлейко", "Алена Батицкая"]
	]

	current_codes_info = [
		"",
		"1 — число цели, которая проявляется в форме агрессивности и амбиций",
		"2 — число равновесия и контраста одновременно, поддерживает равновесие, смешивая позитивные и негативные качества",
		"3 — неустойчивость, объединяет талант и весёлость, символ приспосабливаемости",
		"4 — означает устойчивость и прочность",
		"5 — символизирует риск, свободу и душевное беспокойство, которое толкает человека к путешествиям и новому опыту",
		"6 — символ надёжности. Идеальное число, которое делится как на чётное, так и на нечётное, объединяя элементы каждого",
		"7 — символизирует тайну, а также изучение и знание как путь исследования неизвестного и невидимого",
		"8 — число материального успеха, означает надёжность, доведённую до совершенства, символ всеобщего успеха",
		"9 — указывает на сильную личность с потенциальным интеллектом, способную к высокому развитию"
	]

	get_namecodes_information(current_mentors, current_codes_info)