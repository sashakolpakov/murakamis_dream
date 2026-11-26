# An analytic Euler transition on actual endpoint head blocks

Private written proof, 18 November 2026.

After explicit factorial endpoint gauges, a compressed literal crossing
has a uniformly bounded transfer generator. Its entire finite Euler
polynomial converges in operator norm to the exponential of that
generator, with error \(O(N^{-1})\). The inverse has the corresponding
estimate. This is an actual finite-matrix transition, not substitution
of commuting symbols into a formal Euler series.

A single quadratic zero permits a head collar of width \(O(N^{1/2})\).
Two quadratic zeros permit two collars of width \(O(N^{3/4})\).
Every collar is a single interval. Monotonicity proves the exact
compression identity even when a transfer can exit a collar. All
complementary blocks remain source currents, with no smallness claim.
The finite Fourier projector and the original quantum/meridian normal
rows are retained.

The complete directs are B, the literal balanced crossing; E, the actual
endpoint factorial chart; and V, the common two-wall module. Their pins
are below. The new analytic estimates and compression proof are given
in full here. No neighboring-network packet hypothesis is inferred.

## 1. The actual finite Euler factors

Fix \(N\ge2\), \(d=N-1\), and use
\[
 h_N=\frac{2\pi i}{N},\qquad Q=e^h,\qquad q=e^{h/2},
 \qquad x=-M/q.
 \tag{1}
\]
On the original balanced head, with basis \(w_0,\ldots,w_d\), let
\[
 \mathcal E w_a=\alpha_a w_{a-1},\quad
 \alpha_a=MQ^{-a}-M^{-1}\quad(a\ge1),\qquad
 \mathcal E w_0=0,
 \tag{2}
\]
\[
 Fw_a=(1-Q^{a+1})w_{a+1}\quad(a<d),\qquad Fw_d=0.
 \tag{3}
\]
These are the actual compressed matrices before specialization.
Away from the ordinary-color path they are auxiliary finite matrices,
not a generic finite-dimensional Hopf representation. V retains their
exact Hopf defect.

Put \(A=\mathcal E_1\otimes F_2\), so \(A^N=0\), and
\(F_n(Q)=\prod_{j=1}^n(1-Q^j)\), \(F_0=1\).
B gives the literal positive uncheck Euler factor and its inverse:
\[
 \Theta_N(A)=\sum_{n=0}^{d}
       \frac{(-1)^n q^{n^2}}{F_n(Q)}A^n,\qquad
 \Theta_N(A)^{-1}=\sum_{n=0}^{d}
       \frac{q^n}{F_n(Q)}A^n.
 \tag{4}
\]
The positive crossing is \(\kappa\,\mathsf P D\Theta_N\);
the negative is its literal inverse. Here \(\mathsf P\) is the flip,
\(D_{a,b}=x^{-a-b}Q^{ab}\), and \(\kappa\) is the unchanged common
Cartan line. All pivots and framing remain their original matrices.

For completeness (4) is a finite algebraic identity whenever \(F_n\),
\(n<N\), are units. The two displayed polynomials \(U,V\), with
\(A\) replaced by \(z\), have coefficient recurrences giving,
modulo \(z^N\),
\[
 U(Qz)=U(z)/(1-qz),\qquad V(Qz)=(1-qz)V(z).
 \tag{5}
\]
Hence \(U(z)V(z)=1\) modulo \(z^N\): its positive coefficients below
\(N\) vanish since \(1-Q^j\ne0\). Substitute \(z=A\). This proof uses
no infinite product convergence and applies on the normal disks below.

## 2. A global factorial majorant and the uniform exponential limit

At \(h=h_N\),
\[
 |1-Q^j|=2\sin(\pi j/N)\ge\frac4N\min(j,N-j).
 \tag{6}
\]
For \(n\le N/2\), this directly gives
\(|F_n|\ge(4/N)^n n!\). For \(n>N/2\), the ratio
\(\prod_{j=1}^n\min(j,N-j)/n!\) decreases to
\[
 \binom{N-1}{\lfloor N/2\rfloor}^{-1}
       \ge2^{-(N-1)}\ge4^{-n}.
 \tag{7}
\]
Consequently, at every level and for every \(0\le n<N\),
\[
                  |F_n(Q_N)|\ge N^{-n}n!.
 \tag{8}
\]

