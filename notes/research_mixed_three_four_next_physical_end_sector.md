# A complete physical end sector in the next mixed attachment

Research deduction, 7 November 2026. The last \(N/1000\) incoming
sampling rows in the exact transfer \(34\to343,344\) have a uniform
exponential rate below one. The two conditional kernels both terminate
there, while the first cap retains its complete coherent endpoint
coefficients. An elementary lower bound for the actual next action
pays this entire sector. Both Fourier coefficients are combined by
the exact root sum; no continuous arc or individual Fourier sector
is identified with the deleted rows. No numerical evaluation is used.

## 1. The exact sector and its complete first-cap moments

Put \(D=N-1\), \(r=e^{-2\pi i/N}\), \(P_j=(r;r)_j\),
\(S_j=|P_j|\), and \(p_j(X)=(rX;r)_j\). Use the original sources
of [the exact next attachment](research_mixed_three_four_next_conditional_attachment.md):
\[
\begin{split}
 U_{0,N}(w,X)&=\sum_{\ell=0}^{D}
              \frac{H_N(w,r^{-\ell})}{P_\ell}p_\ell(X),\\
 F_N(w,Y)&=N\operatorname{CT}_X[U_{0,N}(w,X)C_{1,N}(X,Y)],\\
 C_{\beta,N}(Y,Z)&=\sum_{k=0}^{D}
       \frac{Y^{-k}p_k(Y)p_k(Z)}{P_k^{2+\beta}},
                         \qquad\beta\in\{0,1\}.
\end{split}                                                    \tag{1}
\]
The next conditional polynomial is exactly
\[
 \mathcal F_{\beta,N}(w,Z)
   =\sum_{b=0}^{D}\frac{F_N(w,r^b)}{P_b}C_{\beta,N}(r^b,Z).
                                                               \tag{2}
\]
Define its final physical sector by
\[
 \mathcal E_{\beta,N}(w,Z)
   =\sum_{b=\lceil999N/1000\rceil}^{D}
              \frac{F_N(w,r^b)}{P_b}C_{\beta,N}(r^b,Z).
                                                               \tag{3}
\]
An empty sum is zero. No additional \(N\), \(\kappa_N\), or
Gram factor belongs outside (2)--(3).

For \(0\le j<N\), set
\[
 T_{j,N}(w)=\operatorname{CT}_X
                     [X^{-j}p_j(X)U_{0,N}(w,X)].
                                                               \tag{4}
\]
At a physical incoming node the first conditional kernel terminates
exactly, giving
\[
 F_N(w,r^b)
   =N\sum_{j=0}^{D-b}
             \frac{P_{b+j}}{P_bP_j^3}\,T_{j,N}(w).
                                                               \tag{5}
\]
Every factorial in (5) is nonzero. In particular
\[
 F_N(w,r^D)=N T_{0,N}(w)
          =N\sum_{\ell=0}^{D}\frac{H_N(w,r^{-\ell})}{P_\ell}.
                                                               \tag{6}
\]
The relevant coherent seam ceiling is \(b_1=433/500\), not the
unweighted \(b_0\) ceiling.

The [coherent seam bound](research_mixed_cap_seam_source_bounds.md),
Theorem 1, and its
[all-real-color extension](research_mixed_terminal_real_color_decay.md),
Lemma 2, give
\[
 \sum_{\ell=0}^{D}\frac{|H_N(w,r^{-\ell})|}{S_\ell}
       \le C_\tau N^{A_\tau}e^{N(b_1+\tau)},\qquad b_1=433/500.
                                                               \tag{7}
\]
This holds for every real \(w\in[-2,2]\), and on a sufficiently
small fixed complex disk about \(-2\) for each \(\tau>0\).
Every \(H_N\) remains its complete complex value.

