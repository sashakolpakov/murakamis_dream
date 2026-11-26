# A wider input rectangle for the original retained three-crossing packet

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

This extends the actual retained source, not just its analytic critical
phase, to an input rectangle twice as wide in the real direction. The
outgoing coordinate square is unchanged. It provides a source packet on
near-input tails of a subsequent attachment; the complementary wire
integral and its closing coefficient remain separate questions.

## 1. Exact source and domain

Put
\[
 x_h=\frac16+\frac{i\log2}{2\pi},\qquad
 \begin{split}
 \mathcal X&=\{x_h+a+ib:|a|\le1/100,\ |b|\le1/200\},\\
 \mathcal Q&=\{x_h+a+ib:|a|,|b|\le1/200\}.
 \end{split}
 \tag{1}
\]
Use precisely the L40 source of
[the genuine bidisk theorem](research_three_vertex_bidisk_packet.md):
\[
 L_{40}=\lfloor N/40\rfloor,\quad
 E_{40}=M^TP_{L_{40}}JM P_{L_{40}}M,\quad
 \widetilde V_N^{(40)}(x,y)=h(x)^T(JM^3-E_{40})h(y).
 \tag{2}
\]
Thus the literal root-product double sum omits exactly the square
\(i,j\le L_{40}\), retaining all other finite rows and the original
physical first normals. This is the same finite source as the bidisk
theorem, and is distinct from the earlier L50 source.

**Theorem 1.** On a fixed open neighborhood of
\(\mathcal X\times\mathcal Q\), at both level parities,
\[
 \widetilde V_N^{(40)}(x,y)=
 \kappa N^{-1/2}a(x,y)e^{N\Phi(x,y)}(1+O(N^{-1})).
 \tag{3}
\]
Here \(\Phi,a\) are the original branches in the bidisk theorem,
\(a\) is holomorphic and nonzero, and the normalized error is
holomorphic and uniformly \(O(N^{-1})\), including every fixed
parameter derivative on a smaller neighborhood.

## 2. Exhaustive compact comparisons

Retain the original phase \(F\), critical formulas and logarithmic
lifts from equations (4), (12), (14) of the bidisk theorem. Write
\(F_c=F(s_c,t_c;X,Y)\), where \(X=e^{2\pi ix},Y=e^{2\pi iy}\).
The outward certificate proves on the whole domain (1):
\[
 \begin{gathered}
 \Im\Delta>0,\quad U_c,V_c\text{ in the lower-left quadrant},\\
 \Re X,\Im X,\Re Y,\Im Y>2/25,\quad |X|,|Y|<27/50,\\
 3/10<\Re s_c,\Re t_c<2/5,\quad
 |\Im s_c|,|\Im t_c|<193/10000,\quad \Re F_c>-1/10.
 \end{gathered}
 \tag{4}
\]
The connected parameter rectangle and the homogeneous normalization
fix the original index-equation lifts. The enlarged contour is
\[
 B_*=[47/200,9/20],\qquad h_*=39/2000,\qquad
 \mathcal R_*=B_*+i[-h_*,h_*].
 \tag{5}
\]
The former height \(17/1000\) cannot contain all critical points
of this larger input rectangle. Both the lower real cut and the
height in (5) are part of the present proof.

For each of the following three real-index regions, and separately
with the two indices interchanged, the certificate proves
\[
 \begin{split}
 E_0&=\{0\le s\le1/40,\ 1/40\le t,\ s+t\le99/100\},\\
 E_1&=\{1/40\le s\le47/200,\ 0\le t,\ s+t\le99/100\},\\
 E_2&=\{s=9/20,\ 0\le t\le54/100\},\\
 &\hspace{30mm}\Re(F_c-F)>1/250.
 \end{split}
 \tag{6}
\]
The interchange is checked with the original, unequally sized wire
domains; it is not inferred by treating those domains as symmetric.
On every product of index sides with at least one vertical side,
and on the four horizontal-side products, respectively,
\[
 \Re(F_c-F)>1/10000,
 \qquad
 \Re(F-F_c)<1/20.
 \tag{7}
\]

There are 369 exact parameter domains: one four-dimensional branch
domain, 16 critical-floor domains, 96 real-index complement domains,
and 256 side products. For the last three groups, separate harmonicity
in the two complex wire variables reduces the extrema to all 16
ordered pairs of their rectangle sides. Each inequality is accepted
on a full rational box by an outward center value and an interval
derivative bound. The author cover has 31,570 leaves. The independent
replayer verifies the exact binary partition, both orders in (6),
all original phase branches, and the full interval inequalities.

