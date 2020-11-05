from queue import Queue

class Vertex:
  def _init_(self, value):
    self.value = value
    self.connections = {}

  def _str_(self):
    return str(self.value) + 'connections ' + str([x.value for x in self.connections])
  
  def add_connection(self, vert, weight = 0):
    self.connections[vert] = weight

  def get_connections(self):
    return self.connections.keys()
  
  def get_value(self):
    return self.value

  def get_weight(self, vert):
    return self.connections[vert]

class Graph:
  def _init(self):
    self.vertices = {}
    self.count = 0

  def _contains_(self, vert):
    return vert in self.vertices

  def _iter_(self):
    return iter(self.vertices.values())

  def add_vertex(self, value):
    self.count += 1
    new_vert = Vertex(value)
    self.vertices[value] = new_vert
    return new_vert

  def add_edge(self, v1, v2, weight = 0):
    if v1 not in self.vertices:
      self.add_vertex(v1)
    if v2 not in self.vertices:
      self.add_vertex(v2)
    self.vertices[v1].add_connections(self.vertices[v2], weight)

  def get_vertices(self):
    return self.vertices.keys()

  def bfs(self, starting_vert):
    to_visit = Queue()
    visited = set()
    to_visit.enqueue(starting_vert)
    visited.add(starting_vert)
    while to_visit.size() > 0:
      current_vert = to_visit.dequeue()
      for next_vert in current_vert.get_connections():
        if next_vert not in visited:
          visited.add(next_vert)
          to_visit.enqueue(next_vert)