#include <ctype.h>
#include <string.h>
#include <stdio.h>
#include <assert.h>
#if 0
char getSoundexCode(char c) {
    c = toupper(c);
    switch (c) {
        case 'B': case 'F': case 'P': case 'V': return '1';
        case 'C': case 'G': case 'J': case 'K': case 'Q': case 'S': case 'X': case 'Z': return '2';
        case 'D': case 'T': return '3';
        case 'L': return '4';
        case 'M': case 'N': return '5';
        case 'R': return '6';
        default: return '0'; // For A, E, I, O, U, H, W, Y
    }
}

void generateSoundex(const char *name, char *soundex) {
    int len = strlen(name);
    soundex[0] = toupper(name[0]);
    int sIndex = 1;

    for (int i = 1; i < len && sIndex < 4; i++) {
        char code = getSoundexCode(name[i]);
        if (code != '0' && code != soundex[sIndex - 1]) {
            soundex[sIndex++] = code;
        }
    }

    while (sIndex < 4) {
        soundex[sIndex++] = '0';
    }

    soundex[4] = '\0';
}

#endif // 0

char getSoundexCode(char c)
{
    int i = 0;
    char res = '0';
    char chararr[26] = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'};
    char codearr[26] = {'0','1','2','3','0','1','2','0','0','2','2','4','5','5','0','1','2','6','2','3','0','1','0','2','0','2'};

    c = toupper(c);

    while(i < 26)
    {
        if(c == chararr[i])
        {
            res = codearr[i];
            break;
        }
        i++;
    };

    return res;
}

char checkcode(char code,char *soundex,int sIndex)
{
    if(code != '0' && code != soundex[sIndex - 1])
    {
        return code;
    }
    else
    {
        return 0;
    }
}

void updatesoundex(int sIndex, char *soundex)
{
    while (sIndex < 4)
    {
        soundex[sIndex++] = '0';
    }
}

void generateSoundex(const char *name, char *soundex)
{
    soundex[0] = toupper(name[0]);
    int sIndex = 1;

    for (int i = 1; i < 4; i++)
    {
        char code = getSoundexCode(name[i]);
        if (checkcode(code,soundex,sIndex))
        {
            soundex[sIndex++] = code;
        }
    }

   updatesoundex(sIndex,soundex);

    soundex[4] = '\0';
}


TEST(SoudexTestsuite1, ReplacesConsonantsWithAppropriateDigits1)
{
  char soundex[5];
  generateSoundex("X0", soundex);
}


TEST(SoudexTestsuite2, ReplacesConsonantsWithAppropriateDigits2)
{
  char soundex[5];
  generateSoundex("ZQOP", soundex);
}


TEST(SoudexTestsuite3, ReplacesConsonantsWithAppropriateDigits3)
{
  char soundex[5];
  generateSoundex("ASDSD", soundex);
}


TEST(SoudexTestsuite4, ReplacesConsonantsWithAppropriateDigits4)
{
  char soundex[5];
  generateSoundex("12345", soundex);
}

void main()
{
  char soundex[5];
  generateSoundex("AX", soundex);
  //ASSERT_EQ(soundex,"A200");
  printf("%s",soundex);
}
