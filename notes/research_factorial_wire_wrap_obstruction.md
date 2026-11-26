# A wrap contribution in the original factorial wire period

Private written research note, 16 November 2026.

The original factorial interpolation has a positive wrap contribution
whose exponential rate can exceed the positive geometric edge action.
This occurs at both level parities, including an open family with both
angles strictly in the lower half-plane. Consequently a contour with
the same wire endpoints cannot have a geometric saddle piece and only
smaller connecting pieces throughout the positive edge domain.

This is a statement about an untraced edge period. Changing its endpoints
in height retains an explicit multiple of the full trace polynomials.
Those terms vanish in the appropriate tensor Hermite quotient, but
must be combined before estimates are taken. Section 4 performs that
combination on a fixed microscopic wrap layer and obtains an exact
representative of polynomial size on full-grid angular rectangles.
No conclusion about the remaining closed scalar or a volume limit
is inferred.

## 1. The actual period and its wrap layer

Put
\[
 N\ge2,\quad D=N-1,\quad \eta=(-1)^D,\quad b_N=-\frac1{2N},
 \qquad z(t)=-2\cos t,\qquad P_N(z)=2T_N(z/2)+2.
 \tag{1}
\]
Use the specified canonical Gamma-product factorial \(G_N\), and set
\[
 B_N(x,t)=
 \frac{N}{
 G_N(D/2-Nx+Nt/(2\pi))
 G_N(D/2-Nx-Nt/(2\pi))G_N(Nx)^2},
 \tag{2}
\]
\[
 I_N(h;t,u)=\int_{b_N+ih}^{b_N+1+ih}
                      B_N(x,t)B_N(x,u)\,dx .
 \tag{3}
\]
Thus the finite wire normalization is \(N I_N\), when (3) is used
inside the original traced source. Formula (2) retains the actual
offset \(-1/2\) in both shifted factorials.

**Theorem 1.** For every compact set of \(H,K\ge0\), there are
\(c>0\) and \(N_0\), independent of parity, such that
\[
 I_N(0;-iH,-iK)\ \ge\
               cN^{-9/2}e^{N(H+K)}
                 \qquad(N\ge N_0).
 \tag{4}
\]
The period in (4) is real and nonnegative. Its wrap layer alone has
the displayed lower bound.

**Proof.** The defining Gamma product is of real type. Its recurrence
and reflection identities are
\[
 G_N(z+1)=2\sin\frac{\pi(z+1)}N\,G_N(z),\qquad
 G_N(z)G_N(D-z)=N,\qquad
 G_N(z+N)=-2\sin(\pi z)G_N(z).
 \tag{5}
\]
For clarity, reflection follows directly from the exact derivative
\[
 g_N'(z)=\frac{\pi}{N^2}\sum_{j=0}^{D}
                  (z-j)\cot\frac{\pi(z-j)}N:
 \tag{6}
\]
reversing \(j\) gives \(g_N'(D-z)=g_N'(z)\).
The product in (5) is constant, and at \(z=0\) its value is
\(\prod_{j=1}^{D}2\sin(\pi j/N)=N\).
The last identity in (5) follows by multiplying the recurrence
through \(N\) steps. All identities continue meromorphically.

For real \(x\in[b_N,b_N+1]\), \(G_N(Nx)\) is real and nonzero.
The two shifted arguments in (2) are conjugate at \(t=-iH\).
Hence \(B_N(x,-iH)>0\) if \(H>0\), and it is nonnegative if
\(H=0\); the reciprocal-factorial zeros are included in this
last assertion. In particular the entire integrand in (4) is
nonnegative.

Take
\[
 x=1-\frac{s}{N},\qquad
 \frac34\le s\le\frac78,\qquad r=s-\frac12,\qquad
 \beta=\frac{H}{2\pi}.
 \tag{7}
\]
This interval lies inside the period, beyond its last physical
integer index \(D/N\). Applying (5) to (2) gives the exact formula
\[
 B_N(1-s/N,-iH)=
 \frac{4|\sin\pi(-N/2+r+iN\beta)|^2\,G_N(s-1)^2}
 {N\,|G_N(N/2+r+iN\beta)|^2}.
 \tag{8}
\]
It remains valid at \(H=0\). No asymptotic continuation of an
integer factorial was used to obtain it.

