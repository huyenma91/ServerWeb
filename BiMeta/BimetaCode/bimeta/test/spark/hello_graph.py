from pyspark import *
from pyspark.sql import *
from graphframes import *

"""
Run command:
spark-submit --packages graphframes:graphframes:0.8.1-spark3.0-s_2.12 hello_graph.py
"""

spark = SparkSession.builder.appName("fun").getOrCreate()
vertices = spark.createDataFrame(
    [
        ("1", "Carter", "Derrick", 50),
        ("2", "May", "Derrick", 26),
        ("3", "Mills", "Jeff", 80),
        ("4", "Hood", "Robert", 65),
        ("5", "Banks", "Mike", 93),
        ("98", "Berg", "Tim", 28),
        ("99", "Page", "Allan", 16),
    ],
    ["id", "name", "firstname", "age"],
)
edges = spark.createDataFrame(
    [
        ("1", "2", "friend"),
        ("2", "1", "friend"),
        ("3", "1", "friend"),
        ("1", "3", "friend"),
        ("2", "3", "follows"),
        ("3", "4", "friend"),
        ("4", "3", "friend"),
        ("5", "3", "friend"),
        ("3", "5", "friend"),
        ("4", "5", "follows"),
        ("98", "99", "friend"),
        ("99", "98", "friend"),
    ],
    ["src", "dst", "type"],
)
g = GraphFrame(vertices, edges)
## Take a look at the DataFrames
g.vertices.show()
g.edges.show()
## Check the number of edges of each vertex
g.degrees.show()