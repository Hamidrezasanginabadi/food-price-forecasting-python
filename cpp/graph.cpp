#include <iostream>
#include <vector>
using namespace std;

class Graph {
public:
    vector<vector<int>> adj;

    Graph(int n) {
        adj.resize(n);
    }

    void addEdge(int u, int v) {
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    void dfsUtil(int v, vector<bool>& visited) {
        visited[v] = true;
        cout << v << " ";

        for (int next : adj[v]) {
            if (!visited[next]) dfsUtil(next, visited);
        }
    }

    void dfs(int start) {
        vector<bool> visited(adj.size(), false);
        cout << "DFS: ";
        dfsUtil(start, visited);
        cout << endl;
    }
};

int main() {
    Graph g(6);

    g.addEdge(1, 2);
    g.addEdge(1, 3);
    g.addEdge(2, 4);

    g.dfs(1);

    return 0;
}
