# A paid positive taper and the small right midpoint cap

Private finite-source deduction, 9 November 2026. The remaining
positive lower outer contour can be tapered to the real axis along
the curve that minimizes the original phase in height. The extra
endpoint term in the available inner-source envelope is strictly
paid on that curve. A genuine real-continuum source bound, followed
by the exact finite polynomial degree, pays a small two-sided
midpoint cap. The long upper vertical remains explicit.

No mathematical numerical evaluation, saved-value arithmetic, or
frozen-source edit is used.

## 1. Original current and conclusion

Use the exact observation and current of
[positive outer segments](research_mixed_next_outer_positive_segments.md):
\[
\begin{split}
 \mathcal I_{N,k}(\gamma)
 =\frac{\chi_N C_{N,3}N}{4\pi}
 \int_\gamma H_N(u)a_N(u)Q_N^{\rm sh}(u)
 e^{N(3iu^2/(4\pi)-i\delta u)}(1+e^{-2iku})\,du,\\
 H_N(u)=\frac1{1-\eta_Ne^{-iNu}},\quad
 \eta_N=(-1)^{N-1},\quad
 C_{N,3}=e^{3\pi i(N-1)^2/(4N)},\quad
 \delta=\frac12-\frac{k}{N}.
\end{split}
\tag{1}
\]
The exact parity factors are
\[
 a_N(u)=\begin{cases}
 \sin u,&N\text{ even},\\
 \sin u\sin(u/2)/\cos^2(\pi/(2N)),&N\text{ odd},
 \end{cases}
 \qquad
 \chi_N=\begin{cases}i,&N\text{ even},\\-1,&N\text{ odd}.
 \end{cases}
\tag{2}
\]
The source is the original full inner Hermite trace with only
its second kernel shortened to \(U=\lfloor N/2\rfloor-1\).
In particular
\[
 Q_N^{\rm sh}(u)=\widehat Q_N^{\rm sh}(-2\cos u),
                  \qquad\deg\widehat Q_N^{\rm sh}\le U.
\tag{3}
\]
All first normals and the odd simple node remain in this source.
Its use in (1) is the adopted exact physical-node reduction,
not an off-grid equality with the full outgoing kernel.

Fix \(0<\delta_1\le1/2\), and consider the original integer
frequencies with \(\delta_1\le\delta\le1/2\). Retain
\[
 u_\delta=\beta_\delta-iK_\delta,\qquad
 \Psi_\delta(u)=S(u)+\frac{3iu^2}{4\pi}-i\delta u,
 \qquad\Gamma(\delta)=\Re\Psi_\delta(u_\delta).
\tag{4}
\]
Put \(b=8/7\). On this compact charge interval,
\[
 \beta_+:=\max\beta_\delta<b,\qquad
 K_-:=\min K_\delta>0,\qquad K_+:=\max K_\delta<2/5.
\tag{5}
\]
Use the unchanged midpoint from the paired-contour theorem:
\[
 T_N=\frac{2\pi}{N}
 \left(\left\lceil\frac{3N}{4\pi}-\rho_N-\frac12\right\rceil
                   +\rho_N+\frac12\right),\qquad
 \rho_N=\begin{cases}1/2,&N\text{ even},\\0,&N\text{ odd}.
 \end{cases}
\tag{6}
\]
Thus \(3/2\le T_N<3/2+2\pi/N<\pi/2\) for large \(N\),
and \(\eta_Ne^{-iNT_N}=-1\).

