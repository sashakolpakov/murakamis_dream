# The complete first real arc with the second coordinate selected

Private written proof, 11 November 2026. The original three-factor
source for an actual word beginning with \(443\) or \(444\) has a
strict gap on the complete first real interval \([1/2,7/8]\), while
the second coordinate stays on its selected plateau and the third
stays on its original plateau. Both first Fourier choices are retained.

The new comparison is a lower trial for an original cap main
profile: its real-half-face envelope exceeds \(181/200\).
This pays the extra \(9/10\) alternative in complete cap transport.
It is not a lower bound for a finite cap value and uses no
positivity or noncancellation of a finite sum.

## 1. Literal source and the existing half-face calibration

Fix an actual positive three/four word of length \(m\ge4\) with
first three flags \((1,1,\beta)\), \(\beta\in\{0,1\}\). Use the
coupled reference, original logarithmic lifts and scalar of the
[second-selected right-half connections](research_mixed_complete44_second_selected_right_half_connections.md).
Put
\[
 H=1/100,\qquad P=[11/50,9/20],\qquad
 a\in[1/2,7/8],\quad y=b+iH,\quad z=v+i\Im r_3,\quad b,v\in P.
 \tag{1}
\]
The actual cap height \(h_e\) belongs to \((-.051,-.019)\), and
the first ordinary index height \(h_s\) belongs to \((-.102,-.001)\).
They are not varied independently as geometric references.

With \(q_N=e^{-2\pi i/N}\), \(P_j=(q_N;q_N)_j\), and
\(p_j(X)=(q_NX;q_N)_j\), keep
\[
\begin{split}
 U_{1,N}(w,X)&=\sum_{i=0}^{N-1}H_N(w,q_N^{-i})p_i(X)/P_i^2,\\
 C_{\epsilon,N}(X,Y)&=\sum_{j=0}^{N-1}
                   X^{-j}p_j(X)p_j(Y)/P_j^{2+\epsilon},\\
 {\cal B}_{\sigma,\beta,N}
 &=|U_{1,N}(w,X)C_{1,N}(X,Y)C_{\beta,N}(Y,Z)
          d_N(X)X^{-\sigma N}d_N(Y)Y^{-N}|\,
                                 |d_N(Z)|^{\beta/2},\\
 X&=e^{-2\pi ia},\qquad Y=e^{-2\pi iy},\qquad Z=e^{-2\pi iz},
                        \qquad \sigma\in\{0,1\}.
\end{split}
 \tag{2}
\]
For \(\beta=0\) the last factor is defined to be one.
Every endpoint coefficient \(H_N\), each polynomial weight,
and every physical row is complete.

Let \(g\) and \(J\) be the original primitives, with
\[
 g(w)=J(w)+\frac{\pi i}{2}(w-w^2),\qquad
 J'(w)=\operatorname{Log}(2\sin\pi w),\qquad J(0)=0 .
 \tag{3}
\]
Write
\[
\begin{split}
 \Psi(e,a)&=S(e)+g(e+a)-g(a)-g(e)
                              -\frac{\pi i}{2}(e-e^2),\\
 Q_\epsilon(s;a,y)&=g(s+a)+g(s+y)-(2+\epsilon)g(s)
                              -g(a)-g(y)+2\pi ias .
\end{split}
 \tag{4}
\]
The original affine action is
\[
\begin{split}
 F_{123}(e,s_2,s_3;z_1,z_2,z_3)
 &=\Psi(e,z_1)+Q_1(s_2;z_1,z_2)+Q_\beta(s_3;z_2,z_3)\\
 &\hspace{1em}-g(z_1)-g(z_2)-\frac\beta2g(z_3),\\
 \Lambda_{123}(z)&=\Re F_{123,*}+\Re\{p_R(z-r_3)\}.
\end{split}
 \tag{5}
\]
Here \(F_{123,*}\) is evaluated at the unchanged critical
reference and \(p_R\) is its original third-coordinate marginal.
This is the same normalization as equations (6), (28) of the
right-half connection theorem.

