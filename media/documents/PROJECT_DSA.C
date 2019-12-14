#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<time.h>
#include<math.h>
#include<conio.h>
#include<windows.h>



#define RED   "x1B[31m"
#define GRN   "x1B[32m"
#define YEL   "x1B[33m"
#define BLU   "x1B[34m"
#define MAG   "x1B[35m"
#define CYN   "x1B[36m"
#define WHT   "x1B[37m"
#define RESET "x1B[0m"

void choose_level();
void showHangMan(int);
int easy(void);
int intermid(void);
int hard(void);

int main()
{
    srand(time(0));
    printf("\n");
    printf(RED"\t\t\n"RESET);
    printf(RED"\t\t|  |  |  |  ---|/%c|  |  |  |  |\n"RESET,'\\');
    Sleep(1);
    printf("\t\t|  |  | |  |%c  ||   |%c  /|  ||  |%c  |\n",'\\','\\','\\');
    Sleep(1);
    printf(RED"\t\t|  ||  |%c  ||  |%c /|  ||  |%c  |\n"RESET,'\\','\\','\\');
    Sleep(1);
    printf("\t\t|  |  |  |  | %c  ||   |%c/ |  |  |  |  %c  |\n",'\\','\\','\\');
    Sleep(1);
    printf(RED"\t\t|----|  |---|  |  %c  ||  __|   |  ||----|  |  %c  |\n"RESET,'\\','\\');
    Sleep(1);
    printf("\t\t|  ||  ||  %c  ||  |||  ||  ||  %c |\n",'\\','\\');
    Sleep(1);
    printf(RED"\t\t|  ||  || %c ||  ||  ||  || %c |\n"RESET,'\\','\\');
    Sleep(1);
    printf("\t\t|  ||  ||  %c ||  || || ||  %c|\n",'\\','\\');
    Sleep(1);
    printf(RED"\t\t|  ||  ||  |%c___/ |  ||  ||  |\n"RESET,'\\');
    printf("\n");
    printf("\n\n WELCOEME TO HANGMAN GAME \n\n");
    printf("--------------------------------------\n");
    usleep(3);
    printf("Please choose the difficulty level to start the game.\n");
    printf("\nDifficulties\n");
    printf(GRN "SWITCH 1---Easiest level\n"RESET);
    printf("               6 guesses\n\n");
    printf(YEL "SWITCH 2---Intermediate Level\n"RESET);
    printf("               5 guesses\n\n");
    printf(RED "SWITCH 3---Hard Level\n"RESET);
    printf("               4 guesses\n\n");
    choose_level();
    return(0);

}

