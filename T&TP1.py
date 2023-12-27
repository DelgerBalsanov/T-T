def check_budget(models, brand, model, budget):
    if brand in models and model in models[brand]:
        price = models[brand][model]
        if price <= budget:
            return f"Вы можете купить {brand} {model} за {price} рублей"
        else:
            return f"У вас недостаточно денег для покупки {brand} {model}"
    else:
        return "Такой модели нет в нашем магазине"


def glossary_models():
    return {
        'Samsung': {
            'Galaxy S21': 50000,
            'Galaxy S20': 40000,
            'Galaxy A51': 30000
        },
        'Apple': {
            'iPhone 13': 70000,
            'iPhone 12': 50000,
            'iPhone 11': 40000
        },
        'Xiaomi': {
            'Mi 11': 60000,
            'Redmi Note 10': 40000,
            'Poco X3 Pro': 40000
        }
    }


def brand_input():
    return input('Введите бренд:')


def model_input():
    return input('Введите модель:')


def budget_input():
    return input('Введите бюджет:')


def main():
    models = glossary_models()
    brand = brand_input()
    model = model_input()
    budget = int(budget_input())
    result = check_budget(models, brand, model, budget)
    print(result)


if __name__ in '__main__':
    print(1)
    main()


