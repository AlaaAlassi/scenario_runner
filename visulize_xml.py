import xml.etree.ElementTree
import graphviz

tree = xml.etree.ElementTree.parse('srunner/examples/dummy.xosc')
root = tree.getroot()

f = graphviz.Digraph('finite_state_machine', filename='fsm.gv')
#f.attr(rankdir='LR', size='8,5')



print(root.tag)
storyBoardNode = root.find('./Storyboard')
storyNode = storyBoardNode.find('./Story')
ActNode = storyNode.find('./Act')
ManeuverGroupNode = ActNode.find('./ManeuverGroup')
ManeuverNode = ManeuverGroupNode.find('./Maneuver')
my_pets = ['Dog', 'Cat', 'Bunny', 'Fish']
cn = ['g', 'h', 'o', 'p']
cl = ["g", "h", "o", "p"]
i=0
currentNode = 'start'
for event in ManeuverNode:
    event_tag = event.tag
    event_name = event.get('name')
    print(event_name)
    with f.subgraph(name='cluster_'+str(i)) as c:
        c.attr(color='blue')
        c.node_attr.update(style='filled', color='gray')
        consitionTag = event.findall('.//StartTrigger/ConditionGroup/Condition')
        
        for tags in event:
            if tags.tag == 'Action':
                c.node(tags.get('name'))
                f.edge(currentNode,tags.get('name'),label=consitionTag.pop().get('name'))
                currentNode = tags.get('name')
    i+=1
f.view()
