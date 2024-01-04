#include <stdio.h>
#include <stdlib.h>
#include<math.h>
#include <time.h>

int M[5000][5000];
time_t t1,t2;
double main_time=0.0;
double input_time=0.0;
double run_time=0.0;

int main()
{
    int i,j,n,ed,degree,edge;

    printf("Enter how many vertices you want to see : ");
    scanf("%d",&n);
    t1= clock();
    printf("\nThis is your Adjacency Matrix for Undirected Graph :\n\n");
    ed=n-1;
    edge=(ed*(ed+1))/2;

    for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++)
        {
            M[i][j]=1;
            if(i==j)
                M[i][j]=0;
            printf("%d ",M[i][j]);
        }
        printf("\n");
    }

    printf("\n\tVertices\tDegree");
    printf("\n\t--------\t------");
    degree=n-1;

    for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++)
        {

        }
        printf("\n\n\t    %d\t\t   %d",i,degree);
    }
    printf("\n\nIn this graph sum of all the degree is %d and there total %d edge\n\n",n*degree,edge);
    if(2*edge==n*degree)
    {
        printf("Yes. This undirected matrix hold Handshaking theorem\n");
    }
    else
    {
        printf("This undirected matrix does not hold Handshaking theorem\n");
    }
    t2 = clock();

    input_time= ((double)(t1)/CLOCKS_PER_SEC)*pow(10,9);
    printf("\nInput Time is= %lf ns(nanoseconds)\n",input_time);

    run_time = ((double)(t2)/CLOCKS_PER_SEC)*pow(10,9);
    printf("Total Time is= %lf ns(nanoseconds)\n\t",run_time);

    main_time = ((double)(t2-t1)/CLOCKS_PER_SEC)*pow(10,9);
    printf("\n\n\t\t\t\t_____________ When n=%d _____________\t\n\n",n);
    printf("\t\t\t  Main run Time is= %lf ns(nanoseconds) \n\t\n",main_time);



    return 0;

}
