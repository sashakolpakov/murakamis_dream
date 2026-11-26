# The complete equal-endpoint Fourier packet of the adjacent pair

Research deduction, 7 November 2026. The original finite adjacent
power-two source has a nonzero asymptotic at its original equal
Fourier endpoints. First discard only original physical rows whose
absolute contributions have a proved gap. The remaining exact
central sources have two parity lattices. Their complete outer
contours, including both infinite aliases and both entire side
currents, leave one common Gaussian. The two parity contributions
add with the same coefficient.

This is an asymptotic for \(h(x_0)^TA_2^2h(x_0)\). It is not a
lower bound for an arbitrary prescribed knot closing, and no
ordinary normal adapter is replaced by an interpolation derivative.
No numerical evaluation is used.

## 1. An exact physical reduction with its absolute errors

Retain the original conventions of
[the merged-source theorem](research_mixed_two_adjacent_merged_source.md):
\[
\begin{gathered}
 D=N-1,\qquad r=e^{-2\pi i/N},\qquad
 P_j=(r;r)_j,\quad p_j(X)=(rX;r)_j,\\
 x_0=\xi+i\upsilon,\quad X=e^{-2\pi ix_0},\\
 V_N:=h(x_0)^TA_2^2h(x_0)
   =e^{2\pi iDx_0}\sum_{m=0}^{D}\sum_{j=0}^m T_{N,m,j},\\
 T_{N,m,j}=
 \frac{r^{-j(m-j)}P_m p_j(X)p_{m-j}(X)}
                         {P_j^2P_{m-j}^2}.
\end{gathered}
\tag{1}
\]
There is no additional outside \(N\) or \(\kappa\).
Let \(\phi(c)=F(c/2,c/2;x_0,x_0)\) be the original reduced
phase, \(c_*=2a_*\) its original critical point, and put
\[
 H_*=\Im c_*>0,\qquad
 \mathcal S=\phi(c_*)+2\pi ix_0,\qquad M=\Re\mathcal S.
\tag{2}
\]
The absolute constant and zero logarithmic lift are those of
[the critical-corridor theorem](research_mixed_two_adjacent_critical_corridor.md)
and [the total-phase theorem](research_mixed_two_adjacent_total_phase.md).

For \(\sigma=0,1/2\), use the exact central finite source
\[
\begin{split}
 \mathcal H_{\sigma,N}(c)
   &=\sum_{\substack{d\in\mathbb Z+\sigma\\|d|\le N/5}}
          T_N(c/2+d/N;c,x_0),\\
 T_N(a;c,x_0)
   &=e^{2\pi iNa(c-a)}\Pi_N(c)
       \Pi_N(a+x_0)\Pi_N(c-a+x_0)
       E_N(a)^2E_N(c-a)^2E_N(x_0)^2.
\end{split}
\tag{3}
\]
All arguments are in original regular strips when
\(1/2\le\Re c<1\), at every finite height.
At a physical \(c=m/N\), the correct parity is
\(\sigma(m)\equiv m/2\pmod1\); then (3) is exactly the
original subset \(|j-m/2|\le N/5\).

[The global central-truncation theorem](research_mixed_two_adjacent_global_central_truncation.md),
equation (21), proves
\[
 V_N=e^{2\pi iDx_0}
       \sum_{N/2<m<N}\mathcal H_{\sigma(m),N}(m/N)
       +O\!\left(N^b e^{N(M-1/500)}\right).
\tag{4}
\]
This includes all physical totals at most \(1/2\) and every
discarded inner row above \(1/2\). It is an absolute estimate
on original terms, before any outer cancellation.

