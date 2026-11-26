# All revived upper rows on the transformed left taper

Research deduction, 7 November 2026. A three-factorial conditional
row has a simple endpoint-only upper-tail theorem on an asymmetric
incoming/outgoing domain. It includes the complete left taper of the
original ordinary three/four pair after fixing its nonphysical outgoing
private leg. The resulting finite bound keeps every revived row,
the first-argument chirp, and both parities. No new numerical
evaluation is used.

## 1. An independent-target row theorem

Let
\[
 a=x+ih_a,\qquad z=Z+ih_z,\qquad
 R_a=e^{2\pi h_a},\quad R_z=e^{2\pi h_z},
\]
and suppose
\[
 0\le x\le2/5,\qquad 1/3\le Z\le11/30,
 \qquad 4/5\le R_a\le1,\qquad 0<R_z\le1.
 \tag{1}
\]
Thus both heights are nonpositive, but no reference-root correlation
is required. Define the original own-four row rate
\[
 E_1(u;a,z)=I_a(u)+I_z(u)-3J(u)-2\pi h_a u,
 \quad I_b(u)=\int_0^u\log|1-e^{-2\pi i(b+s)}|\,ds,
 \quad J(u)=\int_0^u\log(2\sin\pi s)\,ds.
 \tag{2}
\]
All zero-height logarithmic singularities are interpreted by their
integrable limits.

**Theorem 1.** On the whole independent domain (1),
\[
 \max_{1/2\le u\le1}E_1(u;a,z)
     =\max\{E_1(1/2;a,z),E_1(1;a,z)\}.
 \tag{3}
\]
The last value is exactly \(E_1(1;a,z)=-2\pi h_a\).
Any original row-independent Fourier allocation may be added to both
sides of (3). The theorem does not compare different allocated types.

To prove it, put
\[
 f_R(s)=\log|1-Re^{-2\pi is}|,\qquad
 G_R(t)=\int_0^t f_R(s)\,ds,
 \qquad F(v)=E_1(1-v;a,z)-E_1(1;a,z).
\]
For \(0<R\le1\), the function \(f_R\) is even, periodic,
and increasing on \([0,1/2]\); its integral over a period is zero.
The primitive is odd and periodic, and
\[
                   G_R(t)\ge J(t),\qquad 0\le t\le1/2.
 \tag{4}
\]
These are the original radial facts in
[the row-reflection proof](research_mixed_right_tail_reflection.md),
equations (1)--(2). For example, differentiating its dilogarithm
primitive with respect to \(R\) gives
\(-\arg(1-Re^{-2\pi it})/(2\pi R)\le0\), so its minimum
is the unit-radius value \(J(t)\). The full-period mean-zero
identity also includes \(R=1\) by integrable continuity.

The exact reflection, retaining the chirp in (2), is
\[
 F(v)=-\int_{x-v}^{x}f_{R_a}(s)\,ds
       -\int_{Z-v}^{Z}f_{R_z}(s)\,ds
       +3J(v)+v\log R_a,
                  \qquad0\le v\le1/2.
 \tag{5}
\]
In particular the drift is not an independently chosen number.

## 2. The short reflected arcs are below the last row

An arc of length \(v\le1/2\) has its smallest integral of
\(f_R\) when centered at an integer. Even radial monotonicity and
(4) therefore give, at any incoming angle,
\[
       \int_{x-v}^{x}f_{R_a}(s)\,ds
                    \ge2G_{R_a}(v/2)\ge2J(v/2).
 \tag{6}
\]
For \(0\le v\le1/5\), the other interval lies in
\([0,1/2]\), because \(v\le Z\le11/30\). Its left
endpoint is nonnegative. Translating it to \([0,v]\) can only
lower its integral, so
\[
        \int_{Z-v}^{Z}f_{R_z}(s)\,ds
                         \ge G_{R_z}(v)\ge J(v).
 \tag{7}
\]
Combining (5)--(7), and using \(\sin\pi s\le\pi s\),
\[
\begin{split}
 F(v)&\le2[J(v)-J(v/2)]+v\log R_a\\
 &\le v\{\log(4\pi v)-1\}+v\log R_a<0,
                          \qquad 0<v\le1/5.
\end{split}                                                        \tag{8}
\]
Indeed \(4\pi/5<88/35<8/3<e\), by \(\pi<22/7\)
and the positive exponential series. Also \(\log R_a\le0\).
The value at \(v=0\) is zero. This part uses no incoming-angle
restriction at all.

## 3. The remaining reflected interval increases to the half row