Retain its five bare cap profiles at \(a=1/2\), with real cuts
\(.27,.49\), main height \(h_e\), lower height \(-.055\),
upper height \(.04\), and penalties \(.11\pi,.08\pi\).
In particular
\[
 A_0(0)=\max_{.27\le u\le.49}\Re\Psi(u+ih_e,1/2).
 \tag{6}
\]
Include the same true-end constant
\[
 E_*=\frac35+\frac{2\pi}{100}+\frac{\log4}{100}<\frac{69}{100},
 \qquad
 {\cal A}=\max\{A_0(0),A_L(0),A_R(0),A_-(0),A_+(0),E_*\}.
 \tag{7}
\]

Let \(\Theta(a,y)\) be the original conditional critical action.
The [positive-output conditional theorem](research_mixed_four_conditional_positive_output_real_arc.md)
defines
\[
 L(y)=E_{1/2}(2/25;y),\qquad
 M_2(y)=\max_{2/25\le t\le r_0}\Re Q_1(t+ih_s;1/2,y),
 \tag{8}
\]
where \(r_0<1/2\) can be chosen sufficiently close to one half
to contain the whole compact critical family. This is compatible
with the right-half connection theorem: its initial choice of
the right-cut collar allows every sufficiently small further
decrease of its width before \(N\).

Corollary 2 of that connection theorem gives, for every one of
the six entries \(A_\ell(0)\) in (7), every third-factor profile
\(R_j^3(y,z)\), and either complete second-weight rate
\[
 W_2^{\rm fac}=-\Re g(y)-2\pi H,\qquad W_2^{\rm force}=0,
 \tag{9}
\]
the individual inequalities
\[
 A_\ell(0)+B+R_j^3(y,z)+W_2^\nu-\frac\beta2\Re g(z)
            \le\Lambda_{123}(z)-\frac1{6400},
          \qquad B\in\{M_2(y),L(y)\}.
 \tag{10}
\]
These are formal profile comparisons proved before finite summation,
not an inference from the modulus of the three-factor product.
The complete finite third factor on (1) has its original four
profiles, by Section 2 of the
[second-selection source reduction](research_mixed_second_selected_plateau_reduction.md).

## 2. A written lower bound for the midpoint endpoint action

Use the original coefficient action
\[
\begin{split}
 F(e,u)&=-2J(1/2-u)-3J(u)-J(e-u)+i\pi eu,\\
 S(e)&=F(e,u_c(e)),\qquad \lambda(t)=\Re S(t)\quad(t\ \hbox{real}),\\
 u_c(1/2)&=1/4+i h_*,\qquad h_*=\frac{\log3}{4\pi}.
\end{split}
 \tag{11}
\]
The branches and constants are those in the
[complete-column source](research_mixed_symmetric_closing_complete_column_norm.md)
and its [midpoint action proof](research_mixed_symmetric_closing_complete_column_obstruction.md).
For \(L(h)=\Re F(1/2,1/4+ih)\), their exact identities are
\[
 L(0)=\frac32b_2,\quad L'(0)=-\frac\pi2,\quad
 L''(h)=6\pi\frac{1-\tanh^2(\pi h)}{1+\tanh^2(\pi h)},
 \qquad b_2=\frac2\pi
       \sum_{k\ge0}\frac{(-1)^k}{(2k+1)^2}.
 \tag{12}
\]
On \(0\le h\le h_*\),
\(\tanh(\pi h)\le2-\sqrt3<1/3\). Hence \(L''>24\pi/5\).
Twice integrating this inequality, with the fixed initial
values in (12), gives
\[
 \lambda(1/2)>
       \frac32b_2-\frac{\log3}{8}
                         +\frac{3(\log3)^2}{20\pi}.
 \tag{13}
\]