Choose a fixed number \(R\in(9/10,1)\) inside the paid
physical diagonal collar of
[the diagonal-strip theorem](research_mixed_two_adjacent_physical_diagonal_strip.md).
It can be chosen so that all original physical terms with
\(m/N>R\) have total absolute size at most
\(C N^b e^{N(M-1/2500)}\). The same bound applies to their
central subset in (3). The continuous physical rate at
the central point of total \(R\) also gives
\[
                  \Re\phi(R)-2\pi\upsilon<M-1/2500.
\tag{5}
\]
Let \(M_N=\lfloor NR\rfloor\), \(L_N=\lfloor N/2\rfloor+1\).
Then (4) reduces the exact source to
\[
 V_N=e^{2\pi iDx_0}
       \sum_{\sigma=0,1/2}
       \ \sum_{\substack{L_N\le m\le M_N\\
                          m/2\equiv\sigma\ ({\rm mod}\ 1)}}
                      \mathcal H_{\sigma,N}(m/N)
       +O\!\left(N^b e^{N(M-\delta_{\rm phys})}\right)
\tag{6}
\]
for a fixed \(\delta_{\rm phys}>0\).
Every complementary total has now been accounted for by an
original absolute source bound.

The all-height theorem
[for (3)](research_mixed_two_adjacent_all_height_central_packet.md)
gives, uniformly on each relevant fixed compact complex set,
\[
 \mathcal H_{\sigma,N}(c)
       =N^{-1}\mathcal A(c)e^{N\phi(c)}
                           (1+\varepsilon_{\sigma,N}(c)),
 \qquad \varepsilon_{\sigma,N}=O(N^{-1}).
\tag{7}
\]
The coefficient is nonzero, is the same for both parities,
and the normalized errors have all fixed derivatives of
order \(O(N^{-1})\). This is a theorem for the exact finite
sources on those complex sets, not continuation of an
error estimated only at real samples.

## 2. Convexity on every outer vertical line

The original reduced derivative identity is
\[
 \phi''(c)=\pi\left\{-\csc(\pi c)
             +\frac12\cot\pi(c/2+x_0)+\frac i2\right\}.
\tag{8}
\]

**Lemma 1.** For \(1/2\le u<1\), at every real \(t\),
\[
                         \Re\phi''(u+it)<0.
\tag{9}
\]
Consequently \(f_u(t)=\Re\phi(u+it)\) is strictly convex,
and
\[
 \lim_{t\to-\infty}f_u'(t)=-\pi u,\qquad
 \lim_{t\to+\infty}f_u'(t)=2\pi\xi.
\tag{10}
\]

*Proof.* If \(u\ge1-2\xi\), the cotangent real part in (8)
is nonpositive, while the real cosecant is positive.
This is already the right-side comparison in the
total-phase theorem.

For \(1/2\le u\le1-2\xi\), put \(C=\cosh(\pi t)\) and
\(S=e^{2\pi\upsilon}<33/20\). The original bounds give
\(\sin(2\pi\xi)>91/100\). Hence
\[
 \Re\csc\pi(u+it)
   =\frac{\sin(\pi u)C}{C^2-\cos^2(\pi u)}
        \ge\frac{\sin(\pi u)}C>\frac{91}{100C}.
\tag{11}
\]
The shifted cotangent has nonnegative numerator and
nonpositive cosine in its denominator. Also
\(\cosh(\pi t+2\pi\upsilon)\ge C/S\). Therefore
\[
 \frac12\Re\cot\pi((u+it)/2+x_0)
       \le\frac{S}{2C}<\frac{33}{40C}.
\tag{12}
\]
Equations (11)--(12) prove (9) in the remaining interval.
The equality case at the threshold causes no problem.

For (10), use the original disk primitives, with their
constants. At negative height every moving \(g\) has a
constant limit up to exponentially decaying derivatives;
the remaining term \(\pi ic^2/2\) gives slope \(-\pi u\).
At positive height the quadratic parts cancel and the
only \(c\)-dependent limiting term is \(-2\pi ix_0c\),
giving slope \(2\pi\xi\). These same limits follow from
the exact logarithmic derivative of the phase. \(\square\)

Since a convex function has increasing derivative, (9)--(10)
imply, for every \(t\),
\[
       f_u'(t)+\pi>\pi(1-u)>0,\qquad
       f_u'(t)-\pi<2\pi\xi-\pi<0.
\tag{13}
\]
In particular define
\[
 p_{H_*}(t)=
 \begin{cases}
    \pi(-t)_+,&t<H_*,\\
    \pi t_+,&t\ge H_*.
 \end{cases}
\tag{14}
\]
The negative weighted part increases up to \(t=0\);
the positive weighted part decreases after \(H_*\);
and convexity bounds the unpenalized segment between
those heights by its endpoints. Thus
\[
 f_u(t)-p_{H_*}(t)
          \le\max\{f_u(0),f_u(H_*)\}
                         \qquad(t\in\mathbb R).
\tag{15}
\]
This is the full outer side-profile comparison, including
the interval with no small sampling weight.

