#Search for all products with prefix searchWord in a list of products

class Node:
    def __init__(self, end=False):
        self.end = end
        self.edges = {}

def dfs(node, current_word, ans_list):
    if node.end:
        ans_list.append(current_word[:])
    for edge in node.edges:
        current_word.append(edge)
        dfs(node.edges[edge],current_word, ans_list)
        current_word.pop()    
        
    
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        root = Node(False)
        for word in products:
            current_node = root
            for letter in word:
                if letter not in current_node.edges:
                    next_node = Node(False)
                    current_node.edges[letter] = next_node
                else:
                    next_node = current_node.edges[letter]
                current_node = next_node
            current_node.end = True
        final_ans = []
        current_node = root
        for letter in searchWord:
            if letter in current_node.edges:
                current_node = current_node.edges[letter]
            else:
                break
        else:
            prelim_ans = []
            dfs(current_node, list(searchWord), prelim_ans)
            print(f"prelim : {prelim_ans}")
            for l in prelim_ans:
                final_ans.append(''.join(l))
        return [final_ans]
            
            
            
                
            
                    
                
                
            
        
        
        
