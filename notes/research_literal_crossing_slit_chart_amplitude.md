# Literal crossing amplitudes on complex slit charts

Private written proof, 18 November 2026.

The exact root-factorial interpolant has a uniform nonzero local
amplitude on a larger domain than its original vertical strip.
The domain includes every nonreal scaled factorial length. Applied
to the literal balanced signed crossing, this gives its actual
five-factor amplitude without a coherent occupation sum or a
change of the physical imaginary quantum ray.

The hypothesis is that all the affine factorial lengths lie in
one compact part of the stated slit domain. Existence of such
a simultaneous logarithmic chart at a geometric representation
is not proved here. Neither an interpolation nor its nonzero
amplitude selects the original finite support cycle.

The complete proof directs are I, the exact factorial interpolant;
V, its moving-period version; and B, the literal balanced crossing.
Their pins appear below.

## 1. The same marked factorial on a larger domain

Put
\[
 \mathcal D=\mathbb C\setminus
                 ((-\infty,0]\cup[1,\infty)),\qquad
 h_N=2\pi i/N,\quad q_N=e^{h_N/2},\quad Q_N=e^{h_N},
 \qquad N\ge2 .
 \tag{1}
\]
The domain \(\mathcal D\) is simply connected. For example
\(z\mapsto z/(1-z)\) maps it to the plane slit along the
nonpositive real ray. All logarithms below are continued from
the interval \(0<z<1\) in this domain.

Keep I's exact function, with positive-base powers marked by
their real logarithms:
\[
 G_N(\zeta)=
 (2\pi/N)^\zeta\Gamma(\zeta+1)
 \prod_{k\ge1}
 \frac{\Gamma(Nk+\zeta+1)}
      {\Gamma(Nk-\zeta)(Nk)^{2\zeta+1}},
 \qquad
 \widehat F_N(\zeta)=
 e^{\,\pi i\zeta(\zeta+1)/(2N)-\pi i\zeta/2}G_N(\zeta).
 \tag{2}
\]
This is the original section, not another solution of its
difference equation. Its exact identities are
\[
 \widehat F_N(\zeta+1)
       =(1-Q_N^{\zeta+1})\widehat F_N(\zeta),\qquad
 \widehat F_N(0)=1,\qquad
 \widehat F_N(n)=(Q_N;Q_N)_n\quad(0\le n<N).
 \tag{3}
\]
In particular every original finite factorial is unchanged.

For every compact \(K\Subset\mathcal D\), (2) evaluated at
\(\zeta=Nz\) is holomorphic and nonzero on a neighborhood of
\(K\). Indeed none of
\[
 Nz+1,\qquad N(k+z)+1,\qquad N(k-z)
 \tag{4}
\]
is a Gamma pole there. Each possible pole would require a
real \(z\le0\) or \(z\ge1\). For large \(k\) the logarithm
of the product factor is \(O_{N,K}(k^{-2})\), by the same
cancelled Gamma-ratio expansion as in I. Its derivatives
converge normally too. Thus the product continues the
original function to this whole domain. The simply connected
domain fixes its logarithm by the original positive interval.

Define the analytic functions on \(\mathcal D\)
\[
 J(z)=\int_0^z\Log(2\sin\pi t)\,dt,\qquad
 \mathcal H(z)=J(z)+\frac{\pi i}{2}(z^2-z),
 \tag{5}
\]
\[
 \mathcal L(z)=\mathcal H'(z)
       =\Log(2\sin\pi z)+\pi i(z-\tfrac12),\qquad
 a(z)=\exp\!\left\{
        \tfrac12\Log(2\sin\pi z)+\tfrac{\pi i z}{2}\right\}.
 \tag{6}
\]
The endpoint in (5) is its integrable logarithmic endpoint
on the original interval, followed by analytic continuation.
These marks give
\[
 e^{\mathcal L(z)}=1-e^{2\pi i z},\qquad
 a(z)^2=i(1-e^{2\pi i z}).
 \tag{7}
\]
They do not reset either logarithm or square root.
Equivalently \(\mathcal H\) is the continued branch of
\((\operatorname{Li}_2(1)-\operatorname{Li}_2(e^{2\pi iz}))
 /(2\pi i)\).

