# A source-selected conserved channel and physical Gaussian compression

24 November 2026. Research note. Written proof.

The actual cups of an even plat select one conserved channel exactly.
At its source-selected parameter the complete conserved spectrum remains
simple at every level, with controlled projectors and a known nonzero
normalization of zero volume rate. Inside the selected channel its
orthogonalizing metric is exactly the original physical metric.

There is also a quantitative estimate on the previously constructed
physical source spaces: a short operator block supported on at most
half the heads retains its entire Hilbert--Schmidt norm up to an explicit
power of the level. Thus a proved whole-block Hilbert--Schmidt model
gives a relative operator model on the actual source, without an inverse
fusion Gram. The original closing remains. These results do not give a
relative scalar error or the hyperbolic value of the fixed-degree minimum.

## 1. The original source and the spaces being restricted

Put \(N\ge2\), \(d=N-1\), \(q=e^{\pi i/N}\), \(Q=q^2\),
\(x=-q^{-1}\), and take \(b=2k\ge2\) physical heads. Use the
orthonormal balanced basis of H and G. Its actual complete generators are
\[
 Ke_a=xQ^{-a}e_a,\quad Ee_a=(Q^{-a}-1)e_{a-1},\quad
 Fe_a=(1-Q^{a+1})e_{a+1},
 \tag{1}
\]
with the two missing arrows zero. Here \(E\) is the scaled generator.
Totals use \(\Delta E=E\otimes K+1\otimes E\),
\(\Delta F=F\otimes1+K^{-1}\otimes F\), and
\(\mathsf K=K_1\cdots K_b\).

The literal ordinary cup, ordinary cap and marked cap are, by H and P,
\[
 p_{uv}=Nx^{-v}\delta_{u+v,d},\qquad
 \ell_{uv}=x^u\delta_{u+v,d}/N,\qquad
 m_{uv}=x^v/N^2.
 \tag{2}
\]
The last has no degree delta. Keep the actual order of the paired heads,
and put \(u_0=p^{\otimes k}\). Let \(\ell_0\) be the tensor of
the original \(k-1\) ordinary top caps and the one full marked cap.
For the actual unmarked signed braid operator \(R\), the scalar is
\[
                       \mathcal K_N=\chi_N\ell_0Ru_0.
 \tag{3}
\]
All original turns, dual identifications, pivots and normalizations are
in these data; \(\chi_N\) is the unchanged external scalar. No bound
for it is inferred in an unreduced convention. The standard complete
dual identification makes these the common total operators (1), not
an unauthorized permutation of physical wires.

Let \(\mathcal H=V_N^{\otimes b}\), with its physical norm, and define
\[
 T=kd,\quad \mathcal H_T=\operatorname{span}\{|a\rangle:\sum a_i=T\},
 \qquad \mathcal I=\mathcal H_T\cap\ker\mathsf E\cap\ker\mathsf F.
 \tag{4}
\]
This is H's full root invariant space. Let \(\mathcal S\subset\mathcal I\)
be the saturated specialization of the generic invariant lattice in U.
It can be smaller than \(\mathcal I\). U and D already prove that
the original cup source and its regular braid orbit lie in \(\mathcal S\),
with the literal closing retained. They also give stronger invariant-space
dimension reductions than the conserved channel used next.

## 2. The parameter selected by the cups is spectrally regular

Use C's conserved operators
\[
 B_c=\mathsf F-(\mathsf E-cI)\mathsf K^{-1},\qquad H_c=B_c-2I,
 \quad p_N(z)=2iT_N\!\left(\frac{z}{2\sqrt q}\right),
 \quad \sqrt q=e^{\pi i/(2N)}.
 \tag{5}
\]
Here \(T_N\) is Chebyshev of the first kind.
The auxiliary parameter is now \(c=2\). It is distinct from the
eigenvalue \(2\) being selected. C proves on the full head space
\(p_N(B_c)=\gamma^bp_N(c)I\), \(\gamma=(-1)^{N+1}\), with exact
companion form and minimal polynomial of degree \(N\). Since \(b\)
is even, the minimal polynomial at this parameter is
\(p_N(z)-p_N(2)\).

