from settings import PUZZLE_INPUT_PATH


class Node:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = {}
        self.files = []
        self.size = 0

    def add_child(self, child_name):
        self.children[child_name] = Node(child_name, self)

    def add_file(self, filename, size):
        self.files.append((filename, size))

    def get_file_sizes(self) -> int:
        return sum(int(size) for (file, size) in self.files)

    def get_child_sizes(self) -> int:
        return sum(child.size for child in self.children.values())

    def update_size(self):
        self.size = self.get_file_sizes() + self.get_child_sizes()


def grow_tree(node: Node, rep_loops: list):
    if not rep_loops:
        return node
    cmd = rep_loops[0]
    remaining_rep_loops = rep_loops[1:]
    if cmd[0][0] == "cd":
        if cmd[0][1] == "..":
            return grow_tree(node=node.parent, rep_loops=remaining_rep_loops)
        else:
            if cmd[0][1] in node.children.keys():
                return grow_tree(
                    node=node.children[cmd[0][1]], rep_loops=remaining_rep_loops
                )
            else:
                return grow_tree(
                    node=Node(cmd[0][1], parent=node), rep_loops=remaining_rep_loops
                )
    else:  # cmd[0][0] == 'ls'
        for output in cmd[1:]:
            if output[0] == "dir":
                if output[1] not in node.children.keys():
                    node.add_child(output[1])
            else:  # output[0] == a number
                node.add_file(output[1], output[0])
        return grow_tree(node=node, rep_loops=remaining_rep_loops)


def map_dir_sizes(node, dir_sizes: list[tuple[str, int]]):
    if not node.children:
        node.update_size()
        dir_sizes.append((node.name, node.size))
        return dir_sizes
    for child in node.children.values():
        map_dir_sizes(node=child, dir_sizes=dir_sizes)
    node.update_size()
    dir_sizes.append((node.name, node.size))
    return dir_sizes


def compute_star_1(puzzle_input):
    rep_loops = [
        [split.split() for split in split_cmds.strip().split("\n")]
        for split_cmds in puzzle_input.strip().split("$")
        if split_cmds
    ]
    rep_loops.pop(0)  # Drop the root node's creation
    root_node = Node("root", None)
    grow_tree(root_node, rep_loops)
    dir_sizes = map_dir_sizes(root_node, [])
    return sum(size for (name, size) in dir_sizes if size <= 100000)


def compute_star_2(puzzle_input):
    rep_loops = [
        [split.split() for split in split_cmds.strip().split("\n")]
        for split_cmds in puzzle_input.strip().split("$")
        if split_cmds
    ]
    rep_loops.pop(0)  # Drop the root node's creation
    root_node = Node("root", None)
    grow_tree(root_node, rep_loops)
    dir_sizes = map_dir_sizes(root_node, [])
    total_disk_space = 70000000
    space_required_for_update = 30000000
    space_to_free_up = space_required_for_update - (total_disk_space - root_node.size)
    return min(size for (name, size) in dir_sizes if size >= space_to_free_up)


print("day  7, star  1: ", compute_star_1(open(PUZZLE_INPUT_PATH / "day7.txt").read()))
print("day  7, star  2: ", compute_star_2(open(PUZZLE_INPUT_PATH / "day7.txt").read()))
