name = input()
global_init(name)
session = create_session()
for job in session.query(Jobs).filter(Jobs.work_size < 20, Jobs.is_finished == 0):
    print("<Job>", job.job)