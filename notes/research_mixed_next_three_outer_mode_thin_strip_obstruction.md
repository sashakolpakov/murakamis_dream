# A thin-strip obstruction for the largest outer Chebyshev mode

Private exact source deduction, 8 November 2026. No mathematical
numerical evaluation, saved-value calculation, or frozen-source edit
is used.

The largest Chebyshev mode allowed by the exact middle amplitude
cannot be bounded at the proposed preceding-factor rate by a
pointwise majorant on the inherited thin angular strip. This follows
from the nonzero original single-three packet, with its complete
Hermite trace retained. The assertion concerns a contour majorant,
not the signed value of that mode.

## 1. The original observation and its exact contour

Keep
\[
 N\ge3,\quad D=N-1,\quad q=e^{\pi i/N},\quad
 \eta_N=(-1)^D,\quad
 M=\lceil N/2\rceil,\quad
 U=\lfloor N/2\rfloor-1,\quad L=\lfloor N/6\rfloor,
 \qquad d_N=U-L.
 \tag{1}
\]
Here \(d_N\) denotes the largest amplitude degree, not the
forced factorial polynomial. In particular
\[
 \frac N3-2<d_N<\frac N3,\qquad
 \gamma_N=\frac12-\frac{d_N}{N}
       \in\left(\frac16,\frac16+\frac2N\right).
 \tag{2}
\]
All statements below concern sufficiently large levels, so
\(d_N>0\).

Use the original polynomials, crossing and closing functional
of [the radical contraction theorem](research_high_newton_radical_contraction.md):
\[
 s_a=2\sin(\pi a/N),\quad S_a=\prod_{\nu=1}^a s_\nu,\quad
 c_a=2\cos((2a+1)\pi/N),\quad
 e_a(x)=S_a^{-2}\prod_{\nu<a}(c_\nu-x).
 \tag{3}
\]
Let \(\mathcal K_{3,N}\) be the full original single-three
two-boundary kernel, including the first normals of its selected
trace. The outer mode is
\[
 \mathcal L_N(T_{d_N})
 =\phi_N^{(x)}
   [R(x)^3e_M(x)\mathcal K_{3,N}(-2,x)T_{d_N}(x/2)],
 \tag{4}
\]
where \(T_a(\cos u)=\cos(au)\). The radical \(e_M\) consumes
the outer normal exactly; it does not change the inner trace.
This is the literal mode functional in
[the outer Casimir observation](research_mixed_next_three_outer_casimir_observation.md).

For \(\Im u<0\), put
\[
 W_N(u)=\frac{e^{-iNu}}{(1-\eta_Ne^{-iNu})^2}
 \tag{5}
\]
and define the complete lower-horizontal integrand
\[
 \mathcal I_N(u)=
 \sin u\,e_M(-2\cos u)\,T_{d_N}(-\cos u)\,
 \mathcal K_{3,N}(-2,-2\cos u)\,
 e^{3iNu^2/(4\pi)}W_N(u).
 \tag{6}
\]
For any \(h>0\), the exact full trace formula is
\[
\begin{split}
 \mathcal L_N(T_{d_N})
 ={}&-\frac{N^2C_{N,3}}{\pi i}
       \int_{-\pi-ih}^{\pi-ih}\mathcal I_N(u)\,du\\
 &+\frac{\eta_NN^2C_{N,3}}{\pi}
       \int_{-h}^{h}
       \frac{g_N(\pi+iv)}{4\cosh^2(Nv/2)}\,dv,
 \qquad C_{N,3}=q^{3D^2/4},
\end{split}
 \tag{7}
\]
where \(g_N=\mathcal I_N/W_N\).
This is [the exact complete trace, Proposition 2](research_exact_complete_trace_contour.md).
The vertical current in (7) remains present. The lower integral
may be deformed within the open lower half-plane, with its
endpoints fixed, because its integrand is holomorphic there.

## 2. Exact radical factors at both parities

