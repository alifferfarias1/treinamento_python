from random import uniform 
print('Bem vindo ao meu jogo de batalha personagens de animes diversos\n escolha o seu personagem.')
print('Cada personagem tem atributos unicos ATK E HP, dependendo do local da luta podem enfraquecer ou ganhar buffs cada personagem tem 2 ataques.')

personagens_escolhidos = []
personagens_validos = ["Luffy", "Griffith(Femto)", "Hiei", "Sasuke"]

while True:
    def definir_personagem(personagem, jogador):
        if personagem == 'L':
            print(f'você escolheu(Player-{jogador}) o Luffy, o personagem tem 55 de ATK e 890 de HP possui bastante vida por ser de borracha.\n')
            vida = 890
            ataque = 55
            personagens = 'Luffy'

        elif personagem == 'G':
            print(f'você escolheu(Player-{jogador}) o Griffith(Femto), o personagem tem 70 de ATK e 700 de HP é balanceado por ser um tipo de demonio.\n')
            vida = 700
            ataque = 70
            personagens = 'Griffith'


        elif personagem == 'H':
            print(f'você escolheu(Player-{jogador}) o Hiei o personagem tem 80 de ATK e 600 de HP por ter habilidades de fogo poderosas.\n')
            vida = 600
            ataque = 80
            personagens = 'Hiei'

                
        elif personagem == 'S':
            print(f'você escolheu(Player-{jogador}) o Sasuke, o personagem tem 82 de ATK e 590 de HP e possui grande ataque pelas habilidades de ninjutsu.\n')
            vida = 590  
            ataque = 82
            personagens = 'Sasuke'

        else:
            print('personagem invalido.')
                
        return vida, ataque, personagens
    
    def ataque(personagem, nome):
        if personagem == 'L':
                
            ataque_bazooka = uniform(1.5, 2)
            ataque_balloon = 1.2
                
            print(f'Escolha o seu ataque {nome}')
            print('1 - Gomu Gomu No Bazooka: ')
            print('2 - Gomu Gomu No Ballon: ')
                
            escolha = input('Digite o numero correspondente ao ataque desejado: ')
        


            if escolha == '1':
                multiplicador = ataque_bazooka
                print('Você escolhe Gomu Gomu no Bazooka!')
                
                
            elif escolha == '2':
                multiplicador = ataque_balloon
                print('você escolheu Gomu Gomu no Fusen, diminui o próximo dano inimigo!')
                
            else:
                print('Ataque inválido!')
                multiplicador = 1
            
                
        if personagem == 'G':
            ataque_blackhole = uniform(1.6, 2.2)
            ataque_demonios = uniform(1.5, 1.8)
                    
            print(f'Escolha o seu ataque {nome}')
            print('1 - Black Hole: ')
            print('2 - Invocação de demonios: ')
                
            escolha= input('Digite o numero correspondente ao ataque desejado: ')
                

                    
            if escolha == '1':
                multiplicador = ataque_blackhole
                print('Você escolheu Black Hole!')
                
            elif escolha == '2':
                multiplicador = ataque_demonios
                print('Você invocou um demônio!')
            else:
                print('Ataque inválido!')
                multiplicador = 1
            
        if personagem == 'H':
            ataque_chamasnegras = uniform(1.7, 2)
            ataque_jaganshi = 1.3
                    
            print(f'Escolha o seu ataque {nome}')
            print('1 - Chamas negras mortais: ')
            print('2 - Jaganshi: ')
                
            escolha = input('Digite o numero correspondente ao ataque desejado: ')

                    
            if escolha == '1':
                multiplicador = ataque_chamasnegras
                print('Você escolheu Chamas negras mortais!')
                    
            if escolha == '1':
                    multiplicador = ataque_chamasnegras 
                    print('você escolheu Jaganshi e obteve um acerto crítico de 70%!')

                    
                
            elif escolha == '2':
                multiplicador = ataque_jaganshi
                print('você escolheu Jaganshi!')
                
            else:
                print('Ataque inválido!')
                multiplicador = 1
            
        if personagem == 'S':
            ataque_chidorionyx = uniform(2, 2.4)
            ataque_amenetojikara = uniform(1.4, 2.2)
                    
            print(f'Escolha o seu ataque {nome}')
            print('1 - Chidori Onyx: ')
            print('2 - Amenetojikara: ')
                
            escolha = input('Digite o numero correspondente ao ataque desejado: ')

                    
            if escolha == '1':
                multiplicador = ataque_chidorionyx
                print('Você escolheu Chidori Onyx!')
                
            elif escolha == '2':
                multiplicador = ataque_amenetojikara
        
                print('você escolheu Amenetojikara sasuke desvia!')
                
            else:
                print('Ataque inválido!')
                multiplicador = 1
                
        
        return multiplicador
    

    
    personagem_jogador1 =  input('Player-1 escolha entre, [L]uffy, [G]riffith(Femto), [H]iei, e [S]asuke(rinnesharingan): ').upper()
    personagem_jogador2 =  input('Player-2 escolha entre, [L]uffy, [G]riffith(Femto), [H]iei, e [S]asuke(rinnesharingan): ').upper()
    
    vida_p1,ataque_p1, nome = definir_personagem(personagem_jogador1, 1)
    vida_p2, ataque_p2, nome_2 = definir_personagem(personagem_jogador2, 2)
   
    while vida_p1 > 0 and vida_p2 > 0:
        multiplicador_p1 = ataque(personagem_jogador1, nome)
        multiplicador_p2 = ataque(personagem_jogador2, nome_2)
        ataque_final_p1 = ataque_p1 * multiplicador_p1 
        ataque_final_p2 = ataque_p2 * multiplicador_p2

            
        print(f'Player-1 {nome} causou o dano de:{ataque_final_p1:.2f} ponto(s) a Player-2 {nome_2}')
        vida_p2 -= (ataque_final_p1)
        print(f'vida de player-2 {nome_2} é de: {vida_p2:.2f}')
        
        print(f'Player-2 {nome_2} causou o dano de:{ataque_final_p2:.2f} ponto(s) a Player-1 {nome}')
        vida_p1 -= (ataque_final_p2)
        print(f'vida de player-1 {nome} é de: {vida_p1:.2f}')
        

    if vida_p2 <= 0:
        print(f'Player-1 Venceu!')
        break
                    
    if vida_p1 <= 0:
        print(f'Player-2 Venceu!')
        break
        




               