For any \(0\le R\le1\), convexity of
\(1+R^2-2R\cos(2\pi s)\) as a function of \(R\) gives
\[
           |1-Re^{-2\pi is}|
                  \le\max\{1,2|\sin\pi s|\}.
 \tag{9}
\]
On \(1/5\le v\le1/2\), (1) implies
\[
 |x-v|\le v\le1/2,\qquad |Z-v|\le1/6,
                      \qquad 2\sin\pi v>1.
\]
Consequently
\[
 |1-R_a e^{-2\pi i(x-v)}|\le2\sin\pi v,
 \qquad |1-R_z e^{-2\pi i(Z-v)}|\le1.
 \tag{10}
\]
Away from the possible integrable zeros, differentiation of (5) gives
\[
\begin{split}
 F'(v)&=3\log(2\sin\pi v)
   -\log|1-R_a e^{-2\pi i(x-v)}|
   -\log|1-R_z e^{-2\pi i(Z-v)}|+\log R_a\\
 &\ge\log\{R_a(2\sin\pi v)^2\}>\log(16/15)>0.
\end{split}                                                        \tag{11}
\]
The strict rational witness is
\(4\sin^2(\pi/5)=(5-\sqrt5)/2>4/3\), since
\(\sqrt5<7/3\), together with \(R_a\ge4/5\).
If a denominator in (11) vanishes, its logarithmic contribution is
integrable; integrating the inequality on the complementary intervals
and taking limits proves the same strict monotonicity. No derivative
at the zero is asserted.

Equation (8) bounds the first part by \(F(0)=0\), and (11)
bounds the second part by \(F(1/2)\). This proves (3), including
all zero-height and endpoint limits.

## 4. Exact finite rows and the actual incoming taper

Use the literal restored upper sum
\[
 C^{\rm up}_{1,N}(X,Y)=
   \sum_{j=\lceil N/2\rceil}^{N-1}
          \frac{X^{-j}p_j(X)p_j(Y)}{P_j^3},
 \quad p_j(V)=(rV;r)_j,\quad P_j=(r;r)_j,
 \quad r=e^{-2\pi i/N}.
 \tag{12}
\]
At even levels the exact half row is present; at odd levels the
first row is just above it. Every \(j<N\) in the indicated
range is included regardless of whether \(Y\) is physical.
The normalization and chirp are unchanged.

On every fixed compact subset of (1), for any \(\tau>0\),
the zero-safe numerator-product estimate and the denominator
factorial estimate yield
\[
\begin{split}
 \sum_{j=\lceil N/2\rceil}^{N-1}
       \left|\frac{X^{-j}p_j(X)p_j(Y)}{P_j^3}\right|
 &\le C_\tau N^{B_\tau}
   e^{N\{\max(E_1(1/2;a,z),E_1(1;a,z))+\tau\}}\\
 &\le C_\tau N^{B_\tau}
  \left(e^{N(E_1(1/2;a,z)+\tau)}
                    +e^{N(E_1(1;a,z)+\tau)}\right).
\end{split}                                                        \tag{13}
\]
For clarity, the product bound at unit-radius zeros is an upper
estimate: replace \(\log|1-Re^{i\theta}|\) by
\(\log(|1-Re^{i\theta}|+\delta)\), take its uniformly
bounded Riemann-sum error for fixed \(\delta\), and then let
\(\delta\downarrow0\). The integral error is uniformly
\(O(\delta(1+|\log\delta|))\). The denominator sine products
retain their \(O(\log N)\) endpoint error, including \(j=N-1\).
This is the source estimate in Section 2 of
[the conditional contour allowance](research_mixed_conditional_contour_allowance.md).
Thus (13) does not divide a vanishing row and does not extrapolate
an interior asymptotic to the true last physical row.

Now specialize to the original pair's fixed outgoing private leg
\(z_*=Z+ih_z\) and actual incoming taper
\[
 a(x)=x+i h(x),\quad h(x)=c\frac{x-1/10}{3/25},
 \quad 1/10\le x\le11/50,\qquad -7/200<c<0,
 \quad .349<Z<.350,\quad -137/4000<h_z<-1/30.
 \tag{14}
\]
These are the same saved-reference consequences used in
[the calibrated transformed complement](research_mixed_three_four_transformed_complement_calibration.md).
All angles lie strictly inside the angular conditions of (1), and
\(0<R_z<1\). Also \(-2\pi h(x)<11/50\), and
\[
 e^{11/50}\le1+\frac{11}{50}
       +\frac{(11/50)^2}{2(1-11/150)}
       =\frac{17321}{13900}<\frac54.
 \tag{15}
\]
The exponential bound follows termwise from
\(n!\ge2\,3^{n-2}\), \(n\ge2\).
Hence \(R_a>4/5\) on the whole taper, including the unit radius
at \(x=1/10\). Theorem 1 and (13) therefore apply without
restricting the complex outgoing variable to a physical support wall.