int easy(void)
{
    char hangmanWord[100],tempWord[100];
    char hangmanOutput[100];
    int wrongTry=6,matchFound=0;

    int counter=0,position=0,winner,length,i;
    char alphabetFromUser;
    system("cls");
    printf("\n\nEnter any word in spell case and hit ENTER");
    printf("\n\n\t Entere here: ");
    scanf("%s",hangmanWord);
    printf("\n\n Now give the computer to your friend and see if they can crack it");
    printf("\n\n\t Hit Enter");
    getch();
    length=strlen(hangmanWord);
    system("cls");
    printf("\n\n WELCOME TO HANGMAN GAME \n\n\n");
    printf("\n\n You will get 6 chances to guess the right word ");
    printf("\n\n So help the Man and set set go ");
    getch();
    printf("\n\n\t Hit Enter");
    getch();
    system("cls");
    printf("\n\t|| ----");
    printf("\n\t||  |  ");
    printf("\n\t|| ");
    printf("\n\t|| ");
    printf("\n\t|| ");
    printf("\n\t|| ");
    printf("\n\n The word has %d alphabets \n\n",length);

    for(i=0; i<length; i++)
    {
        hangmanOutput[i]='_ ';
        hangmanOutput[length]='\0';
    }
    for(i=0; i<length; i++)
    {
        printf(" ");
        printf("%c",hangmanOutput[i]);
    }
    while(wrongTry!=0)
    {
        matchFound = 0;
        printf("\n\n Enter any alphabet from a to z and use small case ");
        printf("\n\n\t Enter here ");
        fflush(stdin);
        scanf("%c",&alphabetFromUser);
        if(alphabetFromUser<'a'||alphabetFromUser>'z')
        {
            system("cls");
            printf("\n\n\t Wrong Input ");
            matchFound=2;
        }
        fflush(stdin);
        if(matchFound!=2)
        {
            for(counter=0; counter<length; counter++)
            {
                if(alphabetFromUser==hangmanWord[counter])
                {
                    matchFound=1;
                }
            }
            if(matchFound==0)
            {
                printf("\n\t:You have %d tries left ",--wrongTry);
                getch();
                showHangman(wrongTry);
                getch();
            }
            else
            {
                for(counter=0; counter<length; counter++)
                {
                    matchFound=0;
                    if(alphabetFromUser==hangmanWord[counter])
                    {
                        position=counter;
                        matchFound=1;
                    }
                    if(matchFound==1)
                    {
                        for(i=0; i<length; i++)
                        {
                            if(i==position)
                            {
                                hangmanOutput[i]=alphabetFromUser;
                            }
                            else if(hangmanOutput[i]>='a'&& hangmanOutput[i]<='z')
                            {
                                continue;
                            }
                            else
                            {
                                hangmanOutput[i]='_';
                            }
                        }
                        tempWord[position]=alphabetFromUser;
                        tempWord[length]='\0';
                        winner=strcmp(tempWord,hangmanWord);
                        if(winner==0)
                        {
                            printf("\n\n\t\t You are the winner!! ");
                            printf("\n\n\t The Word was %s ",hangmanWord);
                            printf("\n\n\n\n\t EASY HUH ?? \n\n ");
                            getch();
                            return 0;
                        }
                    }
                }
            }
        }
        printf("\n\n\t");
        for(i=0; i<length; i++)
        {
            printf(" ");
            printf("%c",hangmanOutput[i]);
        }
        getch();
    }
    if(wrongTry<=0)
    {
        printf("\n\n\t The Word was %s",hangmanWord);
        printf("\n\n\t The Man is dead ");
        printf("\n\n\t Better luck Next Time ");
    }
    getch();
    return 0;
}