## 2. Uniform asymptotics and bounded endpoint shifts

Uniformly on every \(K\Subset\mathcal D\),
\[
 \Log G_N(Nz)
 =NJ(z)+\tfrac12\Log(2N\sin\pi z)
      +\frac{\pi\cot\pi z}{12N}+O_K(N^{-3}).
 \tag{8}
\]
All fixed holomorphic derivatives have the same remainder
bound on a smaller compact set.

Here is why the strip proof extends without a new summation
argument. For the finitely many small \(k\), the numbers
\(z,k+z,k-z\), with \(z\in K\), avoid zero and the negative
real ray. Compactness puts them in sectors
\(|\arg w|\le\pi-\delta_K\), with moduli bounded below.
For the remaining \(k\), the arguments in (4) lie in a
fixed smaller sector around the positive real axis and
have size comparable to \(Nk\).
The uniform Gamma expansion used and justified in I therefore
has remainder \(O_K(N^{-3})\) for the initial term and
\(O_K(N^{-3}k^{-3})\) for the \(k\)-th product term.
To make its enlarged sector scope explicit, the Euler
remainder after \(1/(12w)\), initially on \(\Re w>0\),
can be integrated by parts twice. It is a fixed multiple
of \(w^{-3}\) plus a fixed multiple of
\(\int_0^\infty\widetilde B_4(t)(w+t)^{-4}\,dt\), where
\(\widetilde B_4\) is the bounded periodic fourth Bernoulli
polynomial. This integral is holomorphic on the plane slit
along the nonpositive real ray, so the same formula
continues there. If \(|\arg w|\le\pi-\delta\), splitting
the integral at \(2|w|\) bounds its absolute value by
\(C_\delta|w|^{-3}\): on the first interval
\(|w+t|\ge c_\delta|w|\), and on the tail
\(|w+t|\ge t/2\). This proves precisely the sector bound
needed above, including arguments with negative real part.

In detail that product logarithm is
\[
 N\phi_k(z)+\tfrac12\Log(1-z^2/k^2)
 +\frac1{12N}\left(\frac1{k+z}-\frac1{k-z}\right)
 +O_K(N^{-3}k^{-3}),
 \tag{9}
\]
\[
 \phi_k(z)=(k+z)\Log(1+z/k)
            -(k-z)\Log(1-z/k)-2z.
\]
The finite small-\(k\) constants can be enlarged to give the
single summable remainder in (9). All its logarithms have
their continuation from the original strip.
The sums of the displayed terms converge normally. Their
sine-product and cotangent identities hold on the original
strip by I and hence on \(\mathcal D\) by analytic continuation.
Summing (9), including the initial Gamma factor, proves (8).
The proof uses the actual product, not continuation of an
asymptotic identity without a remainder bound.

It follows that
\[
 \widehat F_N(Nz)=
 N^{1/2}a(z)e^{N\mathcal H(z)}
 \exp\!\left\{\frac{\pi\cot\pi z}{12N}+O_K(N^{-3})\right\}.
 \tag{10}
\]
For a bounded complex shift \(\gamma\), Taylor expansion
on a slightly larger compact subset of \(\mathcal D\) gives
\[
 \boxed{\quad
 \widehat F_N(Nz+\gamma)=
 N^{1/2}a(z)e^{\gamma\mathcal L(z)}
                 e^{N\mathcal H(z)}(1+O(N^{-1})).
 \quad}
 \tag{11}
\]
The bound is uniform for \(z\) and \(\gamma\) in fixed compacts,
with every fixed derivative on smaller compacts. The leading
amplitude is a holomorphic unit, bounded above and below there.
This includes bounded affine offsets which depend on \(N\),
such as the offset in \(\lfloor N/2\rfloor\). No convergence
of those offsets is needed for the uniform assertion.

