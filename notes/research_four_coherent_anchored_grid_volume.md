# Positive boundary transport gives the cube rate on an anchored grid

22 November 2026. Research note. Earlier final notes and public
manuscripts remain unchanged.

The original four-coherent scalar has a noncancelling geometric
asymptotic on a continuous family of half-grid boundary paths. An
exact three-input source initializes a positive recurrence. Its
growth exponent equals the action of the actual ideal cube.
This is a source estimate, with its original closing and phase,
rather than an estimate for a norm or for a formal critical value.

The result requires the displayed anchor and stops a fixed distance
before the boundary fold. Generic grid offsets and pair-wall starts
are not included.

## 1. Source, geometric domain and theorem

Use the full algebra of the
[four-boundary source theorem](research_four_coherent_boundary_polynomial_source.md).
Put
\[
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 \kappa=e^{\pi i d^2/(2N)},\quad
 U_a=\sum_{\ell=0}^d a^\ell f_\ell ,
 \tag{1}
\]
where the centered basis is orthonormal in the positive Newton
coefficient norm. All repeated-root Hermite coordinates, original
products, turns and Frobenius closings remain present. Define
\[
 \Phi_N(y,z;s,t)=\phi(U_yU_zU_sU_t).
 \tag{2}
\]

Write \(S=b+c\). Our parameter domain is
\[
 \begin{gathered}
 b,c>0,\qquad S<1,\qquad
                 1-S<R<1-\max(b,c),\\
                         0<h<R/2 .
 \end{gathered}
 \tag{3}
\]
For fixed \(b,c,R\), put
\[
 \begin{gathered}
 y=-e^{-2\pi ib},\quad z=-e^{-2\pi ic},\quad
 r=e^{-2\pi iR},\\
 h_j=(j+\tfrac12)/N,\quad k_j=R-h_j,\quad
 s_j=-q^{-1}Q^{-j},\quad t_j=-qrQ^j .
 \end{gathered}
 \tag{4}
\]
Thus \(s_j=-e^{-2\pi ih_j}\), \(t_j=-e^{-2\pi ik_j}\), and
\(s_jt_j=r\). The entries \(j=-1,0\) will initialize transport.

Let \(L(x)=\int_0^x\log|2\sin\pi v|\,dv\), with its odd,
one-periodic extension. On its strict multiplication domain set
\[
 m(x,y,u)=L(x+y)+L(u)-L(x)-L(y)
             -L(u-x)-L(u-y)-L(x+y-u).
 \tag{5}
\]
For \(k=R-h\), define
\[
 \begin{split}
 I_h&=\bigl(\max(b,c,1-R),\ \min(S,1-h,1-k)\bigr),\\
 \mathcal F(b,c,R,h)&=
       \max_{u\in I_h}\{m(b,c,u)+m(h,k,1-u)\}.
 \end{split}
 \tag{6}
\]
Every quadruple in (3) has all six pair sums below one and
total \(S+R>1\). The
[positive cube theorem](actual_newton_ideal_prism_and_associativity.md)
therefore gives a unique strict interior maximizer and an actual
convex ideal cube of volume \(\pi\mathcal F\).
Its usual second action \(m(u,h,1-k)\) equals
\(m(h,k,1-u)\) by \(L(1-x)=-L(x)\).

**Theorem.** For every compact \(\mathcal K\) in (3), there
are constants \(C_{\mathcal K},N_{\mathcal K}\) such that, whenever
\(N\ge N_{\mathcal K}\), \(j\ge0\), and
\((b,c,R,h_j)\in\mathcal K\),
\[
 \boxed{\quad
 \Phi_N(y,z;s_j,t_j)=
       e^{-\pi i d(S+R)}\,P_{N,j},\qquad P_{N,j}>0,\qquad
 |\log P_{N,j}-N\mathcal F(b,c,R,h_j)|
                         \le C_{\mathcal K}\log N .
 \quad}
 \tag{7}
\]
The assertion includes both parities and composite levels.
The original normalized closing of the two turned products is
\(\Phi_N/N^2\), since all four coherent inputs have norm
\(\sqrt N\). It has the same exponential rate. In particular,
on convergent shape sequences in this compact domain,
\(\pi N^{-1}\log|\Phi_N/N^2|\) tends to the volume of this cube.
No knot-volume conclusion is asserted.

## 2. The exact carrier and the two source initial values

