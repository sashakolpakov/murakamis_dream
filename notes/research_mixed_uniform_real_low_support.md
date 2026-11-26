# A uniform real low-angle bound with one plateau reset cost reserved

Research corollary, 4 November 2026. This joins the proved zero collar
to a fixed compact part of the coherent real one-small theorem. It is
an upper bound for the original finite block, uniform through the low
endpoint. It does not continue a conditional saddle to that endpoint.

## 1. Source, reference, and closed target domain

Keep the original normalized finite kernel
\[
 C_{\epsilon,N}(X,Y)=\sum_{j=0}^{N-1}
       \frac{X^{-j}(r_NX;r_N)_j(r_NY;r_N)_j}
            {(r_N;r_N)_j^{2+\epsilon}},
 \qquad r_N=e^{-2\pi i/N},
\]
and the original Fourier polynomial
\(d_N(r_N^j)=(r_N;r_N)_j^{-1}\), \(\deg d_N<N\).
For real targets put
\[
 \mathcal B_{\eta\epsilon,N}(t)=
 |C_{\epsilon,N}(e^{-2\pi it_1},e^{-2\pi it_2})|
 |d_N(e^{-2\pi it_1})|^{\eta/2}
 |d_N(e^{-2\pi it_2})|^{\epsilon/2}.                         \tag{1}
\]
Here \(\eta,\epsilon\in\{0,1\}\) are the two original type
indicators. The half-powers denote nonnegative moduli and recombine
into the original integer powers in complete contractions.

Let the independent complex reference pair range over
\[
 r\in R_{3+\eta}\times R_{3+\epsilon},\qquad
 R_3=[.30,.39]+i[-.03,.02],\quad
 R_4=[.27,.33]+i[-.057,-.02].                                \tag{2}
\]
Use the original zero-lift phase \(\phi_{\eta\epsilon}\), with
\(g(z)=(\operatorname{Li}_2(e^{-2\pi iz})-\pi^2/6)/(2\pi i)\),
and the full complex tangent
\[
 \Gamma_r(t)=\phi_{\eta\epsilon}(r)
                 +\phi_{\eta\epsilon}'(r)\cdot(t-r).
                                                               \tag{3}
\]
Both input theorems below use exactly (1)--(3), including the original
chirp, additive constant and Fourier factors.

Set
\[
 \mathcal D=
 ([0,1/10]\times[1/10,9/20])\ \cup\
 ([1/10,9/20]\times[0,1/10]).                               \tag{4}
\]
All target heights are zero.

**Corollary 1.** Uniformly over (2) and (4), for both integer-level
parities and all sufficiently large \(N\),
\[
 \mathcal B_{\eta\epsilon,N}(t)
       \le C N^A\exp N\{\Re\Gamma_r(t)-1/20\}.              \tag{5}
\]
The low angle may equal zero or approach it with \(N\). Every
allowed selection of the original outer frequency factors obeys the
same bound, since those factors have modulus one on these real targets.

**Proof.** Put \(\ell=1/1000\). When the low target belongs to
\([0,\ell]\), the
[extended real zero collar](research_mixed_real_zero_collar_extension.md)
applies, because the other interval in (4) is contained in
\([.1,.5]\). Its raw row-sum bound is stronger than a bound for
the kernel modulus and gives gap \(3/50>1/20\).

For the remaining low targets use the fixed compact set
\[
 K=([\ell,1/10]\times[1/10,9/20])\ \cup\
   ([1/10,9/20]\times[\ell,1/10]).                           \tag{6}
\]
Every coordinate of \(K\) is strictly between zero and \(1/2\),
and each point has a coordinate at most \(1/10\). Thus \(K\)
is a compact subset of the exact domain of the
[real one-small finite-source theorem](research_mixed_real_one_small_support.md),
Theorem 1. Its finite gap is \(1/20\), uniformly over the same
reference rectangles. Its exact level power is
\[
 -\frac{1+\epsilon}{2}-\frac{\eta+\epsilon}{4}
                   =-\frac{2+\eta+3\epsilon}{4},
\]
from the original conditional kernel and its allocated halfweights.
This power can be absorbed in \(N^A\) together with the polynomial
loss of the raw collar, without altering an exponential constant.

The two closed pieces overlap at low angle \(\ell\). Take the
larger finite constants, level thresholds and polynomial power over
the two orientations and four type pairs. This proves (5) uniformly
on the entire closed domain (4). No root or phase derivative at a
zero target is used. \(\square\)

The sum of absolute rows is used only on the zero collar. Corollary 1
does not assert that stronger raw bound throughout (4): its other
piece uses the coherent complete kernel.

## 2. Reserving a complete oriented plateau reset cost

The [oriented height-reset theorem](research_mixed_oriented_height_reset.md)
has the two one-height costs
\[
 q_0c^2=\frac{11}{2}c^2,\qquad
 q_1c^2=\frac{151}{20}c^2,
\]
according to the position of the reset argument. The original
reference heights satisfy \(|c|\le57/1000\). In particular
\[
 q c^2\le\frac{151}{20}\left(\frac{57}{1000}\right)^2
          =\frac{490599}{20000000}<\frac3{100},
 \qquad 0\le q\le\frac{151}{20}.                           \tag{7}
\]
Multiplying (5) by the full reserved rate \(e^{Nqc^2}\) gives
\[
 \mathcal B_{\eta\epsilon,N}(t)e^{Nqc^2}
       \le C N^A\exp N\{\Re\Gamma_r(t)-1/50\}.              \tag{8}
\]
Indeed the sharper remaining gap is
\[
 \frac1{20}-\frac{490599}{20000000}
       =\frac{509401}{20000000}>rac1{50}.                  \tag{9}
\]
This reserves the entire cost, not just a fraction associated with
part of a contour deformation.

For its literal neighboring-block interpretation, suppose the paid
block has both real target coordinates in the plateau
\(P=[.22,.45]\), one height reset to zero and the other left at
its original reference height. Both real coordinates may readjust.
The oriented theorem gives that block's original upper rate
\(\Re\Gamma_{\rm adj}+qc^2\). On this compact plateau every
unselected type-four height is in \([-.057,0]\) and its relative
Fourier estimate is valid. The corresponding finite bound therefore
has only a polynomial loss, with no positive rate tolerance required.
Selection at the reset real coordinate is harmless. Selection at the
unchanged complex coordinate is outside this interpretation and needs
its own existing selected-block estimate.

Under precisely these neighboring-block hypotheses, multiplying the
two original allocated bounds leaves at least the gap \(1/50\)
against the sum of their original tangents. Formula (8) itself is
simply the reserved single-block estimate and holds for all real
targets (4), regardless of whether such an adjacent plateau block is
present. No incidence charge is assigned more than once by this local
statement; an assembly must supply its own allocation.

## 3. Scope and reproduction

All finite sums, Fourier forcing terms, original normalizations and
parities are retained. No nonzero coefficient, derivative estimate,
or transport inequality is asserted at a zero target. In particular,
the corollary may be used as an endpoint bound when low and early
coordinates meet; it does not justify differentiating a degenerate
conditional root there or control an entire mixed integration region.

```sh
python3 experiments/check_mixed_uniform_real_low_support.py
```

The checker verifies the compact-domain inclusions, matching source
normalizations and exact reserve, and validates the current source
records and their inherited bindings. It does not repeat the already
completed continuum covers.