All factors of \(p_\ell p_j\) have unit-modulus coefficients.
The coefficient of \(X^j\) therefore has modulus at most
\(\binom{\ell+j}{j}\le\binom{N+j}{j}\). Consequently
\[
 |T_{j,N}(w)|
   \le \binom{N+j}{j}\,
          C_\tau N^{A_\tau}e^{N(b_1+\tau)}.
                                                               \tag{8}
\]
For \(t=j/N\), the binomial theorem, applied at
probability \(j/(N+j)\), implies
\[
 \binom{N+j}{j}\le e^{N\rho(t)},\qquad
 \rho(t)=(1+t)\log(1+t)-t\log t,\quad \rho(0)=0.
                                                               \tag{9}
\]
Thus no estimate of separate Newton terms or of an off-grid cap
is needed in (8).

## 2. A uniform finite-source ceiling

Write
\[
 J(t)=\int_0^t\log(2\sin\pi u)\,du,\qquad
 \log S_j=NJ(j/N)+O(\log N),\quad 0\le j<N.
                                                               \tag{10}
\]
The error is uniform through both physical endpoints. Also
\(J(1-t)=-J(t)\), and \(J\) decreases on \([0,1/6]\).

Fix a summand of (3), and put
\[
 v=1-b/N,\qquad t=j/N,\qquad s=k/N.
\]
The exact supports in (5) and in \(C_{\beta,N}(r^b,Z)\) give
\[
 0\le t,s\le v-1/N<v\le1/1000.                         \tag{11}
\]
For \(|Z|\le3\), use the zero-safe bound
\(|p_k(Z)|\le4^k\). The two retained row rates, including (8),
are respectively
\[
\begin{split}
 b_1+\tau+\rho(t)+J(v)-J(v-t)-3J(t),\\
 J(v)-J(v-s)-(2+\beta)J(s)+s\log4.
\end{split}                                                    \tag{12}
\]
The weight \(1/P_b\) contributes \(J(v)\). The factors
\(r^{-bk}\) have modulus one and have not changed these rates.
Since \(J(v)-J(v-t)\le0\), \(J(v)-J(v-s)\le0\), and \(J(v)\le0\),
the full product in (3), before polynomial factors, is bounded by
\[
 b_1+\tau-(5+\beta)J(v)+\rho(v)+v\log4 .
                                                               \tag{13}
\]
Here \(\rho\) increases, and \(-J\) increases on (11).

There is a purely elementary fixed reserve in (13).
For \(0\le u\le1/2\), \(2\sin\pi u\ge4u\), hence
\[
 -J(v)\le v(1-\log(4v))\le v(1-\log v).
\]
Also \(\rho(v)\le v(2-\log v)\) for \(0\le v\le1\).
The two right sides increase on \([0,1/1000]\).
Since \(1000<2^{10}\) and \(\log2<7/10\), one has
\(\log1000<7\); also \(\log4<2\). Therefore
\[
 -(5+\beta)J(v)+\rho(v)+v\log4
          <\frac{6\cdot8+9+2}{1000}=\frac{59}{1000},
 \qquad b_1+\frac{59}{1000}=\frac{37}{40}.              \tag{14}
\]
Choose the color tolerance in (7) smaller than \(1/80\).
The finite numbers of \(b,j,k,\ell\) rows and all errors in (10)
contribute only a polynomial factor.

**Theorem 1.** The sum of the absolute values of the products in
(3) satisfies
\[
 \sum_{b=\lceil999N/1000\rceil}^{D}
    \left|\frac{F_N(w,r^b)}{P_b}C_{\beta,N}(r^b,Z)\right|
      \le C N^A e^{15N/16},\qquad |Z|\le3.              \tag{15}
\]
The assertion holds for both \(\beta\), both level parities,
every real ordinary color, and on a sufficiently small fixed
complex disk about \(-2\).

Fixed ordinary-color derivatives satisfy the same positive-row
bound with a different polynomial prefactor. For real colors apply
Markov's inequality to the complete polynomials \(T_{j,N}\),
whose degrees are at most \(N-1\), before summing (5).
For complex colors apply Cauchy's formula on a smaller disk.
Fixed \(Z\)-derivatives are allowed on every smaller disk
\(|Z|\le R_0<3\), by Cauchy's formula applied before the positive
row summation. This retains every finite numerator zero.

