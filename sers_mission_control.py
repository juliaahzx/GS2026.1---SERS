# ============================================================
# SERS MISSION CONTROL AI
# Sistema Inteligente de Monitoramento de Energia Renovavel
# em Missao Espacial Experimental
# ============================================================
# Projeto desenvolvido para a Global Solution - SERS
# Tema: Solucoes em Energias Renovaveis e Sustentaveis
# ============================================================

nome_missao = "SERS ORBITAL - IRON X"
nome_equipe = "IRON"

# Estrutura dos dados simulados por ciclo:
# [temperatura, comunicacao, bateria, geracao_solar, consumo_energia, estabilidade]
# temperatura: graus Celsius
# comunicacao: percentual de qualidade do sinal
# bateria: percentual de carga disponivel
# geracao_solar: energia gerada pelos paineis solares em kWh
# consumo_energia: energia consumida pelos modulos em kWh
# estabilidade: percentual de estabilidade operacional

dados_missao = [
    [19, 97, 95, 88, 42, 96],
    [23, 89, 84, 80, 51, 88],
    [28, 74, 69, 63, 67, 79],
    [33, 61, 53, 45, 82, 67],
    [37, 45, 34, 28, 94, 49],
    [29, 58, 47, 55, 76, 63],
]

areas_monitoradas = [
    "Controle termico",
    "Comunicacao orbital",
    "Bateria principal",
    "Geracao solar renovavel",
    "Consumo energetico",
    "Estabilidade operacional",
]


# ============================================================
# FUNCOES DE APOIO
# ============================================================

def calcular_pontos(status):
    """Converte o status operacional em pontuacao de risco."""
    if status == "CRITICO":
        return 2
    elif status == "ATENCAO":
        return 1
    return 0


def classificar_ciclo(pontos):
    """Classifica o risco total de um ciclo monitorado."""
    if pontos <= 2:
        return "MISSAO ESTAVEL"
    elif pontos <= 5:
        return "MISSAO EM ATENCAO"
    return "MISSAO CRITICA"


def calcular_media(indice):
    """Calcula a media de uma coluna dos dados simulados."""
    soma = 0

    for ciclo in dados_missao:
        soma += ciclo[indice]

    return soma / len(dados_missao)


def calcular_indice_sustentabilidade(geracao_solar, consumo_energia):
    """
    Calcula um indice simples de sustentabilidade energetica.
    Quanto maior o percentual, melhor a relacao entre energia renovavel gerada
    e energia consumida pelos modulos da missao.
    """
    if consumo_energia == 0:
        return 100

    return (geracao_solar / consumo_energia) * 100


# ============================================================
# ANALISES DOS MODULOS
# ============================================================

def analisar_temperatura(valor):
    if valor < 18:
        return "ATENCAO", "Temperatura abaixo do recomendado"
    elif valor <= 30:
        return "NORMAL", "Temperatura controlada"
    elif valor <= 35:
        return "ATENCAO", "Aumento termico identificado"
    return "CRITICO", "Superaquecimento detectado"


def analisar_comunicacao(valor):
    if valor < 30:
        return "CRITICO", "Comunicacao critica com a base"
    elif valor <= 59:
        return "ATENCAO", "Oscilacao de sinal"
    return "NORMAL", "Comunicacao estavel"


def analisar_bateria(valor):
    if valor < 20:
        return "CRITICO", "Energia da bateria em nivel critico"
    elif valor <= 49:
        return "ATENCAO", "Nivel da bateria reduzido"
    return "NORMAL", "Bateria operacional estavel"


def analisar_geracao_solar(valor):
    if valor < 30:
        return "CRITICO", "Geracao solar insuficiente para sustentar os modulos"
    elif valor <= 60:
        return "ATENCAO", "Geracao solar abaixo do ideal"
    return "NORMAL", "Geracao solar renovavel adequada"


def analisar_consumo_energia(valor):
    if valor > 90:
        return "CRITICO", "Consumo energetico excessivo"
    elif valor > 70:
        return "ATENCAO", "Consumo energetico elevado"
    return "NORMAL", "Consumo energetico controlado"


def analisar_estabilidade(valor):
    if valor < 40:
        return "CRITICO", "Estabilidade severamente comprometida"
    elif valor <= 69:
        return "ATENCAO", "Instabilidade operacional"
    return "NORMAL", "Sistemas estabilizados"


def analisar_sustentabilidade(indice):
    if indice < 40:
        return "CRITICO", "Baixa sustentabilidade energetica da operacao"
    elif indice < 80:
        return "ATENCAO", "Sustentabilidade energetica moderada"
    return "NORMAL", "Operacao energeticamente sustentavel"


