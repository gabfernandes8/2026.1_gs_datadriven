# ========================================
# SISTEMA DE ANÁLISE DE ATIVIDADE VULCÂNICA
# ========================================

# Listas para armazenar os dados

titulo="#### Monitoramento de Atividade Vulcânica via Satélite ####"
print(f'\n{titulo:^30}')

tipos_eventos = []
paises = []
regioes = []
cidades = []
areas_afetadas = []
intensidades = []
ocorrencias = []

# Entrada da quantidade de eventos
quantidade = int(input("Insira a quantidade de eventos: "))

# Cadastro dos eventos
for i in range(quantidade):

    print(f"\n--- Evento {i + 1} ---")

    tipo = input("Tipo de evento: ")
    pais = input("País: ")
    regiao = input("Região: ")
    cidade = input("Cidade: ")

    # Validação da área
    area = float(input("Área afetada (km²): "))
    while area <= 0:
        print("ERRO! A área deve ser maior que zero.")
        area = float(input("Área afetada (km²): "))

    # Validação da intensidade
    intensidade = int(input("Intensidade (1 a 10): "))
    while intensidade < 1 or intensidade > 10:
        print("ERRO! A intensidade deve estar entre 1 e 10.")
        intensidade = int(input("Intensidade (1 a 10): "))

    ocorrencia = int(input("Número de ocorrências: "))

    # Armazenando nas listas
    tipos_eventos.append(tipo)
    paises.append(pais)
    regioes.append(regiao)
    cidades.append(cidade)
    areas_afetadas.append(area)
    intensidades.append(intensidade)
    ocorrencias.append(ocorrencia)

# ========================================
# ANÁLISE DOS DADOS
# ========================================

# Total de eventos
total_eventos = len(tipos_eventos)

# Soma total das áreas afetadas
soma_areas = 0
for area in areas_afetadas:
    soma_areas += area

# Média das intensidades
soma_intensidades = 0
for intensidade in intensidades:
    soma_intensidades += intensidade

media_intensidade = soma_intensidades / total_eventos

# Evento com maior área afetada
maior_area = max(areas_afetadas)
indice_maior_area = areas_afetadas.index(maior_area)

# Região com maior número de ocorrências
maior_ocorrencia = max(ocorrencias)
indice_maior_ocorrencia = ocorrencias.index(maior_ocorrencia)
regiao_maior_ocorrencia = regioes[indice_maior_ocorrencia]

# Densidade média (ocorrências ÷ área)
soma_densidade = 0

for i in range(total_eventos):
    densidade = ocorrencias[i] / areas_afetadas[i]
    soma_densidade += densidade

densidade_media = soma_densidade / total_eventos

# Quantidade de eventos acima da média de intensidade
eventos_acima_media = 0

for intensidade in intensidades:
    if intensidade > media_intensidade:
        eventos_acima_media += 1

# Evento mais crítico
# Critério: intensidade + área afetada

maior_criticidade = 0
indice_critico = 0

for i in range(total_eventos):

    criticidade = intensidades[i] + areas_afetadas[i]

    if criticidade > maior_criticidade:
        maior_criticidade = criticidade
        indice_critico = i

# ========================================
# RELATÓRIO FINAL
# ========================================

print("\n========================================")
print("      RELATÓRIO DE ANÁLISE")
print("========================================")

print(f"\nTotal de eventos registrados: {total_eventos}")

print("\n----------------------------------------")
print("Resumo Geral")
print("----------------------------------------")

print(f"Área total afetada: {soma_areas} km²")
print(f"Média de intensidade: {media_intensidade:.1f}")

print("\n----------------------------------------")
print("Análises")
print("----------------------------------------")

print(f"Região com maior número de ocorrências: {regiao_maior_ocorrencia}")
print(f"Quantidade de eventos acima da média de intensidade: {eventos_acima_media}")
print(f"Densidade média de ocorrências: {densidade_media:.2f} ocorrências/km²")

print("\n----------------------------------------")
print("Evento Mais Crítico")
print("----------------------------------------")

print(f"Tipo: {tipos_eventos[indice_critico]}")
print(f"Local: {cidades[indice_critico]}, {regioes[indice_critico]}, {paises[indice_critico]}")
print(f"Intensidade: {intensidades[indice_critico]}")
print(f"Área afetada: {areas_afetadas[indice_critico]} km²")

print("\n========================================")
print(f"Total de desastres registrados: {total_eventos}")
print("========================================")