Choose a sufficiently small absolute \(\eta>0\). On the doubled
normal bidisk
\[
 |h-h_N|\le2\eta N^{-2},\qquad |M-1|\le2\eta N^{-1},
 \tag{9}
\]
every \(1-Q^j\) and \(\alpha_j\), \(1\le j<N\), remains a unit,
with modulus at least half its root modulus. Indeed the change of
either factor is at most \(C\eta/N\), whereas its root modulus is
at least \(4\min(j,N-j)/N\). Decrease \(\eta\) once. Thus
\[
                 |F_n(Q)|\ge (2N)^{-n}n!
 \tag{10}
\]
on (9).

Uniformly there, the two normalized coefficients satisfy
\[
 \left|\frac{(-1)^n q^{n^2}h^n}{F_n(Q)}-\frac1{n!}\right|
       \le \frac{C^n n^2}{Nn!},
 \qquad
 \left|\frac{q^nh^n}{F_n(Q)}-\frac{(-1)^n}{n!}\right|
       \le \frac{C^n n^2}{Nn!}.
 \tag{11}
\]
The right sides are zero at \(n=0\). To prove this, first take
\(n\le N/2\). Each factor
\[
                  \frac{-hj}{1-e^{hj}}
 \tag{12}
\]
is bounded by an absolute constant and differs from one by at most
\(Cj/N\); the apparent value at \(hj=0\) is removable.
Telescoping their product gives \(C^n n^2/N\).
The additional phases \(e^{hn^2/2}\) and \(e^{hn/2}\) are uniformly
bounded in modulus on (9) and differ from one by at most
\(Cn^2/N\). This proves (11) in the first half. In the second
half (10) and \(|h|\le C/N\) bound either normalized coefficient
times \(n!\) by \(C^n\), while \(n^2/N\ge1/2\). Enlarging \(C\)
proves (11) for that half too.

It follows for every finite operator \(T\) with \(T^N=0\) and
\(\|T\|\le R\) that
\[
 \|\Theta_N(hT)-e^T\|\le C_R/N,\qquad
 \|\Theta_N(hT)^{-1}-e^{-T}\|\le C_R/N.
 \tag{13}
\]
Both exponential series terminate. Sum (11) against \(R^n\);
\(\sum n^2(CR)^n/n!\) is finite independently of \(N\).
In particular both operators in (4) have uniformly bounded norms
and inverses on such a family. Their least singular value is bounded
below by \(1/(e^R+C_R/N)\). This is an operator statement; it does
not bound an arbitrary prescribed scalar contraction below.

## 3. The two exact endpoint gauges

Define diagonal matrices, all regular and invertible on (9), by
\[
 G_F w_a=F_a(Q)w_a,\qquad
 G_E w_a=H_a(Q,M)^{-1}w_a,\qquad
 H_a=\prod_{j=1}^a\alpha_j,\quad H_0=1.
 \tag{14}
\]
Direct coefficient calculation gives
\[
 G_F^{-1}FG_F=S,\qquad
 G_F^{-1}\mathcal E G_F\,w_a=\beta_a w_{a-1},
 \quad \beta_a=(1-Q^a)\alpha_a,
 \tag{15}
\]
where \(S\) is the physical unilateral raising matrix, zero at \(d\).
Similarly
\[
 G_E^{-1}\mathcal E G_E=S^*,\qquad
 G_E^{-1}FG_E\,w_a=\beta_{a+1}w_{a+1}\quad(a<d),
 \tag{16}
\]
and the last arrow is still zero. No factor at index \(N\) is
inverted or used to replace that forced zero.

At \(M=1,h=h_N\),
\[
 \beta_a=\frac{(1-Q^a)^2}{Q^a}=-4\sin^2(\pi a/N),
 \qquad H_a=Q^{-a(a+1)/2}F_a.
 \tag{17}
\]
Thus each gauge has E's endpoint condition-number bound, up to
reversal:
\[
 \operatorname{cond}(G|_I)
       \le N\left(\frac{eN}{R}\right)^{2R}
 \tag{18}
\]
for an interval \(I=[0,R]\) or \([d-R,d]\), \(R\le d/2\);
interpret the bracket as one for \(R=0\).
In particular every collar \(R=o(N)\) has subexponential gauge cost.

The same conclusion holds uniformly on (9), with an additional
fixed power of \(N\). Each factor relative to its root value differs
from one by at most \(C\eta/\min(j,N-j)\); it stays in a fixed
disk away from zero. Summing its log-modulus over \(j<N\) costs
at most \(C\log N\). This proves the extra polynomial bound for
both the gauges and their inverses, including upper collars.
Their fixed normal derivatives have the usual further polynomial
cost by Cauchy's formula on smaller bidisks.

