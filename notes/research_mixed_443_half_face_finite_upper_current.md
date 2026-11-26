# A calibrated finite upper sampling current at the second half face

Private written proof, 11 November 2026. A fixed positive private
height controls the upper sampling current of the first conditional
factor at the real second midpoint. Its rate is compared directly
with the original negative-height main profile. The comparison
retains the cap and the third factor through their already proved
joint calibration.

The first coordinate in the calibrated consequence is restricted to
the core parts of its existing paths. This does not estimate the
early first pieces, the complete conditional sum on a new domain,
or the real second interval beyond its midpoint. No numerical
evaluation or modification of a frozen source is used.

## 1. Original phase and the finite-height comparison

Use the actual positive three/four words of length at least four
beginning with powers \(4,4,3\), and their original coupled reference
as in the adopted
[second half-face theorem](research_mixed_443_complete_second_half_face.md).
In particular
\[
 -39/500<c_1<-1/50,\qquad -51/500<h_2<-1/1000.
 \tag{1}
\]
The original ordinary third variable and its private variable obey
the ranges in that source; neither is changed here.

Write
\[
 a=x+ih,\qquad 11/50\le x\le1/2,\qquad c_1\le h\le1/100,
 \qquad y=1/2,
 \tag{2}
\]
and retain the original primitive and conditional phase
\[
\begin{split}
 g'(w)&=\operatorname{Log}(1-e^{-2\pi iw}),\qquad g(0)=0,\\
 Q(s;a)&=g(s+a)+g(s+1/2)-3g(s)-g(a)-g(1/2)+2\pi ias.
\end{split}
 \tag{3}
\]
All logarithms have their original strip marks. Set
\[
             h_U=\frac{\log2}{4\pi},\qquad
             e^{2\pi h_U}=\sqrt2.
 \tag{4}
\]
For any fixed \(1/5<r_0<1/2\), define
\[
 M(a)=\max_{1/8\le t\le r_0}\Re Q(t+ih_2;a).
 \tag{5}
\]

**Proposition 1.** Uniformly on (1)--(2),
\[
 \max_{1/8\le t\le r_0}
       \{\Re Q(t+ih_U;a)-2\pi h_U\}
                  <M(a)-\frac1{162}.
 \tag{6}
\]
The statement uses the actual fixed private height \(h_2\). It
does not replace it by a new critical height or by a real-row rate.

## 2. Where the upper-line maximum can occur

At height \(h_U\), put \(\rho=\sqrt2\) and
\(T=e^{-2\pi h}>15/16\). For the latter bound,
\(\log(16/15)>2/31>\pi/50\) suffices.
On \(1/8\le t\le1/5\), both shifted cosines obey
\[
 \cos 2\pi(x+t)<-3/10,\qquad
 \cos 2\pi(1/2+t)<-3/10,
 \qquad \cos2\pi t>3/10.
 \tag{7}
\]
Indeed \(x+t\in[69/200,7/10]\), and the larger shifted
cosine is at most \(-\cos(2\pi/5)<-3/10\).
The last radical comparison is
\(\cos(2\pi/5)=(\sqrt5-1)/4>3/10\).

Fold the first incoming chirp into its numerator. The two squared
numerators and the squared own denominator therefore satisfy
\[
\begin{split}
 |T-\rho e^{-2\pi i(x+t)}|^2
 &>\frac{225}{256}+2+\frac{63}{80}>\frac{18}{5},\\
 |1-\rho e^{-2\pi i(1/2+t)}|^2&>\frac{96}{25},\\
 |1-\rho e^{-2\pi it}|^2&<\frac{54}{25}.
\end{split}
 \tag{8}
\]
Here \(\sqrt2>7/5\); for the first inequality
\(225/256+63/80=2133/1280>8/5\).
Consequently the squared modulus of the original private force is
\[
 |e^{Q_s}|^2>
    \frac{(18/5)(96/25)}{(54/25)^3}>1,
 \tag{9}
\]
where the cleared comparison is \(216000>157464\).
Thus \(\partial_t\Re Q>0\) on this whole lower interval.
The penalty \(2\pi h_U\) is independent of \(t\), so its
upper-line maximum occurs with \(t\ge1/5\).