## 5. The calibrated finite high-row gap

Let \(P_* =\Re\mathcal P_{34}(-2,z_*)>181/100\) be the
original pre-Gram action from the calibration. The two terms in (13)
are paid separately after multiplication by the whole first cap.

For the half row, use the pointwise source statements of
[the original left-taper completion](research_mixed_three_four_left_taper_source_completion.md),
Sections 2--4, not its summed terminal conclusion. Its Section 4
first bullet includes the real transform face \(t=.5\) at
every original private main point. The actual point \(e=z_*\)
belongs to that main segment. The fixed-cut transport in
[the original-transform-cut theorem](research_mixed_three_four_left_original_transform_cut.md),
Section 4, includes \(.49\le\Re t\le.5\) and height zero.
It transports every regular first-cap profile, and the separate
true-cap-end alternative, from its raw \(1/20000\) calibration
at incoming \(x=.22\) throughout (14).

On this fixed slice the exact retained terminal interpolant is
\[
 \widehat J_N(a;z_*,t,-2)=D_N(z_*)R_N(t;a,z_*),
 \quad D_N(z)=\Delta_N(z)^{-1}\mathcal C_N(z,-2),
 \quad \Phi(a;t,z_*)=E_{\rm end}(z_*)+Q(t;a,z_*).
 \tag{16}
\]
The endpoint packet makes \(D_N\) nonzero on a fixed neighborhood
for all sufficiently large levels. The exact quotient, its phase,
and its original mark are recorded in
[the transformed plateau source](research_mixed_three_four_transformed_plateau_source.md),
Section 2. At \(t=.5\), all shifted real arguments are regular,
so \(\Re Q=E_1(1/2;a,z_*)\). Subtracting only the constant
\(\Re E_{\rm end}(z_*)\) from the pointwise coupled profile
gives
\[
 \text{complete-cap upper rate at }a(x)
          +E_1(1/2;a(x),z_*)\le P_*-1/20000.
 \tag{17}
\]
The complete-cap upper rate here is the maximum of the original
five-profile envelope and its separately retained true ends. Each
profile satisfies the same bound before taking that maximum.
There is no division of an estimate for \(\mathcal V_{1,N}\),
and no use of its physical upper-triangle restriction.

The last branch uses instead the complete disk cap ceiling in
Section 5 of the plateau source. Since \(|X(x)|\le1\),
the positive sum of complete endpoint coefficients and the full
arc-product bound give, for arbitrary positive tolerances,
\[
 |U_{0,N}(w,X(x))|
   \le\operatorname{poly}(N)e^{N(433/500+1/3+\tau)}.
\]
Together with \(E_1(1)=-2\pi h(x)<11/50\), its rate is
\[
             433/500+1/3+11/50=2129/1500<3/2<P_*.
 \tag{18}
\]
This also keeps the cap's true private ends and its full Newton sums.

**Corollary 2.** There is a fixed neighborhood of \((-2,z_*)\)
such that, for every fixed \(k,\ell\),
\[
 \sup_{1/10\le x\le11/50}
 \left|\partial_w^k\partial_z^\ell
  \left[e^{-N\mathcal P_{34}(w,z)}
       U_{0,N}(w,e^{-2\pi ia(x)})
       C^{\rm up}_{1,N}(e^{-2\pi ia(x)},e^{-2\pi iz})\right]\right|
      \le C_{k,\ell}N^{B_{k,\ell}}e^{-N/80000}.
 \tag{19}
\]
Both parities and all restored rows are retained. The same estimate
holds after integration over the finite taper with its original
Jacobian and any original polynomial normalization.

To justify the neighborhood and derivatives, first choose all finite
product, cap, and profile tolerances smaller than a fixed fraction of
the raw margin in (17). The outgoing point is interior to (1), with
strictly negative height; thus the endpoint theorem persists on a
fixed complex \(z\)-disk. The pointwise terminal slice, endpoint
packet, and complete cap envelope also persist on compact source
neighborhoods. Shrink the \((w,z)\)-bidisk so the continuous action
\(\Re\mathcal P_{34}(w,z)\) differs from \(P_*\) by less
than the remaining allotted fraction. Equations (13), (17), and (18)
then prove a uniform normalized bound with margin larger than
\(1/80000\). Cauchy's formula on smaller bidisks gives (19).
No new incoming-height complex neighborhood is needed at the unit
radius endpoint; the incoming path stays fixed and the numerator
bound there is already zero-safe.

This corollary pays the high conditional rows only. The retained
transform currents and low physical rows on the left taper require
their own source comparisons. It neither asserts a whole transformed
prefix asymptotic by itself nor enlarges the actual reference family.