# ============================================================
# TOMADA DE DECISAO AUTOMATIZADA
# ============================================================

def gerar_recomendacao(status, indice_sustentabilidade):
    """Gera uma resposta automatizada com base no risco do ciclo."""
    if status.count("CRITICO") >= 3:
        return "Acionar protocolo emergencial, reduzir consumo e priorizar modulos essenciais."

    if "CRITICO" in status and indice_sustentabilidade < 40:
        return "Ativar modo economia extrema e redirecionar energia para suporte vital e comunicacao."

    if "CRITICO" in status:
        return "Realizar intervencao imediata no sistema afetado."

    if "ATENCAO" in status and indice_sustentabilidade < 80:
        return "Intensificar monitoramento e otimizar o uso de energia renovavel."

    if "ATENCAO" in status:
        return "Monitoramento intensificado recomendado."

    return "Operacao nominal mantida com uso eficiente de energia renovavel."


def sugerir_acao_energetica(geracao_solar, consumo_energia, bateria):
    """Sugere uma acao especifica para melhorar eficiencia e sustentabilidade."""
    if geracao_solar < consumo_energia and bateria <= 49:
        return "Reduzir cargas nao essenciais e priorizar recarga da bateria."

    if geracao_solar < consumo_energia:
        return "Ajustar orientacao dos paineis solares e reduzir consumo secundario."

    if bateria >= 80 and geracao_solar > consumo_energia:
        return "Armazenar excedente de energia para ciclos de baixa geracao."

    return "Manter equilibrio entre geracao renovavel e consumo dos modulos."


def analisar_tendencia(riscos):
    if riscos[-1] > riscos[0]:
        return "A missao apresentou piora progressiva."
    elif riscos[-1] < riscos[0]:
        return "A missao apresentou recuperacao operacional."
    return "A missao permaneceu estavel."


def identificar_area_mais_afetada(riscos_area):
    maior = max(riscos_area)
    indice = riscos_area.index(maior)
    return areas_monitoradas[indice], maior


# ============================================================
# VISUALIZACAO SIMPLIFICADA
# ============================================================

def gerar_barra(valor, maximo=100, tamanho=20):
    """Gera uma barra visual simples para exibicao no terminal."""
    quantidade = int((valor / maximo) * tamanho)

    if quantidade > tamanho:
        quantidade = tamanho

    return "#" * quantidade + "-" * (tamanho - quantidade)


def exibir_dashboard_ciclo(numero, ciclo, resultados, risco_total, indice_sustentabilidade, recomendacao):
    temperatura, comunicacao, bateria, geracao_solar, consumo_energia, estabilidade = ciclo

    print(f"\nCICLO {numero}")
    print("-" * 78)

    print(f"Temperatura:       {temperatura:>6} C  | {resultados[0][0]:<7} | {resultados[0][1]}")
    print(f"Comunicacao:       {comunicacao:>6}%   | {resultados[1][0]:<7} | {resultados[1][1]}")
    print(f"Bateria:           {bateria:>6}%   | {resultados[2][0]:<7} | {resultados[2][1]}")
    print(f"Geracao solar:     {geracao_solar:>6} kWh | {resultados[3][0]:<7} | {resultados[3][1]}")
    print(f"Consumo energia:   {consumo_energia:>6} kWh | {resultados[4][0]:<7} | {resultados[4][1]}")
    print(f"Estabilidade:      {estabilidade:>6}%   | {resultados[5][0]:<7} | {resultados[5][1]}")
    print(f"Sustentabilidade:  {indice_sustentabilidade:>6.2f}% | {resultados[6][0]:<7} | {resultados[6][1]}")

    print("\nVisualizacao rapida:")
    print(f"Bateria          [{gerar_barra(bateria)}] {bateria}%")
    print(f"Comunicacao      [{gerar_barra(comunicacao)}] {comunicacao}%")
    print(f"Estabilidade     [{gerar_barra(estabilidade)}] {estabilidade}%")
    print(f"Sustentabilidade [{gerar_barra(indice_sustentabilidade)}] {indice_sustentabilidade:.2f}%")

    print(f"\nPontuacao de risco: {risco_total}")
    print(f"Status do ciclo: {classificar_ciclo(risco_total)}")
    print(f"Recomendacao automatizada: {recomendacao}")
    print(f"Acao energetica sugerida: {sugerir_acao_energetica(geracao_solar, consumo_energia, bateria)}")


# ============================================================
# RELATORIO FINAL
# ============================================================

