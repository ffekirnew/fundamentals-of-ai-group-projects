import matplotlib.pyplot as plt
import networkx as nx

def stack_plot(label: str, x_row: list, y_data: list[list], labels):
    """Create a stack plot using plt.stackplot.

    Args:
        label (str): The label for the entire plot.
        x_row (list): The labels to be put on the x axis.
        y_data (list[list]): The data to be stacked on the y-axis.
        labels (_type_): The data to be put as legend.
    """
    colors = ['#F72585', '#7209B7', '#3A0CA3', '#4361EE', '#4895EF', '#4CC9F0', '#A3F7B5', '#457B9D', '#1D3557', '#E63946', '#F1FAEE', '#A8DADC', '#FCA311', '#FFD5C2', '#9C89B8', '#6D597A']
    plt.figure(figsize=(30, 8))
    plt.stackplot(x_row, y_data, labels=labels, colors=colors)
    plt.title(label)
    plt.tight_layout()
    plt.legend(loc='upper left')
    plt.savefig(f'output/{label}.png', format='png')

def graph_visualizer(graphs, save=True):
    """Create a visualizer for a given graph.

    Args:
        graphs (list[Graph]): the graphs to be visualized in groups of four.
    """
    # Create the figure and subplots
    fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(10, 10))

    # Iterate over the experiment graphs and plot them
    for k in range(1, 5):
        for (i, j), (label, graph) in zip([(0, 0), (0, 1), (1, 0), (1, 1), (0, 0), (0, 1), (1, 0), (1, 1), (0, 0), (0, 1), (1, 0), (1, 1), (0, 0), (0, 1), (1, 0), (1, 1)], graphs):
            if label.startswith(f"{k}0"):
                data = graph.graph

                # Create an empty graph
                G = nx.Graph()

                # Add nodes with their location as the node label
                for node, (location, edges) in data.items():
                    G.add_node(node, pos=location)

                # Add edges
                for node, (location, edges) in data.items():
                    for target_node, weight in edges.items():
                        G.add_edge(node, target_node, weight=weight)

                # Get node positions from their labels
                node_pos = nx.get_node_attributes(G, 'pos')

                # Draw the graph on the appropriate subplot
                nx.draw(G, pos=node_pos, with_labels=True, ax=axs[i][j])
                axs[i][j].set_title(label)

        # Save the figures or show them
        if save:
            plt.savefig(f'output/experiment_graph_with_{k}0_nodes.png', format='png')
        else:
            plt.show()
