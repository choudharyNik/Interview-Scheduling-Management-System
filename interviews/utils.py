def InterviewMode(candidate):
    vacancies = candidate.requirement.vacancies
    min_experience = candidate.requirement.min_experience

    print('vacan,min_exp: ', vacancies, min_experience)

    if vacancies<=3:
        if min_experience<=3:
            return 'Online Test'
        elif min_experience<=6:
            return 'In Person'
        else:
            return 'Telephonic'
    
    else:
        if min_experience<=3:
            return 'Online Test'
        elif min_experience<=6:
            return 'Online Test'
        else:
            return 'In Person'



def InterviewResult(interview_marks, candidate):
    rank = candidate.rank
    print('rank: ', rank)


    if interview_marks>80:
        return 'Selected'
    elif interview_marks>70:
        if rank=='R1' or rank=='R2':
            return 'Selected'
        else:
            return 'Rejected'
    elif interview_marks>50:
        if rank=='R1':
            return 'Selected'
        else:
            return 'Rejected'
    else:
        return 'Rejected'