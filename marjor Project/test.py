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
        # Implement less than comparison based on priority and timestamp
        if self.priority == other.priority:
            return self.timestamp < other.timestamp
        return self.priority < other.priority

# Load XML file
tree = ET.parse("text1.xml")
root = tree.getroot()

# Create priority queue for XML nodes
pq = queue.PriorityQueue()

# Define a function to recursively insert XML elements into the priority queue with timestamp
def insert_into_priority_queue(element, priority):
    timestamp = time.time()  # Current timestamp
    pq.put(XMLNode(element, priority, timestamp))
    for child in element:
        insert_into_priority_queue(child, priority + 1)

# Insert root element into the priority queue
insert_into_priority_queue(root, 0)

# Process elements in priority queue
while not pq.empty():
    xml_node = pq.get()
    element = xml_node.element
    priority = xml_node.priority
    timestamp = xml_node.timestamp
    print(f"Tag: {element.tag}, Text: {element.text}, Priority: {priority}, Timestamp: {timestamp}")
