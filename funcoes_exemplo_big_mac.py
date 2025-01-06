def fazer_big_mac(nome):
    print(f"Big Mac {nome}")

def fazer_batata(tamanho):
    print(f"Batata {tamanho}")
    
def prepara_refri(sabor,tamanho):
    print(f"Refrigerante {sabor}{tamanho}")

#fazer_big_mac("Gleyson")
#fazer_big_mac("Flávio")
#fazer_big_mac("Rosangela")
#fazer_big_mac("Gleyson")
#fazer_batata("Grande")
#prepara_refri("Guaraná","Grande")

def fazer_combo_big_mac(nome, tamanho_batata, tipo_refri, tamanho_refri):
    fazer_big_mac(nome)
    fazer_batata(tamanho_batata)
    prepara_refri(tipo_refri, tamanho_refri)

fazer_combo_big_mac(f"Nome do pedido: ", "Grande", "Guaraná", "Médio")