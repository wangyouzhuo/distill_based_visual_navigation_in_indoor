
# ----------------------------------global count--------------------------------
def _init_train_count():
    global EPISODE_COUNT
    EPISODE_COUNT = 0

def _add_train_count():
    global EPISODE_COUNT
    EPISODE_COUNT = EPISODE_COUNT + 1
    return EPISODE_COUNT

def _get_train_count():
    global EPISODE_COUNT
    return EPISODE_COUNT

# ---------------------------------evaluate count--------------------------------
def _init_evaluate_count():
    global EVALUATE_COUNT
    EVALUATE_COUNT = 0

def _add_evaluate_count():
    global EVALUATE_COUNT
    EVALUATE_COUNT = EVALUATE_COUNT + 1

def _get_evaluate_count():
    global EVALUATE_COUNT
    return EVALUATE_COUNT

def _reset_evaluate_count():
    global EVALUATE_COUNT
    EVALUATE_COUNT = 0


# ----------------------------evaluate roa & reward list--------------------------
def _init_evaluate_list():
    global ROA_LIST,REWARD_LIST
    ROA_LIST,REWARD_LIST = [],[]

def _append_evaluate_list(roa,reward):
    global ROA_LIST, REWARD_LIST
    ROA_LIST.append(roa)
    REWARD_LIST.append(reward)

def _length_evaluate_list():
    global ROA_LIST, REWARD_LIST
    return len(ROA_LIST), len(REWARD_LIST)

def _evaluate_list_mean():
    global ROA_LIST, REWARD_LIST
    print("ROA_LIST : ",ROA_LIST)
    return average(ROA_LIST),average(REWARD_LIST)

def _reset_evaluate_list():
    global ROA_LIST, REWARD_LIST
    ROA_LIST, REWARD_LIST = [], []



#-----------------------------store roa_mean & reward_mean-------------------------------
def _init_result_mean_list():
    global ROA_MEAN,REWARD_LIST
    ROA_MEAN, REWARD_LIST = [],[]

def _append_result_mean_list(roa,reward):
    global ROA_MEAN,REWARD_LIST
    ROA_MEAN.append(roa)
    REWARD_LIST.append(reward)

def _reset_result_mean_list():
    global ROA_MEAN, REWARD_LIST
    ROA_MEAN, REWARD_LIST = [], []


def _get_result_mean_list():
    global ROA_MEAN, REWARD_LIST
    return ROA_MEAN, REWARD_LIST









def average(target):
    sum = 0
    for item in target:
        sum = sum + item
    mean = sum * 1.0 / len(target)
    return mean