Here are estimates at \(c=2\), outside C's exterior-parameter range.
Set
\[
 \theta=\frac{\pi}{2N},\quad s=\sin\theta,\quad
 \alpha=\operatorname{arsinh}\sqrt s,\quad
 \beta=\arcsin\sqrt s,\quad w=e^{\alpha-i\beta}.
 \tag{6}
\]
Then \(w+w^{-1}=2/\sqrt q\) exactly: its half-sum has real part
\(\sqrt{1+s}\sqrt{1-s}=\cos\theta\) and imaginary part \(-s\).
Also
\[
 (2N)^{-1/2}\le\alpha\le\sqrt{\pi/(2N)},\quad N\alpha\ge1,
 \quad |w^N-w^{-N}|\ge(1-e^{-2})e^{\sqrt{N/2}}.
 \tag{7}
\]
Indeed \(N^{-1}\le\sin\theta\le\pi/(2N)\) and
\(z/\sqrt2\le\operatorname{arsinh}z\le z\) for \(0\le z\le1\).

The roots are \(\lambda_j=\sqrt q(wQ^j+w^{-1}Q^{-j})\),
\(0\le j<N\), with \(\lambda_0=2\). For \(v_j=wQ^j\),
Chebyshev differentiation gives
\[
 |p_N'(\lambda_j)|
 =N\frac{|w^N-w^{-N}|}{|v_j-v_j^{-1}|}
 \ge\frac{1-e^{-2}}{2\sqrt2}N e^{\sqrt{N/2}}.
 \tag{8}
\]
The denominator is at most \(2\cosh\alpha\le2\sqrt2\).
Thus every root is simple, at every \(N\), without a parity or
prime-level exception. C gives its full eigenspace rank \(N^{b-1}\).
The Lagrange spectral projectors satisfy
\[
 \|\Pi_j\|\le
 \frac{(4b+2+2\sqrt2)^{N-1}}
 {[(1-e^{-2})/(2\sqrt2)]N e^{\sqrt{N/2}}},\qquad
 G_2=\sum_j\Pi_j^*\Pi_j,\quad
 N^{-1}I\le G_2\le e^{C_bN}I.
 \tag{9}
\]
Here \(\|B_2\|\le4b+2\), and each \(|\lambda_j|\le2\sqrt2\).
The denominator in the projector product is \(|p_N'(\lambda_j)|\).
There is no product-of-nearest-gaps \(N\log N\) loss.

Write \(\mathcal E_2=\ker(B_2-2I)\). Its exact projector is
\[
 \Pi_2=\frac{r_N(B_2)}{p_N'(2)},\qquad
 r_N(z)=\frac{p_N(z)-p_N(2)}{z-2}.
 \tag{10}
\]
The subscript denotes the eigenvalue, and \(r_N\) is a polynomial;
no inverse of \(B_2-2I\) occurs. All complex phases of the derivative
are retained. Its modulus has the explicit calibration
\[
 |p_N'(2)|=\frac{N|w^N-w^{-N}|}{2\sqrt{2\sin\theta}},\qquad
 \log|p_N'(2)|=\sqrt{\pi N/2}+\tfrac32\log N+O(1).
 \tag{11}
\]
For the first formula use \(|w-w^{-1}|^2=8\sin\theta\).
For the second use
\(\alpha=\sqrt\theta+O(\theta^{3/2})\) and
\(|w^N-w^{-N}|=e^{N\alpha}(1+O(e^{-2N\alpha}))\).
In particular this known nonzero projector normalization has zero
exponential rate after division of its logarithm by \(N\).

## 3. Exact source selection and the physical norm

The ordinary cup obeys
\(E_{12}p=F_{12}p=0\), \(K_{12}p=p\). These follow termwise
from (1)--(2), including the zero arrows; H and P already establish
them for the original turns. Tensoring gives
\[
 \mathsf E u_0=\mathsf F u_0=0,\quad\mathsf K u_0=u_0,
 \quad B_2u_0=2u_0,\quad
 \mathcal K_N=\chi_N\ell_0\Pi_2R\Pi_2u_0.
 \tag{12}
\]
Every actual unmarked signed crossing intertwines the totals. Thus no
other coideal channel contributes to this source. This selection is
not inferred from a preferred geometric eigenvalue. It is an exact
consequence of the original incoming cups. In particular
\(e^{rH_2/h}u_0=u_0\) and \(e^{rH_2/h}Ru_0=Ru_0\) for every
finite \(r\), where \(h=2\pi i/N\). This removes a redundant finite
gauge direction; it constructs no nontrivial relative geometric transport.
The eigenvalue alone does not select the discrete-faithful critical branch.

For \(v\in\mathcal E_2\), \(\Pi_2v=v\) and the other projectors
kill it. Hence \(\langle G_2v,v\rangle=\|v\|^2\): the channel
metric is exactly the original physical norm on that whole space.
Moreover
\[
             \mathcal S\subset\mathcal I
                  =\mathcal E_2\cap\mathcal H_T.
 \tag{13}
\]
Indeed \(\mathsf K=1\) on \(\mathcal H_T\), so
\((B_2-2)v=\mathsf Fv-\mathsf Ev\) there. Its two terms have
different integer degrees \(T+1,T-1\), even at \(N=2\), and must
vanish separately. This does not identify \(\mathcal S\) with the
larger root invariant space, or identify \(\Pi_2\) with an orthogonal
projection onto their intersection.

## 4. A physical norm test for an entire short block

Consider a contiguous block of \(1\le r\le k\) heads. Let \(A_N\) be
a regular original integer-degree-preserving Hopf-intertwining
endomorphism supported on this block, such as a fixed unmarked signed
braid block. Its generic lift
is required when using \(\mathcal S\). Let \(A_N^{\rm glob}\)
include the spectator identities. For each
\(\mathcal T\in\{\mathcal S,\mathcal I,\mathcal E_2\}\),
\[
 \boxed{\quad
 N^{-r/2}\|A_N\|_{\rm HS}
       \le\|A_N^{\rm glob}|_{\mathcal T}\|_{\rm op}
       \le\|A_N\|_{\rm op}.
 \quad}
 \tag{14}
\]
These are physical operator norms. Every indicated space is preserved.

Here is an original-source witness for the lower bound. Let \(L,R\)
be the outside head counts, \(L+R=2k-r\). Choose an integer
\[
 \max(0,r-R)\le a\le\min(r,L),\qquad a\equiv L\pmod2.
 \tag{15}
\]
Such an integer exists: if the interval contains consecutive integers
both parities occur; if it is a singleton, \(2k-2r\) even forces
the stated parity. Pair the first \(a\) block heads, nested in order,
to the closest left outside heads. Pair the remaining block heads
nested to the closest right outside heads. Fill the even leftover
outside intervals by adjacent ordinary cups. This is a noncrossing
matching made from actual cups, not a free physical permutation.

Normalize this tensor to a unit vector \(v\). It has a regular generic
cup lift, so \(v\in\mathcal S\). Every block head has its own outside
partner. Since every cup coefficient has constant modulus, the block
reduced density of \(v\) is exactly \(I/N^r\). Thus
\(\|A_N^{\rm glob}v\|^2=\|A_N\|_{\rm HS}^2/N^r\), proving
(14). All cup phases and normalizations were used before normalization.
This applies to a whole supported short block, not merely one entry.

Let \(Q_{\mathcal T}\) denote the physical orthogonal projector onto
one of these spaces. A supplied whole-block model \(D_N\) gives
\[
 \|A_N^{\rm glob}|_{\mathcal T}
       -Q_{\mathcal T}D_N^{\rm glob}|_{\mathcal T}\|_{\rm op}
                   \le\|A_N-D_N\|_{\rm HS}.
 \tag{16}
\]
Only the pair/block error is used; spectator identities have operator
norm one. If \(A_N\ne0\), a relative Hilbert--Schmidt error
\(\varepsilon_N\) therefore becomes a relative operator error at
most \(N^{r/2}\varepsilon_N\). The model itself need not preserve
the source before this orthogonal compression. A whole-block
approximation must actually be proved; it is not supplied by (14).

## 5. The full physical crossing Gaussian on the source

For \(b\ge4\), use (14) with \(r=2\) and either signed crossing.
For every fixed integer \(J\ge0\),
G's zero-tilt full physical model \(\mathcal G_{N,J}^{\pm}\), with
all exact entry phases and support retained, obeys
\[
 \|R^{\pm}-\mathcal G_{N,J}^{\pm}\|_{\rm HS}
         \le C_JN^{-(J+1)/2}\|R^{\pm}\|_{\rm HS}.
 \tag{17}
\]
Consequently its source orthogonal compression has relative operator
error at most \(C_JN^{-(J-1)/2}\), independently of the spectator
width. One may instead first project the pair model orthogonally onto
the full physical algebra \(\mathbb C[\Omega]\), as G proves.
This contracts the error. The resulting polynomial \(f_N(\Omega)\)
has a regular generic lift using the same coefficients and the generic
Casimir. It therefore preserves all three source spaces, including
\(\mathcal S\), without a subsequent global projection.

No Casimir value quotient is used: its first-normal channels remain.
There is no fusion-coordinate conditioning or spectator Hilbert--Schmidt
factor in this relative operator estimate. In particular (14) and G give
\[
 \log\|R_i^{\pm}|_{\mathcal T}\|_{\rm op}
                         =\frac{2G_{\rm Cat}}\pi N+O_b(\log N).
 \tag{18}
\]
Here \(G_{\rm Cat}=\sum_{a\ge0}(-1)^a/(2a+1)^2\) is Catalan's constant.
This Gaussian assertion is at sufficiently large levels for each fixed
order. At two heads the source remains exact but this two-head norm
comparison is not asserted. The models are not declared exact inverses
or a new braid representation.

## 6. The literal closing still has to observe the propagated vector

There are simple polynomial bounds in the same physical metric:
\[
 \|u_0\|=N^{3k/2},\qquad
 N^{-3k/2}\le\|\ell_0|_{\mathcal T}\|
             \le N^{-(k+2)/2},\qquad
                         \mathcal T=\mathcal S,\mathcal I.
 \tag{19}
\]
For the upper bound ordinary caps force degree \(d\) on their pairs.
On the central degree \(kd\), the last marked pair then also has
degree \(d\). Its restricted row has norm \(N^{-3/2}\), and the
ordinary rows contribute \(N^{-(k-1)/2}\). This is P's permitted
whole-degree restriction, not a replacement of an arbitrary marked cap.

For the lower bound use the actual cyclic noncrossing cup matching
\((1,2k),(2,3),(4,5),\ldots,(2k-2,2k-1)\). It has a regular
generic lift, norm \(N^{3k/2}\), and its literal pairing with
\(\ell_0\) is exactly one. Indeed all odd indices become one index
\(a\), all even indices \(d-a\); the monomial powers in (2) cancel,
and each of the \(N\) remaining summands is \(1/N\).
This proves (19) on both source spaces. Thus the bare linear root row
\(A\mapsto\ell_0Au_0\) on \(\operatorname{End}(\mathcal T)\)
has Hilbert--Schmidt dual norm between \(1\) and \(N^{k-1}\).
If \(\chi_N\) is included in that row, multiply both bounds by
\(|\chi_N|\).

H and D already supply stronger source restrictions and polynomial
boundary estimates in their stated frames. The additions here are the
source-selected spectrally regular coideal channel and the quantitative
physical block/Gaussian norm test. They can supply known budgets to an
existing fixed-degree compiler; no new capacity identity is needed.

The remaining scalar is still exactly \(\chi_N\ell_0Ru_0\).
A lower bound for a row norm gives no lower bound for its value on this
particular propagated vector. Neither (16) nor an all-order local
relative operator model gives a relative scalar error after an arbitrary
word and closing. The geometric value and noncancellation after fixed
short partial fillings remain unproved. Fixed polynomial degree bounds
neither the growing source dimension nor this missing precision.
All results here are complete-root values, not off-root normal jets.

## Complete sources and closest coverage

| Label | Complete text | Lines | SHA256 |
| --- | --- | ---: | --- |
| C | [Conserved coideal channels](research_conserved_coideal_braid_channels.md) | 437 | b2a8c539742b4662ab8acbf4dc11c9bfa6acd27e895653ccfc47848278899fd4 |
| H | [Complete original invariant module](actual_complete_source_multiplicity_module.md) | 602 | 14cfb558f50c5b091cec9439692dfeb87129e31f38588cb1ebfd8e8547ac99a9 |
| G | [Whole physical crossing Gaussian](research_full_physical_crossing_gaussian_packet.md) | 306 | 7f1b9932f88aa549bc55088b6f056f5a362548bc51c9fdd7c6b00469e725f531 |
| U | [Saturated source and uniform confluence](research_uniform_fusion_confluence_source.md) | 439 | c39b8eaab1e1b4fcd1cdf7bc034a5a4419a33d40e058c2b6d6d06f8096414864 |
| D | [Earlier divided source projection](actual_all_width_divided_source_projection.md) | 204 | dc83b5e232a3d258f516a479d7257e85b9e5663a38e166f07c6ad9ae81004a68 |
| P | [Original cup/cap Gram supports](actual_plat_cup_cap_gram_support.md) | 229 | d780592fac1067eba868d2a8939ea1bf6a4191361d1c100eefe789833fe1451d |

Only written mathematics, source reads and text/hash operations were
used. Earlier final notes, the ledger and public manuscripts are unchanged.
