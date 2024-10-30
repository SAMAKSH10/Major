import lxml.etree as ET
import queue
import time

# Define a wrapper class for XML elements with priority and timestamp
class XMLNode:
    def __init__(self, element, priority, timestamp):
        self.element = element
        self.priority = priority
        self.timestamp = timestamp

    def __lt__(self, other):
        # Comparison based on priority, then timestamp
        if self.priority == other.priority:
            return self.timestamp < other.timestamp
        return self.priority < other.priority

# Load XML file
tree = ET.parse("text1.xml")
root = tree.getroot()

# Create a priority queue for XML nodes
pq = queue.PriorityQueue()

# Function to recursively insert XML elements into the priority queue with timestamp
def insert_into_priority_queue(element, priority):
    timestamp = time.time()  # Current timestamp
    pq.put(XMLNode(element, priority, timestamp))
    for child in element:
        insert_into_priority_queue(child, priority + 1)

# Insert root element into the priority queue
insert_into_priority_queue(root, 0)

# Helper function to write data to a file
def write_to_file(filename, data):
    with open(filename, "w") as file:
        file.write(data)

# Traversal function for preorder
def preorder_traversal(element, priority, output):
    output.append(f"Tag: {element.tag}, Text: {element.text}, Priority: {priority}\n")
    for child in element:
        preorder_traversal(child, priority + 1, output)

# Traversal function for inorder
def inorder_traversal(element, priority, output):
    children = list(element)
    if children:
        inorder_traversal(children[0], priority + 1, output)
    output.append(f"Tag: {element.tag}, Text: {element.text}, Priority: {priority}\n")
    for child in children[1:]:
        inorder_traversal(child, priority + 1, output)

# Traversal function for postorder
def postorder_traversal(element, priority, output):
    for child in element:
        postorder_traversal(child, priority + 1, output)
    output.append(f"Tag: {element.tag}, Text: {element.text}, Priority: {priority}\n")

# Function to perform traversal, measure time, and write output to file
def perform_traversal(traversal_func, filename):
    output = []
    start_time = time.time()
    traversal_func(root, 0, output)  # Start traversal from root with priority 0
    end_time = time.time()
    write_to_file(filename, ''.join(output))  # Write all collected output to file
    print(f"Time taken for {filename}: {end_time - start_time:.4f} seconds")

# Execute traversals and write results to respective files
perform_traversal(preorder_traversal, "preorder_output.txt")
perform_traversal(inorder_traversal, "inorder_output.txt")
perform_traversal(postorder_traversal, "postorder_output.txt")