## 3. A lower bound for the actual next conditional action

The original pair action is
\[
 W(v,w)=J(v+w)-J(v)-J(w)+i\pi vw
       =g(v+w)-g(v)-g(w)+2\pi ivw .
                                                               \tag{16}
\]
On \(Q=[.23,.45]+i[-.12,.12]\), the original pair Hessian
is strictly accretive. The real-height floor and joint vertical
convexity proved in
[terminal transform tails, Lemma 1](research_mixed_terminal_transform_tails.md),
equations (8)--(10), therefore give, for every independent
\(v,w\in Q\),
\[
 \Re W(v,w)>
       \frac15-\pi\{\Re v\,\Im w+\Re w\,\Im v\}.        \tag{17}
\]
This is the first inequality in that proof, before its more
special endpoint-height substitution.

The original primitive also satisfies
\[
                    \Re g(x+ih)<0\qquad
                    (0<x<1/2,\ h\in\mathbb R).
                                                               \tag{18}
\]
For \(h\le0\), the disk primitive proves (18) by
\(\arg(1-Re^{-2\pi ix})>0\), \(0<R\le1\), and integration
from radial zero. For \(h>0\), Schwarz reflection of the
original \(J\) gives
\[
 \Re g(x+ih)=\Re g(x-ih)-\pi(1-2x)h<0.
                                                               \tag{19}
\]
This uses the original regular strip and does not choose a new
logarithmic lift.

At any actual ordinary or terminal next reference in
[the local attachment theorem](research_mixed_three_four_next_local_source.md),
put \(y=t_2\), \(s=s_3\), \(z=t_3\). Then
\[
 y\in O_4,\qquad s,z\in Q,\qquad \Im y<0.               \tag{20}
\]
For a terminal vertex \(z\) is private; its endpoint rectangle
is nevertheless contained in \(Q\). The old prefix is evaluated
at \(y=q_{34}(s)\), with \(s\in O_{3+\beta}\) or
\(A_{3+\beta}\). The proved
[full-disk remainder theorem](research_mixed_three_four_following_remainder_gaps.md)
therefore gives
\[
                    \Re\mathcal P_{34}(-2,y)>7/4.      \tag{21}
\]

With the exact conditional gauge, the new action increment is
\[
\begin{split}
 \mathcal P_\beta^+(-2,z)-\mathcal P_{34}(-2,y)
 &=G(y,s)+V_\beta(s,z)-(1-\beta)g(z)\\
 &=W(y,s)+W(s,z)-g(y)-\beta g(s)-2\pi isz .
\end{split}                                                    \tag{22}
\]
Combining (17)--(20) yields
\[
\begin{split}
 \Re\{\mathcal P_\beta^+-\mathcal P_{34}\}
 &>\frac25+\pi\{\Im s(\Re z-\Re y)
                         +\Re s(\Im z-\Im y)\}\\
 &\ge \frac25-\pi\left(\frac3{25}\frac{11}{50}
                            +\frac9{20}\frac3{25}\right)\\
 &=\frac25-\frac{201\pi}{2500}>\frac18 .
\end{split}                                                    \tag{23}
\]
The last inequality follows from \(\pi<22/7\). All quantities
in (22) are evaluated at the matched original critical point;
the independent box is used only for the lower bound.
Consequently
\[
                       \Re\mathcal P_\beta^+(-2,z)>15/8
                                                               \tag{24}
\]
uniformly on the compact ordinary following families and the two
terminal bases. The action includes the precise subtraction
\(-(1-\beta)g(z)\); (24) is not a bound in a different row gauge.

## 4. Payment, derivatives, and the remaining cycle