## 3. An elementary argument inequality

For \(0<k\le1/3\), define
\[
 F_k(v)=\arctan(k/v)+3\arctan(kv),\qquad v>0.
\]
Then
\[
                       F_k(v)\ge3\arctan k.
 \tag{10}
\]
Here is a proof which retains all arguments. Differentiating in
\(v\) shows that the unique interior minimum is at
\[
 v^2=\frac{1-3k^2}{3-k^2}.
\]
Its value tends to zero as \(k\downarrow0\). The derivative of
that minimum with respect to \(k\) equals
\[
 \frac{2\sqrt{(1-3k^2)(3-k^2)}}{1-k^4}
                   >\frac3{1+k^2}.
 \tag{11}
\]
After squaring, (11) is
\(3-22w+3w^2>0\), \(w=k^2\le1/9\); the left side decreases
there and its endpoint is \(16/27>0\). Integration proves (10).
The continuous case \(k=0\) is immediate.

We also need an upper bound at the positive height. If
\(0<k\le3-2\sqrt2<7/40\) and \(0<v\le7/5\), the
same derivative calculation shows that \(F_k\) has only an
interior minimum. Its endpoint values are bounded by
\[
 F_k(0+)=\pi/2,\qquad
 F_k(7/5)\le k(5/7+21/5)<43/50<\pi/2.
\]
Hence
\[
          F_k(v)\le\pi/2\quad(0<v\le7/5).
 \tag{12}
\]
The assertion at \(k=0\) follows directly and needs no endpoint
interchange. The bound \(3-2\sqrt2<7/40\) follows by squaring
\(113/80<\sqrt2\).

## 4. Comparison with the actual main height

Fix \(1/5\le t\le r_0\), and write
\[
 I(\sigma)=\Im Q_s(t+i\sigma;a).
\]
For every height, the original incoming argument is at least
\(\min\{0,\pi(1-2x-2t)\}\). At a nonpositive private height,
put \(k=\tanh(\pi|\sigma|)\). The own and half-shifted
arguments are exactly
\[
\begin{split}
 \Arg(1-e^{2\pi\sigma-2\pi it})
      &=\pi(1/2-t)-\arctan(k\cot\pi t),\\
 \Arg(1+e^{2\pi\sigma-2\pi it})
      &=-\pi t+\arctan(k\tan\pi t).
\end{split}
 \tag{13}
\]
Thus, for \(-51/500\le\sigma\le0\),
\[
 I(\sigma)\ge-\frac{33\pi}{50}
                   +3\arctan(\tanh(\pi|\sigma|)).
 \tag{14}
\]
To see the constant, if \(x+t\ge1/2\), the incoming lower
bound gives \(-\pi/2\) before the two arctangents. Otherwise
\(x+t\ge21/50\), giving
\(2\pi(x+t)-3\pi/2\ge-33\pi/50\).
Use (10) with \(v=\cot\pi t\). Its radius condition holds:
\(2\pi(51/500)<2/3<\log2\), so \(k<1/3\).

At \(0\le\sigma\le h_U\), the two arctangent signs in
(13) reverse, and \(k\le3-2\sqrt2<7/40\). We claim
\[
                           I(\sigma)>-\pi.
 \tag{15}
\]
If \(x+t\ge1/2\), the baseline is \(-\pi/2\), and
\(\cot\pi t\le\cot(\pi/5)<7/5\); apply (12).
For the cotangent inequality, its square is
\(1+2/\sqrt5<21/11<49/25\).
If \(x+t<1/2\), then \(t<7/25\), so
\[
 \tan\pi t<5/4,\qquad \cot\pi t<7/5.
\]
For the tangent bound, write
\(7\pi/25=\pi/4+3\pi/100\), use
\(\tan(3\pi/100)<1/10\), and obtain
\(\tan(7\pi/25)<11/9<5/4\).
The arctangent loss is therefore less than
\[
             (7/40)(5/4+21/5)=763/800<17\pi/50.
\]
Together with the baseline \(-33\pi/50\), this proves (15).
The tangent estimate follows from
\(\tan u\le u/(1-u^2/2)\) and \(u<33/350\).