## 3. Exact parity contours and fixed-level aliases

Choose the common full-grid midpoint cuts
\[
 \ell_N=\frac{\lfloor N/2\rfloor+1/2}{N},\qquad
 u_N=\frac{M_N+1/2}{N}.
\tag{16}
\]
They lie strictly between consecutive physical total indices.
For each parity put
\[
 k_{\sigma,N}(c)
   =\frac1{1-\zeta_\sigma e^{-\pi iNc}},
       \qquad \zeta_\sigma=e^{2\pi i\sigma}\in\{1,-1\}.
\tag{17}
\]
Its physical poles are exactly the totals of that parity,
with residue \(1/(\pi iN)\). Accordingly the residue density
is \(N/2\), not \(N\). The central source (3) is holomorphic
on the entire finite rectangle between (16), at all heights.

At either cut \(q_N=\ell_N\) or \(u_N\), the number
\(\zeta_\sigma e^{-\pi iNq_N}\) is \(i\) or \(-i\).
It follows that
\[
\begin{split}
 |k_{\sigma,N}(q_N+it)|
       &=\frac1{\sqrt{1+e^{2\pi Nt}}},\\
 |k_{\sigma,N}(q_N+it)-1|
       &=\frac{e^{\pi Nt}}{\sqrt{1+e^{2\pi Nt}}}.
\end{split}
\tag{18}
\]
Both level parities and both total parities are included
in these exact formulas.

The horizontal aliases can be removed at fixed level.
Here their tails must be checked on the actual central
source, rather than on a formal phase continuation.
Let \(\gamma_N=N/12-1/4+1/(12N)\), the constant of the
original exact factorial. For \(c=u+iT\), at fixed \(N\),
the marked upper factorial formula gives
\[
 T_N(c/2+d/N;c,x_0)
   =C_N^+(x_0)e^{-2\pi iNx_0c}(1+o(1)),
                       \qquad T\to+\infty,
\tag{19}
\]
where
\[
 C_N^+(x_0)=N^{-1/2}e^{i\pi\gamma_N}E_N(x_0)^2
       e^{\,\pi iN(2x_0-2x_0^2)-2\pi ix_0}.
\tag{20}
\]
This coefficient is independent of \(d,c\).
In fact the entire polynomial in the moving upper
factorials and chirp is exactly
\[
                   \pi iN(2x_0-2cx_0-2x_0^2)-2\pi ix_0.
\tag{21}
\]
Thus no finite-level term proportional to \(T\) is omitted.

For \(c=u-iT\), the lower exact formula instead gives
\[
\begin{split}
 T_N(c/2+d/N;c,x_0)
 &=C_N^-(x_0)
      e^{\,\pi iNc^2/2-2\pi id^2/N}(1+o(1)),\\
 C_N^-(x_0)&=N^{-1/2}e^{-i\pi\gamma_N}E_N(x_0)^2 .
\end{split}
\tag{22}
\]
Equations (19)--(22) follow directly from
[the exact upper and lower factorial tails](research_mixed_fourier_factorial_alias_elimination.md),
equations (2)--(7). Every moving argument here has real
part in a fixed regular strip. In particular the lower
deformation meets no negative-grid numerator pole.

The upper alias \(k_{\sigma,N}\) costs \(e^{-\pi NT}\)
and the lower alias \(k_{\sigma,N}-1\) costs the same
factor. On the full interval (16), their strict decay
slopes are respectively
\[
              \pi N(1-2\xi),\qquad \pi N(1-u).
\tag{23}
\]
For sufficiently large \(N\), \(u_N\le(1+R)/2<1\).
Thus both slopes have a fixed positive lower multiple
of \(N\). There are finitely many \(d\)'s at each level,
so both complete horizontal aliases tend to zero.