int intermid(void)
{
    char hangmanWord[100],tempWord[100];
    char hangmanOutput[100];
    int wrongTry=4, matchFound=0;
    int counter=0,position=0,winner,length,i;
    char alphabetFromUser;
    system("cls");
    printf("\n\n Enter any word in small case and hit enter");
    printf("\n\n\t Enter here");
    scanf("%s",&hangmanWord);
    printf(" Now see if they can crack it ");
    printf("\n\n\t HIT ENTER");
    getch();
    length=strlen(hangmanWord);
    system("cls");
    printf("\n\n Welcome to hangman game \n\n\n");
    printf("\n\n You will get 4 chances to guess the right word ");
    printf("\n\n So help the Man and set set go ");
    getch();
    printf("\n\n\t Hit Enter");
    getch();
    system("cls");
    printf("\n\t|| ----");
    printf("\n\t||  |  ");
    printf("\n\t|| ");
    printf("\n\t|| ");
    printf("\n\t|| ");
    printf("\n\t|| ");
    printf("\n\n The word has %d alphabets \n\n",length);

    for(i=0; i<length; i++)
    {
        hangmanOutput[i]='_ ';
        hangmanOutput[length]='\0';
    }
    for(i=0; i<length; i++)
    {
        printf(" ");
        printf("%c",hangmanOutput[i]);
    }
    while(wrongTry!=0)
    {
        matchFound=0;
        printf("\n\n Enter any alphabet from a to z and use small case ");
        printf("\n\n\t Enter here ");
        fflush(stdin);
        scanf("%c",&alphabetFromUser);
        if(alphabetFromUser<'a'||alphabetFromUser>'z')
        {
            system("cls");
            printf("\n\n\t Wrong Input ");
            matchFound=2;
        }
        fflush(stdin);
        if(matchFound!=2)
        {
            for(counter=0; counter<length; counter++)
            {
                if(alphabetFromUser==hangmanWord[counter])
                {
                    matchFound=1;
                }
            }
            if(matchFound==0)
            {
                printf("\n\t:You have %d tries left ",--wrongTry);
                getch();
                showHangman(wrongTry);
                getch();
            }
            else
            {
                for(counter=0; counter<length; counter++)
                {
                    matchFound=0;
                    if(alphabetFromUser==hangmanWord[counter])
                    {
                        position=counter;
                        matchFound=1;
                    }
                    if(matchFound==1)
                    {
                        for(i=0; i<length; i++)
                        {
                            if(i==position)
                            {
                                hangmanOutput[i]=alphabetFromUser;
                            }
                            else if(hangmanOutput[i]>='a'&& hangmanOutput[i]<='z')
                            {
                                continue;
                            }
                            else
                            {
                                hangmanOutput[i]='_';
                            }
                        }
                        tempWord[position]=alphabetFromUser;
                        tempWord[length]='\0';
                        winner=strcmp(tempWord,hangmanWord);
                        if(winner==0)
                        {
                            printf("\n\n\t\t You are the winner!! ");
                            printf("\n\n\t The Word was %s ",hangmanWord);
                            printf("\n\n\n\n\t EASY HUH ?? \n\n ");
                            getch();
                            return 0;
                        }
                    }
                }
            }
        }
        printf("\n\n\t");
        for(i=0; i<length; i++)
        {
            printf(" ");
            printf("%c",hangmanOutput[i]);
        }
        getch();
    }
    if(wrongTry<=0)
    {
        printf("\n\n\t The Word was %s",hangmanWord);
        printf("\n\n\t The Man is dead ");
        printf("\n\n\t Better luck Next Time ");
    }
    getch();
    return 0;
}

