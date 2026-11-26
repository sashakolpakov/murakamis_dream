# Exact positive transition weights for the attached outgoing coefficients

Private finite-source deduction, 9 November 2026. The original radical
Newton products have alternating Chebyshev coefficients with strictly
positive magnitudes at both parities. Their alternating row sign cancels
the original factor \((-q)^b\); all remaining outgoing phases are retained.
The exact weights have a uniform logarithmic rate, giving a strictly
sharper coefficient ceiling at every fixed interior frequency.

No lower bound for a coherent coefficient or adequate attachment budget
is inferred. No mathematical numerical evaluation, saved-value arithmetic,
or frozen-source edit is used.

## 1. Unchanged full outgoing source

Keep the normalization of
[the attached action-weighted source, (29)--(33)](research_mixed_next_outgoing_action_weighted_green_ellipse.md):
\[
\begin{gathered}
 D=N-1,\quad\theta=\pi/N,\quad q=e^{i\theta},\quad r=q^{-2},
 \quad M=\lceil N/2\rceil,\quad U=D-M=\lfloor N/2\rfloor-1,
 \quad\kappa_N=q^{D^2/2},\\
 s_j=2\sin(j\theta),\quad S_j=\prod_{h=1}^js_h,\quad S_0=1,
 \quad c_j=2\cos((2j+1)\theta),\\
 P_b^{\rm rad}(X)=\frac{e_b(X)}{e_M(X)}
       =\prod_{h=M}^{b-1}\frac{c_h-X}{s_{h+1}^2},
                       \qquad M\le b\le D,\\
 C_{b,N}(Z)=\sum_{\ell=0}^{D-b}
       \frac{r^{-b\ell}(r^{b+1};r)_\ell(rZ;r)_\ell}
                         {(r;r)_\ell^2},\qquad
 \alpha_{b,N}=(-q)^bC_{b,N},\\
 F_N^+(X,Z)=\sum_{b=M}^{D}\alpha_{b,N}(Z)P_b^{\rm rad}(X)
           =\sum_{k=0}^{U}f_{k,N}(Z)T_k(-X/2).
\end{gathered}
\tag{1}
\]
The quotient is an ordinary polynomial, including at zeros of \(e_M\).
The stop \(D-b\) is literal, and \(C_{D,N}=1\). No outgoing cutoff
is introduced.

Write \(b=M+d\), \(0\le d\le U\), and set
\[
 \mathcal D_d=\prod_{h=M}^{M+d-1}s_{h+1}^2
       =S_{M+d}^2/S_M^2>0,\quad \mathcal D_0=1,\qquad
 \eta_k=\begin{cases}1,&k=0,\\2,&k>0.\end{cases}
\tag{2}
\]
For integers \(0\le j\le n<N\), define
\[
                         B_{n,j}=\frac{S_n}{S_jS_{n-j}}>0.
\tag{3}
\]

## 2. Exact finite expansions at both parities

The elementary finite binomial identity gives
\[
 \prod_{h=0}^{n-1}(1-q^{2h-(n-1)}z)
           =\sum_{j=0}^n(-1)^jB_{n,j}z^j,\qquad n<N.
\tag{4}
\]
Here is the phase check. Expanding the uncentered product, by induction
on its number of factors, gives coefficient
\[
 (-1)^j(q^2)^{j(j-1)/2}
       \prod_{h=1}^j\frac{1-q^{2(n-j+h)}}{1-q^{2h}}.
\]
Since \(1-q^{2a}=-iq^a s_a\), the quotient product equals
\(q^{j(n-j)}B_{n,j}\). Replacing \(z\) by \(q^{-(n-1)}z\)
cancels the entire phase:
\(j(j-1)+j(n-j)-j(n-1)=0\). No sine denominator vanishes.

Put \(X=-(z+z^{-1})\). At even levels,
\(c_{M+h}=-2\cos((2h+1)\theta)\), so
\[
 \mathcal D_dP_{M+d}^{\rm rad}(-(z+z^{-1}))
             =z^{-d}(q^{-(2d-1)}z;q^2)_{2d}.
\tag{5}
\]
The case \(d=0\) is the empty product. By (4) and reciprocal symmetry,
\[
 P_{M+d}^{\rm rad}(X)
      =\sum_{k=0}^d(-1)^{d+k}\beta_{d,k,N}T_k(-X/2),\qquad
 \beta_{d,k,N}=\frac{\eta_kB_{2d,d-k}}{\mathcal D_d}>0
                                    \quad(N\ \mathrm{even}).
\tag{6}
\]
The factor \(\eta_k\) combines opposite Laurent powers when \(k>0\)
and keeps the constant coefficient once.