Put \(d=-h_2\in[0,51/500]\). Since
\(\partial_\sigma\Re Q=-I\), (14)--(15) imply
\[
\begin{split}
 \Re Q(t+ih_U;a)-2\pi h_U-\Re Q(t+ih_2;a)
 \le{}&\frac{33\pi}{50}d
       -3\int_0^d\arctan(\tanh\pi v)\,dv-\pi h_U.
\end{split}
 \tag{16}
\]
The elementary inequalities
\(\tanh u\ge u-u^3/3\) and
\(\arctan w\ge w-w^3/3\), together with \(\tanh u\le u\),
give
\[
 \frac{33\pi}{50}d
       -3\int_0^d\arctan(\tanh\pi v)\,dv
 \le \frac{33\pi}{50}d-\frac{3\pi}{2}d^2+\frac{\pi^3}{2}d^4.
 \tag{17}
\]
The polynomial on the right increases on this interval. At its
right endpoint it is less than
\[
 \frac{13\pi}{250}+\frac{16}{6561}
 <\frac{143}{875}+\frac{16}{6561}<\frac16.
 \tag{18}
\]
Indeed its linear-minus-quadratic coefficient is
\(25857/500000<13/250\), and
\(\pi^3/2<16\), \(51/500<1/9\).
For the last comparison,
\(1/6-143/875=17/5250>16/6561\).
The derivative is positive already after dropping its cubic term,
since \(33/50-3d>0\).

Finally
\[
 \pi h_U=\frac14\log2>\frac{14}{81},\qquad
                      \frac{14}{81}-\frac16=\frac1{162},
 \tag{19}
\]
where \(\log2>2/3+2/81\) is the positive atanh series.
Equations (16)--(19), followed by the maximizing-index restriction
of Section 2, prove Proposition 1.

## 5. The original finite upper current and its calibration

Let \(G_N\) be the original normalized Gamma product and use the
negative-root marking from the joint global chart:
\[
 \Pi_N(w)=G_N(Nw)
       \exp\{(\pi i/2)[N(w-w^2)-w]\},\qquad
 E_N(w)=1/\Pi_N(w)\quad(0<\Re w<1).
\]
In particular its step recurrence is
\(\Pi_N(w+1/N)=(1-e^{-2\pi i(w+1/N)})\Pi_N(w)\).
Retain
\[
 T_N(s;a)=e^{2\pi iNas}\Pi_N(s+a)\Pi_N(s+1/2)
                       E_N(a)E_N(1/2)E_N(s)^3.
 \tag{20}
\]
At every physical private index this is precisely the original
row of \(C_{1,N}(X,-1)\), \(X=e^{-2\pi ia}\).
Choose the inward half-grid cuts
\(\ell_N\in[1/8,1/8+1/N]\),
\(r_N\in[r_0-1/N,r_0]\), and retain the exact upper horizontal
correction
\[
 \mathcal A_N(a)=\frac{N}{2i}
    \int_{r_N+ih_U}^{\ell_N+ih_U}
         T_N(s;a)\{\cot(\pi Ns)+i\}\,ds.
 \tag{21}
\]
The orientation and coefficient are those of the original split
cotangent contour. The regular factorial arguments in (20) remain
in fixed compact substrips. Its original uniform upper expansion,
and \(|\cot(\pi Ns)+i|\le4e^{-2\pi Nh_U}\), give, for every
prescribed \(\tau>0\),
\[
       |\mathcal A_N(a)|\le C_\tau N^{B_\tau}
                      e^{N\{M(a)-1/162+\tau\}}.
 \tag{22}
\]
The inward rounding leaves the entire horizontal inside the interval
of Proposition 1. Thus it changes no exponential comparison. The
fixed height and limiting cuts are chosen before \(N\), and both
level parities are included. Other finite rows and currents are not
deleted by defining (21); this note estimates this current only.

