# The actual root head: a smooth matrix block and its retained cut

Private written proof, 18 November 2026.

The literal highest-weight \(N\)-head lies at a smooth Azumaya point
of the unrestricted algebra in its actual even-order root convention.
An explicit local matrix presentation proves this; simplicity of the
matrix image alone would not. The whole Frobenius fiber is larger,
and the original marked cut is not a cyclic trace on this block.

The complete proof directs are C and B, pinned below. C identifies
the root head and its existing regular matrix-image family. B fixes
the balanced basis, full crossing and original selected closure.
All central presentation and trace-descent calculations are given here.
No geometric framing measure or nonzero closure is inferred.

## 1. Conventions and the actual point

Fix \(N\ge2\), \(q=e^{\pi i/N}\), \(Q=q^2\), and
\(\rho=q-q^{-1}\ne0\). Let \(U\) have generators
\(E,F,K,K^{-1}\) and relations
\[
 KE=QEK,\qquad KF=Q^{-1}FK,\qquad
 [E,F]=(K-K^{-1})/\rho .
 \tag{1}
\]
This is the unrestricted specialization with these generators,
not the divided-power form or a quotient imposing central powers.
In B's factorial basis \(E=\mathcal E/\rho^2\). At the physical
complete color \(M=1\), its head has
\[
 K w_j=-q^{-1}Q^{-j}w_j,\quad
 \mathcal E w_j=(Q^{-j}-1)w_{j-1},\quad
 Fw_j=(1-Q^{j+1})w_{j+1},\quad 0\le j<N,
 \tag{2}
\]
with the original zero extreme arrows.
All internal arrows in (2) are nonzero.

Put
\[
 C=\rho^2FE+qK+q^{-1}K^{-1},\qquad
 e=E^N,\quad f=F^N,\quad k=K^N.
 \tag{3}
\]
These elements are central. For the powers, expand
\([E^N,F]\) as a sum of \(N\) commutators and move \(K^{\pm1}\)
past the powers of \(E\); both coefficients are geometric sums
of a nontrivial primitive \(N\)-th root and vanish. The other
commutators are the same calculation. Substitution of (1) checks
centrality of \(C\). In particular
\[
 FE=\frac{C-qK-q^{-1}K^{-1}}{\rho^2},\qquad
 EF=\frac{C-q^{-1}K-qK^{-1}}{\rho^2}.
 \tag{4}
\]

On the actual head,
\[
 e=f=0,\qquad k=(-1)^{N-1},\qquad C=-2.
 \tag{5}
\]
For example \(FEw_j=[j]_q^2w_j\), and
\(qK+q^{-1}K^{-1}=-(Q^{-j}+Q^j)\).
Equations (2)--(5) agree with C's head after its explicit diagonal
basis change. No tensor coproduct, pivot or framing has been changed.

## 2. An explicit local presentation

Adjoin a central root \(\lambda^N=k\), and choose its value
\(\lambda_0=q^{N-1}=-q^{-1}\) over (5). This is an étale extension:
\(N\lambda^{N-1}\) is a unit. The \(K\) spectral projectors are
\[
 p_j=\frac1N\sum_{r=0}^{N-1}(K/(\lambda Q^{-j}))^r,\qquad
 0\le j<N.
 \tag{6}
\]
They are mutually orthogonal, sum to one, and
\(Kp_j=\lambda Q^{-j}p_j\). Indices on the following \(d_j\)
are taken modulo \(N\):
\[
 d_j=\frac{C-q\lambda Q^{-j}-q^{-1}\lambda^{-1}Q^j}{\rho^2},
 \qquad D_j=\prod_{a=1}^j d_a,\quad D_0=1,\quad D=D_{N-1}.
 \tag{7}
\]
Thus \(FEp_j=d_jp_j\) and \(EFp_j=d_{j+1}p_j\).
At (5),
\[
 d_0=0,\qquad
 d_j=\frac{\sin^2(\pi j/N)}{\sin^2(\pi/N)}\ne0
 \quad(1\le j<N).
 \tag{8}
\]
This includes both parities of \(N\).

Localize at the central element \(D\). Define
\[
 u_j=F^jp_0,\qquad v_j=D_j^{-1}p_0E^j,\qquad
 m_{ij}=u_iv_j .
 \tag{9}
\]
The weight projectors and (4) give
\[
 v_iu_j=\delta_{ij}p_0,\qquad
 u_jv_j=p_j,\qquad
 m_{ij}m_{ab}=\delta_{ja}m_{ib},\qquad
 \sum_jm_{jj}=1.
 \tag{10}
\]
For example \(E^jF^jp_0=D_jp_0\), while
\(F^jE^jp_j=D_jp_j\). The unit factors in (7) are essential.

