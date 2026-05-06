# Explicação do arquivo `debug.py`

O arquivo `debug.py` é um pequeno programa em Python que calcula o valor total de uma compra com três itens, aplicando imposto e desconto.

## Fluxo do programa

1. Entrada de dados:
   - recebe o nome do cliente;
   - pede a quantidade e o preço de três itens;
   - pergunta se o cliente possui um cupom de desconto em percentual.

2. Cálculo dos itens:
   - multiplica a quantidade pelo preço de cada item;
   - soma os totais de cada item para obter o subtotal.

3. Cálculo do imposto:
   - aplica 10% sobre o subtotal.

4. Cálculo do desconto:
   - aplica o percentual informado sobre o subtotal.

5. Total final:
   - soma o subtotal com o imposto e subtrai o desconto.

## Saída

O programa imprime na tela:
- nome do cliente;
- total de cada item;
- subtotal;
- valor do imposto;
- valor do desconto (se houver);
- total final da compra.

## Observações

- O imposto é fixo em 10%.
- O desconto é opcional e depende do valor digitado pelo usuário.
- O formato usa duas casas decimais para valores monetários.