Every actual outgoing coordinate in (20) satisfies
\(|e^{-2\pi iz}|<3\), with a fixed reserve: indeed
\(2\pi\Im z\le .24\pi<1\) and \(e<3\).
Theorem 1 and (24), followed by compact continuity, give uniform
small complex parameter neighborhoods on which
\(\Re\mathcal P_\beta^+(w,z)>29/16\).
On smaller neighborhoods, Cauchy's formula applied to the exact
holomorphic normalized sector gives, for every fixed mixed order,
\[
 \left|\partial_w^j\partial_z^k
 \left[e^{-N\mathcal P_\beta^+(w,z)}
       \mathcal E_{\beta,N}(w,e^{-2\pi iz})\right]\right|
       \le C_{j,k}N^{A_{j,k}}e^{-3N/4}.                \tag{25}
\]
For all real ordinary colors, the positive-row derivative bound
in Theorem 1 is instead compared with the complete-color action
in (24). No assertion about the complex-color action at remote
real colors is needed.

Equations (3) and (25) delete an actual part of the exact next
finite contraction (2). They combine the two Fourier coefficients
by the already proved root identity and preserve the original
weight \(1/P_b\). They do not bound either Fourier coefficient
separately, identify a partial root sum with an arc, or permit a
partial contour deformation without its sampling currents.
The complementary rows \(b/N<999/1000\) remain their exact
finite sum. The outgoing row scalar and the final ordinary
observation remain precisely those in the next-attachment
theorem, equations (13)--(14). No whole next-prefix or new
knot-family conclusion is asserted.

## 5. The same argument pays the last four percent

There is also a wider useful sector, with a smaller positive gap.
Set
\[
 \widetilde{\mathcal E}_{\beta,N}(w,Z)
   =\sum_{b=\lceil24N/25\rceil}^{D}
       \frac{F_N(w,r^b)}{P_b}C_{\beta,N}(r^b,Z).
                                                               \tag{26}
\]
Its exact supports still give \(0\le t,s<v=1-b/N\le1/25<1/6\).
Therefore the derivation of the full rate (13) is unchanged.
On \([0,1/6]\), concavity of sine gives \(2\sin\pi u\ge6u\);
consequently
\[
 -J(v)\le v(1-\log(6v))
       \le\frac1{25}\left(1+\log\frac{25}{6}\right)<\frac1{10}.
                                                               \tag{27}
\]
The last inequality uses
\[
 e^{3/2}>1+\frac32+\frac{(3/2)^2}{2}
                       +\frac{(3/2)^3}{6}
          =\frac{67}{16}>\frac{25}{6}.
\]
Similarly \(e^{5/3}>\sum_{j=0}^{4}(5/3)^j/j!
=10009/1944>5\), so \(\log25<10/3\). Hence
\[
 \rho(v)<\frac{16}{75},\qquad
 v\log4<\frac7{125},\qquad
 b_1-6J(v)+\rho(v)+v\log4
       <\frac{2603}{1500}<\frac74 .
                                                               \tag{28}
\]
The reserve in the last comparison is exactly \(11/750\).
Choosing the seam/color tolerance below this reserve proves
\[
 \sum_{b=\lceil24N/25\rceil}^{D}
    \left|\frac{F_N(w,r^b)}{P_b}C_{\beta,N}(r^b,Z)\right|
       \le C N^A e^{7N/4},\qquad |Z|\le3.              \tag{29}
\]
All source, parity, color and derivative assertions of Theorem 1
hold for (29), with the same proofs.

On the fixed neighborhoods used in Section 4,
\(\Re\mathcal P_\beta^+>29/16\). Therefore the complete
normalized sector in (26), with every fixed mixed derivative,
satisfies
\[
 \left|\partial_w^j\partial_z^k
 \left[e^{-N\mathcal P_\beta^+(w,z)}
       \widetilde{\mathcal E}_{\beta,N}(w,e^{-2\pi iz})\right]\right|
     \le C_{j,k}N^{A_{j,k}}e^{-N/32}.                  \tag{30}
\]
This wider deletion has exactly the same physical-sum scope as
(25). In particular its remaining complement and the separation
of the two Fourier coefficients are still retained.
