class Graph:
    graph={}
    path=[]
    flights=[]

    def __init__(self,routes):
        self.routes=routes

    def create_graph(self):
        for i in self.routes:
            if i[0] in self.graph:
                self.graph[i[0]].append(i[1])
            else:
                self.graph[i[0]]=[i[1]]

    def find_path(self,start,end):
        if end in self.graph[start]:
            self.path.append(end)
            self.flights.append(self.path)
            self.path=[]
            return
        for i in self.graph[start]:
            self.path.append(i)
            self.find_path(i,end)

    def find_sh_path(self,start):
        count=0
        sh_path=[]
        for i in self.flights:
            length=len([start]+i)
            if count==0:
               sh_len=length
            if length<=sh_len:
                sh_path.append([start]+i)
            count+=1
        print("The shortest path:")
        print(sh_path)

routes=[("Pakistan","Dubai"),
        ("Dubai","Australia"),
        ("Pakistan","Russia"),
        ("Russia","China"),
        ("China","Australia"),
        ("Pakistan","India"),
        ("India","Australia")]
route_graph=Graph(routes)
route_graph.create_graph()
start="Pakistan"
end="Australia"
route_graph.find_path(start,end)
route_graph.find_sh_path(start)