More generally, for a fixed finite list and integer signs
\(\varepsilon_\nu\),
\[
 \prod_\nu\widehat F_N(Nz_\nu+\gamma_\nu)^{\varepsilon_\nu}
 =N^{\frac12\sum_\nu\varepsilon_\nu}
 \prod_\nu
    [a(z_\nu)e^{\gamma_\nu\mathcal L(z_\nu)}]^{\varepsilon_\nu}
 \exp\!\left\{N\sum_\nu\varepsilon_\nu\mathcal H(z_\nu)\right\}
 (1+O(N^{-1})).
 \tag{12}
\]
Every \(z_\nu\) must remain in the same fixed compact
subset of \(\mathcal D\). Cancellations in a later sum
are not estimated by (12).

## 3. The literal two signed balanced coefficients

Use B's equal-color factorial basis, with \(d=N-1\),
\[
 x=-M/q_N,\qquad
 D e_{a,b}=x^{-a-b}Q_N^{ab}e_{a,b},\qquad
 \kappa=q_N^{H^2/2},\quad q_N^H=x.
 \tag{13}
\]
The last equality uses the original marked logarithm,
\(\log x=(N-1)\log q_N+\log M\).
The common Cartan scalar \(\kappa\) is retained.
On the finite head,
\[
 E e_a=(MQ_N^{-a}-M^{-1})e_{a-1},\qquad
 F e_b=(1-Q_N^{b+1})e_{b+1},
 \tag{14}
\]
with the actual zero extreme arrows. Let \(P\) be the flip.
The checked crossings, in their actual order, are
\[
 R_+=\kappa P D
       \sum_{n=0}^{d}\frac{(-1)^nq_N^{n^2}}{(Q_N;Q_N)_n}
                              E_1^nF_2^n ,
\]
\[
 R_-=\kappa^{-1}
       \sum_{n=0}^{d}\frac{q_N^n}{(Q_N;Q_N)_n}
                              E_1^nF_2^n\,D^{-1}P.
 \tag{15}
\]
There is no cyclic wrap or added high occupation.

Choose the logarithm of \(M\) near one and set
\[
                      \alpha=-2\log M/h_N,\qquad
                         Q_N^\alpha=M^{-2}.
 \tag{16}
\]
For positive crossing input \((a,b)\), the output is
\((b+n,a-n)\), with
\(0\le n\le\min(a,d-b)\). Its exact interpolated coefficient is
\[
 \boxed{\quad
 R_+(a,b,n)=m_+(a,b,n;M)
 \frac{\widehat F_N(b+n)\widehat F_N(a+\alpha)}
      {\widehat F_N(b)\widehat F_N(n)
                         \widehat F_N(a-n+\alpha)},\quad}
 \tag{17}
\]
\[
 m_+=\kappa\,(-1)^nq_N^{n^2}x^{-a-b}
       Q_N^{(a-n)(b+n)}
       M^n Q_N^{-n(2a-n+1)/2}.
 \tag{18}
\]
For negative crossing input \((a,b)\), the output is
\((b-n,a+n)\), with \(0\le n\le\min(b,d-a)\). Its exact
interpolated coefficient is
\[
 \boxed{\quad
 R_-(a,b,n)=m_-(a,b,n;M)
 \frac{\widehat F_N(a+n)\widehat F_N(b+\alpha)}
      {\widehat F_N(a)\widehat F_N(n)
                         \widehat F_N(b-n+\alpha)},\quad}
 \tag{19}
\]
\[
 m_-=\kappa^{-1}q_N^n x^{a+b}Q_N^{-ab}
                    M^nQ_N^{-n(2b-n+1)/2}.
 \tag{20}
\]
Off the integer lattice, \((-1)^n\) in (18) means the fixed
interpolation \(e^{\pi i n}\); all other powers use the
displayed original logarithms.