At odd levels, \(c_{M+h}=-2\cos((2h+2)\theta)\). The centered
product has an extra middle factor \(1-z\), which cancels exactly:
\[
 \mathcal D_dP_{M+d}^{\rm rad}(-(z+z^{-1}))
       =z^{-d}\frac{(q^{-2d}z;q^2)_{2d+1}}{1-z}.
\tag{7}
\]
This is a polynomial quotient, with no singularity at \(z=1\).
For \(0\le j\le d\) put
\[
 w_{d,j,N}=(-1)^j\sum_{\ell=0}^j(-1)^\ell B_{2d+1,\ell}.
\tag{8}
\]
These numbers are strictly positive. Indeed, for \(1\le j\le d\),
\[
 \frac{B_{2d+1,j}}{B_{2d+1,j-1}}
       =\frac{\sin((2d+2-j)\theta)}{\sin(j\theta)}>1,
\tag{9}
\]
because the numerator-minus-denominator difference is
\(2\cos((d+1)\theta)\sin((d+1-j)\theta)>0\);
here \(d+1\le(N-1)/2\). Pairing successive terms of (8) proves
positivity, including \(w_{d,0,N}=1\).

The coefficient of \(z^{j-d}\) in (7) is
\(\sum_{\ell=0}^j(-1)^\ell B_{2d+1,\ell}\). The original product
is invariant under \(z\mapsto z^{-1}\), supplying the coefficients
with \(j>d\). Thus (6) holds at odd levels as well, now with
\[
          \beta_{d,k,N}
             =\frac{\eta_kw_{d,d-k,N}}{\mathcal D_d}>0
                                    \quad(N\ \mathrm{odd}).
\tag{10}
\]
Both formulas include every row through \(b=D\).

## 3. Uniform comparison for the odd partial sum

The recursion \(w_{d,j,N}=B_{2d+1,j}-w_{d,j-1,N}\) and positivity
give, for \(1\le j\le d\),
\[
 B_{2d+1,j}-B_{2d+1,j-1}
                   \le w_{d,j,N}\le B_{2d+1,j}.
\tag{11}
\]
For \(j=d-k\ge1\), its relative lower bound is
\[
 1-\frac{B_{2d+1,j-1}}{B_{2d+1,j}}
 =\frac{2\cos((d+1)\theta)\sin((k+1)\theta)}
                  {\sin((d+k+2)\theta)}\ge\frac4{N^2}.
\tag{12}
\]
The denominator is positive and at most one. Also
\[
 \cos((d+1)\theta)\ge\sin(\pi/(2N))\ge1/N,\qquad
 \sin((k+1)\theta)\ge2(k+1)/N\ge2/N,
\]
using \(\sin x\ge2x/\pi\) on \([0,\pi/2]\). For \(j=0\),
\(w=B=1\), and the same comparison holds. Thus
\[
 \frac4{N^2}\frac{\eta_kB_{2d+1,d-k}}{\mathcal D_d}
 \le\beta_{d,k,N}
 \le\frac{\eta_kB_{2d+1,d-k}}{\mathcal D_d}
                                        \quad(N\ \mathrm{odd}).
\tag{13}
\]
The odd partial sum therefore changes the sine-binomial magnitude
by at most a fixed power of \(N\).

## 4. The signed actual coefficient and its dual finite source

Equations (1), (6), and (10) give exactly
\[
 \boxed{\quad
 f_{k,N}(Z)=(-1)^{M+k}
       \sum_{d=k}^{U}q^{M+d}\beta_{d,k,N}C_{M+d,N}(Z),
                          \qquad0\le k\le U.
 \quad}
\tag{14}
\]
Indeed \((-q)^{M+d}(-1)^{d+k}=(-1)^{M+k}q^{M+d}\).
The row alternation cancels; the conditional polynomial and its
remaining phase do not. Positivity of \(\beta\) is not positivity
of this sum.

