class node:
    def __init__(self, input_str):
        self.number_of_children = input_str[0]
        self.metadata_tags = input_str[1]
        self.next_nodes = []
        self.metadata = []
        self.input_str = input_str       
        
    def find_subnodes(self):
        total_length = 2
        if self.number_of_children == 0:
            for tag in range(self.metadata_tags):
                self.metadata.append(self.input_str[total_length + tag])
            return 2 + self.metadata_tags        
        
        for child in range(self.number_of_children):
            new_node = node(self.input_str[total_length:])
            total_length += new_node.find_subnodes()
            self.next_nodes.append(new_node)
            
        for tag in range(self.metadata_tags):
            self.metadata.append(self.input_str[total_length + tag])    
            
        return total_length + self.metadata_tags

class graph_rep:
    def __init__(self, head_node):
       
        self.head = node(head_node)
        self.head.find_subnodes()
        #self.all_nodes = [head_node]
        

    def print_metadata(self):
        metadata = self._print_metadata(self.head, [])
        print(' '.join(map(str, metadata)))
        
    def print_sum(self, show=False):
        metadata = self._print_metadata(self.head, [])
        print(f"Sum of all metadata tags are: {sum(metadata)}")
        return sum(metadata)
        
    def _print_metadata(self, node, metadata):
        if len(node.next_nodes) == 0:
            metadata += node.metadata  
            
        else:
            metadata += node.metadata
            for _node in node.next_nodes:
                self._print_metadata(_node, metadata)
                
        return metadata

test_1 = graph_rep([0, 1, 99])
test_2 = graph_rep([1, 1, 0, 1, 99, 2])
test_3 = graph_rep([2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2])

test_3.print_sum()

data = list(map(int, open('input.txt').read().strip().split(' ')))

actual = graph_rep(data)
total = actual.print_sum()
print(f"Part #1) {total}")