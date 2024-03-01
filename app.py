# app.py
class Customer:
    def __init__(self, name, email, phone, subscription_plan, expiration_days):
        self.name = name
        self.email = email
        self.phone = phone
        self.subscription_plan = subscription_plan
        self.expiration_days = expiration_days

    def notify_expiration(self):
        if self.expiration_days <= 5:
            return f"⚠️ A assinatura de {self.name} está prestes a expirar em {self.expiration_days} dias!"
        else:
            return ""

class CustomerManagement:
    def __init__(self):
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)
        return f"Cliente {customer.name} adicionado com sucesso."

    def remove_customer(self, customer):
        if customer in self.customers:
            self.customers.remove(customer)
            return f"Cliente {customer.name} removido com sucesso."
        else:
            return f"Cliente {customer.name} não encontrado."

    def list_customers(self):
        result = "Lista de Clientes:\n"
        for customer in self.customers:
            result += f"Nome: {customer.name}, Email: {customer.email}, Telefone: {customer.phone}, " \
                      f"Plano: {customer.subscription_plan}, Dias para expirar: {customer.expiration_days}\n"
            result += customer.notify_expiration() + "\n"
        return result

# Exemplo de uso
if __name__ == "__main__":
    cliente1 = Customer("João Silva", "joao@example.com", "123-456-7890", "Plano Premium", 10)
    cliente2 = Customer("Maria Santos", "maria@example.com", "987-654-3210", "Plano Básico", 3)

    gerenciamento_clientes = CustomerManagement()
    print(gerenciamento_clientes.add_customer(cliente1))
    print(gerenciamento_clientes.add_customer(cliente2))

    print(gerenciamento_clientes.list_customers())

    print(gerenciamento_clientes.remove_customer(cliente1))
    print(gerenciamento_clientes.list_customers())