One may use a globally tame change of head basis throughout the
original network. For each chosen interval set
\[
                  \widetilde G=G P_I+(I-P_I).
 \tag{18a}
\]
E's separate bounds for the gauge and its reciprocal, and the
factor-ratio argument above, give
\[
 \|\widetilde G\|\,\|\widetilde G^{-1}\|
       \le N^{C}\left(\frac{eN}{R}\right)^{2R}.
 \tag{18b}
\]
This is subexponential for \(R=o(N)\). The internal interval arrows
are exactly (15) or (16); interface arrows use their literal two
endpoint gauge factors. The compressed operators below are therefore
the same whether one uses \(G\) or \(\widetilde G\). No exponentially
conditioned full-head change is needed to obtain them.

All changes are exact source changes of basis: neighboring tensors
carry the two inverse factors, exposed rows and columns transform,
and diagonal pivots commute with the gauges. The transformation is
not an equality of two independently reset boundary probes.

## 4. Monotone compression retains the exact cutoff

Let \(I,J\) be single intervals of integer head indices and let
\(P=P_I\otimes P_J\). In any of the diagonal gauges above, \(A\)
moves \((a,b)\) to \((a-1,b+1)\), or is zero. If its initial and
final indices lie in \(I\times J\), every intermediate index does.
Therefore, exactly,
\[
              P A^n P=(PAP)^n\quad\hbox{on }\operatorname{im}P.
 \tag{19}
\]
This remains true when a transfer can exit the interval: it cannot
return. Hence, writing \(T=PAP/h\) on that image,
\[
 P\Theta_N(A)P=\Theta_N(hT),\qquad
 P\Theta_N(A)^{-1}P=\Theta_N(hT)^{-1}.
 \tag{20}
\]
The two compressed factors are exact inverses, not merely asymptotic
ones. The union of an upper and a lower collar is not a single
interval and is not covered by (19); its cross-collar blocks remain.

There are two useful bounded-generator regimes. Constants in the
following bounds may depend on the fixed collar constants. Every
collar width also satisfies \(0\le R_i\le\lfloor d/2\rfloor\):

* **One quadratic zero.** Use \(G_F\) on the donor, leave the
  recipient balanced, and take the donor interval to be a lower
  or upper collar of width \(R_1\le C_1N^{1/2}\). The recipient
  interval may be any physical interval, including the whole head.
  On (9),
  \[
       \|T\|\le C(R_1+1)^2/N\le C'.
       \tag{21}
  \]
* **Two quadratic zeros.** Use \(G_F\) on the donor and \(G_E\)
  on the recipient. Let both intervals be lower or upper collars,
  of widths \(R_i\le C_iN^{3/4}\). Then
  \[
       \|T\|\le C(R_1+1)^2(R_2+1)^2/N^3\le C'.
       \tag{22}
  \]

For the proof, on either donor collar
\(|\beta_a|\le C(R_1+1)^2/N^2\), and on either recipient
collar \(|\beta_{b+1}|\le C(R_2+1)^2/N^2\).
These estimates follow directly from (9) and (15)--(17), including
the actual zero endpoint arrows. The unchanged balanced \(F\) has
norm bounded by an absolute constant on (9).
A weighted transfer is an injective partial shift of basis vectors,
so its norm is the maximum coefficient. Finally \(|h|^{-1}\le CN\).
This proves (21)--(22).

Apply (13) to obtain the claimed uniform exponential transitions
and uniform inverses on all these compressed blocks. For a checked
positive crossing the output projector is \(\mathsf P P\mathsf P\).
The exact remaining factor is \(\kappa\mathsf P D\). At the physical
complete root it is unitary in the gauged coordinate norm, since
its diagonal entries have modulus one. Thus the corresponding
compressed actual checked block is uniformly invertible as a map
between these two projected spaces. The negative block, with the
input/output spaces exchanged, is exactly its inverse.
Away from that fiber the entire \(D,\kappa\) factors are retained;
no normal of them is omitted by the Euler estimate.

## 5. Finite projectors, outgoing blocks and normal rows

The gauge is diagonal and does not change \(P_I\). Its exact
root Fourier kernel is
\[
 (P_I)_{jk}^{\mathrm{Fourier}}
       =\frac1N\sum_{a=L}^{U}Q^{a(k-j)}.
 \tag{23}
\]
Keeping the same unwrapped ratio \(t\) gives the finite polynomial
\[
 \frac1N t^L K_{U-L}(t),\qquad
 K_R(t)=\sum_{a=0}^R t^a,\qquad K_R(1)=R+1.
 \tag{24}
\]
Both endpoints, and the upper-collar power \(t^{d-R}\), remain.
No delta-function matching or independent cancellation of the two
apparent \(1-t\) poles is part of (13).

