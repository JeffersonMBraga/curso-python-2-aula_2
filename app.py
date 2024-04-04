from modelos.restaurante import Restaurante
from modelos.cardapio.bebidas import Bebidas
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebidas ('Suco de Manga', 12.0, 'Grande')
bebida_suco.aplicar_desconto()
prato_pao_de_queijo = Prato ('Pao de queijo', 20.00, 'Um pão de queijo tipicamente Mimeiro')
prato_pao_de_queijo.aplicar_desconto()
restaurante_praca.adcionar_ao_cardapio(bebida_suco)
restaurante_praca.adcionar_ao_cardapio(prato_pao_de_queijo)

def main():
    restaurante_praca.exibir_cardapio


if __name__ == '__main__':
    main()