int hard(void)
{
    char hangmanWord[100],tempWord[100];
    char hangmanOutput[100];
    int wrongTry=3,matchFound=0;

    int counter=0,position=0,winner,length,i;
    char alphabetFromUser[10];
    system("cls");
    printf("\n\nEnter any word in spell case and hit ENTER");
    printf("\n\n\t Entere here: ");
    scanf("%s",hangmanWord);
    printf("\n\n Now give the computer to your friend and see if they can crack it");
    printf("\n\n\t Hit Enter");
    getch();
    length=strlen(hangmanWord);
    system("cls");
    printf("\n\n WELCOME TO HANGMAN GAME \n\n\n");
    printf("\n\n You will get 6 chances to guess the right word ");
    printf("\n\n So help the Man and set set go ");
    getch();
    printf("\n\n\t Hit Enter");
    getch();
    system("cls");
    printf("\n\t|| ----");
    printf("\n\t||  |  ");
    printf("\n\t|| ");
    printf("\n\t|| ");
    printf("\n\t|| ");
    printf("\n\t|| ");
    printf("\n\n The word has %d alphabets \n\n",length);

    for(i=0; i<length; i++)
    {
        hangmanOutput[i]='_ ';
        hangmanOutput[length]='\0';
    }
    for(i=0; i<length; i++)
    {
        printf(" ");
        printf("%c",hangmanOutput[i]);
    }
    while(wrongTry!=0)
    {
        matchFound=0;
        printf("\n\n Enter any alphabet from a to z and use small case ");
        printf("\n\n\t Enter here ");
        fflush(stdin);
        scanf("%c",&alphabetFromUser);
        if(alphabetFromUser < 'a' || alphabetFromUser > 'z')
        {
            system("cls");
            printf("\n\n\t Wrong Input ");
            matchFound=2;
        }
        fflush(stdin);
        if(matchFound!=2)
        {
            for(counter=0; counter<length; counter++)
            {
                if(alphabetFromUser==hangmanWord[counter])
                {
                    matchFound=1;
                }
            }
            if(matchFound==0)
            {
                printf("\n\t:You have %d tries left ",--wrongTry);
                getch();
                showHangman(wrongTry);
                getch();
            }
            else
            {
                for(counter=0; counter<length; counter++)
                {
                    matchFound=0;
                    if(alphabetFromUser==hangmanWord[counter])
                    {
                        position=counter;
                        matchFound=1;
                    }
                    if(matchFound==1)
                    {
                        for(i=0; i<length; i++)
                        {
                            if(i==position)
                            {
                                hangmanOutput[i]=alphabetFromUser;
                            }
                            else if(hangmanOutput[i]>='a'&& hangmanOutput[i]<='z')
                            {
                                continue;
                            }
                            else
                            {
                                hangmanOutput[i]='_';
                            }
                        }
                        tempWord[position]=alphabetFromUser;
                        tempWord[length]='\0';
                        winner=strcmp(tempWord,hangmanWord);
                        if(winner==0)
                        {
                            printf("\n\n\t\t You are the winner!! ");
                            printf("\n\n\t The Word was %s ",hangmanWord);
                            printf("\n\n\n\n\t EASY HUH ?? \n\n\ ");
                            getch();
                            return 0;
                        }
                    }
                }
            }
        }
        printf("\n\n\t");
        for(i=0; i<length; i++)
        {
            printf(" ");
            printf("%c",hangmanOutput[i]);
        }
        getch();
    }
    if(wrongTry<=0)
    {
        printf("\n\n\t The Word was %s",hangmanWord);
        printf("\n\n\t The Man is dead ");
        printf("\n\n\t Better luck Next Time ");
    }
    getch();
    return 0;
}

void showHangman(int choice)
{
    switch(choice)
    {
    case 0:
        system("cls");
        printf("\n\t||====");
        printf("\n\t|| | ");
        printf("\n\t|| %c*/",'\\');
        printf("\n\t|| |  ");
        printf("\n\t|| / %c",'\\');
        printf("\n\t|| ");
        break;
    case 1:
        system("cls");
        printf("\n\t||==== ");
        printf("\n\t|| | ");
        printf("\n\t|| %c0/",'\\');
        printf("\n\t|| |  ");
        printf("\n\t|| %c",'\\');
        printf("\n\t|| ");
        break;
    case 2:
        system("cls");
        printf("\n\t||==== ");
        printf("\n\t|| | ");
        printf("\n\t|| %c0/",'\\');
        printf("\n\t|| |  ");
        printf("\n\t|| ");
        printf("\n\t|| ");
        break;
    case 3:
        system("cls");
        printf("\n\t||====");
        printf("\n\t|| | ");
        printf("\n\t|| %c0/",'\\');
        printf("\n\t|| ");
        printf("\n\t|| ");
        printf("\n\t|| ");
        break;
    case 4:
        system("cls");
        printf("\n\t||==== ");
        printf("\n\t|| | ");
        printf("\n\t|| %c0 ",'\\');
        printf("\n\t|| ");
        printf("\n\t|| ");
        printf("\n\t|| ");
        break;
    case 5:
        system("cls");
        printf("\n\t||==== ");
        printf("\n\t|| | ");
        printf("\n\t|| 0 ");
        printf("\n\t|| ");
        printf("\n\t|| ");
        printf("\n\t|| ");
        break;
    }
    return;
}

void choose_level()
{
    int level;
    scanf("%d",&level);
    switch(level)
    {
    case 1:
        easy();
    case 2:
        intermid();
    case 3:
        hard();
    default:
        printf(" no such level is programmed ");
        break;
    }
}