The full crossing is not replaced by its compressed block.
Its four \(P,(I-P)\) blocks are kept exactly. In particular the
unestimated outgoing/incoming currents can be written without
changing a coefficient:
\[
 [\Theta_N(A),P]
   =\sum_{n=1}^{d}\frac{(-1)^nq^{n^2}}{F_n(Q)}
       \sum_{j=0}^{n-1}A^j[A,P]A^{n-1-j}.
 \tag{25}
\]
The elementary \([A,P]\) is supported on the interval-edge arrows;
the surrounding powers can transport it far outside the collar.
No small bound for (25) or for an unrestricted exterior follows.

The actual head-normal rows also remain. In V's ambient module, put
\[
 \delta=1-Q^N,\qquad w=MQ^{-N}-M^{-1},\qquad
 \rho=q-q^{-1},\qquad K_Hw_a=xQ^{-a}w_a.
 \tag{26}
\]
Here \(U=|N\rangle\langle d|\), \(L=|d\rangle\langle N|\)
are the two ambient head/tail arrows, and \(P_d=|d\rangle\langle d|\).
The head projector \(P_H\) satisfies
\[
 [F,P_H]=\delta U,\qquad
 [\mathcal E,P_H]=-wL,\qquad
 [\mathcal E_H,F_H]-\rho(K_H-K_H^{-1})
                         =-\delta w\,P_d.
 \tag{27}
\]
Extend a head gauge by the identity on the tail, rather than
attempting to invert a factorial at \(N\). The transformed rows
are exactly \(\delta U G\) and \(-wG^{-1}L\); their product retains
the same diagonal head projector. The original marked source and
co-source transform with them. This gives a regular full
normal-germ prescription, without erasing either wall or their
mixed normal.

There is also a quantitative fixed-jet statement for the compressed
transition itself. On a smaller concentric bidisk, (13) and Cauchy's
formula imply for fixed \(j,\ell\ge0\)
\[
 \left\|\partial_h^j\partial_M^\ell
       \bigl(\Theta_N(hT_N)-e^{T_N}\bigr)\right\|
       \le C_{j,\ell}N^{2j+\ell-1},
 \tag{28}
\]
and the same assertion for the inverse. The matrices \(T_N\), including
their gauges, are differentiated as whole analytic functions.
Thus the error is \(O(N^{-1})\) for the corresponding scaled normals.
The genuine ordinary-color path
\(M=-e^{Nh/2}\) lies in (9) on a smaller \(h\)-disk of radius
proportional to \(N^{-2}\). Restricting the exact identities first
therefore retains its actual fixed-\(N\) quantum normals.
A fixed-\(M\) auxiliary array is not declared a generic representation.

## 6. The scalar Poisson profile requires an explicit packet

The paid unconditional conclusion is the operator \(e^{T_N}\)
with the original finite projection. A scalar \(e^\xi\) requires
more. For example suppose a normalized incoming packet \(v_N\)
lies in \(\operatorname{im}P\), \(|\xi_N|\le R\), and satisfies
\[
                  \|(T_N-\xi_N)v_N\|\le\varepsilon_N.
 \tag{29}
\]
Then the integral identity for the difference of two exponentials
and the uniform bound for \(T_N\) give
\[
 \|\Theta_N(hT_N)v_N-e^{\xi_N}v_N\|
                    \le C_R(\varepsilon_N+N^{-1}).
 \tag{30}
\]
This is a precise sufficient packet hypothesis. It is not assumed
for the original neighboring tangle, and (30) does not control the
discarded-output blocks in (25).

The quadratic and quartic geometric contacts motivate the collar
scales in (21)--(22); the proof itself uses only the literal matrix
coefficients and the displayed width conditions. It does not choose
which geometric endpoint, normal contour or relative framing interval
occurs in the original global state. Uniform invertibility of this
local compressed transition is not a lower bound for the knot scalar.

## Complete proof-source pins

* B: notes/balanced_verma_coherent_braiding.md, SHA256
  0203bdd7dbb36a4f8deb1c310b3445608e53d10922049447da8eecec4f87d1c4.
* E: notes/actual_endpoint_head_factorial_chart.md, SHA256
  5cea9fc9b738c68e77b8d86b0445d4110df14f614b333032ba87faa98bff1b0c.
* V: notes/common_verma_two_wall_source.md, SHA256
  b94f53c2f92840a3817af0619e1a7ec0c6e73403f0ea01463c7bc3d27878d1fd.

All three complete directs were read nontruncated in the current
author sequence and their used implications checked. The q-Hahn
partner/fold statements were inspected for coverage only: their
spectral-channel collision estimates do not give the operator
transition proved here. Only written mathematics and text operations
were used. Frozen and public files are unchanged.
