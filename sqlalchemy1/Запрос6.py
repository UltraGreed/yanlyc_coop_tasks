name = input()
global_init(name)
session = create_session()
biggest = 0
teams = set()
for job in session.query(Jobs):
    length = len(job.collaborators.split())
    if length >= biggest:
        biggest = length

for job in session.query(Jobs):
    length = len(job.collaborators.split())
    if length == biggest:
        teams.add(job.collaborators)
leaders = list()
for job in session.query(Jobs).filter(Jobs.collaborators.in_(teams)):
    user = session.query(User).filter(User.id == job.team_leader).first()
    full_name = f'{user.name} {user.surname}'
    if full_name not in leaders:
        leaders.append(full_name)
print(*leaders, sep='\n')