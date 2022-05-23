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
from diagrams.k8s.network import SVC
from diagrams.k8s.compute import RS
from diagrams.onprem.network import Istio
from diagrams.generic.device import Mobile
from diagrams.custom import Custom

graph_attr = {
    "fontsize": "24",
    "bgcolor": "transparant"
    "fontcolor": "#FFFFFF",
}
subs_attr = {
    "fontsize": "22",
    "bgcolor": "#0E487A",
    "fontcolor": "#FFFFFF",
    "fontname": "Arial"
}
node_attr = {
    "fontsize": "14",
    "bgcolor": "yellow"
    "fontcolor": "#FFFFFF",
}
edge_attr = {
    "fontsize": "18",
    "bgcolor": "blue"
    "fontcolor": "#FFFFFF",
}

with Diagram(name="F5 Cloud Native Solutions", show=False, direction="LR", filename="SPK-diagram", outformat="png", graph_attr=graph_attr,node_attr=node_attr,edge_attr=edge_attr):

    subscribers = Mobile("Subscribers")
    with Cluster("BIG-IP NEXT",graph_attr=subs_attr):
        spk = Custom("Service Proxy", "f5-logo-white.png")
        subscribers - spk
    with Cluster("Kubernetes"):
        diameter = RS("Diameter")
        spk - diameter
        sip = RS("SIP")
        spk - sip
        http2 = RS("HTTP/2")
        spk - http2
        servicemesh = Istio("Service Mesh")
        diameter - servicemesh
        sip - servicemesh
        http2 - servicemesh