**Theorem.** There is a fixed \(\epsilon>0\) such that, at
both parities, uniformly in these frequencies and all sufficiently
large \(N\),
\[
 \left|J_{N,k}^{+}
 +\mathcal I_{N,k}([T_N-iK_\delta,T_N+i/N])\right|
                \le C e^{N\{\Gamma(\delta)-\epsilon\}}.
\tag{7}
\]
Here \(J^+\) is the original horizontal current from
\(b-iK_\delta\) to \(T_N-iK_\delta\). Consequently the
exact decomposition in the cited positive-segment theorem becomes
\[
 \mathcal O_{N,k}
  =G_{N,k}+J_{N,k}^{-}
     +\mathcal I_{N,k}([T_N+i/N,T_N+iK_\delta])
     +O(e^{N\{\Gamma(\delta)-\epsilon'\}})
\tag{8}
\]
for some fixed \(\epsilon'>0\). The nonzero local Gaussian
\(G_{N,k}\), the entire negative bottom current \(J^-\),
and every original scalar are unchanged.

In particular (7) does not estimate the long upper vertical
in (8). Evenness sends its source to a negative lower angle;
the positive source theorem does not cover that angle.

## 2. A curve minimizing height

Write
\[
 f(u)=\operatorname{arsinh}\{c(u)\tan(u/2)\},\qquad
 c(u)=\cos(t_*(u)/2),\qquad S'=-f/\pi,
\]
and define \(V_\delta(x,h)=\Re\Psi_\delta(x-ih)\).
The adopted [two-sided descent theorem](research_mixed_next_charged_curve_two_sided_descent.md) gives on
\(0\le x\le4/3,\ 0\le h\le1/2\)
\[
 \Re f'>1/50,\qquad |f'|<3/2.
\tag{9}
\]
The exact derivatives are
\[
 \begin{split}
 V_h&=\frac{3x}{2\pi}-\delta-\frac{\Im f(x-ih)}\pi,\\
 V_{xx}&=-\frac{\Re f'}\pi<0,\qquad
 V_{hh}=\frac{\Re f'}\pi>0,\qquad
 V_{xh}=\frac{3/2-\Im f'}\pi>0.
 \end{split}
\tag{10}
\]
All strict inequalities have uniform positive margins on any
of the compact parameter sets used below.

At the selected point both first derivatives vanish. Hence,
for every \(b\le x\le4/3\),
\[
                         V_h(x,K_\delta)>0.
\tag{11}
\]
Indeed integrate \(V_{xh}>0\) from \(\beta_\delta<x\)
at the fixed height \(K_\delta\).
The original charged-curve guard,
[Section 2 of its full-interval proof](research_mixed_next_selected_charged_curve_full_interval.md),
is \(\Im f(u)<3/7\) on this positive rectangle.
Thus at \(x=4/3\), for every \(0\le h\le K_\delta\),
\[
 V_h(4/3,h)>
       \frac{11}{7\pi}-\frac12
       =\frac{22-7\pi}{14\pi}>0.
\tag{12}
\]
The final strict inequality uses \(\pi<22/7\).

For each \(x\in[b,4/3]\), let \(h_\delta(x)\) be the
unique minimizer of \(V_\delta(x,\cdot)\) on
\([0,K_\delta]\). Equations (10)--(11) give the explicit
description
\[
 h_\delta(x)=
 \begin{cases}
 0,&V_h(x,0)\ge0,\\
 \text{the unique root of }V_h(x,h)=0,&V_h(x,0)<0.
 \end{cases}
\tag{13}
\]
Where positive it is smooth and
\[
                     h_\delta'(x)=-V_{xh}/V_{hh}<0.
\tag{14}
\]
It is continuous up to its zero, uniformly Lipschitz on the
compact family, and thereafter stays zero. To see the last
point, \(V_h(x,0)\) increases strictly with \(x\).
By (12), its zero-height endpoint
\(x_\delta\) belongs to \([b,4/3)\); if it already
vanishes at \(b\), set \(x_\delta=b\).
Extend \(h_\delta(x)=0\) to \(x\in[4/3,\pi/2]\).

Put
\[
                         g=\frac{(b-\beta_+)^2}{100\pi}>0.
\tag{15}
\]
Horizontal descent gives \(V_\delta(b,K_\delta)\le\Gamma-g\).
The vertical drop at \(x=b\) from \(K_\delta\) to its
minimizing height does not increase this value. Moreover
\(V_x(b,h_\delta(b))\le V_x(b,K_\delta)<0\), by (10).
On a positive-height portion of the minimizing curve,
\[
 \frac d{dx}V_x(x,h_\delta(x))
                   =V_{xx}-\frac{V_{xh}^2}{V_{hh}}<0.
\tag{16}
\]
After the curve reaches zero, the real action \(s(x)=\Re S(x)\)
continues to decrease to \(\pi/2\). This last assertion follows
directly from the original cubic derivative: for real \(x>0\),
\(\Re c(x)>3/4\), so
\(\Re\operatorname{arsinh}(c(x)\tan(x/2))>0\).
Consequently
\[
 V_\delta(x,h_\delta(x))\le\Gamma(\delta)-g
                         \qquad(b\le x\le\pi/2).
\tag{17}
\]
This is the original calibrated phase, with no new logarithmic
charge or additive constant.

## 3. The endpoint sector is paid on this curve

The new [complete right-half-period source theorem](research_mixed_next_right_half_period_inner_envelope.md) gives
\[
 |Q_N^{\rm sh}(x-ih)|\le C_\tau
   e^{N\{\max(\Re S(x-ih),33/20)+\tau\}},
 \quad b\le x\le\pi/2,\quad0\le h\le2/5.
\tag{18}
\]
This includes every real angle in the displayed interval,
not merely the physical nodes. Its entire original inner
source and all four right-current pieces have already been
estimated before applying (18) here.

On a positive-height minimizing point, set
\[
 \nu=\Im f(x-ih)=3x/2-\pi\delta,\qquad
 D_0=\cos x+\cosh h.
\]
Since \(x\ge8/7\), \(\delta\le1/2\) and \(\pi<22/7\),
\[
                              \nu>1/7>0.
\tag{19}
\]
Write \(c=p+iq\), where the original cubic guards give
\(p>3/4\) and \(0<q<1/3\). For
\(w=c\tan((x-ih)/2)=X+iY\), the principal branch has
\(X>0\). Its positive return imaginary part in (19) implies
\(Y>0\), and
\[
 0<Y/X<q/p<4/9,\qquad
 Y=\frac{q\sin x-p\sinh h}{D_0}
           <\frac{\sin x/3-3h/4}{D_0}.
\tag{20}
\]
On the segment \(X+iv\), \(0\le v\le Y<X\),
\(\Re(1+(X+iv)^2)\ge1\). The same original principal
return therefore satisfies
\[
 \nu=\int_0^Y\Re\{1+(X+iv)^2\}^{-1/2}\,dv\le Y.
\tag{21}
\]
Equations (20)--(21), followed by completing a real square,
give
\[
 \begin{split}
 h\nu
 &<\frac43\nu(\sin x/3-D_0\nu)
 \le\frac{\sin^2x}{27D_0}
 \le\frac{1-\cos x}{27}<\frac{23}{810}.
 \end{split}
\tag{22}
\]
The last bound uses \(x\le4/3\) and the original
\(\cos(4/3)>7/30\). It is only needed while \(h>0\).

The endpoint contribution in (18), after the original
outer crossing and charge are attached, is consequently
\[
 \frac{33}{20}+h\left(\frac{3x}{2\pi}-\delta\right)
 =\frac{33}{20}+\frac{h\nu}{\pi}
 <\frac{33}{20}+\frac{23}{2430}
 <\frac{83}{50}.
\tag{23}
\]
Here \(\pi>3\) and \(2300<2430\). At a zero-height
point the same final bound holds directly.
The [exact physical-tail proof](research_mixed_next_outer_far_nodes_and_paired_contour.md) already gives
\[
 \Gamma(\delta)>M_3-34/275>461/275,\qquad
                    \frac{461}{275}-\frac{83}{50}=\frac9{550}.
\tag{24}
\]
Thus the extra endpoint sector has a fixed gap; it is not
discarded because the geometric sector is smaller.

## 4. A finite path with the complete sampling denominator

For large \(N\), let
\[
             \widehat h_{N,\delta}(x)=\max\{h_\delta(x),1/N\}.
\tag{25}
\]
Use the following path \(\gamma_{N,\delta}\) entirely below
the real axis:
first drop from \(b-iK_\delta\) to
\(b-i\widehat h_{N,\delta}(b)\), and then follow
\(x-i\widehat h_{N,\delta}(x)\) from \(b\) to \(T_N\).
For \(N>K_-^{-1}\) its initial height does not exceed
\(K_\delta\). Its endpoint is \(T_N-i/N\), since
\(T_N>4/3\). Monotonicity of the height gives uniformly
bounded path lengths, including the possible joining point
where (25) becomes constant.

On the initial vertical the full positive-rectangle packet
supplies the finite upper bound at rate \(\Re S\), without
an additional endpoint ceiling. That phase stays at most
\(\Gamma-g\), because the drop stops no lower than its
minimizer. On the graph, (17) remains valid with a uniform
error \(O(1/N)\) after applying (25): all relevant original
phase derivatives are bounded on the fixed compact rectangle.
When its height was raised from zero to \(1/N\), the same
bounded-derivative statement applies. For the other sector,
if (25) changes the height then
\[
 \frac{33}{20}+\frac1N
                 \left(\frac{3x}{2\pi}-\delta\right)
 \le\frac{33}{20}+\frac{3}{4N}<\frac{83}{50}
\tag{26}
\]
for sufficiently large \(N\). Otherwise (23) applies.

Let \(g_* =\min\{g,9/550\}>0\). Equations (17)--(26)
and (18), with \(\tau<g_*/8\), bound the whole finite source
on this path at rate at most \(\Gamma-7g_*/8+O(1/N)\).
The bounded \(O(1)\) cost in the exponent and fixed polynomial
factors can be absorbed while retaining gap \(g_*/2\).
Crucially every point has \(Nh\ge1\), so
\[
 |H_N(x-ih)|\le(1-e^{-1})^{-1},\qquad
                         |1+e^{-2ik(x-ih)}|\le2.
\tag{27}
\]
The parity amplitude is uniformly bounded. The original
factor \(N/(4\pi)\) changes only the polynomial cost.
Thus
\[
                  |\mathcal I_{N,k}(\gamma_{N,\delta})|
                       \le C e^{N\{\Gamma(\delta)-g_*/2\}}.
\tag{28}
\]
This estimate keeps the full rational multiplier; no alias
expansion is truncated as the path approaches the real line.

## 5. The two-sided midpoint cap from a real continuum bound

Use the fixed real interval
\[
             a_- =17/12,\qquad a_+=(3+\pi)/4,\qquad
             I=[-2\cos a_-,-2\cos a_+].
\tag{29}
\]
It satisfies
\(4/3<a_-<3/2<a_+<\pi/2\). For every real
\(x\in[a_-,a_+]\), (17) and the complete continuum
source (18) imply
\[
 |Q_N^{\rm sh}(x)|
       \le C_\tau e^{N\{\Gamma(\delta)-g_*+\tau\}}.
\tag{30}
\]
For the ceiling \(33/20\), use (24) and \(33/20<83/50\).
This is a bound on an entire real interval, and hence on
\(\widehat Q_N^{\rm sh}\) throughout \(I\).

Take a filled Chebyshev ellipse of fixed height
\(\mu=g_*/8\) over \(I\). The ordinary degree in (3)
and the elementary Chebyshev coefficient formula give
\[
 |\widehat Q_N^{\rm sh}(X)|
     \le(2U+1)e^{U\mu}
                      \|\widehat Q_N^{\rm sh}\|_I
\tag{31}
\]
inside that ellipse. Indeed each nonconstant coefficient has
modulus at most twice the real norm, and its order-\(j\)
Chebyshev polynomial has modulus at most \(e^{j\mu}\)
there. This applies to arbitrary complex polynomial coefficients.

The point \(-2\cos(3/2)\) is strictly inside \(I\), and
therefore inside this filled ellipse. Since \(T_N\to3/2\),
for every sufficiently large \(N\), the entire spectral
image of
\[
                         [T_N-i/N,T_N+i/N]
\tag{32}
\]
lies inside the same ellipse. Choose \(\tau=g_*/8\)
in (30). Because \(U<N/2\), (31) loses at most \(Ng_*/16\).
After polynomial absorption, the source on (32) is bounded
by \(C e^{N(\Gamma-g_*/2)}\), with a further fixed margin
available if needed in the cap integral.

On its exact midpoint line the full denominator is
\[
                     H_N(T_N+iy)=\frac1{1+e^{Ny}},
                              \qquad |H_N|\le1.
\tag{33}
\]
For \(|y|\le1/N\), the reflected factor has modulus at
most \(1+e\), since \(2k\le N\). The crossing and character
have only bounded modulus costs, as do the parity amplitude
and the unit scalar. The cap length \(2/N\) is compatible
with the original prefactor \(N/(4\pi)\). The spare margin
in (31) therefore also gives
\[
 \left|\mathcal I_{N,k}([T_N-i/N,T_N+i/N])\right|
                  \le C e^{N\{\Gamma(\delta)-g_*/2\}}.
\tag{34}
\]
This continuation uses (30), not an inference from a short
list of nodes or pointwise physical relative errors.

## 6. Exact deformation and the remaining upper current

The integrand of (1) is holomorphic in the open lower
half-plane. Its only possible sampling poles are real.
The original positive horizontal followed by its right
vertical up to \(T_N-i/N\) has the same endpoints as
\(\gamma_{N,\delta}\). Cauchy's theorem there gives the
exact identity
\[
 J^+_{N,k}
 +\mathcal I_{N,k}([T_N-iK_\delta,T_N+i/N])
 =\mathcal I_{N,k}(\gamma_{N,\delta})
    +\mathcal I_{N,k}([T_N-i/N,T_N+i/N]).
\tag{35}
\]
Only the common small cap crosses the real axis, at an exact
midpoint; it contains no pole. Equations (28),(34) prove (7).
Splitting the original full upward vertical at \(T_N+i/N\)
and using the adopted positive-segment error proves (8).

The original excluded physical-node sum is unchanged, since
\(T_N\) has not moved. Both reflected charges, including the
factor two when \(k=0\), remain in every current. The present
result is uniform for a fixed \(\delta_1>0\), not at the
even zero-response endpoint \(\delta=0\).

The long upper current in (8) must still be handled with its
actual finite source. Its parity reflection is a negative lower
source, not an instance of (18). Neither (7) nor the local
Gaussian alone proves a nonzero asymptotic for the whole
observation, and no attachment to the geometric reference
rate or finite-exceptions conclusion is asserted.

## Frozen source bindings

- Exact positive-current decomposition and all original factors:
  5c0f9ac61c50f13561b6d2ee53370876613198162566d41b49a92d861a0800a3.
- Complete positive-rectangle packet:
  a1520474da2d389cb9cf67e92618f6ca9c552d499f35a039e842f9fc4e5075eb.
- Complete right-half-period continuum envelope:
  5994df2b37ebc8bd016300d5285701827add2d8c25cf170629dca00b3181798a.
- Original phase derivatives on both angular halves:
  102daa403519833ca13414ca2e0e20f351c572a5740ab9ca6ffb1c204d2eda7f.
- Original selected curve, cubic return and imaginary guard:
  6828459338fff642bf52b425120ed806d39bd9847d8df5ea5db8a14f0859da0c.
- Exact midpoint, parity fold and full action-loss bound:
  4ef9ae846444c092aee5a85a36db81f8646307f3bb8d2591ccb678bed6c2bea7.
- Original local Gaussian and unestimated-current inventory:
  6f2b155eee54cfd8a930d9af146ab96c3de277aac70d2de51b5f8318523f45ab.
