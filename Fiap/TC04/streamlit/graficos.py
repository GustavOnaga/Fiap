import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style("whitegrid")

def condition(base):
    base = base.copy()
    base['condition'] = base['Obesity'].str.contains('Obesity', case=False, na=False).astype(int)
    base['condition_name'] = base['Obesity'].apply(
        lambda x: 'Obesity' if isinstance(x, str) and 'obesity' in x.lower() else 'No Obesity'
    )
    return base


def family_history(base):
    base = condition(base)

    fig, ax = plt.subplots(figsize=(6, 4))
    sns.countplot(
        data=base,
        x='family_history',
        hue='condition_name',
        palette=['#0000FF', '#C0C0C0'],
        order=['yes', 'no'],
        ax=ax
    )

    ax.set_ylabel('Quantidade de pessoas')
    ax.grid(linestyle='--', alpha=0.5)

    return fig


def favc(base):
    base = condition(base)

    fig, ax = plt.subplots(figsize=(6, 4))
    sns.countplot(
        data=base,
        x='FAVC',
        hue='condition_name',
        palette=['#0000FF', '#C0C0C0'],
        order=['yes', 'no'],
        ax=ax
    )

    ax.set_ylabel('Quantidade de pessoas')
    ax.grid(linestyle='--', alpha=0.5)

    return fig


def smoke(base):
    base = condition(base)

    fig, ax = plt.subplots(figsize=(6, 4))
    sns.countplot(
        data=base,
        x='SMOKE',
        hue='condition_name',
        palette=['#0000FF', '#C0C0C0'],
        order=['yes', 'no'],
        ax=ax
    )

    ax.set_ylabel('Quantidade de pessoas')
    ax.grid(linestyle='--', alpha=0.3)

    return fig