To verify (17), cancel the finite \(F_2^n\) product against
\((Q_N;Q_N)_n\), giving the Gaussian coefficient
\({b+n\brack n}_{Q_N}\). The remaining color product is exactly
\[
 \prod_{j=a-n+1}^{a}(MQ_N^{-j}-M^{-1})
 =M^nQ_N^{-n(2a-n+1)/2}
             \frac{\widehat F_N(a+\alpha)}
                  {\widehat F_N(a-n+\alpha)}
 \tag{21}
\]
by (3). The Cartan diagonal acts on \((a-n,b+n)\).
For (19), the flip first gives \((b,a)\), its inverse
Cartan scalar is \(x^{a+b}Q_N^{-ab}\), and the inverse
series in (15) has coefficient \(q_N^n\).
The same calculation proves (19)--(20).
At a common zero in an endpoint ratio, equality means
the whole finite product (21) before specialization.
No negative factorial is assigned to a forbidden physical state.

Thus the five leading lengths, before division by \(N\), are
\[
 \begin{array}{c|c|c}
 &\text{numerator}&\text{denominator}\\ \hline
 +&b+n,\ a&b,\ n,\ a-n\\
 -&a+n,\ b&a,\ n,\ b-n .
 \end{array}
 \tag{22}
\]
The color shift \(\alpha\) is a bounded endpoint shift when
\(|M-1|=O(N^{-1})\). Applying (12) proves an actual
nonzero \(N^{-1/2}\) local amplitude for each crossing on
every common compact chart satisfying (22) in \(\mathcal D\).
For example, with \(a=NA,b=NB,n=NC\), the positive
factorial phase is
\[
 \mathcal H(B+C)+\mathcal H(A)-\mathcal H(B)
                    -\mathcal H(C)-\mathcal H(A-C).
 \tag{23}
\]
Its amplitude is the corresponding ratio of the five
\(a(\cdot)\)'s, times
\(e^{\alpha[\mathcal L(A)-\mathcal L(A-C)]}\).
The known scalar (18) remains exact and contributes its
marked polynomial exponential to the full action.
All original pivot, framing and other peripheral multipliers
of a word must likewise be retained, not replaced by one.

## 4. Physical meridian normals and genuine quantum normals

The estimates are joint in bounded \(\alpha\), on larger
compacts before differentiation. Since
\(\partial_M=-2(h_NM)^{-1}\partial_\alpha\), each fixed
meridian normal has polynomial \(N\)-cost. This differentiates
the entire scalar in (18) or (20), including \(\kappa\).
It does not differentiate a specialized color product as if
its meridian dependence had disappeared.

Moving-quantum coefficient normals can also be retained.
Fix \(N\) and all original indices, let
\[
 q=q_Ne^\epsilon,\qquad
 P=\frac{\pi i}{\log q},
 \tag{24}
\]
and use V's same Gamma product \(\widehat F_P\), not a
root reflection with a moving endpoint. In (15)--(21)
replace the quantum parameters by these actual generic
ones, keep \(d=N-1\) fixed, and use
\(\alpha(P)=-2\log M/(2\log q)\).
The finite product identities remain exact as analytic
coefficient identities. If the original finite-color normal
ties \(M\) to \(q\), that relation must be substituted before
differentiation. A fixed-\(M\) auxiliary coefficient germ is
not relabeled as that entire representation family.