For an explicit expansion in the other finite order, the original
physical reflection in
[the exact Newton note, (9)](research_mixed_next_middle_exact_newton_coefficients.md)
gives
\[
 C_{M+d,N}(Z)=\sum_{\ell=0}^{U-d}
   i^\ell q^{-(U-d)\ell+\ell(\ell-1)/2}
       \frac{S_{U-d}}{S_{U-d-\ell}S_\ell^2}(rZ;r)_\ell.
\tag{15}
\]
Changing order inside this finite triangle yields
\[
\boxed{\begin{split}
 f_{k,N}(Z)={}&(-1)^{M+k}
 \sum_{\ell=0}^{U-k}
     i^\ell q^{M-U\ell+\ell(\ell-1)/2}
                 \frac{(rZ;r)_\ell}{S_\ell^2}\\
 &\qquad\cdot\sum_{d=k}^{U-\ell}
       q^{d(\ell+1)}\beta_{d,k,N}
                    \frac{S_{U-d}}{S_{U-d-\ell}} .
\end{split}}
\tag{16}
\]
Every limit is literal. There is no negative factorial or removed
forcing row. At \(d=U\) the terminating value remains \(C_{D,N}=1\).
The phases in both finite sums of (16) still require a coherent
estimate.

At the top frequency only that terminating row contributes:
\[
                  f_{U,N}=2(-q)^D S_M^2/N^2\qquad(U\ge1).
\tag{17}
\]
This agrees with the attached top coefficient after the exact
change from \(T_U(X/2)\) to \(T_U(-X/2)\). If \(U=0\), (1)
instead retains the single constant coefficient.

## 5. The complete uniform rate of the transition weights

Keep
\[
 J(v)=\int_0^v\log(2\sin\pi s)\,ds,\qquad
 J(0)=J(1/2)=J(1)=0,
\]
and, for \(0\le t\le x\le1/2\), define
\[
 \mathcal H(x,t)=J(2x)-J(x-t)-J(x+t)-2J(1/2+x).
\tag{18}
\]
There are absolute constants \(C,A>0\) such that, uniformly at
both parities and every \(0\le k\le d\le U\),
\[
 \boxed{\quad
 C^{-1}N^{-A}e^{N\mathcal H(d/N,k/N)}
   \le\beta_{d,k,N}
   \le CN^Ae^{N\mathcal H(d/N,k/N)}.
 \quad}
\tag{19}
\]

The uniform endpoint details are as follows. The exact sine products
satisfy
\[
               \log S_n=NJ(n/N)+O(\log N),
                              \qquad0\le n\le N-1,
\tag{20}
\]
with an absolute constant. Split the sum and integral at the midpoint,
where the logarithmic sine changes monotonicity. On each other mesh
interval the monotone integral comparison is bounded by endpoint
variation. The first and last cells use
\(2\sin\pi s\asymp s\) near zero and
\(2\sin\pi s\asymp1-s\) near one; their total error is
\(O(\log N)\). The zero product is exact. The same bounds give
\[
 N|J(v+\epsilon)-J(v)|\le C\log N
 \quad\text{if }|\epsilon|\le1/N,\quad v,v+\epsilon\in[0,1].
\tag{21}
\]
No differentiability of \(J\) at its endpoint singularities is used.

At even levels, substitution of (20) in (6) yields (18) directly.
At odd levels the sine-binomial arguments are
\((2d+1)/N,(d-k)/N,(d+k+1)/N\). The two denominator-ratio
arguments are \((M+d)/N\) and \(M/N\), with
\(M/N=1/2+1/(2N)\). Equations (20)--(21) remove these shifts
with total \(O(\log N)\) cost. The comparison factor in (13) and
\(\eta_k\in\{1,2\}\) also cost only \(O(\log N)\).
This proves (19) uniformly, including \(d=0,U\) and \(k=0,d\).

The rate has the exact identities
\[
\begin{gathered}
 \mathcal H(1/2,t)=0,\qquad
 \mathcal H(t,t)=-2J(1/2+t),\qquad \mathcal H(x,0)=0,\\
 \partial_x\mathcal H(x,t)
       =\log\frac{\sin^2(\pi x)}
          {\sin^2(\pi x)-\sin^2(\pi t)}>0
                         \qquad0<t<x<1/2 .
\end{gathered}
\tag{22}
\]
The derivative follows from sine addition and doubling.
The first identity uses \(J(1-v)=-J(v)\); the third follows by
differentiating \(J(2x)-2J(x)-2J(1/2+x)\) and using its value
at zero. Continuity supplies the displayed endpoint values. Hence
\[
 \mathcal H(x,t)\le0,\qquad
 \mathcal H(x,t)<0\quad(0<t\le x<1/2).
\tag{23}
\]
Strictness at \(x=t\) also follows from continuity and strict increase
on \((t,1/2)\).

