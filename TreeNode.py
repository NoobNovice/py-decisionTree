class TreeNode:
    root_label = None
    child = []
    parent = None
    att_split = None
    attr_split_value = None
    label = None

    def __init__(self, par, att, att_value):
        self.parent = par
        self.att_split = att
        self.attr_split_value = att_value
        return