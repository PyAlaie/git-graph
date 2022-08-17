import os

def get_commit_title(commit_hash):
    title = os.popen('git log {} -1 --pretty=oneline'.format(commit_hash)).readlines()[0].split()
    del title[0]
    
    return ''.join(title)

def get_branches():
    branches = os.popen('git branch --format=\'%(refname:short)\' --all').readlines()
    branches = [branch[:-1] for branch in branches]
    # branches.remove('master')
    return branches

def get_commits_of_branch(branch_name):
    branch_commits = os.popen('git log {} --pretty=oneline --first-parent'.format(branch_name)).readlines()
    branch_commits = [commit.split()[0] for commit in branch_commits]
    
    master_commits = os.popen('git log master --pretty=oneline --first-parent'.format(branch_name)).readlines()
    master_commits = [commit.split()[0] for commit in master_commits]

    final = []
    
    for commit in branch_commits:
        if commit not in master_commits:
            final.append(commit)
    
    
    return final

def create_commits_dict(commits):
    commits_dict = {}
    for i,commit in enumerate(commits):
        commits_dict[commit] = i
    return commits_dict

def get_master_branch_commits():
    master_branch_commits = os.popen('git log --pretty=oneline master').readlines()
    master_branch_commits = [commit.split()[0] for commit in master_branch_commits]
    return master_branch_commits

def assign_axis_to_branches(branches):
    branches_dict = {}
    for i, brnach in enumerate(branches, start=0):
        branches_dict[brnach] = i
    return branches_dict

def get_branch_of_commit(commit):
    branch = os.popen('git name-rev {}'.format(commit)).readlines()[0]
    return branch.split()[1]
    
def get_parents_of_commit(commit):
    parents = os.popen('git rev-list -n 1 {} --parents'.format(commit)).readlines()[0].split()[1:]
    return parents

def get_branch_name_of_commit_from_dictionary(commit, dictionary):
    for i in dictionary.values():
        if commit in i:
            for key, value in dictionary.items():
                if i == value:
                    return key
    return False            
    
    
    
dot_config = {
    'zorder': 2,
    'size': 2000
}

line_config = {
    'zorder': 1
}