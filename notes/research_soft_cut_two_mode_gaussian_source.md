# An exact two-mode Gaussian source for the binomial cut

Private written proof, 18 November 2026.

The binomial cut has a finite Gaussian presentation at a bulk
coherent occupation. Two oscillator modes with fixed total
degree \(d=N-1\) realize the original finite head. Composition
of the literal local kernels is exact, and the binomial closing
is a fixed-radius latitude evaluation with a normalization
bounded above and below by constants times \(\sqrt d\).

This construction does not continue the old small-clock Borel
germ to the bulk. It gives a finite-level integral before an
asymptotic expansion, retains the full occupation projector,
and transports finite matrix currents. It is not identified
with the previous finite-\(R\) Borel coarea chain.

The complete proof directs are C, the actual compact coherent
source, and S, the binomial cut and normal-residue density.
Their pins appear at the end. The Gaussian and factorial
calculations needed here are proved directly.

## 1. The finite head in a two-mode Gaussian space

Fix \(N\ge2\) and \(d=N-1\ge1\). Use the original head basis
\(e_0,\ldots,e_d\), with all matrix entries in the conventions
of C and S. On \(\mathbb C^2\), write \(Z=(Z_0,Z_1)\) and use
\[
 d\gamma(Z)=\pi^{-2}e^{-|Z_0|^2-|Z_1|^2}\,d^2Z_0\,d^2Z_1.
 \tag{1}
\]
Angular integration and one-dimensional integration by parts give
\[
 \int_{\mathbb C^2}Z^\alpha\overline Z^\beta\,d\gamma(Z)
                         =\mathbf1_{\alpha=\beta}\alpha!.
 \tag{2}
\]
Indeed each radial factor is
\(\int_0^\infty t^a e^{-t}dt=a!\), starting with the
unit integral and integrating by parts \(a\) times.

Embed the finite head as the homogeneous degree-\(d\) subspace by
\[
 e_j\longmapsto u_j(Z)
       =\frac{Z_1^jZ_0^{d-j}}{\sqrt{d!}},
             \qquad 0\le j\le d.
 \tag{3}
\]
Then
\[
 \langle u_i,u_j\rangle_\gamma
       =\delta_{ij}\frac{j!(d-j)!}{d!}
       =\frac{\delta_{ij}}{\binom dj}.
 \tag{4}
\]
This is exactly C's coherent head metric. No claim that the
literal braiding is unitary in this metric is made.

For an arbitrary finite matrix \(A=(A_{ij})\), define its kernel
\[
 \mathcal K_A(Z,\overline W)
   =\sum_{i,j=0}^d A_{ij}\binom dj\,
                         u_i(Z)\overline{u_j(W)}
   =\frac1{d!}\sum_{i,j=0}^d
       A_{ij}\binom dj Z_1^iZ_0^{d-i}
                     \overline W_1^{\,j}\overline W_0^{\,d-j}.
 \tag{5}
\]
The binomial belongs to the input index. The kernel acts on
the embedded basis by
\[
 \int\mathcal K_A(Z,\overline W)u_j(W)\,d\gamma(W)
                                      =\sum_iA_{ij}u_i(Z).
 \tag{6}
\]
Thus the map is injective and uses the literal finite matrix.

## 2. Exact local composition, trace and occupation projector

Using (2)--(4) on the middle index proves
\[
 \boxed{\quad
 \int_{\mathbb C^2}
   \mathcal K_A(Z,\overline X)\mathcal K_B(X,\overline W)
       \,d\gamma(X)=\mathcal K_{AB}(Z,\overline W),\qquad
 \int\mathcal K_A(Z,\overline Z)\,d\gamma(Z)=\operatorname{Tr}A.
 \quad}
 \tag{7}
\]
All integrands here are finite polynomials times a Gaussian,
so these are absolutely convergent integrals. Tensor products
use one pair of modes for each physical head and product measures.
Rectangular maps between tensor products use the same output
monomials and dual input monomials; their composition proof is
the identical index contraction.

In particular the identity head has kernel
\[
 \Pi_d(Z,\overline W)
       =\frac{(Z_0\overline W_0+Z_1\overline W_1)^d}{d!}
       =[t^d]\exp\!\left(t(Z_0\overline W_0+Z_1\overline W_1)\right).
 \tag{8}
\]
It is the orthogonal projection onto total degree \(d\), rather
than the identity on the full oscillator space. This can be
checked on every monomial using (2): all total degrees other
than \(d\) are annihilated. The coefficient in (8) can equivalently
be retained as a Cauchy integral on any fixed small \(t\)-circle.
Neither a degree tail nor a boundary coefficient is discarded.

Both mode occupations are nonnegative. Their fixed sum is \(d\);
hence the physical occupation \(j\) lies exactly in
\(\{0,\ldots,d\}\). This is a coupled sector condition, not two
independent approximations to a cutoff.