In these matrix units the generators are exactly
\[
 K=\sum_{j=0}^{N-1}\lambda Q^{-j}m_{jj},
 \quad
 F=\sum_{j=0}^{N-2}m_{j+1,j}+f\,m_{0,N-1},
 \tag{11}
\]
\[
 E=\sum_{j=1}^{N-1}d_jm_{j-1,j}+\frac eD m_{N-1,0}.
 \tag{12}
\]
The last arrows follow from the actual central powers \(F^N=f\)
and \(E^N=e\), not from deleting a wrap by hand. The remaining
corner relation \(FEp_0=d_0p_0\) is precisely
\[
                         ef=\prod_{j=0}^{N-1}d_j=Dd_0.
 \tag{13}
\]
An equality first obtained on \(p_0\) holds as a scalar equality
on all corners by (10).

Consequently the exact local algebra is
\[
 U[\lambda]/(\lambda^N-k)[D^{-1}]
       \ \cong\ \operatorname{Mat}_N(R),
 \quad
 R=\frac{\mathbb C[\lambda^{\pm1},C,e,f,D^{-1}]}
              {(ef-\prod_{j=0}^{N-1}d_j)} .
 \tag{14}
\]
Here is also an inverse-presentation check, so no hidden relation
in the corner is assumed. Over the displayed commutative ring \(R\),
take the matrices (11)--(12) in the standard matrix units.
Their products are the two diagonal matrices in (4);
their difference is (1), and their weight relations hold also on
the wrap entries. Their \(N\)-th powers are exactly \(e,f,k=\lambda^N\);
their Casimir is exactly \(C\). These give a homomorphism from the
left side of (14) to the right. It sends (9) to the standard
matrix units. Conversely (9)--(13) give the homomorphism back;
(11)--(12) show that both composites fix all generators and
the central coefficients. Thus (14) is an isomorphism.

At the point (5) the derivative of the relation (13) with respect
to \(C\) is
\[
             -\rho^{-2}D\ne0.
 \tag{15}
\]
Therefore \(R\) is smooth of dimension three there; analytically,
\(e,f,\lambda\) are local coordinates and \(C\) is determined.
This is an actual smooth matrix-algebra neighborhood, not only
a dimension count for one representation.

For precision this is over the full center locally. Center formation
commutes here with the above flat root extension: it is the kernel
of the three commutator maps with \(E,F,K\), and a flat extension
preserves that kernel. Central localization has the same property.
Since the center of the right side of (14) is \(R\), (14) gives
an étale splitting over the actual center of \(U\). Smoothness
and the Azumaya property descend from this étale neighborhood.
There is no assertion of an \(N\)-uniform size or condition number
for this neighborhood or its chosen matrix units.

## 3. Full central character, Frobenius fiber and tensor blocks

Specializing (14) at (5) gives
\[
 U/(E^N,F^N,K^N-(-1)^{N-1},C+2)
                       \cong\operatorname{Mat}_N(\mathbb C).
 \tag{16}
\]
The calculation is also valid directly in that quotient: (8)
makes \(D\) a nonzero scalar and one may set \(\lambda=\lambda_0\).
All remaining central elements therefore act as scalars.
The ideal in (16) is the ideal generated by the full central
character of the head: it is contained in that ideal, and its
matrix quotient has no further proper nonzero ideal. The actual
nonzero head representation rules out the whole quotient.

This is not the entire fiber obtained by imposing only
\(E^N=F^N=0\) and \(K^N=(-1)^{N-1}\). To see its size without
a semisimplicity assertion, the usual ordered monomials
\(F^aK^bE^c\), \(a,c\ge0,\ b\in\mathbb Z\), are a basis of (1).
Spanning follows by its rewrite rules. Independence follows by
mapping to the skew Laurent algebra over
\(\mathbb C[C,K^{\pm1}]\) with
\[
 E=T,\qquad F=d(K)T^{-1},\qquad
 TK=Q^{-1}KT,\qquad
 d(K)=(C-qK-q^{-1}K^{-1})/\rho^2 .
 \tag{17}
\]
These elements satisfy (1); at a fixed Laurent \(T\)-degree,
the largest \(F\)-degree has the largest \(C\)-degree, with
nonzero leading coefficient. Its distinct \(K\)-monomials
cannot cancel. Descending in that degree proves independence.

Thus \(U\) is free of rank \(N^3\) over
\(\mathbb C[E^N,F^N,K^{\pm N}]\), with the three ordered
exponents restricted to \(0,\ldots,N-1\). The whole Frobenius
fiber has dimension \(N^3\), whereas (16) has dimension \(N^2\).
Iterating (4), without any localization, gives
\(E^NF^N=\prod_{j=0}^{N-1}d(Q^jK)\). Thus the following
relation holds on the whole Frobenius fiber, including its other blocks.
Its Casimir relation at the chosen root of \(k\) is
\[
 \prod_{j=0}^{N-1}\bigl(C+Q^j+Q^{-j}\bigr)=0.
 \tag{18}
\]
The root \(C=-2\) is simple. Any repeated values in (18) are
not removed by merely specifying the Frobenius powers.

