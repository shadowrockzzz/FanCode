class UserValidation:
    
    def __init__(self):
        pass

    @staticmethod
    def is_fancode_city(user):
        lat = float(user['address']['geo']['lat'])
        long = float(user['address']['geo']['lng'])
        if(lat>-40 and lat<5 and long>5 and long<100):
            return True
        return False
    
    @staticmethod
    def get_user_tasks(user, tasks):
        userId = user['id']
        for task in tasks:
            if (userId==task['userId']):
                yield task
    
    @staticmethod
    def get_cpompleted_task_percentage(tasks):
        total_tasks = len(tasks)
        completed_tasks = 0
        for task in tasks:
            if(bool(task['completed'])==True):
                completed_tasks+=1
        return (completed_tasks/total_tasks)*100



