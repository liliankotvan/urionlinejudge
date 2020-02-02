N1, N2, N3, N4 = map(float, raw_input().split(" "))

media = round((((N1 * 2) + (N2 * 3) + (N3 * 4) + N4) / 10), 1)

print ("Media: {:.1f}".format(media))

if media >= 7.0:

    print ("Aluno aprovado.")

elif media <= 4.9:

    print ("Aluno reprovado.")

else:

    print ("Aluno em exame.")

    exame = float(input())

    print ("Nota do exame: {:.1f}".format(exame))

    media_final = (media + exame) / 2

    if media_final >= 5.0:

        print ("Aluno aprovado.")
        print ("Media final: {:.1f}".format(media_final))

    else:

        print ("Aluno reprovado.")
        print ("Media final: {:.1f}".format(media_final))
