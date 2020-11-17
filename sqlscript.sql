Atividade 3
Grupo: Bruno Lenzi, Caio Oliveira, Heitor Vaz, Leo Mifune, Tiago Rossi, Kenzo Ishihara;
Script da função

reg = function(x,y,alfa){
  dados = lm(log(y) ~ x)
  respon = summary(dados) 
  a = exp(confint(dados, level = 1 - alfa))
  if(respon$coefficients[2,4] >= alfa){
   cat("não existe relação ", "y :", 
        round(mean(y),2), "\n") 
    if(respon$coefficients[1,1] > 0){
      cat("intervalo angular", round((a[2,] - 1)*100,4)) 
    } 
    else{
      cat("intervalo angular:",round((1 - a[2,] - 1)*100,2))
    } 
    cat("intervalo linear", round(a[1,],2), "\n")
  }else{
    if(respon$coefficients[1,4] >= alfa){
      dados = lm(log((y) ~ x) - 1)
      respon = summary(dados) 
      a = exp(confint(dados, level = 1 - alfa))
      cat("a equação é y = exp(", respon$coefficients[1])
    if(respon$coefficients[1,1] > 0){
      cat("Intervalo:",round((a[2,] - 1)*100,2),) 
   } 
    else{
      cat("Intervalo:",round((1 - a[2,] - 1)*100,2))}
  } 
}
