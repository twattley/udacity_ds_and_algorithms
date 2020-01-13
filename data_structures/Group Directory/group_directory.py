class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name



def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.
    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """

    #straight find
    if user in group.get_users(): return True
    
    #noone in group
    if not group.get_groups(): return False
    
    #recursive search
    else:
        for sub_group in group.get_groups():
            if is_user_in_group(user, sub_group): return True
                
    return False

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)
child.add_group(sub_child)
parent.add_group(child)


sub_child_user = 'test_user_correct'
sub_child.add_user(sub_child_user)
child.add_group(sub_child)
parent.add_group(child)

users = ['test_user_1', 'test_user_2']
for i in users:
    sub_child.add_user(i)
child.add_group(sub_child)
parent.add_group(child)



def test_user_lookup():
    """
    test cases for lookups 
    """
    assert not is_user_in_group('test_user_incorrect', parent)
    assert is_user_in_group('test_user_correct', parent)
    assert is_user_in_group('test_user_1', child)
    assert is_user_in_group('test_user_2', child)
    assert not is_user_in_group('', parent)
    assert not is_user_in_group('', child)
    
    

test_user_lookup()