The sector argument of Section 2 works uniformly for \(P\)
in a sufficiently small relative complex neighborhood of
\(N\), with every scaled argument divided by \(P\).
At fixed indices its logarithmic \(P\)-derivative is bounded
on these compacts: differentiating \(P J(\zeta/P)\) gives
\(J(y)-yJ'(y)\), and the remainder is differentiated on a
larger relative disk. For fixed \(M\), the bounded color
shift causes only bounded additional terms. Since
\(P'(\epsilon)=O(N^2)\),
every factorial ratio and exact monomial has logarithmic
\(\epsilon\)-derivative \(O(N^2)\).
For \(\kappa\) this follows directly from
\(\log\kappa=(\log x)^2/(2\log q)\), with
\(\log x=\pi i-\log q+\log M\).

Consequently, for all sufficiently large \(N\), there is
a disk \(|\epsilon|\le c/N^2\)
on which the full local coefficient divided by its root
value is bounded above and below by fixed constants.
Cauchy's formula gives, for every fixed \(j\),
\[
 \left|\partial_\epsilon^jR_\pm\big|_{\epsilon=0}\right|
             \le C_jN^{2j}|R_\pm|_{\epsilon=0}.
 \tag{25}
\]
Here all five lengths lie in the compact slit chart, so
the root coefficient is nonzero. Fixed physical endpoint
factorials outside this interior hypothesis require V's
separate endpoint bounds; (25) does not silently include them.
The fixed-\(M\) convention in (24) and the fixed endpoint
\(d=N-1\) are part of this assertion.

The same proof includes a specified original parameter path
\(M(\epsilon)\) with \(M(0)=e^{-h_N\alpha_0/2}\), bounded
\(\alpha_0\), and
\(\log M(\epsilon)-\log M(0)=O(N\epsilon)\) holomorphically
on a slightly larger disk, with its Cauchy derivative bounds.
Then \(\alpha(\epsilon)\) remains bounded and
\(\partial_\epsilon\alpha=O(N^2)\); its extra logarithmic
derivative has the same cost as in (25). In particular the
ordinary color relation \(M=-q^N\), based at \(M=1\),
is covered. All its parameter derivatives, rather than a
root-only reflection formula, must be taken.

## 5. The source cycle and the outstanding chart condition

For a literal finite word, replace only its original factorial
products by (2), retaining the original affine matching lattice.
I's sum of small product cotangent circles about the supported
integer points is then an exact period of that same finite sum.
Equations (17)--(22) identify its local signed summands;
they do not replace its support by independent head intervals.
There are no extra coherent input/output occupation sums here.

Five-shape regularity says that certain exponentiated clocks
avoid zero and one. It alone does not put all their compatible
affine logarithmic lengths in \(\mathcal D\).
On real exterior lengths the actual interpolant can have
finite-level zeros or poles; no uniform nonzero amplitude on
a neighborhood containing them follows from this note.
Any whole-ratio cancellation must be verified before changing
that conclusion.

Even on a paid common chart, the original cotangent cycles,
physical support walls, and residual framing direction remain.
No contributing contour, framing-fiber period, geometric
coefficient, or scalar lower bound is asserted.
This is an explicit adapter for the existing factorial
interpolation, not a novelty claim for Gamma asymptotics.

## Complete proof-source pins

* I: notes/exact_factorial_interpolation_and_complex_contours.md,
  SHA256 1f34f65437dfe0bfb4062a7a74840beae1676353cf13bb8a86f8849a8a36bc72.
* V: notes/actual_moving_period_factorial_normals.md,
  SHA256 8fa02b96eaf532ad6b242216e7161b1cfc64a6e6a968563a3da9e5c07f660cd1.
* B: notes/balanced_verma_coherent_braiding.md,
  SHA256 0203bdd7dbb36a4f8deb1c310b3445608e53d10922049447da8eecec4f87d1c4.

I supplies the exact marked product, the summable Gamma
remainder and original finite residue cycle. V supplies its
actual moving-period section and fixed-index convention.
B supplies the balanced signed finite matrices and their
unchanged common Cartan line. The enlarged sector argument,
bounded-shift amplitude, five-factor identities and normal
bounds are written above. Only written mathematics and
source-text operations were used. Frozen/public files are unchanged.
