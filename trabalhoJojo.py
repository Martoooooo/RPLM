# Jonathan, Dio, Speedwagon, Joseph, ACDC, Wham, Kars, Ceasar, Jotaro, Polnareff, Kakyoin, Josuke, Kira, Okuyasu, Koichi
import time 

print(  "⣿⣿⣿⣿⣿⣿⣿⡿⡛⠟⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"+
        "⣿⣿⣿⣿⣿⣿⠿⠨⡀⠄⠄⡘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"+
        "⣿⣿⣿⣿⠿⢁⠼⠊⣱⡃⠄⠈⠹⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"+
        "⣿⣿⡿⠛⡧⠁⡴⣦⣔⣶⣄⢠⠄⠄⠹⣿⣿⣿⣿⣿⣿⣿⣤⠭⠏⠙⢿⣿\n"+
        "⣿⡧⠠⠠⢠⣾⣾⣟⠝⠉⠉⠻⡒⡂⠄⠙⠻⣿⣿⣿⣿⣿⡪⠘⠄⠉⡄⢹\n"+
        "⣿⠃⠁⢐⣷⠉⠿⠐⠑⠠⠠⠄⣈⣿⣄⣱⣠⢻⣿⣿⣿⣿⣯⠷⠈⠉⢀⣾\n"+
        "⣿⣴⠤⣬⣭⣴⠂⠇⡔⠚⠍⠄⠄⠁⠘⢿⣷⢈⣿⣿⣿⣿⡧⠂⣠⠄⠸⡜\n"+
        "⣿⣇⠄⡙⣿⣷⣭⣷⠃⣠⠄⠄⡄⠄⠄⠄⢻⣿⣿⣿⣿⣿⣧⣁⣿⡄⠼⡿\n"+
        "⣿⣷⣥⣴⣿⣿⣿⣿⠷⠲⠄⢠⠄⡆⠄⠄⠄⡨⢿⣿⣿⣿⣿⣿⣎⠐⠄⠈\n"+
        "⣿⣿⣿⣿⣿⣿⢟⠕⠁⠈⢠⢃⢸⣿⣿⣶⡘⠑⠄⠸⣿⣿⣿⣿⣿⣦⡀⡉\n"+
        "⣿⣿⣿⣿⡿⠋⠄⠄⢀⠄⠐⢩⣿⣿⣿⣿⣦⡀⠄⠄⠉⠿⣿⣿⣿⣿⣿⣷\n"+
        "⣿⣿⣿⡟⠄⠄⠄⠄⠄⠋⢀⣼⣿⣿⣿⣿⣿⣿⣿⣶⣦⣀⢟⣻⣿⣿⣿⣿\n"+
        "⣿⣿⣿⡆⠆⠄⠠⡀⡀⠄⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"+
        "⣿⣿⡿⡅⠄⠄⢀⡰⠂⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n")
        
p1= input(" \n \n \nVocê gosta de jojo's? (s - sim \n" +
        "                      n - não \n" +
        "                      nv - nunca vi) \n" +
        "r: ")

while p1.lower() == "não" or p1.lower() == "n" or p1.lower() == "nao":
    p1= input("Você gosta de jojo's? ")

if p1.lower() == "nunca vi" or p1.lower()== "nv":
    print("\n https://www.crunchyroll.com/pt-br/jojos-bizarre-adventure/episode-1-dio-the-invader-652081 ")

