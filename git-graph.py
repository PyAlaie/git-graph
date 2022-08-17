import matplotlib.pyplot as plt
import os
import funcs

colors = list('rgbcm')

# getting all commits
all_commits = os.popen('git log --pretty=oneline --all').readlines()
all_commits = [commit.split()[0] for commit in all_commits]

# creating dictionary that assigns a uniqe index for each commit  
all_commits_dict = funcs.create_commits_dict(all_commits)

# getting master branch commits
master_commits = funcs.get_master_branch_commits()

# getting the name of all exsiting branchs
branches = funcs.get_branches()

# assgning a uniqe index for each branch
branches_dict = funcs.assign_axis_to_branches(branches)

# creating a dictionary that adds every commit to each related branch
# and plots them at the same time
commit_branch_rel = {}
for branch in branches:
    commits = funcs.get_commits_of_branch(branch)
    commit_branch_rel[branch] = commits
    for commit in commits:
        plt.scatter(all_commits_dict[commit], branches_dict[branch], color=colors[0],zorder=2,s=500)
    first_color = colors[0]
    colors.remove(colors[0])
    colors.append(first_color)
commit_branch_rel['master'] = master_commits

# drawing master branch commits
for commit in master_commits:
    plt.scatter(all_commits_dict[commit], branches_dict['master'], color='y',zorder=2, s=500)
    
# draw lines between related commits
for commit in all_commits:
    parents = funcs.get_parents_of_commit(commit)
    for parent in parents:
        parent_branch = funcs.get_branch_name_of_commit_from_dictionary(parent, commit_branch_rel)
        commit_branch = funcs.get_branch_name_of_commit_from_dictionary(commit, commit_branch_rel)
        plt.plot([all_commits_dict[parent],all_commits_dict[commit]], [branches_dict[parent_branch],branches_dict[commit_branch]], color='black',
                 zorder=1,
                 linewidth=1)
        
plt.show()