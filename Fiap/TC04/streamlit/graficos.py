import seaborn as sns
import matplotlib.pyplot as plt

def condition(base):
    base['condition'] = base['Obesity'].str.contains('Obesity', case=False, na=False).astype(int)
    base['condition_name'] = base['Obesity'].apply(
        lambda x: 'Obesity' if isinstance(x, str) and 'obesity' in x.lower() else 'No Obesity'
        )

    print("Coluna 'condition' criada com sucesso!")

def family_history(base):
    
    condition(base)

    plt.figure(figsize=(8,6))
    sns.countplot(data=base, x='family_history', hue='condition_name')
    plt.xlabel('Histórico Familiar')
    plt.ylabel('Quantidade de pessoas')
    plt.legend()
    plt.grid(linestyle='--', alpha=0.3)
    return plt

def favc(base):
    
    condition(base)

    plt.figure(figsize=(8,6))
    sns.countplot(data=base, x='FAVC', hue='condition_name')
    plt.xlabel('FAV')
    plt.ylabel('Quantidade de pessoas')
    plt.legend()
    plt.grid(linestyle='--', alpha=0.3)
    return plt
