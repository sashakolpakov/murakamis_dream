# Domains of the selected Fourier upper rates

Research deduction, 6 November 2026. The exact selected weight has an
additive upper estimate, so its two rates combine by a maximum.
This note restricts where a forced rate can dominate, including for
several selected coordinates simultaneously. It proves no negative
source rate and deletes no physical summand. No numerical evaluation
is performed.

## 1. The original weight and its two rates

Use the original regular-strip primitive and its real restriction
\[
 g(z)=\frac{\operatorname{Li}_2(e^{-2\pi iz})-\pi^2/6}{2\pi i},
 \qquad J(t)=\Re g(t)=\int_0^t\log(2\sin\pi s)\,ds .
 \tag{1}
\]
Here \(0<\Re z<1\), \(0<t<1\), and all logarithms have the
original continuation from that strip. In particular \(J(1/2)=0\).
For an integer \(N\ge2\), let \(d_N\) be the degree-less-than-\(N\) polynomial with
\(d_N(e^{-2\pi ia/N})=\{\prod_{j=1}^a(1-e^{-2\pi ij/N})\}^{-1}\),
\(0\le a<N\), with the empty product equal to one.
The [original Fourier theorem](research_mixed_fourier_weight_continuation.md)
retains the exact residue identity
\(d_N(X)=f_N(z)+(1-X^N)I_N(z)\), where \(X=e^{-2\pi iz}\),
\(f_N\) is the reciprocal factorial continuation, and \(I_N\)
contains all four contour sides. For \(z=x+iH\), \(H\ge0\),
it gives on fixed compact target sets, for every \(\tau>0\),
\[
 |d_N(X)X^{-N}|\le C_\tau N^{A_\tau}
          \{e^{N(w_H(x)+\tau)}+e^{N\tau}\},\qquad
 w_H(x)=-\Re g(x+iH)-2\pi H.
 \tag{2}
\]
The factorial rate is \(w_H(x)\); the forced rate is zero.
One cannot replace their maximum by their minimum.

## 2. Two uniform cutoffs

Put \(P=[11/50,9/20]\). For \(x\in P\), \(H\ge0\),
\[
 \partial_xw_H(x)=-\log|1-e^{2\pi H-2\pi ix}|<0.
 \tag{3}
\]
Indeed \(\cos(2\pi x)<1/5\) and \(R=e^{2\pi H}\ge1\)
give \(1+R^2-2R\cos(2\pi x)>1\).
For \(0<t<1/2\), the argument
\(a(t,h)=\arg(1-e^{2\pi h-2\pi it})\) increases with \(h\):
its derivative with respect to \(R=e^{2\pi h}\) is
\(\sin(2\pi t)/(1-2R\cos(2\pi t)+R^2)>0\).
It starts at \(a(t,0)=\pi(1/2-t)\) and remains below \(\pi\).
Thus \(\partial_Hw_H=a(t,H)-2\pi<0\), and
\[
 w_H(t)\ge(1/2-t)\log(2\sin\pi t)-\pi H(3/2+t).
 \tag{4}
\]
This follows by integrating the height derivative of \(-\Re g\)
and using the increasing real integrand in
\(-J(t)=\int_t^{1/2}\log(2\sin\pi s)\,ds\).

The [second-selection rate-switch proof](research_mixed_second_selected_directional_budget.md),
equation (5a), proves \(w_{1/100}(2/5)>1/875\).
Monotonicity in both variables consequently gives
\[
 w_H(x)>1/875\quad
       (x\in P,\ x\le2/5,\ 0\le H\le1/100).
 \tag{5}
\]
There is also the cutoff needed up to height \(7/500\):
\[
 w_H(x)>19/25000\quad
       (x\in P,\ x\le9/25,\ 0\le H\le7/500).
 \tag{6}
\]
To verify it exactly, \(2\sin(9\pi/25)=2\cos(7\pi/50)>
2-(11/25)^2=1129/625\), using \(\pi<22/7\).
For \(q=59/100\), the positive exponential series gives
\[
 e^q\le\sum_{j=0}^5\frac{q^j}{j!}
       +\frac{q^6}{6!(1-q/7)}
 =\frac{8325767634592441}{4615200000000000}<\frac{1129}{625}.
 \tag{7}
\]
The final rational difference is
\(11129645407559/4615200000000000>0\).
Hence the logarithm in (4) at \(t=9/25\) exceeds \(59/100\).
Equation (4), \(\pi<22/7\), and monotonicity give (6), since
\((7/50)(59/100)-(22/7)(7/500)(93/50)=19/25000\).

## 3. Simultaneous branch-domain restriction

Let \(S\) be any fixed finite set of selected coordinates, with
\(x_i\in P\), fixed \(0\le H_i\le7/500\), and fixed weights \(\gamma_i>0\).
The product of the moduli in (2), raised to these weights, has
upper rate \(\sum_{i\in S}\gamma_i\max(w_{H_i}(x_i),0)\).
Let \(R\) be any common additional profile, including any cap,
kernel or affine terms, on its original joint target set \(\mathcal D\),
with selected coordinates in \(P^S\) and all other variables retained.
Choose \(t_i=2/5\) when \(H_i\le1/100\), or
\(t_i=9/25\) when \(H_i\le7/500\). For a forced set \(F\subseteq S\),
put \(\mathcal D_F=\{x\in\mathcal D:x_i\ge t_i\ (i\in F)\}\).
Then, with the supremum of an empty set interpreted as \(-\infty\),
\[
 \sup_{\mathcal D}\left\{R+\sum_{i\in S}\gamma_i\max(w_{H_i},0)\right\}
 =\max_{F\subseteq S}\ \sup_{\mathcal D_F}
               \left\{R+\sum_{i\notin F}\gamma_i w_{H_i}\right\}.
 \tag{8}
\]
Every restricted branch is below the full pointwise envelope.
Conversely, at each target choose the forced indices only where
\(w_{H_i}<0\). Equations (5)--(6) put all these coordinates in
\(\mathcal D_F\), and this branch attains the envelope there.
This proves (8) without moving any target, reference, contour or
boundary tangent. Factorial coordinates keep their original domains.
It reduces domains of upper-rate comparisons, not physical sums or
the number of source profiles. Their remaining signs are separate.
