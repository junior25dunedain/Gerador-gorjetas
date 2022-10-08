import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt


# gerar variáveis de universo
# qualidade e serviço em faixas subjetivas [0,10]
# gorjetas tem um intervalo de [0,25] %
x_qual = np.arange(0,11,1)
x_serv = np.arange(0,11,1)
x_tip = np.arange(0,26,1)

# notas
nota_comida = 10
nota_servico = 10

# gerar as funções de associação difusas
qual_lo = fuzz.trapmf(x_qual, [0, 0, 1,4])
qual_md = fuzz.trapmf(x_qual,[1,4,6,9])
qual_hi = fuzz.trapmf(x_qual,[6,9,10,10])


serv_lo = fuzz.gaussmf(x_serv,0,1.45)
serv_md = fuzz.gaussmf(x_serv,5,1.45)
serv_hi = fuzz.gaussmf(x_serv,10,1.45)

tip_lo = fuzz.trimf(x_tip,[0,0,13])
tip_md = fuzz.trimf(x_tip,[0,13,25])
tip_hi = fuzz.trimf(x_tip,[13,25,25])    # o primeiro argumento é um vetor que representa a variavel independente,
                                         # cujo os seus valores irão criar as respostas da função de pertinencia triangular
                                         # O segundo parametro da função 'trimf' deve ser um array [a,b,c] com 3 elementos,
                                         # que vai controlar a forma da função triangular, obedecendo esta regra (a <= b <= c).
                                         # Função trapezoidal que possui uma sintaxe semelhante a da função triangular

#visualiza esses universos e funções de associação
fig, (ax0, ax1,ax2)= plt.subplots(nrows=3, figsize=(8,9))

ax0.plot(x_qual, qual_lo,'b',linewidth=1.5, label='Ruim')
ax0.plot(x_qual, qual_md,'g',linewidth=1.5, label='Razoável')
ax0.plot(x_qual, qual_hi,'r',linewidth=1.5, label='Excelente')
ax0.set_title("Qualidade da comida")
ax0.legend()

ax1.plot(x_serv, serv_lo,'b',linewidth=1.5, label='Ruim')
ax1.plot(x_serv, serv_md,'g',linewidth=1.5, label='Razoável')
ax1.plot(x_serv, serv_hi,'r',linewidth=1.5, label='Excelente')
ax1.set_title("Qualidade do serviço")
ax1.legend()

ax2.plot(x_tip, tip_lo,'b',linewidth=1.5, label='Baixo')
ax2.plot(x_tip, tip_md,'g',linewidth=1.5, label='Médio')
ax2.plot(x_tip, tip_hi,'r',linewidth=1.5, label='Alta')
ax2.set_title("Valor da gorjeta")
ax2.legend()

#turn off top/right axes
for ax in (ax0,ax1,ax2):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

plt.tight_layout()
plt.show()

# fuzzificação

ou = fuzz.fuzzy_or(x_qual,fuzz.interp_membership(x_qual,qual_lo, nota_comida),x_serv,fuzz.interp_membership(x_serv, serv_lo,nota_servico))
regra1 = ou[1]


e = fuzz.fuzzy_and(x_tip,regra1,x_tip,tip_lo)
tip_activation_lo = e[1]

u = fuzz.fuzzy_and(x_tip,fuzz.interp_membership(x_serv, serv_md,nota_servico),x_tip,tip_md)
tip_activation_md = u[1]

ou2 = fuzz.fuzzy_or(x_qual,fuzz.interp_membership(x_qual,qual_hi, nota_comida),x_serv,fuzz.interp_membership(x_serv, serv_hi,nota_servico))
regra3 = ou2[1]

u2 = fuzz.fuzzy_and(x_tip,regra3,x_tip,tip_hi)
tip_activation_hi = u2[1]

tip0 = np.zeros_like(x_tip)

# visualizar resultados
fig, ax0 = plt.subplots(figsize=(8,3))

ax0.fill_between(x_tip,tip0,tip_activation_lo,facecolor='b',alpha=0.7)
ax0.plot(x_tip,tip_lo,'b',linewidth=0.5,linestyle='--')
ax0.fill_between(x_tip,tip0,tip_activation_md,facecolor='g',alpha=0.7)
ax0.plot(x_tip,tip_md,'g',linewidth=0.5,linestyle='--')
ax0.fill_between(x_tip,tip0,tip_activation_hi,facecolor='r',alpha=0.7)
ax0.plot(x_tip,tip_hi,'r',linewidth=0.5,linestyle='--')
ax0.set_title('Saida da função de implicação')

for ax in (ax0,):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

plt.tight_layout()
plt.show()

# defuzzificação

agregacao = np.fmax(tip_activation_lo,np.fmax(tip_activation_md,tip_activation_hi))

gorjeta = fuzz.centroid(x_tip,agregacao) # pode-se usar diretamente a função centroid(x,mfx) para a defuzzificação
print(gorjeta)

tip_activation = fuzz.interp_membership(x_tip,agregacao,gorjeta)

# visualizr a gorjeta final
fig, ax0 = plt.subplots(figsize=(8,3))

ax0.plot(x_tip,tip_lo, 'b',linewidth=0.5, linestyle='--',)
ax0.plot(x_tip,tip_md, 'g',linewidth=0.5, linestyle='--')
ax0.plot(x_tip,tip_hi, 'r',linewidth=0.5, linestyle='--')
ax0.fill_between(x_tip, tip0, agregacao, facecolor='Orange',alpha=0.7)
ax0.plot([gorjeta,gorjeta],[0,tip_activation],'k',linewidth=1.5,alpha=0.9)
ax0.set_title('Agregação das saídas e resultados (ver linha)')

for ax in (ax0,):
    ax.spines['top'].set_visible(False) # remove o eixo superior
    ax.spines['right'].set_visible(False) # remove o eixo direito
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

plt.tight_layout()
plt.show()