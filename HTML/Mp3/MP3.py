from gtts import gTTS

texto = '''ABORDAGEM
1.	Inicia rota> chegou no endereço do cliente>  Inicia a WO
2.	Apresentação/ identificação pessoal
3.	Propé
4.	Pedir permissão pra entrar
5.	Confirmar a OS/pacotes e oferecer extensões telefônicas
6.	Confirmar local de instalação dos equipamentos e colocar o eMTA na tomada
7.	Explicar serviços inteligentes do telefone:
HABILITADOS
•	Identificador de chamadas
•	Chamada em espera
•	Conferência a 3
APÓS 1ª FATURA LIGA P/ HABILITAR
•	Bloqueio de Chamadas
•	Siga-me
8.	Wi-FI Analyser (ver se o local escolhido distribui sinal pra todos os cômodos)
•	Entre -10db e -70db
INSTALAÇÃO
9.	Confeccionar conectores RG6, RJ11 e RJ45
10.	Inicia a NR35 no Técnico Nota 10
11.	Anéis de Vedação na TAP e Cable Isolator
12.	Cable DROP na TAP (torque) / Pingadeira com tag identificadora / Amarração no U Span Clamp
13.	Cable Isolator (torque)
14.	Finaliza NR35 no Técnico Nota 10
15.	RG6 Branco > GHS2 (Two Way) (torque) > Decoder e eMTA
16.	Mini Isolator com Sleev (protetor) no eMTA
17.	Limpeza do Local
CONFIGURAÇÃO DO eMTA
1.	Reset de fábrica atrás do eMTA
2.	Conectar o aparelho no WI-FI
3.	Pelo celular ou Notebook acesse a página do eMTA digitando no navegador
•	192.168.0.1
4.	Login: Usuário e Senha padrão na etique do eMTA
5.	Troque o usuário e senha após logar
6.	Siga o passo a passo do próprio eMTA para terminar de configurar
7.	Configure e explique o Band Steering (2.4 e 5ghz em uma única rede)
8.	Fale e configure o “IoT”
9.	Verifique os níveis de sinal pelo
•	www.niveis.virtua.com.br
	TX: 38 a 51 / RX: -12 a 12
	SNR DS: > 35 / SNR US: > 27
10.	Teste de Velocidade:
•	www.brasilbandalarga.com.br
	para velocidades abaixo de 119 Mbps
•	wwwspeedtest.net
	para velocidades abaixo de 119 Mbps
11.	Demonstrar: www.clarotvmais.com.br
CONFIGURAÇÃO DO DECODER
1.	Apresente o Controle Remoto
2.	Menu > config > sist > 8291 > Reset de Fábrica
3.	Canais > tecla verde
4.	Menu > sist > instal >
5.	tx / rx / snr / ber
6.	Menu > sist > decoder (firmware/update)
7.	Menu > sist > conex IP >
8.	Menu > sist > diagn >
9.	Report Back:
•	Canal 262 + tecla azul *8291
10.	HIT: 
•	Canal 270
	explique
11.	Troque a senha de bloqueio e de compra e explique o serviço de bloqueio por canais e por idade
12.	Configuração de resolução e áudio
13.	Ativar e demonstrar o “PIP” (ativar, alternar e desativar)

'''

tts = gTTS(text=texto, lang='pt')
tts.save("audio_certificacao.mp3")
print("Áudio salvo como audio_certificacao.mp3")