## 6. A sharper actual coefficient ceiling

For actual complete \(343\) references of length at least five,
the adopted absolute anchor and terminal normalization give
\[
 |C_{b,N}(Z_*)|\le CN^A e^{N\mathcal E(b/N,Z_*)},
                                         \qquad M\le b\le D.
\tag{24}
\]
The same original action \(\mathcal E\) is continuous and strictly
decreasing on \([1/2,1]\), with terminal value zero. These are the
complete middle and tail results of
[the action-weighted source](research_mixed_next_outgoing_action_weighted_green_ellipse.md)
and [the sharper tail](research_mixed_next_outgoing_sharper_tail_and_ellipse.md).
Define
\[
 \mathcal D(t,Z_*)=
       \max_{t\le x\le1/2}
       \{\mathcal E(1/2+x,Z_*)+\mathcal H(x,t)\},
                                  \qquad0\le t\le1/2.
\tag{25}
\]
Then the exact actual coefficient satisfies
\[
 \boxed{\quad
 |f_{k,N}(Z_*)|\le CN^A e^{N\mathcal D(k/N,Z_*)},
                                   \qquad0\le k\le U.
 \quad}
\tag{26}
\]
Combine (19) and (24) termwise in (14). At odd levels
\((M+d)/N\ge1/2+d/N\), so decreasing action gives the stated
ceiling with no extrapolation beyond an endpoint. Summing at most
\(N\) terms costs only a fixed polynomial.

For every fixed \(0<t<1/2\),
\[
                   \mathcal D(t,Z_*)<
                             \mathcal E(1/2+t,Z_*).
\tag{27}
\]
At \(x=t\), (23) is strict. At each \(x>t\), the decrease of
\(\mathcal E\) is strict and \(\mathcal H\le0\). Compact attainment
of the maximum proves (27). On every fixed compact frequency
interval inside \((0,1/2)\), this saving is uniform over the actual
compact reference family by continuity. At the limiting frequencies,
\[
 \mathcal D(0,Z_*)=\mathcal E(1/2,Z_*),\qquad
 \mathcal D(1/2,Z_*)=0;
\tag{28}
\]
no uniform positive saving at those endpoints is asserted.

The full observation and original scalar are still exactly
\[
 \mathcal L_N(F)=\phi_N[R_N^3e_MQ_N^{\rm full}F],
 \qquad \frac1{\kappa_N^2N}\mathcal L_N(F_N^+).
\tag{29}
\]
Here \(Q_N^{\rm full}\) is the original full inner-three source;
its internal Hermite normals have not been shortened or removed.
For example the adopted whole-frequency bound gives the actual
individual-mode estimate
\[
 |f_{k,N}(Z_*)\mathcal L_N(T_k(-X/2))|
 \le CN^A e^{N\{\mathcal D(k/N,Z_*)+M_3
                  -\gamma_{3,3}(1/2-k/N)^2\}}.
\tag{30}
\]
No pointwise packet error is separated from the full inner source.
The new \(\mathcal D\) is a proved upper envelope, not an asymptotic
coefficient phase. Neither positive transition weights nor their
two-sided estimate remove the phases in (16). No adequate comparison
of all remaining modes with the reference action is claimed.

## Frozen source bindings

- Exact Newton contraction and reflected rows:
  d8b58688c4da4237ac9cc5073fb32e0601d1326aab52dc9d71cee2070618ed48.
- Absolute outgoing anchor:
  51c9e5f1a47be3d9f3e1fa756e390a98c07f84c33f1aa0ad5ee5b948771229ab.
- Original action normalization:
  5b46b329c54cf252fc9d52f91e546fda47eadcfb2a0b62b842881c1bd2d87ce4.
- Complete attached source and observation:
  e39abb76185b6969901b6ee4c95a4f947bdda5f74d8ff57062ed4b6591a0c029.
- Full outgoing action and tail:
  fab5571d039f9fa4e36c0b6ca981f4ebbd2e7384923249882cf22e58eccc8ba3.
- Full finite inner observation:
  24ed707af29a5a15e5f2302210ae492d8256c5b5548145dce31de19dbbd2c489.