To display the extreme physical walls explicitly,
\[
 \mathcal K_{T_0}(Z,\overline W)
       =\frac{(Z_0\overline W_0)^d}{d!},\qquad
 \mathcal K_{T_d}(Z,\overline W)
       =\frac{(Z_1\overline W_1)^d}{d!}.
 \tag{9}
\]
Any actual finite generator relation with lower or upper
projector terms therefore has its exact kernel counterpart
under (7). The finite pivots remain their actual matrices
inside the same formula. The map does not replace them by
an oscillator trace or a classical value.

## 3. The bulk latitude and its normalization

For \(|v|=1\), set
\[
 Z_d(v)=\sqrt{d/2}\,(1,v),\qquad |Z_d(v)|^2=d.
 \tag{10}
\]
C's full coherent symbol at latitude \(T=1/2\) is
\[
 f_C(v,1/2)=2^{-d}
       \sum_{i,j=0}^d C_{ij}\binom dj\,v^{\,i-j}.
 \tag{11}
\]
Direct substitution in (5) gives
\[
 e^{-d}\mathcal K_C(Z_d(v),\overline{Z_d(v)})
                =e^{-d}\frac{d^d}{d!}f_C(v,1/2).
 \tag{12}
\]
Put
\[
                         A_d=\frac{e^d d!}{d^d}.
 \tag{13}
\]
The exact soft-cut identity is consequently
\[
 \boxed{\quad
 \operatorname{Tr}(P_N^{\rm cut}C)
   =\frac{A_d}{2\pi i}
       \oint_{|v|=1}
        e^{-d}\mathcal K_C(Z_d(v),\overline{Z_d(v)})
                                      \frac{dv}{v},\qquad
 P_N^{\rm cut}=\sum_{j=0}^d2^{-d}\binom djT_j .
 \quad}
 \tag{14}
\]
On this contour \(\overline v=v^{-1}\); thus (14) is also a
finite Laurent contour identity. Angular integration kills
\(i\ne j\), with the original diagonal coefficients left intact.

Each fixed angular point is a trace-one rank-one probe:
\[
 (\mathcal P_v)_{ab}=2^{-d}\binom da\,v^{\,b-a},
 \qquad
 \mathcal P_v^2=\mathcal P_v,\quad
 \operatorname{Tr}\mathcal P_v=1.
 \tag{15}
\]
It is positive in the metric (4), and
\(\operatorname{Tr}(\mathcal P_vC)=f_C(v,1/2)\).
The average of these probes is exactly \(P_N^{\rm cut}\).
This does not make an arbitrary closed word or marked current
positive. S proves equality of (14) with the original unmarked
scalar and supplies its exact marked-cut transgression.

## 4. Polynomial conditioning, proved without Stirling's formula

