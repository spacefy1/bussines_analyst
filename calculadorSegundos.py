segundos = int(input("Por favor, entre com o número de segundos que deseja converter "))

dias = segundos // 86400
hora_restante_dia = segundos % 86400

horas = hora_restante_dia // 3600

segundosRestantes = hora_restante_dia % 3600

minutos = segundosRestantes // 60

segundosRestantes_final = segundosRestantes % 60

print(dias, "dias,", horas, "horas,", minutos, "minutos e", segundosRestantes_final, "segundos.")