Define the cut-dependent weight
\[
 w_{\sigma,q_N}(t)
     =k_{\sigma,N}(q_N+it)
                   -\boldsymbol1_{\{t<H_*\}} .
\tag{24}
\]
The exact positive residue contour, followed by removal
of both horizontal aliases and retention of the two
joining sides, now gives
\[
\begin{split}
 \sum_{\substack{L_N\le m\le M_N\\m/2\equiv\sigma\ ({\rm mod}\ 1)}}
       \mathcal H_{\sigma,N}(m/N)
 ={}&\frac N2\int_{\ell_N+iH_*}^{u_N+iH_*}
                              \mathcal H_{\sigma,N}(c)\,dc\\
 &+\frac{iN}{2}\int_{\mathbb R}
   \bigl\{w_{\sigma,u_N}(t)\mathcal H_{\sigma,N}(u_N+it)
       -w_{\sigma,\ell_N}(t)\mathcal H_{\sigma,N}(\ell_N+it)
   \bigr\}\,dt .
\end{split}
\tag{25}
\]
The right side is upward and the left side downward.
The positive horizontal density is \(N/2\) for both
parities. All four original contour sides are accounted
for in this identity.

## 4. Uniform control of the entire outer currents

The passage to infinite heights in (25) was at fixed
level. Uniform estimates on its remote tails follow
separately from the same exact formulas.

There are seven moving factorial copies in a row:
three numerator copies and four own reciprocal copies.
For \(|\Im c|=T\) large, their heights have magnitude
at least \(T/2-\upsilon\). The exact disk remainder
bound therefore gives combined logarithmic error at most
\[
             C N(1+T)e^{-\pi T+2\pi\upsilon}.
\tag{26}
\]
All real arguments and all \(d/N\in[-1/5,1/5]\) are
uniformly bounded in regular strips. The fixed
\(E_N(x_0)^2\) has its original compact packet.
The row power is \(N^{-3/2}\); counting \(O(N)\) rows
and multiplying by the outer density gives at most
a fixed multiple of \(N^{1/2}\).

Using (18), (23), and then increasing a fixed height
cut \(T_0\), one obtains constants \(C_0,C,\lambda>0\),
independent of \(N\), for which the absolute density
of either side of (25) is at most
\[
                 C N^{1/2}e^{N(C_0-\lambda T/2)}
                            \qquad(T\ge T_0).
\tag{27}
\]
Here one can take \(\lambda\) to be any fixed lower
bound for the two coefficients in (23) after division
by \(N\). Formula (26) is absorbed into half that
strict slope. This proves a uniform tail bound without
extrapolating a compact-height packet to infinity.

On the bounded part of each side, (7) and (18) give
\[
 \frac N2
 |w_{\sigma,q_N}(t)\mathcal H_{\sigma,N}(q_N+it)|
       \le C e^{N\{f_{q_N}(t)-p_{H_*}(t)\}}.
\tag{28}
\]
The coefficient and normalized errors in (7) are bounded
on this fixed compact set. Lemma 1 applies to the actual
moving cut, since \(\ell_N\geq1/2\) and \(u_N<1\).

Both endpoint values on the right of (15) are paid.
At the limiting left real cut, the earlier truncation
budget proves
\[
                  \Re\phi(1/2)-2\pi\upsilon<M-3/1000.
\tag{29}
\]
The right real cut is paid by (5).
At height \(H_*\), the total-phase theorem has its
unique maximum at \(c_*\) on the entire interval
\([0,1]+iH_*\). Since
\[
            1/2<\Re c_*<4/5<R,
\]
both limiting top endpoints have a strict phase gap.
Continuity absorbs the \(O(1/N)\) shifts in (16).
It follows that, for some fixed \(\delta>0\) and all
sufficiently large \(N\),
\[
 \max\{f_{q_N}(0),f_{q_N}(H_*)\}
                  \le\Re\phi(c_*)-4\delta
                  \qquad(q_N=\ell_N,u_N).
\tag{30}
\]

