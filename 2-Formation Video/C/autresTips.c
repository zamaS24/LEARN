 -> savoir le temps d'execution de :
        clock_t begin = clock();
        /* here, do your time-consuming job */
        clock_t end = clock();
        double time_spent = (double)(end - begin) / CLOCKS_PER_SEC;
-> tab +i - tab = i // l'algebre dadresses