#import "@preview/quill:0.2.1": *

#table(columns: 9, align: center,
 [*Alice's bits*], $0$,$1$,$1$,$0$,$1$,$0$,$0$,$1$,
 [*Alice's basis*], $+$,$+$,$times$,$+$,$times$, $times$, $times$, $+$,
 [*Alice's polarization*], $arrow.t$, $arrow$, $arrow.br$, $arrow.t$, $arrow.br$, $arrow.tr$, $arrow.tr$, $arrow$,
 [*Bob's basis*], $+$,$times$,$times$,$times$,$+$, $times$, $+$, $+$,
 [*Bob's polarization*], $arrow.t$,$arrow.tr$,$arrow.br$,$arrow.tr$,$arrow$, $arrow.tr$, $arrow$, $arrow$,
 [*Shared secret key*], $0$, "", $1$, "", "", $0$, "", $1$
)

= Introduction

= State of the art

= Method

= Implementation

= Simulations/Real

= Discussion

= Conclusion


#{
  quantum-circuit(
    lstick($|0〉$), $H$, ctrl(1), $X$, [\ ],
    lstick($|0〉$), 1, targ(), 1
  )
}