Apply (15), (28), and (30) on a fixed bounded interval.
Then choose \(T_0\) still larger in (27), so its entire
tails have a strict gap as well. After restoring the
original outside chirp, the two side currents of each
parity satisfy
\[
 \left| e^{2\pi iDx_0}\,\frac{iN}{2}
       \int_{\mathbb R}
       \{w_{\sigma,u_N}\mathcal H_{\sigma,N}
           -w_{\sigma,\ell_N}\mathcal H_{\sigma,N}\}\,dt
 \right|
         \le C N^b e^{N(M-\delta)} .
\tag{31}
\]
In fact the same estimate holds for the sum of their
absolute integrals. The unpenalized segments from
height zero to \(H_*\) are included by convexity in
(15); no side is replaced by its value on the main line.

## 5. The two parity Gaussians and the complete source

On the principal horizontal interval in (25), the
total-phase theorem gives a unique nondegenerate
maximum at \(c_*\). The two limiting real cuts are
strictly on opposite sides of it. Equation (7) holds
uniformly on a complex neighborhood of the whole
principal segment, for both parities.

Ordinary one-dimensional stationary phase, with the
original orientation and square root, therefore gives
\[
\begin{split}
 \frac N2\int_{\ell_N+iH_*}^{u_N+iH_*}
                \mathcal H_{\sigma,N}(c)\,dc
   =N^{-1/2}\frac{\sqrt{2\pi}\,\mathcal A(c_*)}
                         {2\sqrt{-\phi''(c_*)}}\,
                   e^{N\phi(c_*)}(1+O(N^{-1})).
\end{split}
\tag{32}
\]
The normalized error in (7) contributes relative
\(O(N^{-1})\) on this contour: its absolute integral
is bounded by that factor times the Gaussian absolute
integral. Thus it is not propagated through unknown
real-axis cancellation. The usual odd first local terms
integrate to zero; the quartic and symbol errors give
the same relative order. The remaining main complement
has a fixed phase gap.

There is no parity phase in the leading term (32).
Both residue densities are \(N/2\), both principal
orientations are left to right, and the two exact inner
sources have the same \(\mathcal A\). Consequently
their leading terms add.

**Theorem 2.** Along every integer level,
\[
 \boxed{\quad
 h(x_0)^TA_2^2h(x_0)
       =N^{-1/2}\mathcal C_{22}\,
                       e^{N\mathcal S}(1+O(N^{-1})),
       \qquad \mathcal C_{22}\ne0,
 \quad}
\tag{33}
\]
where \(\mathcal S\) is the unchanged original action in
(2), and
\[
 \mathcal C_{22}
   =\frac{\sqrt{2\pi}\,e^{-2\pi ix_0}\mathcal A(c_*)}
                         {\sqrt{-\phi''(c_*)}}
   =\frac{2\pi e^{-2\pi ix_0}b(a_*,a_*;x_0,x_0)}
                 {\sqrt{\det[-F''(a_*,a_*;x_0,x_0)]}} .
\tag{34}
\]
The final square root is the original accretive Gaussian
branch.

*Proof.* Sum (32) over both parities, apply (31), and
restore the errors in (6). Every error outside the
principal Gaussian has a fixed exponential gap at
the same original rate \(M\). The exact outside chirp
is \(e^{2\pi iNx_0}e^{-2\pi ix_0}\), which gives
precisely (33)--(34).

For the last equality in (34), the total-coordinate
normalization is
\[
 \mathcal K(c_*)=2\lambda_-,\qquad
 \phi''(c_*)=\lambda_+/2,\qquad
 \mathcal K(c_*)\phi''(c_*)=\det F''(a_*,a_*).
\tag{35}
\]
Both negative eigenvalue combinations have positive
real part. Their product of Gaussian square roots
is therefore the same branch as the joint Gaussian.
The original symbol is nonzero. Equations (7), (32)
also show the powers directly: \(N^{-1}\), then
density \(N/2\), then \(N^{-1/2}\), with the two halves
adding. This proves the nonzero coefficient and the
claimed all-level expansion. \(\square\)

The resulting two-sided exponential bound is for the
complete equal-endpoint boundary function in (1).
It does not replace an original normal vector or a
prescribed closing row by evaluation at \(x_0\).
No arbitrary signed short cluster, new knot family,
or cofinite filling statement is concluded here.
