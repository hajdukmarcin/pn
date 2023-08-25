#include <stdio.h>
#include <math.h>

main()
{
float depth, surf, mag, amp, impact, surfi, no;
float alphad, alphai, area, triangle1, triangle2;
int i;

  impact=0.3563;
  no=41;
  printf("i     total partial         mag \n");

  for(i=0; i<no; i++){
    depth=i/20.;
    alphad=acos(1.-depth);
    alphai=asin(impact);
    surf = (alphad-((1.-depth)*sin(alphad)))/3.1416;
/*  mag=(-2.5)*log10(0.28+surf/2.);
/*  printf("%2.3f %7.3f %6.1f %6.2f %6.2f %6.3f", i, depth, 180.*alphad/3.1416, 180.*alphai/3.1416, surf, mag);
*/  if(alphad < alphai) area=0;
    if(alphad > alphai){
      if(alphad < (3.1416-alphai)){
        triangle1=0.5*(1.-depth)*(sin(alphad)-tan(alphai)*(1.-depth));
        triangle2=0.5*(depth+(impact/tan(alphai)-1.))*(impact-tan(alphai)*(1.-depth));
	area=(alphad-alphai-triangle1-triangle2)/3.1416/2.;
/*      printf(" %6.3f%6.3f%6.3f%6.3f",area,triangle1,triangle2,alphai);*/}
      }
    if(alphad > (3.1416-alphai)){
      area=(1.-(2.*alphai/3.1416)-((impact*impact/tan(alphai))/3.1416))/2.;
    }
  mag=(-2.5)*log10(1-surf+area);
  printf("%2.3f%7.3f%7.3f%7.3f%7.3f", i/(no-1.), 1.-surf, 1.-surf+area, area, mag);
  printf("\n");
  }
}