The normalization (13) satisfies, for every integer \(d\ge1\),
\[
                  e^{-1/2}\sqrt d\le A_d\le10\sqrt d.
 \tag{16}
\]
Here is a direct proof. The gamma integral from (2), followed
by \(t=dx\), gives
\[
 A_d=d\int_0^\infty e^{-d\psi(x)}\,dx,\qquad
                        \psi(x)=x-1-\log x.
 \tag{17}
\]
For \(1\le x\le1+d^{-1/2}\), one has
\(\psi(x)\le(x-1)^2/2\), because \(\psi(1)=\psi'(1)=0\)
and \(\psi''(x)=x^{-2}\le1\) there. This gives the lower
bound in (16).

On \([1/2,2]\), \(\psi''\ge1/4\), so
\(\psi(x)\ge(x-1)^2/8\). This part of (17) is at most
\(\sqrt{8\pi d}<6\sqrt d\).
For \(x\ge2\), \(\psi'(x)\ge1/2\), so its part is at most
\(2e^{-d\psi(2)}\le2\sqrt d\).
Finally \(\psi\) decreases on \((0,1)\), and
\(\psi(1/2)=\log2-1/2\ge1/6\).
For completeness \(\log2\ge2/3\) follows by integrating
the tangent-line lower bound
\(1/x\ge4/3-4x/9\) on \([1,2]\).
The remaining part is therefore at most
\((d/2)e^{-d/6}\le\sqrt d\); the last inequality follows
by maximizing \(\sqrt t\,e^{-t/6}/2\) for \(t>0\).
Their sum is below the upper constant in (16).
The proof includes \(d=1\).

There is a useful exact probabilistic normalization check.
Let \(J_0,J_1\) be independent Poisson variables of means
\(d/2,d/2\). Then
\[
 \Pr(J_0+J_1=d)=e^{-d}\frac{d^d}{d!}=A_d^{-1},\qquad
 \Pr(J_1=j\mid J_0+J_1=d)=2^{-d}\binom dj.
 \tag{18}
\]
Both equations follow by the binomial theorem in the finite
sum \(J_0+J_1=d\). Thus the bulk cut is an exact conditioning
at the mean total occupation, with polynomial normalization.
This statement concerns the cut probe. It does not change
the coupled transfer variables or Poisson means inside an
actual signed crossing.

## 5. A finite-word integral before asymptotic expansion

Formula (14) need not be applied after computing the unknown
whole cut matrix. Factor that matrix by its given finite
diagram: literal signed crossings, turn maps, pivots, marks,
and the remaining finite partial traces. Apply (5) to each
of those known local arrays, and (7) to every contraction.
For example, for a one-head ordered product
\(C=A_m\cdots A_1\),
\[
 \begin{split}
 \operatorname{Tr}(P_N^{\rm cut}C)
 ={}&\frac{A_d e^{-d}}{2\pi i}\oint\frac{dv}{v}
       \int\mathcal K_{A_m}(Z_d(v),\overline X_{m-1})\\
 &\quad\cdot
       \mathcal K_{A_{m-1}}(X_{m-1},\overline X_{m-2})
       \cdots
       \mathcal K_{A_1}(X_1,\overline{Z_d(v)})
                       \prod_{\ell=1}^{m-1}d\gamma(X_\ell).
 \end{split}
 \tag{19}
\]
The case \(m=1\) means no internal integral. Multi-head words
and the actual partially traced knot network use the tensor
and rectangular versions of the same identity. Their number
of Gaussian mode pairs depends on the fixed diagram, not
on \(N\). All matrix coefficients are the original finite
ones; no unknown scalar defines a kernel or its normalization.

All inserted identity wires use (8). Thus the formula retains
every physical input/output occupation restriction, including
restrictions shared by two legs of one crossing. Reordering
integrations is legitimate because at fixed \(N\) their
integrands are finite polynomials against product Gaussian
measures. The only new outer cut normalization is (13).
The factor \(e^{-d}\) in (19) is the recorded Gaussian weight
at its fixed boundary radius, not an omitted scalar.

For comparison with the compact source, ordinary radial
coordinates give
\[
 d\gamma(Z)=e^{-t}t\,dt\,d\sigma(u),\qquad
 Z=\sqrt t\,u,\quad |u|=1,
 \tag{20}
\]
where \(d\sigma\) is normalized measure on \(S^3\).
Since the trace kernel is homogeneous of bidegree \((d,d)\),
its radial integral is \((d+1)!/d!=N\).
The residual angular integral, after the scalar \(U(1)\)
phase is removed, is exactly C's compact coherent trace
with its factor \(N\). This verifies that (19) is a Gaussian
presentation of the existing finite source, rather than a
different quantum model.

## 6. Currents and the boundary of the conclusion

The injective map (5) and product identity (7) transport every
finite matrix identity, including its marked defects. In
particular, S's exact equation
\[
 \operatorname{Tr}((P_N^{\rm cut}-T_0)C)
          =\operatorname{Tr}(B_N^{\rm cut}[C,\mathcal E])
 \tag{21}
\]
is still the equality of the corresponding Gaussian kernel
contractions. Commutators are Gaussian-composed kernels,
not pointwise products of coherent symbols. Lower and upper
projector terms remain the kernels (9). Their possibly small
values at one latitude do not bound their composition with
a growing source.

At every fixed \(N\), differentiation in meridian or marking
parameters commutes with these identities on compact subsets
where the literal coefficient matrices are holomorphic:
the integrands remain finite polynomial Gaussian moments.
Consequently all finite meridian normals and marked endpoint
currents are retained. This assertion gives no uniform
large-\(N\) estimate for the differentiated whole word.

The coefficient degree and literal entries in (19) grow with
the level. A uniform analytic phase, amplitude or Gevrey
bound on the bulk fields has not been obtained by Gaussian
composition alone. In particular the old highest-cut
small-clock germ cannot be evaluated at a singular bulk
parameter merely because (19) exists.

No Borel cutoff \(R\) was introduced in this construction.
The earlier highest-cut coarea formula has a different
relative chain and explicit upper-\(R\) derivative currents.
Identifying that family with (19), including those currents,
would require an additional source-preserving map; none is
claimed here. The present gain is an exact finite Gaussian
and conditioned-Poisson realization of the bulk cut, with
polynomial outer normalization and complete finite walls.
It supplies neither geometric-cycle occurrence nor a
volume-conjecture lower bound.

## Complete proof-source pins

* C: notes/compact_coherent_source_period.md,
  SHA256 8c6c3277367a4aa6c69269da635139d5f881f3d3d0d894e04dd97028d76537e4.
* S: notes/research_binomial_cut_framing_density.md,
  SHA256 4bc6efc595fd6d59c0bc572d83495fb779cff230ff1cb9c14429a0b7c6a2a1b0.

C supplies the original basis, coherent metric and local
source kernels with their exact composition and wall scope.
S supplies the source-preserving binomial cut and full marked
transgression. The two-mode embedding, Gaussian integral,
projector, bulk normalization and finite-word adapter are
proved above. Only written mathematics and text/hash
operations were used. Frozen sources and public files are unchanged.