All scalar bounds needed here have elementary written witnesses.
Four alternating terms and \(\pi<22/7\) give
\[
 b_2>\frac7{11}\left(1-\frac19+\frac1{25}-\frac1{49}\right)
       =\frac{70112}{121275}>\frac{23}{40};
 \tag{14}
\]
the final cross-product difference is \(15155>0\).
The exponential series gives \(e<3\), and
\[
 e^{11/10}>
 \sum_{k=0}^5\frac{(11/10)^k}{k!}
 =\frac{36015101}{12000000}>3 .
 \tag{15}
\]
Thus \(1<\log3<11/10\). Inserting these bounds in (13) yields
\[
             \lambda(1/2)>
        \frac{69}{80}-\frac{11}{80}+\frac{21}{440}
          =\frac{17}{22}>\frac{77}{100}.
 \tag{16}
\]
No coefficient or action has been evaluated; (13) retains the
positive curvature term on its original critical segment.

## 3. A lower trial for the actual cap main profile

We first show \(\lambda(2/5)>\lambda(1/2)\).
The exact radical derivative identity in Section 2 of the
complete-column source is
\[
 (\lambda+J)'(t)=\frac12\log\frac{1-b(t)}{1+b(t)},\qquad
 \sqrt{1-2e^{2\pi it}}=a(t)+ib(t),\quad a(t)>0.
 \tag{17}
\]
At \(t=2/5\), the original branch has \(b<0\). Since
\(\cos(\pi/5)>4/5\) and \(\sin(\pi/5)<3/5\),
\[
 a^2\ge\Re(1-2e^{4\pi i/5})>\frac{13}{5}>\frac{64}{25},
 \qquad |b|=\frac{\sin(\pi/5)}a<\frac38 .
 \tag{18}
\]
Consequently
\[
 (\lambda+J)'(2/5)<\tfrac12\log(11/5)<\frac25.
 \tag{19}
\]
The logarithmic inequality follows from
\(e^{4/5}>1+4/5+(4/5)^2/2+(4/5)^3/6=827/375>11/5\).
Meanwhile
\[
 J'(2/5)=\log(2\sin(2\pi/5))>\tfrac12\log3>\frac12.
 \tag{20}
\]
Thus \(\lambda'(2/5)<-1/10\). The original real curvature
\(\lambda''<0\) on \((0,1/2)\), proved in Lemma 1 of the
[early real-row source](research_mixed_cap_early_taper_real_rows.md),
implies strict decrease from \(2/5\) to \(1/2\). This proves
the claim.

At the real trial point \(e=2/5\), the original type-four phase is
\[
          \Re\Psi(2/5,1/2)
             =\lambda(2/5)-J(1/10)-J(2/5).
 \tag{21}
\]
The sine upper bound gives
\[
 -J(1/10)\ge\frac1{10}\{1-\log(\pi/5)\}>\frac{29}{200}.
 \tag{22}
\]
Indeed \(\pi/5<22/35\) and
\(\log(35/22)>26/57>9/20\).
Also, on \(2/5\le t\le1/2\),
\(2\sin\pi t>19/10\), using
\(\sin^2(2\pi/5)=(5+\sqrt5)/8>(19/20)^2\) and
\(\sqrt5>111/50\). Therefore
\[
 -J(2/5)=\int_{2/5}^{1/2}\log(2\sin\pi t)\,dt
       >\tfrac1{10}\log(19/10)>\frac3{50},
 \tag{23}
\]
where \(\log(19/10)>18/29>3/5\).

It remains to put the trial on the actual private line.
Set \(e=2/5+i\eta\), \(h_e\le\eta\le0\).
This entire segment is in the
[original endpoint rectangle](research_mixed_endpoint_cap_rectangle.md).
Its original critical root obeys
\[
 \Re u_c>17/100,\qquad \Im u_c>0,\qquad
                         0<\Re(e-u_c)<1/2.
 \tag{24}
\]
The envelope derivative is exactly
\[
                  S'(e)=-J'(e-u_c(e))+i\pi u_c(e).
 \tag{25}
\]
Since \(e-u_c\) has negative imaginary part and real part
between zero and one half, its sine is in the lower right
quadrant. Thus
\(\Im S'(e)>\pi\Re u_c>17\pi/100\).
For the two other logarithms, their radii are at most one
and their original strip arguments give
\[
 \Im g'(9/10+i\eta)\ge-2\pi/5,\qquad
                   \Im g'(2/5+i\eta)\le\pi/10 .
 \tag{26}
\]
Keeping the type-four chirp in (4), equations (25)--(26) give
\[
 \Im\Psi_e(2/5+i\eta,1/2)
 >\frac{17\pi}{100}-\frac{2\pi}{5}-\frac{\pi}{10}
                           -\frac\pi2+\frac{2\pi}{5}
 =-\frac{43\pi}{100}.
 \tag{27}
\]
Therefore \(\partial_\eta\Re\Psi<43\pi/100\) on the whole
segment. Its downward cost from zero to \(h_e>-.051\) is less than
\[
             \frac{51}{1000}\frac{43\pi}{100}<\frac7{100};
 \tag{28}
\]
with \(\pi<22/7\), the final comparison is \(48246<49000\).

Combining (16), (21)--(23), and (28) proves the promised
profile inequality
\[
 \boxed{\quad
 A_0(0)\ge\Re\Psi(2/5+ih_e,1/2)
    >\frac{77}{100}+\frac{29}{200}+\frac3{50}-\frac7{100}
     =\frac{181}{200}=\frac9{10}+\frac1{200}.
 \quad}
 \tag{29}
\]
The trial belongs to the exact main interval in (6).
No lower estimate for \(U_{1,N}\), or for any finite row,
has been used. In particular (29) does not identify a
supporting plane with a contour maximum.

## 4. Every cap and conditional alternative on the real arc

The [complete real cap transport](research_mixed_initial44_complete_real_cap_transport.md)
retains every cap row, both unweighted joins, all six weighted
sampling pieces and the true ends. For either first Fourier choice
it gives, with any prescribed allowance,
\[
 |U_{1,N}(w,X)d_N(X)X^{-\sigma N}|
 \le \operatorname{poly}(N)
                 e^{N\{\max({\cal A},9/10)+\tau_1\}}.
 \tag{30}
\]
On (1), its fixed parameter \(\rho\) may be chosen as \(1/8\).
The whole first Fourier polynomial has upper rate
\(\max\{-J(a),0\}=0\), and \(|X^{-\sigma N}|=1\);
both alternatives, including their zeros, are retained in (30).
Equation (29) makes its maximum exactly \({\cal A}\).

The positive-output conditional theorem gives the complete sum
\[
 |C_{1,N}(X,Y)|\le\operatorname{poly}(N)
              e^{N\{\max(\Re\Theta(a,y),L(y))+\tau_2\}}.
 \tag{31}
\]
Its physical partition retains every index \(0\le j<N\),
including the moving incoming-zero collar, with zero-safe bounds.
Its central contour has the original \(+N\) density, both
unweighted joins, two horizontal corrections and all four
vertical weighted halves. No old nonpositive-output source
statement is being applied at \(H>0\).
Equations (48)--(49) of that theorem prove on (1)
\[
       \Re\Theta(a,y)\le\Re\Theta(1/2,y)\le M_2(y).
 \tag{32}
\]
The first inequality uses the original unit-circle multiplier;
the second uses private vertical convexity at the critical real
index, on the original unsquared branch. In particular it does
not bound a signed sum below by a selected saddle contribution.

Multiply (30)--(31), the complete third-factor four-profile
estimate, the two rates (9), and the unchanged outgoing
halfweight. Equations (10), (29), and (32) pay each term:
\[
 {\cal A}+\max\{\Re\Theta(a,y),L(y)\}
             +R_j^3(y,z)+W_2^\nu-\frac\beta2\Re g(z)
       \le\Lambda_{123}(z)-\frac1{6400}.
 \tag{33}
\]
This explicitly accounts for the formerly additional constant
cap alternative. It uses neither an assertion
\({\cal A}=B_*\) nor an unproved continuation of a calibrated
negative-height source.

**Theorem.** For every \(\tau>0\), both parities, both
\(\sigma,\beta\), and the actual references in (1),
\[
 {\cal B}_{\sigma,\beta,N}(a,y,z)
 \le C_\tau N^{A_\tau}
             e^{N\{\Lambda_{123}(z)-1/12800+\tau\}},
                    \qquad 1/2\le a\le7/8 .
 \tag{34}
\]
The estimate is uniform for \(b,v\in P\) and every real ordinary
color \(w\in[-2,2]\). A sufficiently small fixed ordinary-color
disk, and all fixed derivatives on smaller disks, have the same
bound with polynomial factors.

*Proof.* Equations (30)--(33) retain the full finite inventories.
Allocate a total error less than the spare \(1/12800\), plus
the final prescribed \(\tau\), among their uniform symbols,
rounding allowances and finite sums. The cap source is already
uniform in all real colors. Its exact degree is less than \(N\)
in \(w\); the same interval/Chebyshev continuation as in the
cap theorem costs any separately chosen small rate allowance.
Cauchy's formula supplies fixed jets on smaller disks.
The color-independent weights and kernels are constant
multipliers in this argument, and none is divided out.
This proves (34). \(\square\)

The original \(+N\,da\) integration along any oriented subinterval
of this real arc preserves (34) with polynomial cost and the
unchanged exterior scalar. At \(m=4\) the third conditional
index is ordinary and its outgoing halfweight and marginal meet
the original terminal transform; at larger length they meet
the next ordinary factor. The full first and second weights
in (2) have closed their two incidences exactly once.

This theorem pays this real first-coordinate arc only. It does
not itself complete the first unselected left path, any missing
second-coordinate contour, a second-period packet, or an
arbitrary whole-word asymptotic.

## Direct source versions

| Source | SHA-256 |
|---|---|
| research_mixed_complete44_second_selected_right_half_connections.md | 49358cc1d991a59a8fbf38c64306e9d88e64b127e2e8a5229d741972036d00d5 |
| research_mixed_four_conditional_positive_output_real_arc.md | f3c971ea0c2c24f82c2250db5c8c1196a9700b6d3bb57849cf4130f4353cc0c2 |
| research_mixed_initial44_complete_real_cap_transport.md | dd8d313e1e23240943421b6fbb340f28de769f46d2c0f98f3a4a749be20d4420 |
| research_mixed_symmetric_closing_complete_column_norm.md | 4df2375a3ae9340b0137effb2d8193eed4a3ed090a0c1bde58fb9c434f3fe519 |
| research_mixed_symmetric_closing_complete_column_obstruction.md | c709d3cd53e32c54e036a952588357d1f3e50e422eafc2967fa1f898e1e005cf |
| research_mixed_cap_early_taper_real_rows.md | d82b0506e7e156463360773bc8ab0e798334ee3a733ce9e6275215027c9c7ebc |
| research_mixed_endpoint_cap_rectangle.md | 9211d45bdd031c908690a723ebcd4b40a34fed90f44858301a809ee5901c15e8 |
| research_mixed_second_selected_plateau_reduction.md | 015c85c322ff3563ec6752b5c499080c3e906360920aaeed2063508ef2db868f |
| research_mixed_fourier_weight_continuation.md | 0bae41d83f414eb91fd137de1242120a11408147d56ec752e466ca5ed7e7f48e |

The author read the complete proof and every directly used source
implication and checked the nine bindings. Independent review is
required before adoption. No mathematical numerical evaluation,
saved-value arithmetic, import, test, compilation or frozen-source
edit is used.