## 3. Index concavity on the enlarged contour

Only index concavity is needed with the two wire parameters fixed.
The exact Hessian decomposition is
\[
 -\Re d^2_{s,t}F
     =a(ds+dt)^2+d_xds^2+d_ydt^2,
 \tag{8}
\]
where the coefficients are those of
[the original joint Hessian](research_three_vertex_joint_concavity.md),
equation (3). In the present box the relevant angle in either
\(d\) coefficient lies in
\([7\pi/60,44\pi/75]\), and its absolute imaginary argument is
at most \(\log2+49\pi/1000\). Therefore
\[
 \cosh(\log2+49\pi/1000)<7/5,
 \qquad d_x,d_y>3/2.
 \tag{9}
\]
To verify the second inequality it suffices to check the two
endpoints of
\(\pi\sin\theta/(7/5-\cos\theta)\): its only interior critical
point is a maximum. Both strict endpoint inequalities are included
in the exact scalar certificate.

If \(\Re(s+t)\ge1/2\), then \(a\ge0\). In the newly added
part \(47/100\le\Re(s+t)<1/2\), the general height denominator
\(\cosh(2\pi\Im(s+t))-\cos(2\pi\Re(s+t))\) is at least its
zero-height value. It follows that
\[
 |a|\le\pi\tan(3\pi/100)<1/3,
 \qquad -\Re F''_{s,t}\succ\frac56 I_2.
 \tag{10}
\]
Indeed \((ds+dt)^2\le2(ds^2+dt^2)\). Thus the small extension
below \(\Re(s+t)=1/2\) has not been covered by an unjustified use
of the older joint-concavity chamber.

## 4. Finite contours, original coefficient, and reproduction

The finite complement follows exactly from (6), the original real
index monotonicity, and the top-factorial estimate. For
\(9/20\le s\le9/10\), the wider wire rectangle still satisfies
\(1/4<s-\Re x<3/4\), so
\[
 |1-Xe^{-2\pi is}|\ge\sqrt{1+|X|^2}>2|X|.
 \tag{11}
\]
For \(s\ge9/10\), the numerator is at most
\(2(27/50)\pi/10<1-27/50\). Hence the high strips reduce to
\(E_2\), in either index order. On \(s+t\ge99/100\), the
unchanged original endpoint estimate gives
\[
 \Re F\le-\frac35\frac{99}{100}+\frac49+\frac{13}{300}
       <-\frac1{10}-\frac1{200}<\Re F_c-\frac1{250}.
 \tag{12}
\]
The finite factorial endpoint loss is polynomial in \(N\). All
roundings, including the corner cut and the half-grid real sides,
preserve these fixed strict gaps.

The exact root-Pochhammer interpolant is regular on
\(\mathcal R_*^2\): its numerator strip now has
\(47/100\le\Re(s+t)\le9/10\), and
\((27/50)e^{2\pi h_*}<1\) keeps both denominator factors regular.
Its full symbol is still equation (12) of the bidisk theorem.
The two exact cotangent formulas retain all side products. The
vertical-containing terms have the first gap in (7); maximum
principles supply the connecting side rectangles. Every
nonconstant horizontal cotangent factor pays \(2\pi h_*\), so
the second bound in (7) gives net loss
\[
                         2\pi h_*-1/20>1/20.
 \tag{13}
\]
The constant products combine to the original positive factor
\(+N^2\). They move to the two critical heights, which lie strictly
inside (5). Equation (10) gives the unique maximum on that horizontal
index plane and a nonzero Gaussian determinant. The unchanged
cardinal factors, original symbol, and orientations give precisely
the phase and amplitude in equation (14) of the bidisk theorem;
in particular the power is \(N^{-1/2}\), with no parity change.
The odd Gaussian term integrates to zero and the relative error is
\(O(N^{-1})\). Strict compact margins and Cauchy estimates give
the open neighborhood and derivatives in Theorem 1.

Run

```sh
python3 experiments/certify_three_vertex_input_rectangle.py --precision 160
python3 experiments/replay_three_vertex_input_rectangle.py --precision 192
```