elif p1.lower() == "sim" or p1.lower() == "s":
    
    p2= input("Suponha que você está de frente com essa mesa, cheia de lugares. Cada lugar possui 2 guardanapos: um à esquerda e outro a direita.\n Qual guardanapo você pegaria? O da esquerda?"+ 
            "O da direita? Ou seria mais um que espera a sua vez? \n" +
            "\n (Esquerda / Direita / Espero) \n r: ")

    if p2.lower() == "esquerda":
        print(f" \n Hm..... {p2.lower()}..... interessante escolha..... \n \n ")
        
        p3= input("Você é vidrado na natureza? \n" +
            " (s - sim \n" +
            "  n - não me interessa muito \n" +
            "  r: ")

        if p3.lower() == "sim" or p3.lower() == "s":
            p4= input("\nEstaria disposto a fazer qualquer coisa para salvar o planeta de humanos, seus maiores destruidores?\n "+
            " (s - sim \n" +
            "  n - não \n" +
            "  tf - tanto faz, o que der vontade) \n" +
            "  r: ")

            if p4.lower() == "sim" or p4.lower() == "s":
                print("\nVocê poderia acabar se entendendo com Kars. \nKars é um ser antigo, superior à maioria das formas de vida do planeta." + 
                " Kars supostamente surgiu quando a Terra se sentiu ameaçada pelos humanos, e como tentativa de se proteger, \nKars foi criado para realizar o serviço: executar os humanos e se tornar a forma de vida suprema.\n" +
                "Parabéns, você causou a destruição da humanidade por escolher o guardanapo errado")

            elif p4.lower() == "não" or p4.lower() == "n" or p4.lower() == "nao":
                print("\nVocê possui um traço de personalidade próximo de Wham. \n" +
                "Bom, quem não gosta de natureza neh? Wham é uma forma de vida antiga, ou melhor, um guerreiro, que preza, acima de tudo, por sua honra, não importanto seus objetivos principais")

            elif p4.lower() == "tf" or p4.lower() == "tanto faz":
                print("\nEsse traço de personalidade lembra o de Aisidisi \n" +
                " Aisidisi (ACDC) é uma forma de vida antiga. Porém, apesar de antigo, não é muito sábio. ACDC age na maioria das vezes de acordo com a ordem de seus superiores, mas as vezes pode acabar agindo impulsivamente por conta própria")

        elif p3.lower() == "não" or p3.lower() == "n" or p3.lower() == "não":
            p4= input("Dominação mundial parece algo que você faria? \n" +
            " (s - sim \n" +
            "  n - não \n" +
            "  r: ")

            if p4.lower() == "sim" or p4.lower() == "s":
                print("Hoh.... DIO...." +
                      "Sua característica marcante é o ego. \nDio nasceu e cresceu em uma família pobre, mas utiliza sua inteligência para manipular pessoas e subir na vida. Não deixa que nada atrapalhe sua jornada a caminho de seus objetivos.")
            
            elif p4.lower() == "não" or p4.lower() == "n" or p4.lower() == "não":
                print("Bom, não há muitas palavras para descrever Yoshikage Kira, com quem você se parece... \napenas: \nMeu nome é Yoshikage Kira. Tenho 33 anos. Minha casa fica na parte nordeste de Morioh, onde todas as casas estão, e eu não sou casado. Eu trabalho como funcionário das lojas de departamentos Kame Yu e chego em casa todos os dias às oito da noite, no máximo. Eu não fumo, mas ocasionalmente bebo. Estou na cama às 23 horas e me certifico de ter oito horas de sono, não importa o que aconteça. Depois de tomar um copo de leite morno e fazer cerca de vinte minutos de alongamentos antes de ir para a cama, geralmente não tenho problemas para dormir até de manhã. Assim como um bebê, eu acordo sem nenhum cansaço ou estresse pela manhã. Foi-me dito que não houve problemas no meu último check-up. Estou tentando explicar que sou uma pessoa que deseja viver uma vida muito tranquila. Eu cuido para não me incomodar com inimigos, como ganhar e perder, isso me faria perder o sono à noite. É assim que eu lido com a sociedade e sei que é isso que me traz felicidade. Embora, se eu fosse lutar, não perderia para ninguém.")

    elif p2.lower() == "direita":
        
        print( f" \nHm..... {p2.lower()}..... interessante escolha..... \n \n")
        
        p3= input("Se você visse uma pessoa em uma situação de risco, você a ajudaria? \n" +
                  "(s - sim \n" +
                  " n - não \n" +
                  " dh - depende do meu humor) \n" +
                  " r: ")
        
        if p3.lower() == "sim" or p3.lower() == "s":
            
            p4=input("Você gosta de répteis? \n" +
                     "(s - sim \n" +
                     " n - não \n" +
                     " rj - roubo junto \n"
                     " r: ")
            
            if p4.lower() == "sim" or p4.lower() == "s":
                
                print("\nvocê possui uma personalidade parecida à de Jonathan Joestar" +
                            "\nJonathan Joestar é filho de uma família rica, e quer fazer de tudo para mostrar que ele é de fato um cavalheiro de respeito")
                
            elif p4.lower() == "não" or p4.lower() == "n":
                print("\nVocê possui uma personalidade parecida à de Josuke Higashikata" +
                      "\nJosuke Higashikata é um estudante do ensino médio. Ele não é alguem a se temer, porem, pode se irritar caso insulte seus amigos ou seu penteado")

        elif p3.lower() == "n" or p3.lower() == "não" or p3.lower() == "nao":
            print("Hm.... que saco.... você tem uma personalidade semelhante à do Jotaro Kujoh \n" +
                  "Jotaro é um estudante do ensino médio. Ele é um personagem que não demonstra muitas emoções além de repulsa, odiando todos a sua volta constantemente.\n" +
                  "Apesar disso, ele é muito forte e inteligente, sendo assim capaz de superar suas dificuldades e ajudar quem ele quiser")
        
        elif p3.lower() == "dh" or p3.lower()== "depende do meu humor":
            print("\n Nice! você lembra um pouco Joseph Joestar \n" +
            "Joseph é um jovem muito esperto, e usa sua esperteza para surpreender e chocar as pessoas ao seu redor. Apesar disso, não é muito responsável, falando qualquer coisa que pensar em qualquer situação que se encontre.")
        
    elif p2.lower() == "espero":
        p3= input("Você se irrita fácil? \n" +
                     "(s - sim \n" +
                     " n - não \n" +
                     " r: ")
        
        if p3.lower() == "não" or p3.lower() == "n" or p3.lower() == "nao":
            p4= input("Você se preocupa demais com coisas pequenas? \n" +
                     "(s - sim \n" +
                     " n - não \n" +
                     " r: ")

            if p4.lower() == "sim" or p4.lower() == "s":
                print("Koichi \n" +
                "Koichi é inteligente, diligente e amigável. Ele expressa seu amor por sua família, tenta manter a auto-estima de seus amigos, e tende a julgar pessoas que ele não conhece como inocentes.")

            elif p4.lower() == "não" or p4.lower() == "n" or p3.lower() == "nao":
                p5= input("Você gosta de cereja?"  +
                    " (s - sim \n" +
                    "  n - não \n" +
                    "  r: ")

                if  p5.lower() == "sim" or p5.lower() == "s":
                    print( " Você lembra um pouco a personalidade do Kakyoin"+
                        "Kakyoin é um estudante durão, mas gentil e carismático. Ele consegue se manter calmo em quase qualquer situação, sendo difícil abalar seu psicológico")

                elif p5.lower() == "não" or p3.lower() == "nao" or p5.lower() == "n":
                    print("você lembra um pouco o..... desculpe.... CAEEEESAAAAAAAAAAR \n" +
                    "Caesar é um homem muito comprometido, focado e orgulhoso de suas raízes. Apesar de manter a calma na maioria das situações, é muito vingativo, e isso pode subir à sua cabeça em momentos ruins")

        elif p3.lower() == "sim" or p3.lower() == "s":
            
            p4= input("Você se importa demais com seu cabelo?"  +
            " (s - sim \n" +
            "  n - não \n" +
            "  r: ")
            
            if p4.lower() =="sim" or p4.lower() == "s":
                print("Trè Bien! Polraneff\n" + 
                "Polnareff é um francês orgulhoso e honroso acima de tudo, que faria de tudo por sua família. Ao mesmo tempo que essas características, Polnareff consegue ser bastante vingativo")
            
            elif p4.lower() == "não" or p4.lower() == "n" or p4.lower() == "nao":
                print("Você lembra um pouco a personalidade do Okuyasu \n" +
                "Okuyasu não é uma pessoa que pensa muito, agindo normalmente de acordo com sua emoção no momento.")