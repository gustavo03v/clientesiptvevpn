class Customer:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

class CustomerManagement:
    def __init__(self):
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)
        print(f"Cliente {customer.name} adicionado com sucesso.")

    def remove_customer(self, customer):
        if customer in self.customers:
            self.customers.remove(customer)
            print(f"Cliente {customer.name} removido com sucesso.")
        else:
            print(f"Cliente {customer.name} não encontrado.")

    def list_customers(self):
        print("Lista de Clientes:")
        for customer in self.customers:
            print(f"Nome: {customer.name}, Email: {customer.email}, Telefone: {customer.phone}")

# Exemplo de uso
if __name__ == "__main__":
    cliente1 = Customer("João Silva", "joao@example.com", "123-456-7890")
    cliente2 = Customer("Maria Santos", "maria@example.com", "987-654-3210")

    gerenciamento_clientes = CustomerManagement()
    gerenciamento_clientes.add_customer(cliente1)
    gerenciamento_clientes.add_customer(cliente2)

    gerenciamento_clientes.list_customers()

    gerenciamento_clientes.remove_customer(cliente1)
    gerenciamento_clientes.list_customers()