The common phase in (7) is an exact source property, not a choice
of a positive replacement. Here is a verification from the full
coefficients in the four-boundary theorem. For a unit pair of
angles \(v,w\), write
\(U_{-e^{-2\pi iv}}U_{-e^{-2\pi iw}}=\sum_\ell B_\ell e_\ell\).
At generic parameters its consecutive ratio is real:
\[
 \frac{B_{\ell+1}}{B_\ell}
 =-\frac{\sin\pi x\,\sin\pi(x-v-w)}
         {\sin\pi(x-v+\tfrac1{2N})\,
          \sin\pi(x-w+\tfrac1{2N})},\qquad x=(\ell+1)/N .
 \tag{8}
\]
Its first coefficient divided by
\[
             \theta_N(v+w)=
             -\kappa^2 e^{-\pi i[d(v+w)+1/N]}
 \tag{9}
\]
is real, as follows by writing its finite geometric products as
sines and cosines. Thus every \(B_\ell/\theta_N(v+w)\) is real.
Continuity extends this assertion across exact source zeros.
The original four-input contraction is
\(\sum_\ell B_\ell(y,z)B_{d-\ell}(s,t)\). Since
\(\kappa^4=Q\), the product of its two carriers is exactly
\[
               \omega_N=e^{-\pi i d(S+R)} .
 \tag{10}
\]
Consequently
\(H_j=\omega_N^{-1}\Phi_N(y,z;s_j,t_j)\) is real, including
at the two anchor entries.

The exact unit and socle readouts give
\[
 \begin{split}
 \Phi_N(y,z;s_0,t_0)
     &=\kappa\sqrt N\,\mathcal C_N(y,z,t_0),\\
 \Phi_N(y,z;s_{-1},t_{-1})
     &=\frac{\kappa^2}{N}F_N(y)F_N(z)F_N(t_{-1}),\qquad
 F_N(a)=\sum_{\ell=0}^d(-qa)^\ell .
 \end{split}
 \tag{11}
\]
Here \(t_0\) has angle \(R_N=R-1/(2N)\), whereas \(t_{-1}\)
has angle \(R+1/(2N)\). The triple \(b,c,R_N\) ranges in a
compact strict prism family. The
[initialized three-input theorem](research_single_leg_radial_turn_source.md)
therefore applies with all radii equal to one.

For completeness, its calibrated phase fixes the sign of the
initial value. Let \(A_N=S+R_N\), and denote its action and
amplitude by \(\Psi_3,B_3\), with the canonical branches of that
theorem. The elementary unit-circle dilogarithm formulas give
\[
 \begin{split}
 \Re\Psi_3&=\pi(1-A_N),\qquad
             \arg B_3=-3\pi/4+\pi A_N,\\
 -\Im\Psi_3&=M(b,c,R_N),\qquad
             M(b,c,R)=m(b,c,1-R)>0 .
 \end{split}
 \tag{12}
\]
Indeed \(\Im\operatorname{Li}_2(e^{-2\pi ix})/(2\pi)=L(x)\).
For the real part, apply
\(\Re\operatorname{Li}_2(e^{2\pi ix})
=\pi^2(x^2-x+1/6)\) on \(0\le x\le1\), reducing the
total angle by one. The amplitude phase is the sum of its three
canonical logarithm phases, not a newly chosen square root.
The identity \(L(1-x)=-L(x)\) gives the last equality in (12).

Including both \(\kappa\)'s, the complete initial phase is
\[
 \kappa^2e^{\,i\pi/4-\pi i/(2N)}
 e^{\,i(-3\pi/4+\pi A_N)}e^{\,iN\pi(1-A_N)}
                         =\omega_N .
 \tag{13}
\]
The initialized relative error is \(O_{\mathcal K}(N^{-1})\).
Its nonzero amplitude is uniformly bounded above and below.
Because \(H_0\) is exactly real, (11)--(13) imply, uniformly,
\[
 H_0>0,\qquad
 \log H_0=N M(b,c,R)+O_{\mathcal K}(\log N),\qquad
                         |H_{-1}|\le C_{\mathcal K}/N .
 \tag{14}
\]
The last bound follows from the geometric sums in (11): their
denominators stay away from zero on this compact angle family.
Also \(M\) has a positive compact minimum. Hence
\(\Delta_0:=H_0-H_{-1}>0\) and
\(\Delta_0/H_0=1+O_{\mathcal K}(e^{-c_{\mathcal K}N})\).

## 3. Positive transfer before the fold

