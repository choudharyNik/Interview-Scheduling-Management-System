def CandidateRank(degree, cgpa, experience, required_experience):
    if experience<required_experience:
        return 'Rejected'
    else:
        if degree==2 or degree==4 or degree==6:
            if cgpa>=9.0:
                return 'R1'
            elif cgpa>=8.0:
                return 'R2'
            elif cgpa>=7.0:
                return 'R3'
            elif cgpa>=6.0:
                return 'R4'
            else:
                return 'Rejected'
        else:
            if cgpa>=9.0:
                return 'R2'
            elif cgpa>=8.0:
                return 'R3'
            elif cgpa>=7.0:
                return 'R4'
            else:
                return 'Rejected'