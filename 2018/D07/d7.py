data = open("d7.txt").read().split("\n")[:-1]
data = [i.split(" ") for i in data]
step_bef = [i[1] for i in data]
step_aft = [i[7] for i in data]


class node:

    def __init__(self, name):
        self.name = name
        self.next_nodes = []


class graph_builder:

    def __init__(self):
        self.beginning = None
        self.all_node_names = []

    def dfs(self):
        available_nodes = [self.beginning]
        return_str = ""
        while len(available_nodes) > 0:
            curr_node = available_nodes.pop()
            if curr_node.name not in return_str:
                return_str += curr_node.name
            for i in curr_node.next_nodes:
                available_nodes.append(i)
            available_nodes = sorted(
                available_nodes, key=lambda x: x.name, reverse=True
            )

        return return_str


graph = graph_builder()
for aft, bef in zip(step_bef, step_aft):
    print(f"bef is {bef}, aft is {aft}")
    print(f"Curr node is list {[i.name for i in graph.all_node_names]}")
    if bef in [i.name for i in graph.all_node_names]:

        node_idx = [i.name for i in graph.all_node_names].index(bef)
        new_node = graph.all_node_names[node_idx]
    else:
        new_node = node(bef)
        graph.all_node_names.append(new_node)

    if aft in [i.name for i in graph.all_node_names]:
        node_idx = [i.name for i in graph.all_node_names].index(aft)
        curr_node = graph.all_node_names[node_idx]
        curr_node.next_nodes.append(new_node)
        new_node_aft = curr_node
    else:
        new_node_aft = node(aft)
        graph.all_node_names.append(new_node_aft)
        new_node_aft.next_nodes.append(new_node)
        if graph.beginning == None:
            graph.beginning = new_node_aft

    if graph.beginning.name == bef:
        print("Changed the new node name")
        graph.beginning = new_node_aft
