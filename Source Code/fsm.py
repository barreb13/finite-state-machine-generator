#!/usr/bin/python3
#CSS 390 Scripting Languages - Assignment 5
#Credit Professor Bernstein's lecture

#Prof Bernstein
def iprint(level, *args, **kwargs):
    print("  " * level, end="")
    print(*args, **kwargs)

class Edge(object):
    def __init__(self, event, next_state, action):
        self.event = event
        self.next_state = next_state
        self.action = action
    
    def emit(self):
        iprint(5, f"case {self.event}_EVENT:")
        iprint(6, self.action)
        iprint(6, f"state = {self.next_state}_STATE;")
        iprint(5, "break;")

class Machine(object):

    def __init__(self, name):
        self.name = name
        self._header = ""
        self._footer = ""
        self.states = {}
        self.event_names = set()

    def header(self, text):
        self._header = text

    def footer(self, text):
        self._footer = text

    def state(self, name, action, edges=None):
        if not edges:
            edges = []
        self.states[name] = (action, edges)

    def edge(self, event, next_state, action=""):
        self.event_names.add(event)
        return Edge(event, next_state, action)

    def edges(self, *args_list):
        # return list of edge objects
        # arg1 = event/edge , arg2 = state/vertice
        edgeObjects = []
        for i in args_list:
            newEdgeObject = Edge(i[0], i[1], "")
            self.edge(newEdgeObject.event, newEdgeObject.next_state, "")
            edgeObjects.append(newEdgeObject)
        return edgeObjects

    def events(self, state):
        pass            

    def gen(self):
        print(self._header)
        print("using namespace std;")

        iprint(0, "enum State {")
        for s in self.states.keys():
            iprint(1, f"{s}_STATE,")
        iprint(0, "};")
        print('\n')
        iprint(0, "enum Event{")
        for e in self.event_names:
            iprint(1, f"{e}_EVENT,")
        iprint (1, "INVALID_EVENT")
        iprint(0, "};")
 
        iprint(0, "\nconst char * EVENT_NAMES[] = {") 
        for e in self.event_names:
            iprint(1, "\""f"{e}""\",")                                    
        iprint(0, "};")                             

        print("\nEvent get_next_event();\n")                                                        
        print("\nEvent string_to_event(string event_string) {")                                    
        for e in self.event_names:                                                                 
            iprint(1, "if (event_string == ""\"" f"{e}" "\""")" "  {return " f"{e}_EVENT"";}")     
        iprint(1, "return INVALID_EVENT;")                                                         
        print("}")                                                                                
        print("\n\n")
        iprint(0, f"int {self.name}(State initial_state)" + "{")
        iprint(1, "State state = initial_state;")
        iprint(1, "Event event;")                                                                 
        iprint(1, "while (true) {")
        iprint(2, "switch(state) {")
        for s, (action, edges) in self.states.items():
            iprint(2, f"case {s}_STATE:")
            iprint(3, "cerr << \"state " f"{s}" "\" << endl;")                                    
            iprint(4, action)
            iprint(4, "event = get_next_event();")
            iprint(4, "cerr << \"event \" << EVENT_NAMES[event] << endl;")                       
            iprint(4, "switch (event) {")
            for e in edges:
                e.emit()
            print("\n")
            iprint(4, "default:")
            iprint(5, "cerr << \"INVALID EVENT\" << event << \" in state " f"{s}" "\" << endl;") 
            iprint(5, "return -1;")
            iprint(4, "}")
            iprint(4, "break;")
        iprint(2, "}")            
        iprint(1, "}")
        iprint(0, "}")
        print(self._footer) 