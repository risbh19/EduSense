# skills_db.py
# EduSense - Adaptive Learning Path Recommendation System
# Skill database with keywords, resources, and difficulty metadata

SKILLS_DB = {
    "Arrays": {
        "difficulty": "beginner",
        "keywords": [
            "array", "arrays", "list", "index", "indexing", "subarray",
            "contiguous", "sliding window", "two pointer", "prefix sum",
            "1d array", "2d array", "matrix", "element access",
            "not understanding arrays", "confused about indexing", "array problems"
        ],
        "resources": [
            {
                "title": "Arrays in C++ | Apna College",
                "url": "https://www.youtube.com/watch?v=cDMcSB2-r7Q",
                "type": "video"
            },
            {
                "title": "Array Data Structure - GeeksforGeeks",
                "url": "https://www.geeksforgeeks.org/array-data-structure/",
                "type": "article"
            },
            {
                "title": "Arrays - Abdul Bari",
                "url": "https://www.youtube.com/watch?v=5_Q_T9NVTTE",
                "type": "video"
            },
            {
                "title": "Introduction to Arrays - GFG Practice",
                "url": "https://www.geeksforgeeks.org/introduction-to-arrays-data-structure-and-algorithm-tutorials/",
                "type": "article"
            }
        ]
    },

    "Linked Lists": {
        "difficulty": "beginner",
        "keywords": [
            "linked list", "linkedlist", "singly linked",
            "doubly linked", "circular linked list", "head node", "next pointer",
            "insertion in linked list", "deletion in linked list",
            "slow fast pointer", "floyd cycle", "reverse linked list",
            "struggling with pointers", "linked list problems", "ll"
        ],
        "resources": [
            {
                "title": "Linked List in C++ - Apna College",
                "url": "https://www.youtube.com/watch?v=oAja8-Ulz6o",
                "type": "video"
            },
            {
                "title": "Linked List Data Structure - GeeksforGeeks",
                "url": "https://www.geeksforgeeks.org/data-structures/linked-list/",
                "type": "article"
            },
            {
                "title": "Linked List - Abdul Bari",
                "url": "https://www.youtube.com/watch?v=Ast5sKQXol0",
                "type": "video"
            },
            {
                "title": "Practice Linked List Problems - GFG",
                "url": "https://www.geeksforgeeks.org/linked-list-set-1-introduction/",
                "type": "article"
            }
        ]
    },

    "Trees": {
        "difficulty": "intermediate",
        "keywords": [
            "tree", "binary tree", "bst", "binary search tree", "avl tree",
            "inorder", "preorder", "postorder", "root", "leaf",
            "height of tree", "depth", "level order", "bfs tree", "dfs tree",
            "trie", "segment tree", "fenwick tree", "not understanding trees",
            "tree recursion", "tree problems", "confused about traversal",
            "tree traversal"
        ],
        "resources": [
            {
                "title": "Binary Trees - Apna College",
                "url": "https://www.youtube.com/watch?v=YAdLFsTG70w",
                "type": "video"
            },
            {
                "title": "Tree Data Structure - GeeksforGeeks",
                "url": "https://www.geeksforgeeks.org/binary-tree-data-structure/",
                "type": "article"
            },
            {
                "title": "Binary Search Tree - Abdul Bari",
                "url": "https://www.youtube.com/watch?v=9Jry5-82I68",
                "type": "video"
            },
            {
                "title": "Tree Traversals - GFG",
                "url": "https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/",
                "type": "article"
            }
        ]
    },

    "Graphs": {
        "difficulty": "advanced",
        "keywords": [
            "graph", "graphs", "bfs", "dfs", "breadth first search", "depth first search",
            "adjacency matrix", "adjacency list", "shortest path", "dijkstra",
            "bellman ford", "floyd warshall", "topological sort", "cycle detection",
            "connected components", "minimum spanning tree", "kruskal", "prim",
            "directed graph", "undirected graph", "weighted graph", "dag",
            "graph problems", "not understanding graphs", "confused about bfs dfs"
        ],
        "resources": [
            {
                "title": "Graph Algorithms - Apna College",
                "url": "https://www.youtube.com/watch?v=M3KTWnTrU_c",
                "type": "video"
            },
            {
                "title": "Graph Data Structure And Algorithms - GeeksforGeeks",
                "url": "https://www.geeksforgeeks.org/graph-data-structure-and-algorithms/",
                "type": "article"
            },
            {
                "title": "Graph Theory Algorithms - Abdul Bari",
                "url": "https://www.youtube.com/watch?v=0jNmHPfA_yE",
                "type": "video"
            },
            {
                "title": "Dijkstra's Algorithm - GFG",
                "url": "https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/",
                "type": "article"
            }
        ]
    },

    "Sorting": {
        "difficulty": "beginner",
        "keywords": [
            "sorting", "sort", "bubble sort", "selection sort", "insertion sort",
            "merge sort", "quick sort", "heap sort", "counting sort", "radix sort",
            "time complexity sorting", "comparison based sorting", "in-place sort",
            "stable sort", "not understanding sorting", "confused about quicksort",
            "mergesort recursion", "sorting algorithms"
        ],
        "resources": [
            {
                "title": "Sorting Algorithms - Apna College",
                "url": "https://www.youtube.com/watch?v=F5MZyqRp_IM",
                "type": "video"
            },
            {
                "title": "Sorting Algorithms - GeeksforGeeks",
                "url": "https://www.geeksforgeeks.org/sorting-algorithms/",
                "type": "article"
            },
            {
                "title": "Merge Sort and Quick Sort - Abdul Bari",
                "url": "https://www.youtube.com/watch?v=AZ4jEY_JAVc",
                "type": "video"
            },
            {
                "title": "Time Complexities of Sorting Algorithms - GFG",
                "url": "https://www.geeksforgeeks.org/time-complexities-of-all-sorting-algorithms/",
                "type": "article"
            }
        ]
    },

    "Recursion": {
        "difficulty": "intermediate",
        "keywords": [
            "recursion", "recursive", "base case", "recursive call", "stack overflow",
            "backtracking", "recursive tree", "tail recursion",
            "recursive function", "not understanding recursion", "confused about base case",
            "recursion problems", "how recursion works", "recursion vs iteration",
            "recursive thinking", "subproblem"
        ],
        "resources": [
            {
                "title": "Complete Recursion - Basics to Advanced - Apna College",
                "url": "https://www.youtube.com/watch?v=rVTmdTmAujs",
                "type": "video"
            },
            {
                "title": "Recursion - GeeksforGeeks",
                "url": "https://www.geeksforgeeks.org/recursion/",
                "type": "article"
            },
            {
                "title": "Recursion Concepts - CodeHelp - by Babbar",
                "url": "https://youtu.be/6IIgSFBPQ0U?si=Nxf9JGDwnKJoZpcT",
                "type": "video"
            },
            {
                "title": "Practice Recursion Problems - GFG",
                "url": "https://www.geeksforgeeks.org/recursion-practice-problems-solutions/",
                "type": "article"
            }
        ]
    },

    "Dynamic Programming": {
        "difficulty": "advanced",
        "keywords": [
            "dynamic programming", "dp", "memoization", "tabulation", "optimal substructure",
            "overlapping subproblems", "knapsack", "lcs", "longest common subsequence",
            "longest increasing subsequence", "lis", "coin change", "matrix chain",
            "edit distance", "dp on strings", "dp on trees", "dp problems",
            "not understanding dp", "confused about dp", "top down", "bottom up",
            "0/1 knapsack", "unbounded knapsack"
        ],
        "resources": [
            {
                "title": "Complete Dynamic Programming | DP Series - Lecture 1 - Apna College",
                "url": "https://www.youtube.com/watch?v=uBA8DkCBdco",
                "type": "video"
            },
            {
                "title": "Dynamic Programming - GeeksforGeeks",
                "url": "https://www.geeksforgeeks.org/dynamic-programming/",
                "type": "article"
            },
            {
                "title": "Dynamic Programming Algorithms - Abdul Bari",
                "url": "https://www.youtube.com/watch?v=5dRGRueKU3M",
                "type": "video"
            },
            {
                "title": "Top 20 DP Problems - GFG",
                "url": "https://www.geeksforgeeks.org/top-20-dynamic-programming-interview-questions/",
                "type": "article"
            }
        ]
    },

    "DSA": {
        "difficulty": "intermediate",
        "keywords": [
            "dsa", "data structures", "algorithms", "data structure", "algorithm",
            "time complexity", "space complexity", "big o", "big o notation",
            "complexity analysis", "stack", "queue", "heap", "priority queue",
            "hash map", "hashing", "not understanding dsa", "dsa problems",
            "struggling with dsa", "dsa for interviews", "competitive programming"
        ],
        "resources": [
            {
                "title": "DSA Full Course - Apna College",
                "url": "https://www.youtube.com/watch?v=z9bZufPHFLU",
                "type": "video"
            },
            {
                "title": "DSA Tutorial - GeeksforGeeks",
                "url": "https://www.geeksforgeeks.org/data-structures/",
                "type": "course"
            },
            {
                "title": "Data Structures - Abdul Bari",
                "url": "https://www.youtube.com/watch?v=0IAPZzGSbME",
                "type": "video"
            },
            {
                "title": "Big-O Cheat Sheet - GFG",
                "url": "https://www.geeksforgeeks.org/analysis-of-algorithms-big-o-analysis/",
                "type": "article"
            }
        ]
    },

    "OOP": {
        "difficulty": "beginner",
        "keywords": [
            "oop", "object oriented", "object-oriented programming", "class", "object",
            "inheritance", "polymorphism", "encapsulation", "abstraction",
            "constructor", "destructor", "method overriding", "method overloading",
            "interface", "abstract class", "virtual function", "access modifiers",
            "public private protected", "this keyword", "not understanding oop",
            "confused about inheritance", "oops concepts", "oops"
        ],
        "resources": [
            {
                "title": "OOP in Java - Apna College",
                "url": "https://www.youtube.com/watch?v=BSVKUk58K6U",
                "type": "video"
            },
            {
                "title": "Object Oriented Programming - GeeksforGeeks",
                "url": "https://www.geeksforgeeks.org/object-oriented-programming-oops-concept-in-java/",
                "type": "article"
            },
            {
                "title": "OOP Concepts in C++ - CodeWithHarry",
                "url": "https://www.youtube.com/watch?v=YFC2xIc8T9w",
                "type": "video"
            },
            {
                "title": "4 Pillars of OOP - GFG",
                "url": "https://www.geeksforgeeks.org/four-main-object-oriented-programming-concepts-of-java/",
                "type": "article"
            }
        ]
    },

    "DBMS": {
        "difficulty": "intermediate",
        "keywords": [
            "dbms", "database", "database management", "normalization", "er diagram",
            "entity relationship", "1nf", "2nf", "3nf", "bcnf", "acid properties",
            "transactions", "concurrency control", "locking", "deadlock in database",
            "indexing", "b-tree index", "functional dependency", "relational model",
            "not understanding dbms", "confused about normalization", "database design",
            "schema"
        ],
        "resources": [
            {
                "title": "DBMS Full Course - Apna College",
                "url": "https://www.youtube.com/watch?v=dl00fOOYLOM",
                "type": "video"
            },
            {
                "title": "DBMS Tutorial - GeeksforGeeks",
                "url": "https://www.geeksforgeeks.org/dbms/",
                "type": "course"
            },
            {
                "title": "Database Management System - Abdul Bari",
                "url": "https://www.youtube.com/watch?v=kBdlM6hNDAE",
                "type": "video"
            },
            {
                "title": "Normalization in DBMS - GFG",
                "url": "https://www.geeksforgeeks.org/normal-forms-in-dbms/",
                "type": "article"
            }
        ]
    },

    "SQL": {
        "difficulty": "beginner",
        "keywords": [
            "sql", "structured query language", "select", "insert", "update", "delete",
            "joins", "inner join", "outer join", "left join", "right join", "full join",
            "group by", "having", "order by", "where clause", "subquery",
            "aggregate functions", "count sum avg min max", "distinct",
            "create table", "drop table", "alter table", "constraints",
            "primary key", "foreign key",
            "not understanding sql", "confused about joins", "sql queries", "sql problems"
        ],
        "resources": [
            {
                "title": "SQL Full Course - Apna College",
                "url": "https://www.youtube.com/watch?v=hlGoQC332VM",
                "type": "video"
            },
            {
                "title": "SQL Tutorial - GeeksforGeeks",
                "url": "https://www.geeksforgeeks.org/sql-tutorial/",
                "type": "course"
            },
            {
                "title": "SQL Tutorial for Beginners - CodeWithHarry",
                "url": "https://www.youtube.com/watch?v=weiNEFHMmXY",
                "type": "video"
            },
            {
                "title": "SQL Joins - GFG",
                "url": "https://www.geeksforgeeks.org/sql-join-set-1-inner-left-right-and-full-joins/",
                "type": "article"
            }
        ]
    },

    "Operating Systems": {
        "difficulty": "intermediate",
        "keywords": [
            "operating system", "os", "process", "thread", "multithreading",
            "scheduling", "cpu scheduling", "fcfs", "sjf", "round robin", "priority scheduling",
            "deadlock", "memory management", "paging", "segmentation", "virtual memory",
            "page replacement", "lru", "fifo", "semaphore", "mutex", "synchronization",
            "inter process communication", "ipc", "not understanding os",
            "confused about scheduling", "process vs thread", "deadlock detection"
        ],
        "resources": [
            {
                "title": "Operating System Full Course - Apna College",
                "url": "https://www.youtube.com/watch?v=3obEP8eLsCw",
                "type": "video"
            },
            {
                "title": "Operating Systems Tutorial - GeeksforGeeks",
                "url": "https://www.geeksforgeeks.org/operating-systems/",
                "type": "course"
            },
            {
                "title": "Operating System Concepts - Abdul Bari",
                "url": "https://www.youtube.com/watch?v=vBURTt97EkA",
                "type": "video"
            },
            {
                "title": "CPU Scheduling Algorithms - GFG",
                "url": "https://www.geeksforgeeks.org/cpu-scheduling-in-operating-systems/",
                "type": "article"
            }
        ]
    },

    "Computer Networks": {
        "difficulty": "intermediate",
        "keywords": [
            "computer networks", "networking", "cn", "tcp", "udp", "ip", "tcp/ip",
            "osi model", "osi layers", "http", "https", "dns", "dhcp", "ftp",
            "mac address", "ip address", "subnetting", "routing", "switching",
            "router", "switch", "hub", "ethernet", "wifi", "socket programming",
            "three way handshake", "flow control", "congestion control",
            "not understanding networks", "confused about osi model", "network protocols"
        ],
        "resources": [
            {
                "title": "Computer Networks Full Course - Apna College",
                "url": "https://www.youtube.com/watch?v=JFF2vJaN0Cw",
                "type": "video"
            },
            {
                "title": "Computer Network Tutorial - GeeksforGeeks",
                "url": "https://www.geeksforgeeks.org/computer-network-tutorials/",
                "type": "course"
            },
            {
                "title": "Computer Networks - Abdul Bari",
                "url": "https://www.youtube.com/watch?v=VwN91x5i25g",
                "type": "video"
            },
            {
                "title": "OSI Model Layers - GFG",
                "url": "https://www.geeksforgeeks.org/layers-of-osi-model/",
                "type": "article"
            }
        ]
    },

    "Python": {
        "difficulty": "beginner",
        "keywords": [
            "python", "python programming", "python basics", "python syntax",
            "list comprehension", "dictionary", "tuples", "sets", "lambda",
            "decorators", "generators", "iterators", "file handling", "exception handling",
            "try except", "modules", "packages", "pip", "virtual environment",
            "python oop", "python functions", "not understanding python",
            "confused about python", "python errors", "indentation error"
        ],
        "resources": [
            {
                "title": "Python Full Course - Apna College",
                "url": "https://www.youtube.com/watch?v=ERCMXc8x7mc",
                "type": "video"
            },
            {
                "title": "Python Programming Language - GeeksforGeeks",
                "url": "https://www.geeksforgeeks.org/python-programming-language/",
                "type": "course"
            },
            {
                "title": "Python Tutorial for Beginners - CodeWithHarry",
                "url": "https://www.youtube.com/watch?v=7wnove7K-ZQ",
                "type": "video"
            },
            {
                "title": "Python List Comprehension - GFG",
                "url": "https://www.geeksforgeeks.org/python-list-comprehension/",
                "type": "article"
            }
        ]
    },

    "ML Basics": {
        "difficulty": "intermediate",
        "keywords": [
            "machine learning", "ml", "supervised learning", "unsupervised learning",
            "regression", "classification", "clustering", "linear regression",
            "logistic regression", "decision tree", "random forest", "svm",
            "support vector machine", "k-means", "knn", "k nearest neighbors",
            "overfitting", "underfitting", "bias variance tradeoff",
            "train test split", "cross validation", "gradient descent",
            "loss function", "cost function", "features", "labels",
            "not understanding ml", "confused about gradient descent", "ml algorithms"
        ],
        "resources": [
            {
                "title": "Machine Learning Full Course - Apna College",
                "url": "https://www.youtube.com/watch?v=ZftI2fEz0Fw",
                "type": "video"
            },
            {
                "title": "Machine Learning Tutorial - GeeksforGeeks",
                "url": "https://www.geeksforgeeks.org/machine-learning/",
                "type": "course"
            },
            {
                "title": "Machine Learning in Python - CodeWithHarry",
                "url": "https://www.youtube.com/watch?v=gmvvaobm7eQ",
                "type": "video"
            },
            {
                "title": "Gradient Descent Algorithm - GFG",
                "url": "https://www.geeksforgeeks.org/gradient-descent-algorithm-and-its-variants/",
                "type": "article"
            }
        ]
    },

    "Web Dev": {
        "difficulty": "beginner",
        "keywords": [
            "web development", "web dev", "html", "css", "javascript", "js",
            "frontend", "backend", "full stack", "react", "nodejs", "express",
            "rest api", "json", "dom", "dom manipulation", "responsive design",
            "bootstrap", "flexbox", "grid", "http methods", "get post put delete",
            "not understanding html", "confused about css", "javascript basics",
            "web dev project", "website", "web application"
        ],
        "resources": [
            {
                "title": "Web Development Full Course - Apna College",
                "url": "https://www.youtube.com/watch?v=tVzUXW6siu0",
                "type": "video"
            },
            {
                "title": "Web Development Tutorial - GeeksforGeeks",
                "url": "https://www.geeksforgeeks.org/web-development/",
                "type": "course"
            },
            {
                "title": "HTML CSS JavaScript Full Course - CodeWithHarry",
                "url": "https://www.youtube.com/watch?v=BsDoLVMnmZs",
                "type": "video"
            },
            {
                "title": "REST API Introduction - GFG",
                "url": "https://www.geeksforgeeks.org/rest-api-introduction/",
                "type": "article"
            }
        ]
    },

    "Stacks and Queues": {
        "difficulty": "beginner",
        "keywords": [
            "stack", "queue", "push", "pop", "peek", "top", "lifo", "fifo",
            "deque", "double ended queue", "priority queue", "circular queue",
            "stack underflow", "monotonic stack",
            "not understanding stack", "confused about queue", "stack problems",
            "stack using array", "queue using linked list", "infix postfix prefix"
        ],
        "resources": [
            {
                "title": "Stacks and Queues - Apna College",
                "url": "https://www.youtube.com/watch?v=nqXaPZi99JI",
                "type": "video"
            },
            {
                "title": "Stack Data Structure - GeeksforGeeks",
                "url": "https://www.geeksforgeeks.org/stack-data-structure/",
                "type": "article"
            },
            {
                "title": "Queue Data Structure - Abdul Bari",
                "url": "https://www.youtube.com/watch?v=A5_XdiK4J8A",
                "type": "video"
            },
            {
                "title": "Queue Data Structure - GFG",
                "url": "https://www.geeksforgeeks.org/queue-data-structure/",
                "type": "article"
            }
        ]
    },

    "Hashing": {
        "difficulty": "intermediate",
        "keywords": [
            "hashing", "hash table", "hash map", "hash function", "collision",
            "chaining", "open addressing", "linear probing", "quadratic probing",
            "double hashing", "load factor", "rehashing", "unordered map",
            "key value", "not understanding hashing",
            "confused about hash collision", "hashmap problems", "set"
        ],
        "resources": [
            {
                "title": "Hashing in Data Structures - Apna College",
                "url": "https://www.youtube.com/watch?v=TsrGFT4TMkA",
                "type": "video"
            },
            {
                "title": "Hashing Data Structure - GeeksforGeeks",
                "url": "https://www.geeksforgeeks.org/hashing-data-structure/",
                "type": "article"
            },
            {
                "title": "Collision Resolution Techniques - Abdul Bari",
                "url": "https://www.youtube.com/watch?v=T9gct6Dx-jo",
                "type": "video"
            },
            {
                "title": "Hash Map vs Hash Set - GFG",
                "url": "https://www.geeksforgeeks.org/differences-between-hashmap-and-hashtable-in-java/",
                "type": "article"
            }
        ]
    }
}


# ── Utility helpers ──────────────────────────────────────────────────────────

def get_skill(skill_name: str) -> dict | None:
    for key, value in SKILLS_DB.items():
        if key.lower() == skill_name.lower():
            return value
    return None


def get_skills_by_difficulty(level: str) -> list[str]:
    return [name for name, data in SKILLS_DB.items()
            if data["difficulty"].lower() == level.lower()]


def get_all_skill_names() -> list[str]:
    return sorted(SKILLS_DB.keys())


if __name__ == "__main__":
    print(f"EduSense Skills DB — {len(SKILLS_DB)} skills loaded\n")
    for level in ("beginner", "intermediate", "advanced"):
        skills = get_skills_by_difficulty(level)
        print(f"{level.capitalize():>12}: {', '.join(skills)}")