Uniformly in the fixed \(s\)-interval, the actual Gamma product gives
\[
 G_N(s-1)=
       (2\pi/N)^{s-1}\Gamma(s)(1+O(N^{-2})).
 \tag{9}
\]
Indeed its \(m\)-th logarithmic factor is \(O((Nm)^{-2})\)
uniformly on this compact set. Summing the bound proves (9),
including the specified interpolation and its normalization.

There is a convenient exact control of the other factorial:
\[
 |G_N(N/2+iy)|^2=2N\cosh(\pi y/N).
 \tag{10}
\]
To prove (10), reflect \(N/2+iy\) to \(N/2-1-iy\) and apply
one recurrence step to its conjugate. For \(r\in[1/4,3/8]\),
equation (6) also gives a uniform bound for \(g_N'\) between
\(N/2+iN\beta\) and \(N/2+r+iN\beta\), when \(H\) ranges
over a compact set. In fact each summand can be written as
\(Nw\cot(\pi w)\), where \(w\) stays in a fixed compact set
avoiding the nonzero integer poles; its value at zero is removable.
Thus the sum in (6) is bounded. Integrating this derivative and
using (10) proves
\[
             c_1N\le
       |G_N(N/2+r+iN\beta)|^2\le C_1N .
 \tag{11}
\]
This argument is uniform through \(H=0\), so no half-plane
asymptotic is being applied at its boundary.

Finally
\[
 |\sin\pi(-N/2+r+iN\beta)|^2
   =\sin^2\pi(-N/2+r)+\sinh^2(NH/2).
 \tag{12}
\]
At even \(N\) the first term is \(\sin^2\pi r\); at odd \(N\)
it is \(\cos^2\pi r\). Both have a positive common lower bound
on (7). Therefore (12) is bounded above and below by positive
constants times \(e^{NH}\), uniformly for \(H\) in any compact
subset of \([0,\infty)\). Equations (8)--(12) imply
\[
 c_2N^{-2s}e^{NH}\le B_N(1-s/N,-iH)
                    \le C_2N^{-2s}e^{NH}.
 \tag{13}
\]
Apply this to both endpoints. Since \(4s\le7/2\) and
\(|dx|=ds/N\), integration over (7), followed by positivity
on the rest of the period, proves (4). \(\square\)

## 2. Comparison with the marked positive edge action

Let \(G_{\rm Cat}=\sum_{j\ge0}(-1)^j/(2j+1)^2\) and
\(M_\infty=4G_{\rm Cat}/\pi\). On the family in Theorem 1 put
\[
 \alpha=\tanh(H/2),\qquad \beta=\tanh(K/2),\qquad
                         \alpha^2+\beta^2<1 .
 \tag{14}
\]
The original positive shapes have
\[
 a=-i\alpha,\quad b=-i\beta,\quad
 q=\sqrt{1-\alpha^2-\beta^2}>0.
 \tag{15}
\]
Thus their exact positivity criterion
\(\Re q>\sqrt{(\Re a)^2+(\Re b)^2}\) holds.
On the original complete continuation the returns are
\[
 r_t=-i\arcsin\frac{\alpha}{\sqrt{1-\beta^2}},\qquad
 r_u=-i\arcsin\frac{\beta}{\sqrt{1-\alpha^2}} .
 \tag{16}
\]
Their arcsines lie in \([0,\pi/2)\).

The same-index stationary wire is
\[
 x^*=\pi^{-1}\arctan(1/q)\in[1/4,1/2).
 \tag{17}
\]
The original factorial phase
\[
 b(x,t)=-J(1/2-x+t/(2\pi))
        -J(1/2-x-t/(2\pi))-2J(x),\qquad
 J'(w)=\Log(2\sin\pi w)
 \tag{18}
\]
is regular at (17), with its original strip branches. The critical
value of \(b(x,t)+b(x,u)\) is the marked \(\psi(t,u)\), normalized
by \(\psi(0,0)=M_\infty\) and
\(\psi_t=-r_t/\pi,\ \psi_u=-r_u/\pi\).
These are the original phase identities, not a choice of a new
additive constant.

Scale \((H,K)\) by \(0\le\lambda\le1\). Condition (14) remains
strict. The derivatives in (16) give
\[
 \psi(-iH,-iK)\in\mathbb R,\qquad
       \psi(-iH,-iK)<M_\infty+\frac{H+K}{2}
                     \quad(H+K>0).
 \tag{19}
\]
In particular, on every compact part of
\[
 \alpha^2+\beta^2<1,\qquad H+K>2M_\infty,
 \tag{20}
\]
the rate in (4) exceeds the marked geometric rate by a uniform
positive amount. This domain includes points with \(H,K>0\).
For an exact nonnumerical witness, take \(H=K=\log5\). Then
\(\alpha=\beta=2/3,\ q=1/3\), while
\(\log5=2\operatorname{artanh}(2/3)>4/3>M_\infty\),
using \(G_{\rm Cat}<1\) and \(\pi>3\).

It follows that no bound
\[
 |I_N(0;t,u)|\le C N^A e^{N\Re\psi(t,u)}
 \tag{21}
\]
can hold throughout compact positive edge domains, with any
fixed polynomial factor. More specifically, deforming the real
wire interval with its endpoints fixed through a common pole-free
domain leaves \(I_N(0;t,u)\) unchanged. If one selected local saddle
piece has an upper bound \(CN^Ae^{N\psi}\), its remaining
pieces collectively have rate at least \(H+K\) on (20).
Thus they cannot all have a smaller exponential rate than that
saddle. The conclusion concerns their actual integrals, and is
stronger than the failure of one particular absolute-value
estimate.

For geometric context, the endpoint pair \((-iH_*,0)\), where
\[
 H_*=2\operatorname{artanh}(\sqrt3/2),
 \tag{22}
\]
occurs at the original unit-charge, zero-power trivalent star:
each of its three returns is \(-i\pi/3\).
One can check \(H_*>5/2>2M_\infty\) without numerical evaluation:
\(G_{\rm Cat}<209/225<15/16,\ \pi>3\), and the first five
positive terms of the arctanh series give
\[
 H_*>\sqrt3\,\frac{13063}{8960}>
              \frac{19}{11}\frac{13063}{8960}>\frac52.
 \tag{23}
\]
This identifies an original geometric point, not a new source
formula for that star. Its untraced complete outside ends must
retain their ordinary cardinal factors. At odd levels the value
at \(-2\) is a physical simple-node value and agrees with the
factorial factor; at even levels that replacement is not allowed.
The all-parity theorem above concerns (3), with its stated
factorial endpoints.

## 3. The exact height defect and full Hermite scope

Put \(P_t=P_N(z(t))\) and, away from its removable products, set
\[
 d_N(x)=\frac{(-1)^N}{4\sin^2(\pi Nx)},\qquad
 F_N(x;t,u)=B_N(x,t)B_N(x,u).
 \tag{24}
\]
The exact interpolation period law is
\[
 B_N(x+1,t)=(\eta+d_N(x)P_t)B_N(x,t).
 \tag{25}
\]
Consequently
\[
 F_N(x+1;t,u)-F_N(x;t,u)
 =\{\eta d_N(x)(P_t+P_u)+d_N(x)^2P_tP_u\}F_N(x;t,u),
 \tag{26}
\]
\[
 \frac{d}{dh}I_N(h;t,u)
 =i\{\eta d_N(b_N+ih)(P_t+P_u)
             +d_N(b_N+ih)^2P_tP_u\}F_N(b_N+ih;t,u).
 \tag{27}
\]
Here \(\sin\pi N(b_N+ih)=-\cosh(\pi Nh)\ne0\).
Formula (25) follows directly from (5), or from
\[
 \cos Nt-\eta=\frac{(-1)^N}{2}P_N(-2\cos t).
 \tag{28}
\]
Differentiating the translated path in (3) proves (27).
All statements hold on common analytic domains; in particular
there are no reciprocal-factorial poles on the stated wire
strip at the purely imaginary angles of Theorem 1.

In the tensor product of the two original full Hermite algebras,
\[
 [\,N I_N(h;t,u)\,]
       =[\,K_T(z(t),z(u))\,],\qquad
 K_T(z,w)=\sum_{j=0}^{D}e_j(z)e_j(w),
 \tag{29}
\]
independently of \(h\). This is the exact internal-wire
circle-averaging identity. It retains the first normal at every
double root and the value at the odd simple root. In particular
(26)--(27) are annihilated by the corresponding original
traces, with arbitrary polynomial spectators. They are not
pointwise zero at arbitrary complex angles.

Changing the height of a period therefore retains (27), or its
integral, until the complete trace contraction is performed.
Theorem 1 does not rule out a joint deformation that combines
these terms coherently. It does rule out using positive edge
geometry alone to bound each unweighted real factorial period
at its selected geometric action. Kernel removal in (26) is
not an identification with a smaller filled graph.

The earlier cardinal-kernel obstruction already exhibits a
larger endpoint rate at even levels on \((-iH,0)\). The new
point here is the actual factorial period, its positive off-grid
wrap layer at both parities, and the exact trace-polynomial
defect that is retained when its wire endpoints move. Passing
to the cardinal representative alone is not a general bound
for its off-spectrum values either.

## 4. Removing the wrap term inside the original trace

There is a constructive consequence of the same calculation. A period
shift removes the large wrap factor modulo the full trace polynomial,
and the resulting representative has polynomial size on an angular
rectangle enclosing the entire physical grid.

Fix
\[
 \frac12<s_0\le s\le s_1<1,\qquad
             2s_1-1<c<1,\qquad 0\le T<\infty,\qquad
 a'_{N}=\pi-\frac{c\pi}{N}.
 \tag{30}
\]
Define the even analytic coupon
\[
 A_N(s,t)=
 \frac{G_N(s-1)^2}{
 N\,G_N(N/2+s-1/2+Nt/(2\pi))
       G_N(N/2+s-1/2-Nt/(2\pi))}.
 \tag{31}
\]
**Theorem 2.** On a neighborhood of
\[
                 |\Re t|\le a'_N,\qquad |\Im t|\le T,
 \tag{32}
\]
the following are exact identities:
\[
 \begin{split}
 B_N(1-s/N,t)
   &=(-1)^N\{P_N(z(t))-4\sin^2(\pi s)\}A_N(s,t),\\
 B_N(-s/N,t)&=4\sin^2(\pi s)A_N(s,t).
 \end{split}
 \tag{33}
\]
For every fixed angular derivative order \(j\), constants \(C_j,A_j\)
depending only on (30) satisfy
\[
 \sup_{\substack{s_0\le s\le s_1\\t\text{ in }(32)}}
             |\partial_t^j A_N(s,t)|\le C_j N^{A_j}.
 \tag{34}
\]
In particular
\[
 [\,B_N(1-s/N,t)\,]
       =[\,\eta B_N(-s/N,t)\,]
 \tag{35}
\]
at every physical value and first normal, with the actual odd-level
simple-node convention.

**Proof.** Let
\[
                  Z=N/2+s-1/2+Nt/(2\pi).
 \tag{36}
\]
Reflection gives the useful exact form
\[
 A_N(s,t)=\frac{G_N(s-1)^2}{N^2}
                              \frac{G_N(Z-2s)}{G_N(Z)}.
 \tag{37}
\]
Both \(Z\) and \(Z-2s\), and the horizontal segment between them,
lie in
\[
 -1+\delta\le\Re z\le N-\delta,\qquad
 |\Im z|\le NT/(2\pi),\qquad
                    \delta=\frac{c-2s_1+1}{2}>0.
 \tag{38}
\]
Indeed the two extreme bounds are
\(\Re Z\le N+s-1/2-c/2\) and
\(\Re(Z-2s)\ge-s-1/2+c/2\).
The other bounds are stronger. This proves holomorphy and
nonvanishing of both ratio factors by the original nonzero Gamma
strip. It also proves holomorphy of (31) on a neighborhood of (32).

The exact finite derivative (6) gives
\[
                 |g_N'(z)|\le C_{\delta,T}(1+\log N)
                            \quad\text{on }(38).
 \tag{39}
\]
Here is a direct uniform bound, including the real axis. On the
fixed scaled rectangle, the meromorphic function
\(w\cot(\pi w)\) has only the possible nonremovable poles
\(w=\pm1\). Subtracting those two principal parts leaves a
bounded function. For \(w_j=(z-j)/N\), the two pole sums are
bounded by constants times
\[
 \sum_{j=0}^{D}\frac1{N-\Re z+j}
       +\sum_{j=0}^{D}\frac1{N+\Re z-j}
 \le 2\sum_{j=0}^{D}\frac1{\delta+j}.
 \tag{40}
\]
Equation (6), written as
\((\pi/N)\sum_j w_j\cot(\pi w_j)\), now proves (39).
The imaginary parts can only increase the distances used in
(40).

Integrate (39) along the segment in (38). The ratio in (37)
and its reciprocal are bounded by fixed powers of \(N\).
Equation (9), now on the compact interval \([s_0,s_1]\),
then proves (34) for \(j=0\).
A disk of radius \(\delta\pi/(4N)\) in \(t\) retains half
the real margins in (38) and a fixed imaginary bound.
Cauchy's estimate proves (34) for every fixed \(j\).

For the first identity in (33), apply the \(N\)-shift as in
(8), but before taking absolute values. Its numerator is
\[
 4\sin\pi(-N/2+s-1/2+Nt/(2\pi))
   \sin\pi(-N/2+s-1/2-Nt/(2\pi))
       =(-1)^N\{P_N(z(t))-4\sin^2(\pi s)\}.
 \tag{41}
\]
For the second, (5) gives
\[
                G_N(-s)G_N(s-1)=\frac{N}{2\sin(\pi s)}.
 \tag{42}
\]
Substitution in (2) proves it. The difference in (35) is
exactly \((-1)^NP_N(z(t))A_N(s,t)\).
At a double spectral root it vanishes in value and first
spectral normal. At the odd simple root \(z=-2,t=0\), the
coupon is even and holomorphic; it therefore defines a regular
spectral germ and the required value agrees. No extra normal
is imposed at that simple root. \(\square\)

Since \(c<1\), rectangle (32) contains every physical angle
\(|t|\le\pi-\pi/N\), with a positive margin. It therefore
supports complete lower and upper lenses, rather than a
central angular truncation. For the wrap layer of Theorem 1
one may take \(c=7/8\).

Now let a traced vertex have any attached even holomorphic
spectator on a common neighborhood of the physical grid.
This includes the original crossing Gaussian, with its actual
full-Hermite normalization, or any of its polynomial crossing
representatives. Multiplying the difference in (35) by that
spectator and applying the original trace gives exactly zero.
The same holds when several wrapped halfwires meet a vertex:
replace them successively, and each difference still contains
\(P_N\) times a holomorphic even factor. Applying this at
any finite set of traced vertices retains all mixed normals
and arbitrary untouched exterior variables.

Thus a selected wrap sector of an arbitrary original network
has an exact representative in which each traced halfwire
\(B_N(1-s/N,t)\) is replaced by
\(\eta B_N(-s/N,t)\), with the polynomial bounds (34).
The bounds are uniform even at the moving angular ends.
Ordinary free cardinal factors are left untouched. If both
ends of a same-index edge are traced, the two factors of
\(\eta\) multiply to one.

For completeness, (34) also gives polynomial bounds for the
physical first spectral normals: away from the odd simple
node, divide \(\partial_t\) by \(2\sin t\), whose reciprocal
on the physical double-root grid is \(O(N)\). The simple
node requires only its value. Hence multiplication by any
fixed number of these coupons has polynomial norm on the
finite full-Hermite jet space. This does not bound an attached
spectator whose own physical jets or contour values are large.

The exponentially large term isolated by Theorem 1 can therefore
be removed coherently before absolute values are taken in the
original traces. The resulting coupons still depend on the
angular variables. They are not deleted vertices, deleted edges,
or a proof of a geometric rate for the remaining joint
contraction. In particular this theorem does not extend its
fixed compact \(s\)-range to the singular limit \(s=1\), and
does not supply a global complement estimate for all other
wire regions.

## 5. Direct written sources and version pins

The proof uses the following complete written source versions.
Their directly used implications are the canonical Gamma
product and finite derivative, the full-Hermite circle identity,
the actual same-index phase and critical value, the original
positive shapes and marked returns, and the existing cardinal
comparison/obstruction, respectively.

- [Exact canonical factorial](research_exact_cyclotomic_factorial.md):
  SHA-256 0f989261f53747266ac62dba40ca7548138012b266521e98a03bd94b450c657b.
- [Internal circle averaging](research_internal_wire_exact_circle_averaging.md):
  SHA-256 0efa85a43da064197f25422d86ef37688971f2dface55da9d5efef3ccb0d08ef.
- [Unsummed original network phase](research_unsummed_network_phase_coercivity.md):
  SHA-256 b5441bb508d3ffad3274e38dda2d6aeb099d08ae2ab043a0d12c25234e4a1e1e.
- [Positive edge geometry and primitive periods](research_positive_edge_global_monotonicity.md):
  SHA-256 da5129c7110190035eedb8249d4004dd06b5a7555e78d948234d8de50fa17500.
- [Cardinal/factorial comparison and prior endpoint obstruction](research_free_boundary_cardinal_factorial_comparison.md):
  SHA-256 9ed5b69bad33d7e62a7b40070d86d9d2233f2c34bc7674ddcf8a82e8e0091d5d.

No mathematical execution, numerical evidence, or tests are used.
