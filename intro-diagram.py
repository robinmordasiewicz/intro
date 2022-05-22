from diagrams import Cluster, Diagram, Edge
from diagrams.onprem.analytics import Spark
from diagrams.onprem.compute import Server
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.inmemory import Redis
from diagrams.onprem.aggregator import Fluentd
from diagrams.onprem.monitoring import Grafana, Prometheus
from diagrams.onprem.network import Nginx
from diagrams.onprem.queue import Kafka
from diagrams.k8s.compute import Pod
from diagrams.k8s.network import Ing
from diagrams.onprem.network import Istio
from diagrams.generic.device import Mobile

graph_attr = {
    "fontsize": "45",
    "bgcolor": "transparent"
}

with Diagram(name="BIG-IP NEXT - Cloud Native Solutions", show=False, direction="LR", filename="SPK-diagram", outformat="png", graph_attr=graph_attr):

    userequipment = Mobile("Subscribers")
    spk = Ing("Service Proxy")
    primary = Pod("")
    servicemesh = Istio("Service Mesh")

    userequipment - spk

    with Cluster("BIG-IP NEXT"):
        spk

    with Cluster("Diameter"):
        primary \
            - Edge(color="brown", style="dotted") \
            - Pod("") \
            - Edge(label="") \
            - servicemesh
        spk - Edge(color="brown") - primary

    with Cluster("SIP"):
        primary \
            - Edge(color="brown", style="dotted") \
            - Pod("") \
            - Edge(label="") \
            - servicemesh
        spk - Edge(color="brown") - primary

    with Cluster("HTTP/2"):
        primary \
            - Edge(color="brown", style="dotted") \
            - Pod("") \
            - Edge(label="") \
            - servicemesh
        spk - Edge(color="black") - primary

