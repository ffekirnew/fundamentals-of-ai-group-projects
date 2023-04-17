import matplotlib.pyplot as plt

def stack_plot(label: str, x_row: list, y_data: list[list], labels):
    colors = ['#F72585', '#7209B7', '#3A0CA3', '#4361EE', '#4895EF', '#4CC9F0', '#A3F7B5', '#457B9D', '#1D3557', '#E63946', '#F1FAEE', '#A8DADC', '#FCA311', '#FFD5C2', '#9C89B8', '#6D597A']
    plt.figure(figsize=(18, 8))
    plt.stackplot(x_row, y_data, labels=labels, colors=colors)
    plt.title(label)
    plt.tight_layout()
    plt.legend(loc='upper left')
    plt.savefig(f'output/{label}.png', format='png')