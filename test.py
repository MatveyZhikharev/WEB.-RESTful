from requests import get, post, delete

print(get('http://localhost:8080/api/v2/jobs').json())
print(get('http://localhost:8080/api/v2/jobs/3').json())
print(get('http://localhost:8080/api/v2/jobs/48').json())  # нет работы

print(post('http://localhost:8080/api/v2/jobs').json())  # нет словаря
print(post('http://localhost:8080/api/v2/jobs', json={'job': 'senior programmer'}).json())  # не все поля
print(post('http://localhost:8080/api/v2/jobs', json={'job': 'senior programmer', 'work_size': 10,
                                                      'team_leader': 1, 'collaborators': '4, 5',
                                                      'is_finished': True, 'category': 2}).json())

print(delete('http://localhost:8080/api/v2/jobs/999').json())  # id = 999 нет в базе