Nor does (16) turn a tensor product into a single simple block.
The coproduct has its original Casimir and multiplicity data;
in particular the separate Hermite circle algebra is not the
one-head central-character quotient in (16). C already cautions
that its Borel pointing has a tensor mark relative to the
actual quantum coproduct. All those distinctions survive (14).

## 4. What Morita trace descent does to the original source

On a split patch write the ordinary unnormalized matrix trace as
\(\operatorname{tr}\); it is the reduced trace of the split Azumaya algebra.
The original highest cut on an arbitrary
marked one-cut operator \(A\) is
\[
                 \phi_{T_0}(A)=\operatorname{tr}(T_0A).
 \tag{19}
\]
The tail pivots and all word factors are already part of \(A\);
none is replaced by an ordinary full trace.
For a general probe \(P\), its exact cyclic defect is
\[
 \phi_P([X,A])=\operatorname{tr}([P,X]A).
 \tag{20}
\]
The trace pairing on matrices is nondegenerate, so (20) vanishes
for every \(X,A\) if and only if \(P\) is scalar. Explicitly,
in the head matrix units,
\[
        \phi_{T_0}([m_{01},m_{10}])=1 .
 \tag{21}
\]
Thus the actual marked highest cut does not factor through
the cyclic quotient \(U/[U,U]\), even on the smooth matrix block.
Replacing it by the Morita cyclic trace changes the marked source.
Diagonal softened probes have the same test: the value on this
commutator with indices \(i,j\) is \(P_{ii}-P_{jj}\).

For completeness, the cyclic quotient of \(\operatorname{Mat}_N(R)\)
is \(R\), via the ordinary trace. Off-diagonal matrix units are
commutators with diagonal ones, and diagonal differences are
\([m_{ij},m_{ji}]\); these generate exactly the trace-zero matrices.
This proves both the descent and its limitation directly.

The actual unmarked knot operator is scalar, \(A=c\,I\), as fixed
by B's original selected closure. Hence every trace-one probe gives
\[
               \phi_P(A)=c=\frac1N\operatorname{tr}(A).
 \tag{22}
\]
This is the legitimate positive use of trace descent. It recovers
the existing whole-function scalarity, retaining all external
normalization factors. It gives no nonvanishing assertion about \(c\).
The unmarked equality does not extend to arbitrary marked operators.

A change of splitting by \(g\) preserves the full marked pairing
only with the simultaneous transports
\[
 A\longmapsto gAg^{-1},\qquad P\longmapsto gPg^{-1}.
 \tag{23}
\]
Keeping \(P\) fixed produces exactly (20) infinitesimally.
For an ordered marked word \(BO\) the same identity is
\[
 \operatorname{tr}(P[X,B]O)
 =\operatorname{tr}([P,X]BO)
                   +\operatorname{tr}(PB[O,X]).
 \tag{24}
\]
It retains the cut/pivot and marked-word defects. All identities
are finite-dimensional and hold with the original parameter germs.

Accordingly the source-compatible datum to descend is the matrix
bundle together with its probe and marked word, using (23), or
its linear current description with (20), (24) retained.
It is not the cyclic trace class of the word alone. A proposed
quantum lift of the residual geometric framing flow must still
transport this probe/current and its original relative chain.
The local central coordinates in (14) do not identify that
geometric framing coordinate or supply a measure on its fiber.
In particular they give no bound, nonzero integral, or cycle
coefficient for that fiber. No new relative-cycle descent is claimed.

## Coverage and complete proof sources

The broad central-block/Azumaya theory is classical coverage,
not a novelty claim. Brown--Gordon's
[ramification-of-centers paper](https://arxiv.org/abs/math/9911234)
distinguishes the full center from its central Hopf subalgebra;
its quantum discussion has odd-order hypotheses. Baseilhac's
[root \(U_q\mathfrak{sl}_2\) review](https://arxiv.org/abs/1101.3440)
is further coverage. Neither is a proof premise here. The explicit
presentation above uses the actual \(q\) of order \(2N\), at every \(N\).

* C: notes/cyclic_steinberg_lattice.md, SHA256
  e9149c7e32045c818f9e790e07f7e4989021d459379a8309f6a196216fd53fa4.
* B: notes/balanced_verma_coherent_braiding.md, SHA256
  0203bdd7dbb36a4f8deb1c310b3445608e53d10922049447da8eecec4f87d1c4.

Both complete sources were read nontruncated in the author sequence.
Their used source-identification implications were checked separately
from the local presentation and trace calculations above. Only
written mathematics and text/hash operations were used; no mathematical
program or test was run. Frozen and public files are unchanged.
