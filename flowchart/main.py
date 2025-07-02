import os, graphviz

# Create a new Digraph
flowchart = graphviz.Digraph(format='png')

# Define nodes
flowchart.node('Start', 'Start', shape='oval')
flowchart.node('Menu', 'Display Menu', shape='parallelogram')
flowchart.node('Add', 'Add Product', shape='rectangle')
flowchart.node('Update', 'Update Stock', shape='rectangle')
flowchart.node('View', 'View Products', shape='rectangle')
flowchart.node('Remove', 'Remove Product', shape='rectangle')
flowchart.node('Exit', 'Exit Program', shape='oval')

# Define decision node
flowchart.node('Choice', 'User Choice?', shape='diamond')

# Define edges
flowchart.edge('Start', 'Menu')
flowchart.edge('Menu', 'Choice')

flowchart.edge('Choice', 'Add', label='1. Add Product')
flowchart.edge('Choice', 'Update', label='2. Update Stock')
flowchart.edge('Choice', 'View', label='3. View Products')
flowchart.edge('Choice', 'Remove', label='4. Remove Product')
flowchart.edge('Choice', 'Exit', label='5. Exit')

# Loop back to menu after each action
flowchart.edge('Add', 'Menu')
flowchart.edge('Update', 'Menu')
flowchart.edge('View', 'Menu')
flowchart.edge('Remove', 'Menu')

# Render and open the image
flowchart_path = 'inventory_flowchart'
flowchart.render(flowchart_path, format='png')
os.system(flowchart_path + '.png')