For the calibrated consequence restrict the first coordinate to
the following parts of its adopted original paths:
\[
\begin{array}{c|c}
 \nu=0 &[11/50,1/2]+ic_1\quad\text{and}\quad
                         1/2+i[c_1,0],\\
 \nu=1 &[11/50,1/2]+i/100\quad\text{and}\quad
                         1/2+i[0,1/100].
\end{array}
 \tag{23}
\]
Here \(\nu\) is the first Fourier choice. Keep the third coordinate
\(z\) on its actual old plateau and the unchanged affine action
\(\Lambda_{123}(z)\) from the half-face theorem. Sections 2 and 6
of that theorem compare each complete cap alternative, each original
first-weight alternative, the actual-height first main profile
\(M(a)\), and each complete third profile with
\(\Lambda_{123}(z)\), with a strictly positive reserve. We may
drop that reserve. The comparison is profilewise before the
finite sums are bounded; it is not inferred from the modulus
of a cancelling conditional sum.

Substituting (22) for that first main profile consequently proves,
on a sufficiently small fixed ordinary-color disk and both parities,
\[
\begin{split}
 &|U_{1,N}(w,X)d_N(X)X^{-\nu N}\mathcal A_N(a)
                     d_N(-1)(-1)^{-\sigma N}C_{0,N}(-1,Z)|\\
 &\hspace{25mm}\le C N^B
                  e^{N\{\Lambda_{123}(z)-1/324\}},
                 \qquad \sigma=0,1.
\end{split}
 \tag{24}
\]
All source allowances and the ordinary-color continuation allowance
are chosen to total less than \(1/324\). The diagonal polynomial
at the second half face has upper rate zero by the same source's
equation (24); both second monomials have unit modulus there.
The first weight and its selected monomial in (24) are unchanged.
There is no outgoing halfweight because the third block is three.
The complete third finite contour and physical groups are those
already paid at this same midpoint, not individual real middle rows.

Fixed ordinary derivatives follow on smaller disks with polynomial
cost. Integrating (24) over any of the specified first pieces,
with the original first density, also changes only its polynomial
prefactor. The \(N/(2i)\) in (21) has already been retained.

This pays one actual sampling current at a fixed finite height on
the core first pieces. It does not deform the old entire first
contour, include its early real-angle pieces, or estimate any
new second-coordinate interval. In particular no whole second
period or knot consequence is asserted.

## Direct source versions

The direct source uses are: the actual reference bounds, original
raw midpoint calibration and complete third inventory in the
half-face theorem, Sections 1--2 and 6; the exact phase and
\(+N\), \(N/(2i)\) residue conventions in the asymmetric
contour source, Sections 1 and 4; and the uniform original
factorial interpolation on a fixed regular complex rectangle. The
joint global chart, Section 1, fixes the exact negative-root marking
and its one-step recurrence in (20).

| Direct source | SHA-256 |
|---|---|
| research_mixed_443_complete_second_half_face.md | 11243b9bbf31c2ab1ec662fcb6b47f56f8017a8307f424b5bdf5efcf5d83079b |
| research_mixed_horizontal_asymmetric_contour.md | 2b0984562d9d3c63e2e366d9dc3b68f557512b71c74290f8ac530fcb4d3e7fce |
| exact_factorial_interpolation_and_complex_contours.md | 1f34f65437dfe0bfb4062a7a74840beae1676353cf13bb8a86f8849a8a36bc72 |
| research_mixed_fourier_right_cap_joint_global_chart.md | bf0069e52715e82c34be008c5814373017b43c019dd2a1a71dcd381e96b4da9f |

Author full proof readback and all four direct-source implication
reads and metadata hash checks are complete.
Independent full proof and direct-source review is required before
adoption. No mathematical numerical evaluation, test, import,
compilation, or frozen-source edit is used.
