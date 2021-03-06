// Вам дан список ролей и сценарий пьесы в виде массива строчек.

// Каждая строчка сценария пьесы дана в следующем виде:
// Роль: текст

// Текст может содержать любые символы.

// Напишите метод, который будет группировать строчки по ролям, пронумеровывать их и возвращать результат в виде готового текста (см. пример). Каждая группа распечатывается в следующем виде:

// Роль:
// i) текст
// j) текст2
// ...
// ==перевод строки==

// i и j -- номера строк в сценарии. Индексация строчек начинается с единицы, выводить группы следует в соответствии с порядком ролей. Переводы строк между группами обязательны, переводы строк в конце текста не учитываются.

// Заметим, что вам предстоит обработка огромной пьесы в 50 000 строк для 10 ролей – соответственно, неправильная сборка результирующей строчки может выйти за ограничение по времени.

// Sample Input:
// roles:
// Городничий
// Аммос Федорович
// Артемий Филиппович
// Лука Лукич
// textLines:
// Городничий: Я пригласил вас, господа, с тем, чтобы сообщить вам пренеприятное известие: к нам едет ревизор.
// Аммос Федорович: Как ревизор?
// Артемий Филиппович: Как ревизор?
// Городничий: Ревизор из Петербурга, инкогнито. И еще с секретным предписаньем.
// Аммос Федорович: Вот те на!
// Артемий Филиппович: Вот не было заботы, так подай!
// Лука Лукич: Господи боже! еще и с секретным предписаньем!
// Sample Output:
// Городничий:
// 1) Я пригласил вас, господа, с тем, чтобы сообщить вам пренеприятное известие: к нам едет ревизор.
// 4) Ревизор из Петербурга, инкогнито. И еще с секретным предписаньем.

// Аммос Федорович:
// 2) Как ревизор?
// 5) Вот те на!

// Артемий Филиппович:
// 3) Как ревизор?
// 6) Вот не было заботы, так подай!

// Лука Лукич:
// 7) Господи боже! еще и с секретным предписаньем!


public class TEST {

    public static void main(String[] args) {
        long timestart=System.nanoTime() ;
        String roles [] = new String[4];
        String textLines [] = new String[7];

        roles[0] = "Городничий";
        roles [1] = "Аммос Федорович";
        roles [2] = "Артемий Филиппович";
        roles [3] = "Лука Лукич";

        textLines [0] = "Городничий: Я пригласил вас, господа, с тем, чтобы сообщить вам пренеприятное известие: к нам едет ревизор.";
        textLines [1] = "Аммос Федорович: Как ревизор?";
        textLines [2] = "Артемий Филиппович: Как ревизор?";
        textLines [3] = "Городничий: Ревизор из Петербурга, инкогнито. И еще с секретным предписаньем.";
        textLines [4] = "Аммос Федорович: Вот те на!";
        textLines [5] = "Артемий Филиппович: Вот не было заботы, так подай!";
        textLines [6] = "Лука Лукич: Господи боже! еще и с секретным предписаньем!";

        StringBuilder newText = new StringBuilder();
        for(int i=0;i<roles.length;i++){
            newText.append(roles[i]);
            newText.append(":\n");
            for(int j=0;j<=textLines.length-1;j++){
                if (textLines[j].startsWith(roles[i]+":")){
                    newText.append(j+1);
                    newText.append(")");
                    newText.append(textLines[j].substring(roles[i].length()+1));
                    newText.append("\n");
                }
            }
            newText.append("\n");
        }
        System.out.println(newText);
        
    }

}