The original sine products give
\[
 e_M(-2\cos u)=
 \begin{cases}
  \displaystyle\frac{\cos(Nu/2)}{N},&N=2m,\\[2mm]
  \displaystyle-\frac{\sin(u/2)\sin(Nu/2)}
                 {N\cos^2(\pi/(2N))},&N=2m+1 .
 \end{cases}
 \tag{8}
\]
Indeed at even levels the monic double-node polynomial is
\(2T_m(x/2)\), and \(S_m^2=2N\). At odd levels the monic
distinct-node polynomial is
\[
 Q_{\rm o}(x)=(x+2)\{U_m(x/2)-U_{m-1}(x/2)\},
\]
\[
 Q_{\rm o}(-2\cos u)
       =4(-1)^m\sin(u/2)\sin(Nu/2),\qquad
 S_{m+1}^2=4N\cos^2(\pi/(2N)).
\]
Multiplication by the Newton sign \((-1)^M\) proves (8).
The odd simple node is included in this polynomial and vanishes
under its radical observation; it has not been replaced by a
double-node normal.

Canceling one denominator in (5) gives the exact identities
\[
 e_M(-2\cos u)W_N(u)=
 \begin{cases}
  \displaystyle\frac{e^{-iNu/2}}
                    {2N(1+e^{-iNu})},&N=2m,\\[2mm]
  \displaystyle-\frac{\sin(u/2)e^{-iNu/2}}
              {2iN\cos^2(\pi/(2N))(1-e^{-iNu})},&N=2m+1 .
 \end{cases}
 \tag{9}
\]
They hold throughout the open lower half-plane.
For example the remaining geometric denominator has an
absolutely convergent expansion there. After multiplication
by
\[
 T_{d_N}(-\cos u)=(-1)^{d_N}
                       \frac{e^{id_Nu}+e^{-id_Nu}}2,
 \tag{10}
\]
its two principal charges are
\[
 \frac12-\frac{d_N}{N},\qquad
 \frac12+\frac{d_N}{N}.
 \tag{11}
\]
Every further outer charge adds a positive integer. The
original inner Hermite trace still has its positive integer
charges and their derivative weights. Formula (9) does not
replace that inner trace by distinct-node sampling.

## 3. A lower bound for the actual integrand

The [full degree-two theorem](research_all_nonzero_degree_two_fillings.md),
Theorem 1 and Section 5, gives on a fixed complex bidisk
\[
 \mathcal K_{3,N}(-2,-2\cos u)
  =C_{N,3}N^{-3/2}A_3(0,u)e^{NS_3(0,u)}
                  (1+O_{\rm hol}(N^{-1})),
 \qquad A_3(0,0)\ne0.
 \tag{12}
\]
Its proof retains the full physical trace and every wire
index. Both parities use the same nonzero packet. That
source, Section 4, records the certified strict inequality
\[
 \mathfrak M_3:=\Re S_3(0,0)>\frac95 .
 \tag{13}
\]
Only this written consequence is used here; no certificate
is evaluated or replayed.

Separate evenness and the exact boundary Hessian in its
equation (21) give
\[
 \partial_u S_3(0,0)=0,\qquad
 \partial_u^2S_3(0,0)
       =-\frac{\cos(t_3/2)}{2\pi},\qquad
                   \Re\cos(t_3/2)>0.
 \tag{14}
\]
Consequently there are fixed \(h_0\in(0,1]\) and \(c>0\)
such that the closed segment \(-i[0,h_0]\) lies inside
the packet domain, its amplitude is separated from zero,
and
\[
 \Re S_3(0,-ih)\ge\mathfrak M_3+c h^2
       \qquad(0\le h\le h_0).
 \tag{15}
\]
This follows directly by Taylor expansion at zero and
then shrinking \(h_0\). No continuation to a macroscopic
unproved boundary domain is used.