The exact source equation, with
\(\sigma(s,t)=(Qs,Q^{-1}t)\), is
\[
 B(\sigma\Phi_N-\Phi_N)+D(\sigma^{-1}\Phi_N-\Phi_N)
                  =\lambda_N\Phi_N,\qquad
 \lambda_N=(Q-1)(1-Qyz),
 \tag{15}
\]
\[
 B=\frac{(t+q)^2(1-Qys)(1-Qzs)}{(t-s)(t-Qs)},\qquad
 D=\frac{(s+q)^2(1-Qyt)(1-Qzt)}{(Qt-s)(t-s)}.
 \tag{16}
\]
On (4), \(\sigma\) replaces \(j\) by \(j-1\).
Set \(g_N=-4e^{\pi i(2/N-S)}\),
\(\mathsf b_j=B_j/g_N\), \(\mathsf d_j=D_j/g_N\),
and \(\Lambda_N=\lambda_N/g_N\).
With \(\delta_j=k_j-h_j\), direct sine conversion gives
\[
 \begin{split}
 \mathsf b_j&=
 \frac{\sin^2\pi(k_j+\tfrac1{2N})\,
       \sin\pi(b+h_j-\tfrac1N)\sin\pi(c+h_j-\tfrac1N)}
      {\sin\pi\delta_j\,\sin\pi(\delta_j+\tfrac1N)},\\
 \mathsf d_j&=
 \frac{\sin^2\pi(h_j+\tfrac1{2N})\,
       \sin\pi(b+k_j-\tfrac1N)\sin\pi(c+k_j-\tfrac1N)}
      {\sin\pi\delta_j\,\sin\pi(\delta_j-\tfrac1N)},\\
 \Lambda_N&=\sin(\pi/N)\sin\pi(S-\tfrac1N).
 \end{split}
 \tag{17}
\]
All are positive along the transport path, for large \(N\).
The fixed fold margin supplies
\(\mathsf b_j\ge c_{\mathcal K}>0\) and
\(\Lambda_N/\mathsf b_j\le C_{\mathcal K}/N\).
No uniform lower bound on \(\mathsf d_0\), which is of order
\(N^{-2}\), is asserted.

