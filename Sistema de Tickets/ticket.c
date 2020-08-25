/****************************************************************

                        TICKET SYSTEM
                          Descrição
Sistema para criação de eventos e venda de ingressos via terminal

                Instruções para compilar no CMD
 1) Tenha instalado na máquina o MinGW
 2) Adicione Acentuação UTF-8 no terminal > chcp 65001
 3) Crie o arquivo executavel > gcc -o executavel arquivo.c
 4) Rode o arquivo executavel: executavel.exe

                Instruções para compilar no VSCode
 1) Tenha instalado na máquina o MinGW
 2) Instale os plugins C/C++ e C/C++ Compile Run
 3) Adicione Acentuação UTF-8 no terminal > chcp 65001
 4) Pressione F6 para rodar a versão atualizada do arquivo

                Instruções para compilar online
 1) Acesse: https://www.onlinegdb.com/online_c_compiler 

 ****************************************************************/


#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <conio.h>
#include <math.h>

/* Declaração de Variáveis Globais */
int tecla;
char senha1[5];
char senha2[5];
int modo;
int login;
char evento[7];
int qtd_disp;
int qtd_vend;
int qtd_buy;
float valor;
float saldo;
float gasto;

/* Declaração de Funções Globais */
void limpar(void);
void enter(void);
void cabec(void);
void inicio(void);
void admin(void);
void usuario(void);

/* Função Principal */
int main()
{
    /* Primeiro Acesso */
    cabec();
    printf("Seja Bem Vindo(a), ao Sistema de Ingressos!\n");
    printf("Ambiente de Configuração do Sistema - Primeiro Acesso\n\n");
    enter();
    printf("Defina a senha de administração do sistema (4 dígitos):\n");
    fgets(senha1, 5, stdin);
    limpar();
    printf("\nSua senha foi definida com sucesso!\n");
    printf("A próxima etapa é configurar os ingressos como administrador!\n");
    enter();
    inicio();
    return 0;
}

/* Função Limpar */
void limpar(void){
    char c;
    while ((c = getchar()) != '\n' && c != EOF);
}
/* Função pressione qualquer tecla */
void enter(void){
    printf("\nPressione ENTER - Continuar\nPressione ESC - Sair\n\n");
    tecla = getch();
    if(tecla == 27) {
        exit(1);
    } else {
    } 
    return;
}

/* Função Cabeçário */
void cabec(void){
    printf("=======================================================\n");
    return;
}

/* Função Início */
void inicio(void){
    /* Ambiente de utilização da Máquina */
    cabec();
    printf("Seja Bem Vindo(a) ao Sistema de Ingressos!\n");
    printf("Escolha o modo de acesso:\n");
    printf("[1] Usuário\n[2] Administrador:\n");
    scanf("%i",&modo);
    limpar();
    
    switch (modo){
        
        /* Ambiente de Usuário */
        case 1:
        cabec();
        printf("Olá você entrou no modo de usuário!\n");
        usuario();
        break;
        
        /* Ambiente de Administrador */
        case 2:
        cabec();
        printf("Olá você entrou no modo de administrador!\n");
            /* Solicitação de senha de administrador */
             printf("Digite sua senha para continuar:\n");
            setbuf(stdin,NULL);
            fgets(senha2, 5, stdin);
            limpar();
            login = strcmp(senha1, senha2);
            if(login == 0){
                printf("Acesso permitido!\n\n");
                admin();
            }else{
                printf("Acesso negado!\n");
                cabec();
                inicio();
            }
        break;
    }
    
    return;
}

/* Função Administrador */
void admin(void){
    modo = 0;
    printf("Selecione a operação:\n[1] Criar Ingressos\n[2] Ver Saldo do Sistema\n[3] Redefinir senha de Administrador\n");
    scanf("%i",&modo);
    limpar();
    switch (modo){
        
        /* Ambiente Criar Ingressos */
        case 1:
        printf("\nDefina o nome do evento (Máx: 6 caracteres):\n>>>");
        fgets(evento, 7, stdin);
        limpar();

        printf("Defina a quantidade de ingressos a ser vendida:\n>>>");
        scanf("%i",&qtd_disp);
        limpar();

        printf("Defina o preço individual dos ingressos:\n>>>R$ ");
        scanf("%f",&valor);
        limpar();

        printf("Ingressos criados com sucesso!\n\n");
        printf("Valor dos Ingressos: R$ %.2f \n\n", (float)valor);
        break;
        /* Ambiente Saldo do Sistema */
        case 2:
        
        printf("Saldo do sistema: R$ %.2f.\n\n", saldo);
        break;

        /* Ambiente Redefinir Senha */
        case 3:
        printf("Digite sua nova senha de Administrador:\n");
        fgets(senha1, 5, stdin);
        limpar();
        printf("Senha redefinida com sucesso!\n\n");
        break;
    }
    inicio();
    return;
}

/* Função Usuário */
void usuario(){
    modo = 0;
    printf("Selecione a operação:\n[1] Comprar Ingressos\n[2] Visualizar Evento, Ingressos e Valores\n");
    scanf("%i",&modo);
    limpar();
    switch (modo){
        
        /* Ambiente Comprar Ingressos */
        case 1:
        printf("Defina a quantidade de ingressos que deseja comprar:\n");
        scanf("%i",&qtd_buy);
        limpar();
        gasto = (qtd_buy * valor);
        printf("Operação Finalizada!\nVocê comprou %i ingressos e gastou R$%.2f.!\n\n", qtd_buy, gasto);
            /* Retira ingresso do sistema */
            qtd_disp = qtd_disp - qtd_buy;
            /* Entra dinheiro no sistema */
            saldo = saldo + gasto;
        inicio();
        break;
        /* Ambiente Ver Evento e Ingressos Disponíveis */
        case 2:
         printf("Nome do Evento: %s\nIngressos Disponíveis: %i\nValor dos Ingressos: R$%.2f \n\n", evento, qtd_disp, valor);
        cabec();
        usuario();
        break;
    }
    return;
}