Set
\[
                          x_N=\frac{\pi}{d_N}.
 \tag{16}
\]
Thus \(x_N=O(N^{-1})\). Uniform holomorphy on a slightly
larger compact neighborhood of the segment in (15) implies
\[
 \Re S_3(0,x_N-ih)\ge\mathfrak M_3-C/N
                  \qquad(0\le h\le h_0).
 \tag{17}
\]
Shrinking the segment once if necessary, the amplitude in
(12) stays uniformly nonzero at these points. The complete
relative packet therefore supplies, for large \(N\),
\[
 |\mathcal K_{3,N}(-2,-2\cos(x_N-ih))|
       \ge C^{-1}N^{-3/2}e^{N\mathfrak M_3},
       \qquad 0\le h\le h_0.
 \tag{18}
\]
The fixed factor \(e^{-C}\) from (17) is absorbed in \(C^{-1}\).

At these same points the mode has no small cosine factor:
\[
 |T_{d_N}(-\cos(x_N-ih))|
         =\cosh(d_Nh)\ge\frac12e^{d_Nh}.
 \tag{19}
\]
For every \(0<h\le h_0\), the denominators in (9) have
modulus at most \(2\). The elementary identities
\[
 |\sin(x_N-ih)|\ge\sin x_N\ge C^{-1}N^{-1},
 \qquad
 |\sin((x_N-ih)/2)|\ge C^{-1}N^{-1}
 \tag{20}
\]
are uniform even if \(h\) depends on \(N\) and tends to zero.
Also the original crossing chirp has modulus
\[
 \left|e^{3iN(x_N-ih)^2/(4\pi)}\right|
       =e^{3Nx_Nh/(2\pi)}\ge1 .
 \tag{21}
\]
Equations (9),(18)--(21) prove at both parities
\[
 \boxed{\quad
 |\mathcal I_N(x_N-ih)|
 \ge C^{-1}N^{-5}
             e^{N(\mathfrak M_3-\gamma_Nh)}
 \ge (C')^{-1}N^{-5}e^{N(\mathfrak M_3-1/6)},
 \qquad 0<h\le h_0 .
 \quad}
 \tag{22}
\]
In the last inequality a fixed factor \(e^{-2}\), from
(2) and \(h_0\le1\), is absorbed in \((C')^{-1}\).
The power \(N^{-5}\) is conservative: the odd extra sine
in (9) is included. Nothing in (22) discards an exact
factor or assumes a lower bound for a signed sum.

## 4. The contour-majorant obstruction and its limit

Put \(B_f=77/50+\pi/50\), the proved preceding-factor
attachment budget. The elementary inequality \(\pi<22/7\)
gives
\[
 B_f<\frac{561}{350},\qquad
 \frac95-\frac16-\frac{561}{350}
        =\frac{16}{525}>\frac1{40}.
 \tag{23}
\]
Fix any \(a>0\). Let \(\Gamma_N\) be a continuous path
in
\[
                   \{u:-h_0\le\Im u<0\}
 \tag{24}
\]
whose initial real coordinate is at most \(-a\) and whose
final real coordinate is at least \(a\). For large \(N\),
\(0<x_N<a\), so the path has a point with real coordinate
\(x_N\). Applying (22) there proves
\[
 \boxed{\qquad
 \sup_{u\in\Gamma_N}|\mathcal I_N(u)|
           \ge e^{N(B_f+1/40)}
            \quad\hbox{for all sufficiently large }N.
 \qquad}
 \tag{25}
\]
The estimate includes paths whose depths depend on \(N\).
The exact cancellation (9) is why sending the crossing
point arbitrarily close to the real axis does not evade it.

Thus no pointwise upper bound of polynomial-times-\(e^{NB_f}\)
for this entire lower integrand can hold on a left-to-right
contour confined to the inherited thin strip. This also
excludes the smaller target \(B_0=2383/1500\) for that method.
All polynomial trace prefactors, the original \(1/N\), and
the modulus-one scalars in the actual transfer leave the strict
comparison unchanged.

This does not prove a lower bound for
\(\mathcal L_N(T_{d_N})\). Its lower integral may cancel
internally or against its retained vertical current.
A deeper contour, or a bound that uses the actual
Chebyshev coefficients of \(H_N\) together with this
response, is not excluded. In particular this note does
not assert that a universal signed mode estimate at rate
\(B_f\) is false, and it does not change the exact
remaining-transfer identity.