Put \(\rho_j=\mathsf b_j/\mathsf d_j\). To control it uniformly
even near the initial layer, define
\[
 f_N(v)=
 \frac{\sin^2\pi v}
 {\sin\pi(b-\tfrac3{2N}+v)\sin\pi(c-\tfrac3{2N}+v)}.
 \tag{18}
\]
Then exactly
\[
 \rho_j=
 \frac{f_N(k_j+\tfrac1{2N})}{f_N(h_j+\tfrac1{2N})}
 \frac{\sin\pi(R-\tfrac{2(j+1)}N)}
      {\sin\pi(R-\tfrac{2j}N)} .
 \tag{19}
\]
On the relevant interval, the cotangent is decreasing, so
\((\log f_N)'\ge c_{\mathcal K}>0\). Explicitly it is the
sum of the two positive differences
\(\pi[\cot\pi v-\cot\pi(b-\tfrac3{2N}+v)]\) and its
\(c\)-analogue. All their arguments lie in \((0,1)\).
The identity
\(\cot x-\cot(x+a)=\sin a/[\sin x\sin(x+a)]\)
gives the stated uniform positive lower bound even as \(v\) tends
to zero.
The two arguments of \(f_N\) in (19) have a fixed positive
separation. The last factor is \(1+O_{\mathcal K}(N^{-1})\).
Consequently, throughout transport to a target in \(\mathcal K\),
\[
                         \rho_j\ge1+c_{\mathcal K}.
 \tag{20}
\]

For \(\Delta_j=H_j-H_{j-1}\), (15) now gives
\[
 \Delta_{j+1}=\rho_j\Delta_j+
                   \frac{\Lambda_N}{\mathsf d_j}H_j .
 \tag{21}
\]
Starting from (14), all \(H_j,\Delta_j\) are positive.
Moreover \(\Delta_{j+1}\ge(1+c_{\mathcal K})\Delta_j\);
geometric summation of
\(H_j=H_0+\sum_{m=1}^j\Delta_m\) gives
\[
                    c_{\mathcal K}\le H_j/\Delta_j
                                      \le C_{\mathcal K}.
 \tag{22}
\]
Thus (21) has the sharper form
\[
 \Delta_{j+1}=\rho_j\Delta_j
       \left[1+
       \frac{\Lambda_N}{\mathsf b_j}\frac{H_j}{\Delta_j}\right]
                  =\rho_j\Delta_j[1+O_{\mathcal K}(N^{-1})].
 \tag{23}
\]
There are \(O_{\mathcal K}(N)\) steps. Taking logarithms and
using (14), (22) proves
\[
 \log H_j=\log H_0+\sum_{m=0}^{j-1}\log\rho_m
                                      +O_{\mathcal K}(1).
 \tag{24}
\]
In particular the small coupling in (21) has not changed the
leading exponent.

## 4. The rate integral and the actual cube action

Define the classical ratio
\[
 \rho_0(h)=
 \frac{\sin^2\pi(R-h)\sin\pi(b+h)\sin\pi(c+h)}
      {\sin^2\pi h\sin\pi(b+R-h)\sin\pi(c+R-h)}.
 \tag{25}
\]
In the product of (19), its last factors telescope to
\(\sin\pi(R-2j/N)/\sin\pi R\), bounded above and below.
All remaining factors are smooth log-sine Riemann sums except
the explicit denominator \(\sin(\pi(m+1)/N)\) at zero. On
this interval, \(\log\sin\pi v=\log v+\) a smooth function.
Integral comparison for \(\log(j!)\) bounds its Riemann error
by \(O(\log N)\). The bounded shifts of the other arguments
cost \(O_{\mathcal K}(1)\). Moving the upper integration limit
from \(j/N\) to \(h_j\) costs at most \(O(\log N)\) after
multiplication by \(N\). Hence
\[
 \sum_{m=0}^{j-1}\log\rho_m
      =N\int_0^{h_j}\log\rho_0(v)\,dv
                                  +O_{\mathcal K}(\log N).
 \tag{26}
\]

We next identify this primitive with the cube, rather than only
with a formal boundary characteristic. Let \(u\) be the unique
critical point in (6), and set \(k=R-h\). Its equation is
\[
 \sin\pi(S-u)\sin\pi(u+h)\sin\pi(u+k)
 +\sin\pi(u+R)\sin\pi(u-b)\sin\pi(u-c)=0 .
 \tag{27}
\]
Put
\[
 X=\cot\pi u,\quad B_0=\cot\pi b,\quad C_0=\cot\pi c,\quad
 H=\cot\pi h,\quad K=\cot\pi k .
 \tag{28}
\]
After division by the positive sine factors, (27) becomes
\[
 \begin{split}
 &[(B_0+C_0)X-B_0C_0+1](X+H)(X+K)\\
 &\hspace{5mm}
 +[(H+K)X+HK-1](X-B_0)(X-C_0)\\
 &\hspace{5mm}
 =(X^2+1)[(B_0+C_0+H+K)X+HK-B_0C_0]=0.
 \end{split}
 \tag{29}
\]
Here \(B_0+C_0>0\) and \(H+K>0\), since \(S,R<1\).
It follows that
\[
 \frac{X+H}{X+K}
       =\frac{(B_0+H)(C_0+H)}{(B_0+K)(C_0+K)},\qquad
 \frac{\sin\pi(u+h)}{\sin\pi(u+k)}
       =\frac{\sin\pi k}{\sin\pi h}
        \frac{\sin\pi(b+h)\sin\pi(c+h)}
             {\sin\pi(b+k)\sin\pi(c+k)}.
 \tag{30}
\]
No denominator vanishes in the displayed strict domain.

The envelope derivative of (6), at fixed \(b,c,R\), is
\[
 \partial_h\mathcal F
     =\log\left[
         \frac{\sin\pi k}{\sin\pi h}
         \frac{\sin\pi(u+h)}{\sin\pi(u+k)}\right]
                         =\log\rho_0(h).
 \tag{31}
\]
Smoothness follows either from the strict stationary maximum or
the explicit critical cotangent in (29). As \(h\downarrow0\),
the interval \(I_h\) shrinks to \(u=1-R\), by (3).
The second action tends to \(m(0,R,R)=0\); continuity of \(L\)
therefore gives
\[
 \mathcal F(b,c,R,0)=m(b,c,1-R)=M(b,c,R),\qquad
 \mathcal F=M+\int_0^h\log\rho_0(v)\,dv .
 \tag{32}
\]
Thus (14), (24), (26), and (32) prove (7).

## 5. Scope and complete proof sources

Only \(s_j\), not a generic boundary parameter, lies on the
anchored half-grid. Fixed \(st\) shifts preserve a fractional
grid offset. This proof does not control arbitrary offsets, a
boundary layer connecting them to the anchor, or pair-wall
initializations when \(R\ge1-\max(b,c)\).
It does not cross the fold \(h=R/2\) or estimate its
pole-cancelled normal readout. Symmetry does not automatically cover
\(h>R/2\): the smaller parameter need not lie on this anchored
grid after the swap.

The theorem proves a nonzero original source coefficient and its
geometric rate on the stated universal cell family. It does not
assert a full output approximation, arbitrary Conway composition,
or a finite-exception knot-volume theorem. All coefficients and
carriers come from the original full-Hermite scalar.

The following three complete proof directs were read at their
matching pins:

| Source | SHA-256 |
|---|---|
| Four-boundary source, 409 lines | 93241074830ff4b844ba5baafd06a15bf08ec6bddc3a1498727f110ebe297d84 |
| Single-leg initialized source, 326 lines | c624e0edbaadb57279c00420d3f552e93c67cb84972926aad27ff51c2c973e7e |
| Actual prism and cube geometry, 377 lines | c29321805df39a49854665df1255db1ec7180397a5dd689f19289d61335871c9 |

Only written mathematics and text operations were used.
This research proof is author-final.