The [author checker](../experiments/certify_three_vertex_input_rectangle.py)
and [record](../repro/results/research-three-vertex-input-rectangle.json)
retain the full rational cover and seventeen scalar premises.
The [independent replayer](../experiments/replay_three_vertex_input_rectangle.py)
uses a negative-frequency phase primitive, reconstructs every exact
partition, and checks all domains without importing author code.
Its [record](../repro/results/research-three-vertex-input-rectangle-replay.json)
records the higher-precision result and current dependencies.
The [original L40 corner-transfer bounds](research_three_chain_fourier_corner_transfer.md)
remain unchanged. No further complete-chain lower bound follows
solely from enlarging this retained packet domain.

## 5. A quantitative cubic bound for the original phase

The analytic phase has a useful larger-domain estimate independent of
the finite-source contours above. Set
\[
 z=x-x_h,\quad w=y-x_h,\quad
 k_0=\frac{4\pi}{21}(2\sqrt3-3i),\quad
 |z|\le1/100,\quad |w|\le1/200,
 \tag{14}
\]
and define
\[
 E_{xx}=\Phi_{xx}/k_0+5,\quad
 E_{xy}=\Phi_{xy}/k_0-2,\quad
 E_{yy}=\Phi_{yy}/k_0+5.
 \tag{15}
\]
The exact homogeneous identities give \(E_{ab}(0,0)=0\),
\(\Phi(x_h,x_h)=2c\), and zero gradient there.

**Proposition 2.** Throughout (14), each entry satisfies
\[
 |E_{ab}(z,w)|\le18(|z|+|w|).
 \tag{16}
\]
Consequently the original phase and both original first derivatives
obey, with \(R=|z|+|w|\),
\[
 \begin{split}
 \left|\Phi(x_h+z,x_h+w)-2c+
             \frac{k_0}{2}(5z^2-4zw+5w^2)\right|
       &\le3|k_0|R^3,\\
 |\Phi_x/k_0+5z-2w|,
 \quad |\Phi_y/k_0-2z+5w|&\le9R^2.
 \end{split}
 \tag{17}
\]
This is a phase estimate on complex disks. It does not extend the
finite-source theorem to input imaginary displacement \(.01\);
that theorem has exactly the rectangle (1).

*Proof.* The independently proved analytic majorant in
[the phase-class theorem](research_three_phase_graph_transform.md),
Section 3, gives \(|E_{ab}|<64\) on the larger bidisk
\(|z|,|w|\le R_0=1/50\). The exact selected root and rational
Hessian formulas determine every Taylor coefficient. Compute them
outward through total degree 12. Write the polynomial part as
\(zP_{ab}(z,w)+wQ_{ab}(w)\), putting every monomial with positive
\(z\)-degree in the first group. The constant coefficient is
identically zero, as checked by the exact homogeneous Hessian
identities, not by cancellation of a numerical enclosure.

The Cauchy coefficient bound is \(64R_0^{-j}\) at total degree
\(j\). With \(q_x=1/2,q_y=1/4\), the remainders after factoring
\(z\) and \(w\) are therefore at most
\[
 \begin{split}
 T_z&=\frac{64}{R_0}
 \frac{q_x^{13}/(1-q_x)-q_y^{13}/(1-q_y)}{q_x-q_y}
              <3.125,\\
 T_w&=\frac{64}{R_0}\frac{q_y^{12}}{1-q_y}<.000255.
 \end{split}
 \tag{18}
\]
These are exact geometric sums of all omitted monomials. The
outward total polynomial-plus-tail bounds are strictly below the
following rational numbers:
\[
 \begin{array}{c|cc}
 &\text{coefficient of }|z|&\text{coefficient of }|w|\\ \hline
 E_{xx}&17.568&4.627\\
 E_{xy}&8.058&4.609\\
 E_{yy}&8.056&13.839.
 \end{array}
 \tag{19}
\]
In particular all six coefficients are below 18, proving (16).
Integrate once and twice along \((tz,tw)\), \(0\le t\le1\).
The integrals \(18\int_0^1t\,dt=9\) and
\(18\int_0^1t(1-t)\,dt=3\) prove (17), retaining the original
additive constant. \(\square\)

The [focused checker](../experiments/check_three_vertex_input_phase_remainder.py)
uses coefficient recurrences for both inverses and the selected square
root; it imports neither the earlier Taylor code nor its root solver.
It checks the two exact center identities and six strict outward
coefficient bounds, and records the full degree-12 coefficients and
the exact rational Cauchy tails in
[its result](../repro/results/research-three-vertex-input-phase-remainder.json).
Run

```sh
python3 experiments/check_three_vertex_input_phase_remainder.py --precision 192
```