def gerar_relatorio_final(riscos_ciclos, riscos_area, indices_sustentabilidade):
    print("\n" + "=" * 78)
    print("RELATORIO FINAL DA MISSAO")
    print("=" * 78)

    print(f"Missao: {nome_missao}")
    print(f"Equipe: {nome_equipe}")
    print(f"Ciclos monitorados: {len(dados_missao)}")

    print("\nMedias monitoradas:")
    print(f"Temperatura media:       {calcular_media(0):.2f} C")
    print(f"Comunicacao media:       {calcular_media(1):.2f}%")
    print(f"Bateria media:           {calcular_media(2):.2f}%")
    print(f"Geracao solar media:     {calcular_media(3):.2f} kWh")
    print(f"Consumo energetico medio:{calcular_media(4):.2f} kWh")
    print(f"Estabilidade media:      {calcular_media(5):.2f}%")
    print(f"Sustentabilidade media:  {sum(indices_sustentabilidade) / len(indices_sustentabilidade):.2f}%")

    maior_risco = max(riscos_ciclos)
    ciclo_critico = riscos_ciclos.index(maior_risco) + 1
    risco_medio = sum(riscos_ciclos) / len(riscos_ciclos)

    print("\nAnalise de risco:")
    print(f"Ciclo mais critico: {ciclo_critico}")
    print(f"Maior risco registrado: {maior_risco}")
    print(f"Risco medio da missao: {risco_medio:.2f}")
    print(f"Tendencia operacional: {analisar_tendencia(riscos_ciclos)}")

    print("\nPontuacao acumulada por area:")
    for i in range(len(areas_monitoradas)):
        print(f"{areas_monitoradas[i]}: {riscos_area[i]} pontos")

    area, pontos = identificar_area_mais_afetada(riscos_area)
    print("\nArea mais afetada:")
    print(f"{area} ({pontos} pontos)")

    print("\nClassificacao final:")
    if risco_medio <= 2:
        print("MISSAO ESTAVEL")
    elif risco_medio <= 5:
        print("MISSAO EM ATENCAO")
    else:
        print("MISSAO CRITICA")

    print("\nImpacto potencial da solucao:")
    print("O sistema apoia o monitoramento inteligente de missoes espaciais que dependem")
    print("de energia renovavel, permitindo identificar falhas, reduzir desperdicios")
    print("energeticos e automatizar respostas diante de situacoes criticas simuladas.")


# ============================================================
# EXECUCAO PRINCIPAL
# ============================================================

def executar_sistema():
    riscos_ciclos = []
    riscos_area = [0, 0, 0, 0, 0, 0]
    indices_sustentabilidade = []

    print("=" * 78)
    print("SERS MISSION CONTROL AI")
    print("Sistema Inteligente de Monitoramento de Energia Renovavel")
    print("=" * 78)
    print(f"Missao: {nome_missao}")
    print(f"Equipe: {nome_equipe}")
    print("=" * 78)

    for numero, ciclo in enumerate(dados_missao, start=1):
        temperatura, comunicacao, bateria, geracao_solar, consumo_energia, estabilidade = ciclo

        indice_sustentabilidade = calcular_indice_sustentabilidade(geracao_solar, consumo_energia)
        indices_sustentabilidade.append(indice_sustentabilidade)

        resultados = [
            analisar_temperatura(temperatura),
            analisar_comunicacao(comunicacao),
            analisar_bateria(bateria),
            analisar_geracao_solar(geracao_solar),
            analisar_consumo_energia(consumo_energia),
            analisar_estabilidade(estabilidade),
            analisar_sustentabilidade(indice_sustentabilidade),
        ]

        status = []
        risco_total = 0

        # Somente as 6 areas principais entram na pontuacao acumulada por area.
        # O indice de sustentabilidade influencia a recomendacao automatizada.
        for i in range(6):
            classificacao = resultados[i][0]
            status.append(classificacao)

            pontos = calcular_pontos(classificacao)
            risco_total += pontos
            riscos_area[i] += pontos

        # Acrescenta o status de sustentabilidade na decisao automatizada.
        status.append(resultados[6][0])

        riscos_ciclos.append(risco_total)

        recomendacao = gerar_recomendacao(status, indice_sustentabilidade)

        exibir_dashboard_ciclo(
            numero,
            ciclo,
            resultados,
            risco_total,
            indice_sustentabilidade,
            recomendacao,
        )

    gerar_relatorio_final(riscos_ciclos, riscos_area, indices_sustentabilidade)


if __name__ == "__main__":
    executar_sistema()
